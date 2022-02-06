def rearrange(user_str):
    list_of_words = user_str.split()
    d = {}
    for word in list_of_words:
        num = 0
        digit = [int(ch) for ch in word if (ord(ch)>47) and (ord(ch)<58)]
        for i in range(len(digit)):
            num = num * 10 + digit[i]

        d[num] = word.replace(str(num), '')

    list_k = list(d.keys())
    list_k.sort()
    res_str = ''
    for i in list_k:
        res_str += d[i] + ' '

    return res_str[:-1]


input_str = input('input string: ')
print(rearrange(input_str))
