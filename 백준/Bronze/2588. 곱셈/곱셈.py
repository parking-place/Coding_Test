n1 = int(input())
n2 = input()

n = []

for i in range(len(n2)-1,-1,-1) :
    n.append(n1 * int(n2[i]))
    
n.append(n[0] + n[1]*10 + n[2]*100)

for i in range(len(n)) :
    print(n[i])