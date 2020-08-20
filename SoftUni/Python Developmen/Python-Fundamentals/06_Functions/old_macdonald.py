def old_macdonald(name):
    print(name[0].upper() + name[1:3] + name[3].upper() + name[4::])


def old_macdonald_capitalize(name):
    first_part = name[:3]
    second_part = name[3:]

    return first_part.capitalize() + second_part.capitalize()


old_macdonald("macdonalds")
