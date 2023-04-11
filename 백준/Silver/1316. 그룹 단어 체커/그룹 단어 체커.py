n = int(input())
al = 'abcdefghijklmnopqrstuvwxyz'
c_gw = 0
for _ in range(n):
    c_gw += 1
    s = input()
    for v in al:
        c_a = s.count(v)
        if c_a > 1:
            if s.rfind(v)-s.find(v)+1 > c_a:
                c_gw -= 1
                break
print(c_gw)