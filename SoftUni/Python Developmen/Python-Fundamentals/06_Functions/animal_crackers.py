def animal_crackers(string):
    words = string.lower().split()
    return words[0][0] == words[1][0]


animal_crackers(input())