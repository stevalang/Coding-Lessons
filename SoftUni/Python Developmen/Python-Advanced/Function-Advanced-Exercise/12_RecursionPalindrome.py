def palindrome(word, index):
    if index >= int(len(word)/2):
        return f"{word} is a palindrome"
    if word[index] == word[len(word)-1 - index]:
        return palindrome(word, index + 1)

    return f"{word} is not a palindrome"







# print(palindrome("abcba", 0))
# abcba is a palindrome
print(palindrome("peter", 0))
# peter is not a palindrome

