def to_n_base(n : int, base : int) -> str:
    char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    q, r = n//base, n%base
    if q == 0:
        return char[r]
    else:
        return to_n_base(q, base) + char[r]

n, base = map(int, input().split())
print(to_n_base(n, base))