from jamo import h2j, j2hcj

class Syllable(object):
    def __init__(self, char):
        self.char = char
        self.initial = ''
        self.medial = ''
        self.final = ''
        self.double_final = ''
        self.separate()


    def separate(self):
        result = list(j2hcj(h2j(self.char)))
        self.initial = result[0]
        self.medial = result[1]
        self.final = result[2] if(len(result) > 2) else  ''
        return result

    def search_key(self):
        functions_search = { 
            "before_i": self.starts_with_i, 
            "before_vowel" : self.starts_with_vowel,
            "before_n" : self.initial_is_n,
            "before_s" : self.initial_is_s,
        }
        equiv_key = None
        for key in functions_search:
            if(functions_search[key]()):
                equiv_key = key
                break
        return equiv_key


    def starts_with_vowel(self):
        return self.initial == 'ㅇ'

    
    def starts_with_i(self):
        return (self.starts_with_vowel() and self.medial_is_i())

    
    def medial_is_i(self):
        return self.medial == 'ㅣ'


    def initial_is_s(self):
        return self.initial == 'ㅅ'


    def initial_is_n(self):
        return self.initial == 'ㄴ'


    def initial_is_d(self):
        return self.initial == 'ㄷ'

    def final_is_ps(self):
        return self.final == 'ㅄ'


    def final_is_ss(self):
        return self.final == 'ㅆ'



