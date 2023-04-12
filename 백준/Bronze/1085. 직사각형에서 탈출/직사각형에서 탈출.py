x, y, w, h = map(int, input().split())
# 각각 동, 서, 남, 북으로 이동했을때의 가장자리와의 거리
l = w-x, x, h-y, y
# 가장 짧은 거리를 출력
print(min(l))