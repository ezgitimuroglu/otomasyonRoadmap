while True:
    min = int(input("enter minimum: "))
    max = int(input("enter maximum: "))
    toDivide = int(input("enter number to divide: "))
    numberInSequence = min + 1
    numbersList = []
    while numberInSequence < max:
        if numberInSequence % toDivide == 0:
            numbersList.append(numberInSequence)
            numberInSequence += 1
        else:
            numberInSequence += 1
    else:
        print(numbersList)
        print(f'there are {len(numbersList)} numbers between {min} and {max} that is divisible by {toDivide}')
