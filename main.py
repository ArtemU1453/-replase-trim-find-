greeting = "Hello world"


def find(sourceStr, subStr):
    for i in range(len(sourceStr)):
        if sourceStr[i: i + len(subStr)] == subStr:
            return i
    return -1

    i = 0
    matches = False

    while i < sourceLength:
        matches = False
        j = 0

        while j < substrLength:
            if sourceStr[i + j] == subStr[j]:
                matches = True
            else:
                matches = False
                break
            j = j + 1

        if matches:
            result = i

        i = i + 1

    return result


print(find("     Hello world  ", "world"))

greeting = "Hello world"


def trim(sourceStr):
    space = ' '
    tab = '\t'
    resultStr = ''

    inWordLeft = False
    inWordRight = False

    strLength = len(sourceStr)
    i = 0
    j = strLength - 1

    while i < strLength:
        if (sourceStr[i] != space) and (sourceStr[i] != tab):
            inWordLeft = True

        if (sourceStr[j] != space) and (sourceStr[j] != tab):
            inWordRight = True

        if inWordLeft and inWordRight:
            break
        else:
            if not inWordLeft:
                i = i + 1

            if not inWordRight:
                j = j - 1

    while i <= j:
        resultStr = resultStr + sourceStr[i]
        i = i + 1

    return resultStr


print(trim("  Hello World     "))


greeting = "Hello world"

def replace(sourceStr, templateStr, newSubstr, findAll = False):
    if templateStr == newSubstr:
        return sourceStr
    sourceLength = len(sourceStr)
    templateLength = len(templateStr)
    i = 0

    while i < sourceLength:
        matches = False
        j = 0
        while j < templateLength:
            if sourceStr[i + j] == templateStr[j]:
                matches = True
            else:
                matches = False
                break
            j = j + 1

        if matches:
            firstPart = ''
            secondPart = ''
            k = 0

            while k < i:
                firstPart = firstPart + sourceStr[k]
                k = k + 1
            k = i + templateLength
            while k < sourceLength:
                secondPart = secondPart + sourceStr[k]
                k = k + 1
            sourceStr = firstPart + newSubstr + secondPart
            if findAll == False:
                break

        i = i + 1

        return sourceStr

print(replace("Hello world", "wo", "Wo", False))
