"""
The force users are struggling to remember which side are the different forceUsers from, because they switch them too often. So you are tasked to create a web application to manage their profiles. You should store an information for every unique forceUser, registered in the application.
You will receive several input lines in one of the following formats:
{forceSide} | {forceUser}
{forceUser} -> {forceSide}
The forceUser and forceSide are strings, containing any character. 
If you receive forceSide | forceUser, you should check if such forceUser already exists, and if not, add him/her to the corresponding side. 
If you receive a forceUser -> forceSide, you should check if there is such a forceUser already and if so, change his/her side. If there is no such forceUser, add him/her to the corresponding forceSide, treating the command as a new registered forceUser. Then you should print on the console: "{forceUser} joins the {forceSide} side!" 
You should end your program when you receive the command "Lumpawaroo". At that point you should print each force side, ordered descending by forceUsers count, than ordered by name. For each side print the forceUsers, ordered by name.
In case there are no forceUsers in a side, you shouldn`t print the side information. 
Input / Constraints
The input comes in the form of commands in one of the formats specified above.
The input ends, when you receive the command "Lumpawaroo".
Output
As output for each forceSide, ordered descending by forceUsers count, then by name,  you must print all the forceUsers, ordered by name alphabetically.
The output format is:
Side: {forceSide}, Members: {forceUsers.Count}
! {forceUser}
! {forceUser}
! {forceUser}
In case there are NO forceUsers, don`t print this side. 
"""

force_user = {}

while True:
    line = input()
    if line == "Lumpawaroo":
        break

    args = line.split()
    side = args[0]
    command = args[1]
    name = args[2]
    if command == '|':
        if side not in force_user:
            force_user[side] = []
        force_user[side].append(name)
    else:
        if side not in force_user:
            force_user[side] = [name]
        else:
            a = force_user.pop(force_user[side][name])
            force_user


sorted_users = dict(sorted(force_user.items(), key=lambda x: x[1]))
for key, value in sorted_users.items():
    print(f'Side: {key}, Members: {len(value)}')
    for name in value:
        print(f'! {name}')
