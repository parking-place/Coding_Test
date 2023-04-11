l = []
for _ in range(5):
    l.append([v for v in input()])
max_len = max([len(v) for v in l])
txt = ''
        
for j in range(max_len):
    for i in range(5):
        try:
            txt += l[i][j]
        except:
            pass
print(txt)