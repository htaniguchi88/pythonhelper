def interleave_all_characters(words_list):

    array = []
    j = 0

    def interleave_one_character_of_each_word(words_list):
        for i in range(len(words_list)):
            one_word_list = list(words_list[i])
            if j+1 <= len(one_word_list):
                array.append(one_word_list[j])
            else:
                pass

    while j <= len(max((k for k in words_list))):
        interleave_one_character_of_each_word(words_list)
        j += 1

    array_string = "".join(array)

    print('Output: "' + array_string + '"')

    return array
