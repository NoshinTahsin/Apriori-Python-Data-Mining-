def takeInputFromFile():
    file = open("AprioriDataset", "r+")
    transaction = list()
    while True:
        line = file.readline().strip()
        item = line.split(":")
        if not line:
            break
        transaction.append(item[1])

    return transaction


def apriori(transaction):
    threshold = 2
    listToAppendLevel = list()
    listToAppendSupportCount= list()

    uniqueItemSet = getUniqueItemSet(transaction)
    print(uniqueItemSet)

    level, supportCount = satisfyThreshold(transaction, uniqueItemSet, threshold)

    listToAppendLevel.append(level)
    listToAppendSupportCount.append(supportCount)

    print("listToAppendLevel ")
    print(listToAppendLevel)


    print("level")
    print(level)

    while level:
        next_L = getNext_L(level)

        print(next_L)
        print(level)

        #uniqueItemSet = has_frequent_subset(candidate, Level)

        print("")
        print(next_L)

        level, supportCount = satisfyThreshold(transaction, next_L, threshold)

        listToAppendLevel.append(level)
        listToAppendSupportCount.append(supportCount)

    return listToAppendLevel, listToAppendSupportCount


def satisfyThreshold(transaction, L_to_Check, threshold):
    supportCount = list()
    level = list()

    for checker in L_to_Check:
        count = 0
        elements = checker.split(",")

        for row in transaction:
            flag = True
            for i in range(len(elements)):
                if elements[i] not in row:
                    flag = False
                    break
            if flag == True:
                count += 1

        if count >= threshold:
            supportCount.append(count)
            level.append(checker)

    return level, supportCount


def getNext_L(L1):
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



def getUniqueItemSet(transaction):
    uniqueItemSet = set()
    for row in transaction:
        items = row.split(",")
        for i in range(len(items)):
            uniqueItemSet.add(items[i])

    return list(sorted(uniqueItemSet))



def Input(finalLevel,finalCounter):

        first = input("Enter first input\n")
        second = input("Enter second input)\n")
        firstList = first.split(",")
        secondList = second.split(",")



        unionList = []
        unionList.extend(firstList)
        unionList.extend(secondList)
        unionList = sorted(unionList)

        unionValue = ""
        for i in range(len(unionList)):
           unionValue += unionList[i]
           if i != len(unionList) - 1:
              unionValue += ","

        #return first, unionValue


        firstCount=-1
        secondCount=-1

        for i in range(len(finalLevel)):
            if first in finalLevel[i]:
                firstCount = finalCounter[i] [finalLevel[i].index(first)]
            if unionValue in finalLevel[i]:
                unionCount = finalCounter[i] [finalLevel[i].index(unionValue)]



        if firstCount!=-1 and secondCount!=-1:
            confidence = (unionCount / firstCount) * 100.0
            print("Confidence")
            print(confidence)
        else:
            print("Items are infrequent")


def main():
    transaction = takeInputFromFile()
    print("Transaction data :")
    print(transaction)

    uniqueset = getUniqueItemSet(transaction)
    print(uniqueset)


    finalLevel, finalCounter = apriori(transaction)

    #printing the levels
    for i in range(len(finalLevel)):
        if not finalLevel[i]:
            break
        print("Printing L %d: " % (i + 1))

        for j in range(len(finalLevel[i])):
            print(finalLevel[i][j])
            print(finalLevel[i][j])


    Input(finalLevel,finalCounter)


if __name__ == '__main__':
    main()
