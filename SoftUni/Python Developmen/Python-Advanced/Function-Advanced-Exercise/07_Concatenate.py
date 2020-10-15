def concatenate(*args):
    if len(args) == 1:
        return args[0]
    return args[0] + concatenate(*args[1:])


print(concatenate("Soft", "Uni", "Is", "Great", "!"))