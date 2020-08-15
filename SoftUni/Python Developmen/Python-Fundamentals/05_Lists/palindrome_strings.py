def is_palindrome(word):
    return word == word[::-1]


words = input().split()
palindromes = [word for word in words if is_palindrome(word)]
second_word = input()

print(f'{palindromes}')
print(f'Found palindrome {palindromes.count(second_word)} times')