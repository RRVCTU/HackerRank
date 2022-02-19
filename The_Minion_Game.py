def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    size = len(string)

    for i in range(size):
        if string[i] in vowels:
            kevin_score = kevin_score + (size - i)
        else:
            stuart_score = stuart_score + (size - i)

    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif stuart_score < kevin_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)