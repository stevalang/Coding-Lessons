goal = 10000
steps = input()
steps_count = 0
is_going_home = False

while steps_count <= goal:
    if steps == "Going home":
        is_going_home = True
        steps_going_home = int(input())
        steps_count += steps_going_home
        if steps_count >= goal:
            print(f'Goal reached! Good job!')
            break
        else:
            print(f'{abs(goal - steps_count)} more steps to reach goal.')
            break
    else:
        steps = int(steps)
        steps_count += steps
        if steps_count >= goal:
            break
        steps = input()

if not is_going_home:
    print(f'Goal reached! Good job!')
