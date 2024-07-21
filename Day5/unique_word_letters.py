def unique_word_letters(word):
    list_of_letters = list(set(word))

    list_of_letter = [letter for letter in list_of_letters if letter.isalpha() and letter.strip() != '']

    list_of_letter.sort()

    return list_of_letter


print(unique_word_letters('letter    to my  aunt and uncle!'))


# another solution

def unrepited_letters(word):
    my_set = set()

    for letter in word:
        my_set.add(letter)

    my_list = list(my_set)
    my_list.sort()

    return my_list


print(unrepited_letters('pineapple'))
