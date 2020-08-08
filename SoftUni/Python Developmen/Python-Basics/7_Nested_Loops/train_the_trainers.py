judge_count = int(input())
presentation_name = input()
presentation_counter = 0
score_average_training = 0
while presentation_name != 'Finish':
    total_score_presentation = 0
    score_average_presentation = 0
    presentation_name = str(presentation_name)
    for i in range(1, judge_count + 1):
        score = float(input())
        total_score_presentation += score
        score_average_presentation = total_score_presentation / i
    print(f'{presentation_name} - {score_average_presentation:.2f}.')
    score_average_training += score_average_presentation
    presentation_counter += 1
    presentation_name = input()
print(f"Student's final assessment is {(score_average_training / presentation_counter):.2f}.")
