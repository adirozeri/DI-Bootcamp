print('please add a comma seperateds equence of words: ')
# words = input()
words = 'Write,a,program,that,accepts,a,comma,separated,sequence,of,words,as,input,and,prints,the,words,in,a,comma,separated,sequence,after,sorting,them,alphabetically'
current_word = ''
words_list = []
i=0
j=0
while i < len(words):
    # input()
    # print(f'big while i = {i}')

    if words[i] == ',' or i == len(words)-1:
        # print(f'j= {j} i = {i}')
        word = ''.join(words[j:i])
        # print(word)
        words_list.append(word)
        # print(f'words_list {words_list}')
        j=i+1

        # print(f'current_word = {current_word}')
    
    i = i + 1
print(sorted(words_list, key=lambda x: (x.lower(), x)))
# print(words_list[0])