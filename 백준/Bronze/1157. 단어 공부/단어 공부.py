s = input()
al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
al_dict = {}
s = s.upper()
for v in al:
    al_dict[v] = s.count(v)
c_l = [*al_dict.values()]
max_c = max(c_l)
if c_l.count(max_c) > 1:
    print('?')
else:
    print(al[c_l.index(max_c)])