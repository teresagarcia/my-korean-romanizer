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


    def starts_with_vowel(self):
        return self.initial == 'ㅇ'

    
    def starts_with_i(self):
        return (self.starts_with_vowel() and self.medial_is_i())

    
    def medial_is_i(self):
        return self.medial == 'ㅣ'


    def initial_is_s(self):
        return self.initial == 'ㅅ'
