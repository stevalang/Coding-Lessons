notes = []
while True:
    string = input()
    if string == 'End':
        break
    tokens = string.split('-')
    importance = int(tokens[0])
    task = tokens[1]
    notes.append((importance, task))
result = [task_name for importance, task_name in sorted(notes) if importance != 0]

print(result)
