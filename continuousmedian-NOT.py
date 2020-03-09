numberCases = int(input())

for case in range(numberCases):
    lenCase = int(input())

    # Quitar espacios en blanco
    inputCase = input().replace(" ", "")

    output = 0

    for i in range(lenCase):
        auxInput = inputCase[0:i+1]

        lenAuxInput = len(auxInput)

        # Pasar de string a lista, y convertir de cada elemento de la lista a Int
        auxInput = list(map(int, list(auxInput)))
        # Ordenar la lista
        auxInput = sorted(auxInput)
        # Pasar de int a string  a cada elemento de la lista
        auxInput = list(map(str, auxInput))
        # Convertir de lista a un String
        auxInput = "".join(auxInput)

        # print("Caso a evaluar = " + auxInput)

        if lenAuxInput % 2 == 0:
            nMoreOnePosition = int((lenAuxInput)/2)
            nPosition = nMoreOnePosition - 1
            output += (int(auxInput[nPosition]) +
                       int(auxInput[nMoreOnePosition])) // 2
            # print("Caso :" + auxInput + " outpur = " +
            #       str((int(auxInput[nPosition]) + int(auxInput[nMoreOnePosition])) // 2))
        else:
            middlePosition = int((lenAuxInput+1)/2)
            output += int(auxInput[middlePosition-1])
            # print("Caso :" + auxInput + " outpur = " +
            #       auxInput[middlePosition-1])

    print(output)
    # print(lenCase)
    # print(inputCase)
