people_number = int(input())
elevator_capacity = int(input())
counter_courses = 0
counter = 0
for i in range(1, people_number + 1):
    if elevator_capacity > people_number:
        print(1)
        break
    while people_number > elevator_capacity:
        people_number -= elevator_capacity
        counter += 1
    else:
        counter += 1
        break
print(counter)