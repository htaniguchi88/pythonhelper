def reverse(input):
  input_list = list(input)
 #for character in (reversed(str_list)):
  output_list = [str(i) for i in reversed(input)]
  output = ''.join(output_list)

  print('Output: "' + output + '"')

  return output
