n = int(input())
count = 1
room = 1
i = 1
while True:
    if n <= room:
        break
    room += 6*i
    i += 1
    count += 1
print(count)