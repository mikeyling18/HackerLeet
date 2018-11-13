vowels = ['A', 'E', 'E', 'O', 'U']
stuart_dict = {}
kevin_dict = {}


def is_vowel(char):
    if char in vowels:
        return True
    else:
        return False


def create_stuart_dict(string):
    for i in range(len(string)):
        score = 0
        current_substring = string[0:i + 1]
        for char in range(len(string)):
            score += string[char: char + len(current_substring)] == current_substring
        # print('{} {}'.format(current_substring, score))
        if current_substring not in stuart_dict.keys():
            stuart_dict[current_substring] = score


def create_kevin_dict(string):
    for i in range(len(string)):
        score = 0
        current_substring = string[0:i + 1]
        for char in range(len(string)):
            score += string[char: char + len(current_substring)] == current_substring
        if current_substring not in kevin_dict.keys():
            kevin_dict[current_substring] = score


def minion_game(string):
    start_index = 0
    for i in range(start_index, len(string)):
        if is_vowel(string[i]) is True:
            create_kevin_dict(string[i:])
        else:
            create_stuart_dict(string[i:])

    kevinScore = sum(kevin_dict.values())
    stuartScore = sum(stuart_dict.values())
    if kevinScore > stuartScore:
        print('Kevin {}'.format(kevinScore))
    elif kevinScore < stuartScore:
        print('Stuart {}'.format(stuartScore))
    else:
        print('Draw')
