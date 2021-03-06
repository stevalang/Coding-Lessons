def get_sub_expressions(expression):
    opening_bracket_indices = []
    sub_expression = []
    for i in range(len(expression)):
        ch = expression[i]
        if ch == '(':
            opening_bracket_indices.append(i)
        elif ch == ')':
            start_index = opening_bracket_indices.pop()
            end_index = i
            sub_expression.append(expression[start_index:end_index + 1 ])

    return sub_expression


expression = input()
sub_expressions = get_sub_expressions(expression)
[print(exp) for exp in sub_expressions]
