class AnagramChecker:
    def __init__(self, ) -> None:
        with open(r'c:/DI_Bootcamp/Week3/day5/sowpods.txt') as file:
            lines = file.readlines()
        self.words = [line.strip() for line in lines]
        
    def is_valid_word(self, word):
        return word.upper() in self.words



    def get_anagrams(self, word):
        word = word.upper()
        total_anagrams=[]
        char_count = { char : word.count(char) for char in word}
        for valid_word in self.words:
            if char_count == { char : valid_word.count(char) for char in valid_word.upper()}:
                total_anagrams.append(valid_word)
        return total_anagrams 
        

# lala=[  
# 'BADDER',
# 'BADDE','apers']
# d = AnagramChecker()
# for a in lala:
#     print(f'word is {a} num of anagrams is {d.get_anagrams(a)}')