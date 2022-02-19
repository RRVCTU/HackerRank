def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        unique = ''
        for character in string[i:i+k]:
            if character not in unique:
                unique = unique + character
        print(unique)


if __name__ == '__main__':
    # string, k = input(), int(input())
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)
