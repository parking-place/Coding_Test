drawing_paper = [[0 for _ in range(100)] for _ in range(100)]
n= int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            drawing_paper[x+i][y+j] = 1
print(sum([sum(v) for v in drawing_paper]))