cards = input().split()
shuffles_count = int(input())
middle_length = len(cards) // 2
for _ in range(shuffles_count):
    result = []
    for index in range(middle_length):
        first_card = cards[index]
        current_index_second_deck = index + middle_length
        second_card = cards[current_index_second_deck]

        result.append(first_card)
        result.append(second_card)
    cards = result
print(result)