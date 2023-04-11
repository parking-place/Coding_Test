h, m = input().split(' ')
h, m = int(h), int(m)
t = int(input())

time = h*60 + m + t
print((time//60)%24, time%60)
