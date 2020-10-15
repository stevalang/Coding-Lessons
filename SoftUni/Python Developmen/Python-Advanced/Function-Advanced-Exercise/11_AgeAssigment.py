def age_assignment(*args, **kwargs):
    age_dict = {}

    for name in args:
        age = kwargs[name[0]]
        age_dict[name] = age

    return age_dict


print(age_assignment("Peter", "George", G=26, P=19))
