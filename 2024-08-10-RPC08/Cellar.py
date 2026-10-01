# Serie (A+B) necesita max(A,B) profesores; paralelo (A*B) necesita A+B; () necesita 1.
import sys
def main():
    s = sys.stdin.readline().strip()
    val = [None]; op = [None]
    for ch in s:
        if ch == '(':
            val.append(None); op.append(None)
        elif ch == ')':
            v = val.pop(); op.pop()
            if v is None:
                v = 1
            if val[-1] is None:
                val[-1] = v
            elif op[-1] == '+':
                val[-1] = max(val[-1], v)
            else:
                val[-1] += v
        else:
            op[-1] = ch
    print(val[0])
main()
