# {typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}
# High = 89#Low = 28#Medium = 77#Low = 23

fire = input().split("#")  # the needed water to put out the fire
water = int(input())
effort = 0
totalFire = 0

print("Cells:")
for cells in fire:
    args = cells.split(" = ")
    fire_level = int(args[1])
    fire_type = args[0]
    if water - fire_level >= 0:
        if fire_type == "High":
            if 80 < fire_level < 126:
                water -= fire_level
                effort += fire_level * 0.25
                totalFire += fire_level
                print(f"- {fire_level}")
        elif fire_type == "Medium":
            if 50 < fire_level < 81:
                water -= fire_level
                effort += fire_level * 0.25
                totalFire += fire_level
                print(f"- {fire_level}")
        elif fire_type == "Low":
            if 0 < fire_level < 51:
                water -= fire_level
                effort += fire_level * 0.25
                totalFire += fire_level
                print(f"- {fire_level}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {totalFire}")
