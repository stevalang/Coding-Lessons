"""

Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words
2.00 – 2.99 - "Fail"
3.00 – 3.49 - "Poor"
3.50 – 4.49 - "Good"
4.50 – 5.49 - "Very Good"
5.50 – 6.00 - "Excellent"

"""

def is_fail(grade):
    return 2.00 <= grade <= 2.99


def is_poor(grade):
    return 3.00 <= grade <= 3.49


def is_good(grade):
    return 3.50 <= grade <= 4.49


def is_very_good(grade):
    return 4.50 <= grade <= 5.49


def is_excellent(grade):
    return 5.50 <= grade <= 6.00


def solve(grade):
    grades = [
        [is_fail, "Fail"],
        [is_poor, "Poor"],
        [is_good, "Good"],
        [is_very_good, "Very Good"],
        [is_excellent, "Excellent"],
    ]
    for fn, result in grades:
        if fn(grade):
            return result
    # for item in grades:
    #     fn = item[0]
    #     result = item[1]
    #     if fn(grade):
    #         return result


grade = float(input())
print(f"{solve(grade)}")


# if 2.00 <= grade <= 2.99:
#     return "Fail"
# if 2.00 <= grade <= 2.99:
#     return "Fail"
# if 2.00 <= grade <= 2.99:
#     return "Fail"
# if 2.00 <= grade <= 2.99:
#     return "Fail"
