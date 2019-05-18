from humanize_calculator import transformation


def test_task_example():
    string = {'exp': '3 + 7 = 10'}
    assert transformation('{exp}'.format(**string)) == 'three plus seven equals ten'


def test_start_with_minus():
    string = {'exp': '-2 + 2 = 0'}
    assert transformation('{exp}'.format(**string)) == 'minus two plus two equals zero'


def test_random_space():
    string = {'exp': ' 3+  7=    10   '}
    assert transformation('{exp}'.format(**string)) == 'three plus seven equals ten'


def test_invalid_function():
    string = {'exp': '3 ** 3 = 9'}
    assert transformation('{exp}'.format(**string)) == 'invalid input.'


def test_has_alpha():
    string = {'exp': '3 * a = 9'}
    assert transformation('{exp}'.format(**string)) == 'invalid input.'


def test_one_long_function():
    string = {'exp': '-8 + 6 / 2 * 2 = -2'}
    assert transformation('{exp}'.format(**string)) == 'minus eight plus six divide two multiply two equals minus two'
