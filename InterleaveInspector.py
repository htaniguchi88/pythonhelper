input = ['地上波', 'ダメ', '絶対！！']
array = []
j = 0

def fetch_onecycle(arg_list):
    for i in range(len(arg_list)):
        target_list = list(arg_list[i])
        print(target_list[j])

while j <= len(max((x for x in input), key=len)):
    fetch_onecycle(input)
    j += 1

print(array)

