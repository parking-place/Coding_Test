# 알파벳을 숫자로 변환하기 위한 리스트
alpha = ' abcdefghijklmnopqrstuvwxyz'
n = int(input())
s = input()
# 해시 결과를 저장할 변수
hashing_result = 0
for i, s in enumerate(s):
    # 해시 결과에 더할 값을 구하고, 해시 결과에 더함
    hashing_result += (alpha.index(s) * (31 ** i))
# r mod M꼴에서 M은 1234567891이므로, M으로 나눈 나머지를 구함
hashing_result %= 1234567891
print(hashing_result)