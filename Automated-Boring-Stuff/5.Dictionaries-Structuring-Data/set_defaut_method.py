"""
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
"""

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
