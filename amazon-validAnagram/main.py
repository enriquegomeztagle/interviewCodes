def isAnagram(word1, word2):
    print("\n----------------------------\nValidating anagram")
    print("Word 1: " + word1)
    print("Word 2: " + word2)
    if len(word1) != len(word2):
        return False
    else:
        word1 = sorted(word1.lower())
        print("Sorted word1: ", word1)
        word2 = sorted(word2.lower())
        print("Sorted word2: ", word2)
        for i in range(len(word1)):
            print("Letter: ", word1[i] , "Letter: ", word2[i])
            if word1[i] != word2[i]:
                print("Letter ", word1[i], " does not match letter ", word2[i])
                return False
        return True

print(isAnagram("cat", "rat"))
print(isAnagram("mar", "ram"))

print(isAnagram("Nile", "line"))