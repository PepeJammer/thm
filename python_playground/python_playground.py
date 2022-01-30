hash = 'dxeedxebdwemdwesdxdtdweqdxefdxefdxdudueqduerdvdtdvdu'

def int_to_string(arr):
    txt = ''
    for i in range(0,len(arr),2):
        txt += (chr(arr[i]*26+arr[i+1]))
    return txt

def string_to_int(str):
    intArr =[]
    for l in str:
        intArr.append(ord(l)-97)
    return intArr

password=int_to_string(string_to_int(int_to_string(string_to_int(hash))))
print(password)

