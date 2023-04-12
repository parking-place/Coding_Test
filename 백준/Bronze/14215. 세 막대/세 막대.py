s1, s2, s3 = map(int, input().split())
max_s = max(s1,s2,s3)
total_s = s1 + s2 + s3
while max_s >= total_s - max_s:
    max_s -= 1
    total_s -= 1
print(total_s)