def count_characters(input_string):
    dict = {}
    for character in input_string:
        if character in dict:
            dict[character] += 1
        else:
            dict[character] = 1
    return dict

test = "AABCCHELLO"
print(count_characters(test))
