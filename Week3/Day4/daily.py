import re
class Text:

    def __init__(self, text):
        self.text = text

        # word_list = text.replace(' ','\n').replace('\n',' ').splitlines()
        word_list = re.findall(r"\b\w+(?:'\w+)?\b", text)
        self.word_freq = {}
        for word in word_list: 
            word = word.lower()
            if word in self.word_freq.keys():
                self.word_freq.update({word:self.word_freq[word]+1})
            else:
                self.word_freq.update({word:1})

        
        self.word_freq=sorted(self.word_freq.items(),key= lambda x: x[1])
        # print(self.word_freq)
    
    def freq(self, word):
        try:
            return dict(self.word_freq)[word]
        except KeyError as e:
            print(f'freq method exception - the word {e} is not in text')
            
        except Exception as e:
            print(f'freq method exception - {e}')
            return None
    
    def common(self):
        try:
            return self.word_freq[-1][0]
        except IndexError:
            print('common method exception - empty text')
            return None
        except Exception as e:
            print(f'common method exception - {e}')
            return None
        
    
    def unique(self):
        try:
            return [x[0] for x in self.word_freq if x[1]==1]
        except IndexError:
            print('unique method exception - empty text')
            return None
        except Exception as e:
            print(f'unique method exception - {e}')
            return None
    
    @classmethod
    def from_file(cls, filename):
        with  open(filename, 'r') as file:
            file_content = file.read()
        # print(file_content)
        return cls(file_content)
    

# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Note: Instead of creating a child class, you could also implements those methods as static methods in the Text class.

# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)        
class TextModification(Text):

    def __init__(self, text):
        super().__init__(text)

    def remove_punct(self):
        return re.sub(r'[^0-9a-zA-Z \n]+', '', self.text, count=0, flags=0)




file_path = r'Week3/Day4/assets/the_stranger.txt'
ta = Text.from_file(file_path)
    
text = '''
a3.
a3.
a3
a3
c4
c4
c4
'''
# ta = Text(text)
ta = TextModification(text)
print(f'freq(a)={ta.freq('a')}')
print(f'common {ta.common()}')
print(f'unique {ta.unique()}')
print(f'remove_punct-----------------------\n{ta.remove_punct()}----------------------')











