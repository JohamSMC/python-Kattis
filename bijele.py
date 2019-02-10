def missingFiles(numPart,validSet):
	if numPart==validSet:
		return "0"
	else:
		return str(validSet-numPart)

numbersPart=list(map(int,input().split()))

print(missingFiles(numbersPart[0],1)+" "+missingFiles(numbersPart[1],1)+" "+missingFiles(numbersPart[2],2)+" "+missingFiles(numbersPart[3],2)+" "+missingFiles(numbersPart[4],2)+" "+missingFiles(numbersPart[5],8))
