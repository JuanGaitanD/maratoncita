# Se simula el algoritmo: letra original = cifrada - c; se cuenta la original y si su cuenta es multiplo de K, c sube.
import sys
def main():
    data = sys.stdin.buffer.read().split()
    k = int(data[1])
    cnt = [0] * 26
    c = 0
    out = []
    for w in data[2:2 + int(data[0])]:
        r = bytearray(len(w))
        for i, ch in enumerate(w):
            L = (ch - 97 - c) % 26
            r[i] = L + 97
            cnt[L] += 1
            if cnt[L] % k == 0:
                c += 1
        out.append(r.decode())
    print(" ".join(out))
main()
