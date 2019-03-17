def interleave_all_characters(words_list):

    array = []
    j = 0

    def interleave_one_character_of_each_word(_list):
        for i in range(len(words_list)):
            one_word_list = list(words_list[i])
            if j+1 <= len(one_word_list):
                array.append(one_word_list[j])
            else:
                pass

    while j <= len(max((k for k in input), key=len)):
        interleave_one_character_of_each_word(input)
        j += 1

    array_string = "".join(array)

    print('Output: "' + array_string + ' " ')
