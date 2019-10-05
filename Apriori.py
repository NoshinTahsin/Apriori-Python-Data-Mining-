##################mynewgeneric
transaction=[]
minSupportCount=2

def inputTransactionFromFile(fileName):
    file1 = open(fileName,"r+")
    while True:
        line =file1.readline()
        if not line:
            return transaction

        line = line.rstrip('\n')
        listFromLine = line.split(",")
        listFromLine.pop(0)
        transaction.append(listFromLine)
#EndOfFunction

def createUniqueElementList(inputData):

    uniqueElementList = []

    for eachTransaction in inputData:
        for element in eachTransaction:
            if not element in uniqueElementList:
                uniqueElementList.append(element)

    #uniqueElementList.sort(reverse=True)
    print(uniqueElementList)

    return sorted(uniqueElementList)
#EndOfFunction


def canBeAcceptedAsL(threshold,dataset,uniqueElementList):
    L=[]
    supCountL=[]

    for unique in uniqueElementList:
        uniqueElement=unique.split(",")
        supportCount=0
        subset=""
        print(len(uniqueElement))

        for member in dataset:
            flag=True
            for i in range(0,len(uniqueElement)):
                if uniqueElement[i] not in member:
                    flag=False
                    break

            if flag==True:
                supportCount+=1

        if supportCount>=threshold:
            L.append(unique)
            supCountL.append(supportCount)

    return L,supCountL
#EndOfFunction



def getNextL(L1):
    length=len(L1)
    LToReturn=set()

    for i in range (0,length):
        for j in range(i+1,length):
            subset1=L1[i].split(",")
            subset2=L1[j].split(",")
            flag=True

            for k in range(len(subset1)):
                if(subset1[k]!=subset2[k]):
                    flag=False

            if flag:
                listToappend=L1[i]+","+L1[j][len(subset2)-1]

                print(listToappend)
                LToReturn.add(listToappend)

    return list(sorted(LToReturn))

def isFrequent(nextL,L):

    deleteList=[]

    for row in nextL:
        items=row.split(",")
        itemLength=len(items)

        flag=1

        for outerloop in range (0,itemLength):

            RowToCompare=""
            rowLength=0
            for innerloop in range(0,itemLength):
                if outerloop!=innerloop:
                   RowToCompare+=items[innerloop]
                   rowLength+=1
                   if rowLength!=itemLength-1:
                       RowToCompare+=","

            if RowToCompare not in L:
                 flag=0
                 break

        if flag==0:
            deleteList.append(row)


    nextL=[item for item in nextL if item not in deleteList]
    return nextL




def apriori(transaction):

    uniqueElementList=createUniqueElementList(transaction)
    #print(uniqueElementList)

    #acceptedL,supCntAccL

    threshold=2
    L1,L1_supportCount=canBeAcceptedAsL(threshold,transaction,uniqueElementList)
    #print("L1: ")
    #print(L1)
    #print(L1_supportCount)

    listToKeepLevels=[]
    listSupportCount=[]
    listToKeepLevels.append(L1)
    listSupportCount.append(L1_supportCount)

    print(L1)
    while L1:
        nextL=getNextL(L1)
        nextL=isFrequent(nextL,L1)

        dataset=[]

        for tran in transaction:
            strTran=""
            for itemTran in range(len(tran)):
                strTran+=tran[itemTran]

            dataset.append(strTran)

        level,levelSupCount=canBeAcceptedAsL(threshold,dataset,uniqueElementList)

        listToKeepLevels.append(level)
        listSupportCount.append(levelSupCount)

    return listToKeepLevels,listSupportCount


def main():
    transaction=inputTransactionFromFile("AprioriDataset ")
    print(transaction)

    #All_L,supportCount_for_L=\
    finalLevelList,finalLevelCountList=apriori(transaction)

    print(finalLevelList)
    print(finalLevelCountList)

main()




