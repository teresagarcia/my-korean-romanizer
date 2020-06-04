from jamo import h2j, j2hcj

class Syllable(object):
    def __init__(self, char):
        self.char = char
        self.initial = ''
        self.medial = ''
        self.final = ''
        self.double_final = ''
        if self.is_hangul():
            self.separate()

    def is_hangul(self):
        value = ord(self.char)
        return 0xAC00 <= value <= 0xD7A3

    def separate(self):
        result = list(j2hcj(h2j(self.char)))
        self.initial = result[0]
        self.medial = result[1]
        self.final = result[2] if(len(result) > 2) else  ''
        return result
