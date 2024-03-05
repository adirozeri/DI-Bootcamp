
def seperator(words,seperator):
    i=0
    j=0
    words_list = []
    while i < len(words):
        if words[i] == seperator:
            word = ''.join(words[j:i])
            words_list.append(word)
            j=i+1
        elif i == len(words)-1:
            word = ''.join(words[j:i+1])
            words_list.append(word)
        i = i + 1
    return words_list


words = 'Apple,banana,cat,Dog,apple'
words_comma = 'zzz xxx 123456 23s4567 bbb dnnn'


comma_sorted = sorted(seperator(words,','), key=lambda x: x.lower())
print(f'sorted with commas :{','.join(comma_sorted)}')

print(f'first longet {sorted(seperator(words_comma,' '), key = lambda x: -len(x))[0]}')