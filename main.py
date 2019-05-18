from num2words import num2words
import sys
import re


operations = {
    '+': 'plus',
    '-': 'minus',
    '*': 'multiply',
    '/': 'divide',
    '=': 'equals',
}


def transformation(expression: str):
    resp = []
    dig = ''
    reg = r'^((\-)?(\d+)[\+\-\/\*]){1,}(\d+)(=(\-)?(\d+)){1}$'
    expression = ''.join(expression.split())
    if re.match(reg, expression) is not None:
        for i in expression:
            if i.isdigit():
                dig += i
            elif i in operations.keys():
                try:
                    resp.append(num2words(int(dig), lang='en'))
                except ValueError:
                    pass
                resp.append(operations.get(i))
                dig = ''
        if dig:
            resp.append(num2words(int(dig), lang='en'))
        return ' '.join(resp)
    return 'invalid input.'


if __name__ == '__main__':
    for expression in sys.stdin:
        print(transformation(expression))


