croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for v in croatia_alphabet:
    s = s.replace(v, ' ')
print(len(s))