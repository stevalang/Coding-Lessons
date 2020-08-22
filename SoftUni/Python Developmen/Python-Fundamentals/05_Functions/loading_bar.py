"""

You will receive a single integer number between 0 and 100 which is divided with 10 without residue (0, 10, 20, 30...). 
Your task is to create a function that visualizes a loading bar depending on that number you have received in the input.

"""


# def loading_bar(num):
#     percent = ''
#     for i in range(num/10):
#          '%'.join(percent)
#     dots = ''
#     for i in range((100 - num)/10):
#          '.'.join(percent)
#     print(f'{num}% [{percent}{dots}]\nStill loading...')
#
#
# loading_bar(30)


def loading_bar(percentage):
    loading_bar_list = ["."] * 10
    end = int(percentage/10)
    if percentage == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        for i in range(0, end):
            loading_bar_list[i] = '%'
        print(f"{percentage}% [{''.join(loading_bar_list)}]")
        print("Still loading...")


loading_bar(int(input()))
