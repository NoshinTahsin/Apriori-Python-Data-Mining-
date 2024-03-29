DELIMITER = ","


def main():
    dataset = readFile()
    print("Dataset :")
    print(dataset)

    L1 = find_frequent_1_itemsets(dataset)
    print(L1)


    ItemsetsLevel, ItemsetsCounter = apriori(dataset)

    Print(ItemsetsLevel, ItemsetsCounter)
    given, conValue = Input()
    Confidence(ItemsetsLevel, ItemsetsCounter, given, conValue)


def readFile():
    file = open("tapriori", "r+")
    dataset = list()
    while True:
        line = file.readline().strip()
        item = line.split(" ")
        if not line:
            break
        dataset.append(item[1])

    return dataset


def apriori(dataset):
    threshold = 2
    resultLevel = list()
    resultCounter = list()

    candidate = find_frequent_1_itemsets(dataset)
    print(candidate)

    Level, L_count = has_Minimum_Support_Counter(dataset, candidate, threshold)

    resultLevel.append(Level)
    resultCounter.append(L_count)

    print("Result level")
    print(resultLevel)


    print("LLLLL")
    print(Level)

    while Level:
        candidate = candidate_generator(Level)

        print(candidate)
        print(Level)

        candidate = has_frequent_subset(candidate, Level)

        print("Candidate")
        print(candidate)

        Level, L_count = has_Minimum_Support_Counter(dataset, candidate, threshold)

        resultLevel.append(Level)
        resultCounter.append(L_count)

    print("Result level")
    print(resultLevel)

    return resultLevel, resultCounter


def has_Minimum_Support_Counter(dataset, L, threshold):
    counter = list()
    Level = list()

    for a in L:
        count = 0
        items = a.split(DELIMITER)

        for bought in dataset:
            flag = True
            for i in range(len(items)):
                if items[i] not in bought:
                    flag = False
                    break
            if flag == True:
                count += 1
        if count >= threshold:
            counter.append(count)
            Level.append(a)
    return Level, counter


def has_frequent_subset(candidate, L):
    toBeDeleted = list()

    for elements in candidate:
        items = elements.split(DELIMITER)
        itemLen = len(items)

        flag = True
        for j in range(itemLen):
            subset = ""
            subsetLen = 0
            for k in range(itemLen):
                if j != k:
                   subset += items[k]
                   subsetLen += 1
                   if itemLen - 1 != subsetLen:
                      subset += DELIMITER

            print("subset:::")
            print(subset)

            if subset not in L:

                print("subset not in L::::")
                print(subset)

                flag = False
                break

        if flag == False:
            toBeDeleted.append(elements)
            print("Elements to be deleted")
            print(elements)

    candidate = [values for values in candidate if values not in toBeDeleted]
    return candidate


def candidate_generator(L):
    candidate = set()
    length = len(L)

    for i in range(length):
        for j in range(i + 1, length):
            itemsI = L[i].split(DELIMITER)
            itemsJ = L[j].split(DELIMITER)
            flag = 1
            for x in range(len(itemsI) - 1):
                if itemsI[x] != itemsJ[x]:
                    flag = 0
            if flag:
                new = L[i] + DELIMITER
                #print("newww")
                #print(new)

                new = new+ itemsJ[-1]
                #print(new)

                candidate.add(new)

    return list(sorted(candidate))


def find_frequent_1_itemsets(dataset):
    level1 = set()
    for elements in dataset:
        items = elements.split(DELIMITER)
        for i in range(len(items)):
            level1.add(items[i])

    return list(sorted(level1))


def Print(Level, counter):
    for i in range(len(Level)):
        if not Level[i]:
            break
        print("Level %d: " % (i + 1))
        print(Level[i])
        print('========================================')
        for j in range(len(Level[i])):
            print("'{0}'\t\t" .format(Level[i][j]), counter[i][j])



def Input():
    ans = input("Want to find confidence? (y/n)\n")
    if ans == "y":
        given = input("Given? (Format: I1,I2)\n")
        conFor = input("Confidence For? (Format: I5)\n")
        givenList = given.split(DELIMITER)
        conForList = conFor.split(DELIMITER)

        conValueList = list()
        conValueList.extend(givenList)
        conValueList.extend(conForList)
        conValueList = sorted(conValueList)

        conValue = ""
        for i in range(len(conValueList)):
           conValue += conValueList[i]
           if i != len(conValueList) - 1:
              conValue += DELIMITER

        return given, conValue



def Confidence(Level, counter, given, conValue):
    flagG, flagV = False, False
    countG, countV = 0, 0
    for i in range(len(Level)):
        if given in Level[i]:
            flagG = True
            countG = counter[i] [Level[i].index(given)]
        if conValue in Level[i]:
            flagV = True
            countV = counter[i] [Level[i].index(conValue)]

        if flagG and flagV:
            break

    if flagG and flagV:
        confidence = (countV / countG) * 100.0
        print("Confidence of {0} GIVEN {1} : {2:.2f}%" .format(conValue, given, float(confidence)))
    else:
       print("==SPECIFIED ITEMS ARE INFREQUENT==")


if __name__ == '__main__':
    main()









