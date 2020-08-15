lines = int(input())
positive_list = []
negative_list = []
counter = 0
for _ in range(lines):
    number = int(input())
    if number >= 0:
        positive_list.append(number)
        counter += 1
    else:
        negative_list.append(number)
print(positive_list)
print(negative_list)
print(f"Count of positives: {counter}. Sum of negatives: {sum(negative_list)}")