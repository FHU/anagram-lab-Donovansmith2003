def anagram(wordOne, wordTwo):
    isMatch = False 
    alreadyUsed = []
    
    for x in wordOne:
        for y, i in enumerate(wordTwo):
            if x == y and not i in alreadyUsed:
                isMatch = True
                alreadyUsed.append(i)
        if isMatch == True:
            isMatch = False
        else:
            return False
    return True

if __name__ == '__main__':
    
    wordOne = input()
    wordTwo = input()
    
    print(anagram(wordOne, wordTwo))