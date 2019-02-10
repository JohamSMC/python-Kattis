numCase=int(input())

for element in range(numCase):
	input()
	Mg ,Mm = map(int,input().split())
	Lg=map(int,input().split())
	Lm=map(int,input().split())

	if max(Lg)>=max(Lm):
		print("Godzilla")
	else:
		print("MechaGodzilla")
'''
N = int(input())
for i in range(N):
    input() #skip empty line
    amounts = [int(x) for x in input().split()]
    G = [int(x) for x in input().split()]
    M = [int(x) for x in input().split()]
    print("Godzilla" if max(G)>=max(M) else "MechaGodzilla")'''	


	