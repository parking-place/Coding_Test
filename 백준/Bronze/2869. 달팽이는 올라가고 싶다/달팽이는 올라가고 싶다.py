def snail_climbing(a, b, v):
    # v가 a보다 작으면 1일만에 올라갈 수 있음
    if v <= a:
        return 1
    
    # 마지막으로 올라가는 거리는 무조건 a만큼이므로 v-a만큼만 올라가면 남은 날은 하루
    # 하루에 총 a-b만큼 올라갈 수 있으므로 v-a 근처까지 (v-a)//(a-b)일이 걸려 올라간다
    
    # 단 (v-a)//(a-b)가 0이어도 v가 a보다 크므로 2일이 걸림
    if (v-a)//(a-b) == 0:
        return 2
    
    # 이때 v-a까지 남은 거리는 (v-a)%(a-b)
    # 즉 총 남은 거리는 (v-a)%(a-b)+a
    t = (v-a)//(a-b)
    v = (v-a)%(a-b)+a
    
    # 재귀를 통해 남은 거리가 a보다 작아질 때까지 호출
    return t + snail_climbing(a, b, v)

a, b, v = map(int, input().split())
print(snail_climbing(a, b, v))