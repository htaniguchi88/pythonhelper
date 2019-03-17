def interleave_all_characters(input):

    array = []
    j = 0

    def interleave_one_character_of_each_word(input):
        for i in range(len(input)):
            one_word_list = list(input[i])
            if j+1 <= len(one_word_list):
                array.append(one_word_list[j])
            else:
                pass

    while j <= len(max((k for k in input))):
        interleave_one_character_of_each_word(input)
        j += 1

    output = "".join(array)

    print('Output: "' + output + '"')

    return output
