a=[*range(97,123)]
s=input()
print(*[s.find(chr(v))for v in a])