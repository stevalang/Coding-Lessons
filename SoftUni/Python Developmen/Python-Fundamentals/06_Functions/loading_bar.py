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