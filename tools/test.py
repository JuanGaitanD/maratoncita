#!/usr/bin/env python3
"""Corre los casos de prueba de una carpeta de evento.

Uso:  python tools/test.py <carpeta> [NombreProblema] [--py|--cpp]

Convención: en <carpeta>/tests/ hay pares  Nombre.1.in / Nombre.1.out, Nombre.2.in ...
Python se ejecuta con el intérprete local. C++ se compila con -std=c++11 -O2 dentro
del contenedor docker gcc:13 (no hay g++ nativo en Windows) y se ejecuta allí mismo.
"""
import glob, os, subprocess, sys, time

def norm(s):
    return "\n".join(l.rstrip() for l in s.strip().splitlines())

def run(cmd, inp, cwd, timeout=20):
    t = time.time()
    p = subprocess.run(cmd, input=inp, capture_output=True, text=True, cwd=cwd,
                       timeout=timeout, shell=isinstance(cmd, str))
    return p.stdout, p.stderr, time.time() - t

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    folder = args[0]
    only = args[1] if len(args) > 1 else None
    do_py = "--cpp" not in flags
    do_cpp = "--py" not in flags
    tests = sorted(glob.glob(os.path.join(folder, "tests", "*.in")))
    names = sorted({os.path.basename(t).split(".")[0] for t in tests})
    if only:
        names = [n for n in names if n == only]
    ok_all = True
    abs_folder = os.path.abspath(folder).replace("\\", "/")
    for name in names:
        cases = sorted(t for t in tests if os.path.basename(t).split(".")[0] == name)
        langs = []
        if do_py and os.path.exists(os.path.join(folder, name + ".py")):
            langs.append(("py", [sys.executable, name + ".py"]))
        if do_cpp and os.path.exists(os.path.join(folder, name + ".cpp")):
            comp = subprocess.run(["docker", "run", "--rm", "-v", f"{abs_folder}:/w", "-w", "/w", "gcc:13",
                                   "sh", "-c", f"mkdir -p /w/.bin && g++ -std=c++11 -O2 -o /w/.bin/{name} {name}.cpp"],
                                  capture_output=True, text=True)
            if comp.returncode:
                print(f"[{name}] C++ COMPILE ERROR\n{comp.stderr}"); ok_all = False
            else:
                langs.append(("cpp", ["docker", "run", "--rm", "-i", "-v", f"{abs_folder}:/w", "-w", "/w",
                                      "gcc:13", f"/w/.bin/{name}"]))
        for lang, cmd in langs:
            for c in cases:
                exp = open(c[:-3] + ".out", encoding="utf-8").read()
                inp = open(c, encoding="utf-8").read()
                try:
                    out, err, dt = run(cmd, inp, folder)
                except subprocess.TimeoutExpired:
                    print(f"[{name}.{lang}] {os.path.basename(c)} TIMEOUT"); ok_all = False; continue
                if norm(out) == norm(exp):
                    print(f"[{name}.{lang}] {os.path.basename(c)} OK ({dt:.2f}s)")
                else:
                    ok_all = False
                    print(f"[{name}.{lang}] {os.path.basename(c)} WRONG ({dt:.2f}s)\n--- expected\n{exp.strip()}\n--- got\n{out.strip()}\n--- stderr\n{err.strip()[:500]}")
    sys.exit(0 if ok_all else 1)

if __name__ == "__main__":
    main()
