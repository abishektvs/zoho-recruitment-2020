
def print_string(inp_str):
    mid = len(inp_str)//2
    str_len = len(inp_str)

    for i in range(1, str_len+1):

        if mid + i <= str_len:
            print((str_len-i) * ' ' + inp_str[mid: mid + i])
        else:
            print((str_len-i) * ' ' + inp_str[mid: ] + inp_str[0: mid - (str_len - i)])

inp = input()
print_string(inp)