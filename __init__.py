#oldmine

transaction=[]
minSupportCount=2

def inputTransactionFromFile(fileName):
    file1 = open(fileName,"r+")
    while True:
        line =file1.readline()
        if not line:
            return

        line = line.rstrip('\n')
        listFromLine = line.split(",")
        listFromLine.pop(0)
        transaction.append(listFromLine)

#EndOfFunction

numOfUniqueElement=0
uniqueElementList = []

def createUniqueElementList(inputData):

    for eachTransaction in inputData:
        for element in eachTransaction:
            if not element in uniqueElementList:
                uniqueElementList.append(element)

    uniqueElementList.sort(reverse=True)
    print(uniqueElementList)

#EndOfFunction

C1=[]
backUp=[]

def createC1() :
    while True:
        if not uniqueElementList:
            break

        d=uniqueElementList.pop()
        backUp.append(d)
        supportCount=0
        subsetList=[]
        subsetList.append(d)
        #print(subsetList)

        for row in transaction:
            if(all(x in row for x in subsetList)):
                supportCount+=1

        subsetList.append(supportCount)
        C1.append(subsetList)

    print("C1")
    print(C1)

#EndOfFunction


L1=[]

def createL1():
    for row in C1:
        if row[1]>=minSupportCount :
            L1.append(row)

    print("L1")
    print(L1)


def userPrompt():
    print("Enter first value")
    type1=input()
    print("Enter second value")
    type2=input()

    firstList=[]
    firstList.append(type1)
    firstList.append(type2)

    secondList=[]
    secondList.append(type1)

    for row in pL2:
        if(all(x in row for x in firstList)):
            getFirstValue=row[2]
            print(getFirstValue)

    for row in L1:
        if(all(x in row for x in secondList)):
            getSecondValue=row[1]
            print(getSecondValue)


    print("First")
    #print(getFirstValue)
    print("Second")
    #print(getSecondValue)
    confidence=(getFirstValue/getSecondValue)*100
    print(confidence)



inputTransactionFromFile("AprioriDataset")
createUniqueElementList(transaction)
createC1()
createL1()

print(backUp)
backUp.sort(reverse=True)

#l1 er/ l2er, that is, l(k-1) er proti row er length ber kore last column bad diye shob gula column er element ekta notun list e append korte hobe
#proti row er jonno emn korte hobe

k=2
numCol=len(L1[0])
print(numCol)

backUp1=[] #ekta file e rakhte hbe
C2=[]
c=0

popcnt=len(backUp)


for pp in range (0,popcnt):
    d=backUp.pop()
    backUp1.append(d)
    for row in L1:
        C2row=[]
        singly=[]
        for i in range (0,numCol-1):
            print("row[i}: " +row[i])
            C2row.append(row[i])
            print("C2row}: ")
            print(C2row)

            singly.append(d)
            print("singly")
            print(singly)

            supCount=0

            if(all(x in C2row for x in singly)):
                cp=2#backUp.append(d)
            else:
                C2row.append(d)
                print(C2row)
                for row in transaction:
                    if(all(x in row for x in C2row)):
                        supCount+=1


                C2row.append(supCount)
                C2.append(C2row)


#backUp list thke pop kore d te rekhe oi list e append korte hobe proti row er jonno
#check korte hobe d oi list er subset kina...subset hoile append kora jabena
#subset na hoile append korte hobe
#j list pailam oita hocche C(k) er ekta row
#eituk done



#ekhn count korte hobe oi list ta mulDimList er kon kon row er subset
#count er value tao oi list e append kore dite hobe
#oita k ekta notu list e append korte hbe vyrevy
#C[k]
print(C2)
#taile C(k) er ekta row pailam
pL2=[]
for row in C2:
        print(row)
        if row[numCol]>=minSupportCount :
            pL2.append(row)

print(pL2)

userPrompt()
#repeatation check
#loop kotobar cholbe determine kora
#user prompt
#process kore calculation kore output deya
