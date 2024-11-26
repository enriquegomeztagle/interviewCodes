def isAnagram(word1, word2):
    print("\n----------------------------\nValidating anagram")
    print("Word 1:", word1)
    print("Word 2:", word2)
    
    if len(word1) != len(word2):
        return False
    
    count = {}
    
    for char in word1.lower():
        count[char] = count.get(char, 0) + 1
    
    print("Frequency count after word1:", count)
    
    for char in word2.lower():
        if char not in count or count[char] == 0:
            print("Character mismatch found:", char)
            return False
        count[char] -= 1
    
    print("Frequency count after word2:", count)
    
    return all(value == 0 for value in count.values())

print(isAnagram("cat", "rat"))  # False
print(isAnagram("mar", "ram"))  # True
print(isAnagram("Nile", "line"))  # True

####################################################################
#### Time Complexity:
## Final Time Complexity = O(n)

####################################################################

### Space Complexity:
## Final Space Complexity = O(k)

####################################################################