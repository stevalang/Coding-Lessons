def almost_there(num):
    if 90 <= num <=110 or 190 <= num <= 210:
        print(True)
        return True

    else:
        print(False)
        return False


def almost_there_abs(num):
    return (abs(100-num) <= 10) or (abs(200-num) <= 10)


almost_there(int(input()))
