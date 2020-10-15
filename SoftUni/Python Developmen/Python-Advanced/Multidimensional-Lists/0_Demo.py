three_dimensions = [
    [
        # R    G    B   A
        [255, 255, 255, 50],
        [255, 255, 255, 0],

    ],
]

alpha_channel = three_dimensions[0][0][3]
print(alpha_channel)

three_dimensions[0][0][3] = 99

alpha_channel = three_dimensions[0][0][3]
print(alpha_channel)

print(three_dimensions)