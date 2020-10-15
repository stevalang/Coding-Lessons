from collections import defaultdict
import os
import pathlib

directory = input()

directory_dict = defaultdict

for root, dirs, files in os.walk(directory):
    for file in files:
        extension = '.' + file.split('.')[-1]

        directory_dict[extension].append(file)

final_output = ''

for extension in sorted(directory_dict.keys()):
    final_output += extension + '\n'
    for file in sorted(directory_dict[extension]):
        final_output += f'---{file}\n'

print(final_output)

desktop = str(pathlib.Path.home()) + os.path.sep + 'Desktop'
report_path = desktop + os.path.sep + 'report.txt'
with open(report_path, 'x') as file:
    file.write(final_output)


