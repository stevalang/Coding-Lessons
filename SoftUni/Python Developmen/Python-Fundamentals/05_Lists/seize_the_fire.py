"""
The group of adventurists have gone on their first task. Now they have to walk through fire - literally. They have to use all of the water they have left. Your task is to help them survive.
Create a program that calculates the water that is needed to put out a "fire cell", based on the given information about its "fire level" and how much it gets affected by water.
First, you will be given the level of fire inside the cell with the integer value of the cell, which represents the needed water to put out the fire.  They will be given in the following format:
"{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}……"
Afterwards you will receive the amount of water you have for putting out the fires. There is a range of fire for each of the fire types, and if a cell’s value is below or exceeds it, it is invalid and you don’t need to put it out.

If a cell is valid, you have to put it out by reducing the water with its value. Putting out fire also takes effort and you need to calculate it. Its value is equal to 25% of the cell’s value. In the end you will have to print the total effort. Keep putting out cells until you run out of water. If you don’t have enough water to put out a given cell – skip it and try the next one. In the end, print the cells you have put out in the following format:
"Cells:
 - {cell1}
 - {cell2}
 - {cell3}
……
 - {cellN}"
"Effort: {effort}"
In the end, print the total fire you have put out from all of the cells in the following format: "Total Fire: {totalFire}"
Input / Constraints
On the 1st line you are going to receive the fires with their cells in the format described above – integer numbers in the range [1…500]
On the 2nd line, you are going to be given the water – an integer number in the range [0….100000]
Output
Print the cells, which you have put out in the following format:
"Cells:
 - {cell}
 - {cell2}
 - {cell3}
 - {cell5}
……
 - {cellN}"
Print the effort, rounded 2 digits after the decimal separator in the following format:
"Effort: {effort}"
Print the total fire put out
"Total Fire: {totalFire}"

"""

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
