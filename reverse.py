def reverse_all_characters(input):
    output_list = [str(i) for i in reversed(input)]
    output = ''.join(output_list)

    print('Output: "' + output + '"')

    return output
