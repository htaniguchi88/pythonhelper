input = ['地上波', 'ダメ', '絶対！！']
array = []
j = 0

def fetch_onecycle(arg_list):
    for i in range(len(arg_list)):
        target_list = list(arg_list[i])
        if j+1 <= len(target_list):
            array.append(target_list[j])
            print(target_list[j])
        else: 
            pass

while j <= len(max((x for x in input), key=len)):
    fetch_onecycle(input)
    j += 1

print(array)

array_string = "".join(array)

print('"' + array_string + ' " ')

