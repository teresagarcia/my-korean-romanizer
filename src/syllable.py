from jamo import h2j, j2hcj

class Syllable(object):
    def __init__(self, char):
        self.char = char
        self.initial = ''
        self.medial = ''
        self.final = ''
        if self.is_hangul(char):
            self.separate(char)

    def is_hangul(self, char):
        value = ord(char)
        return value >= 4352 and value <= 4607

    def separate(self, char):
        result = list(j2hcj(h2j(char)))
        self.initial = result[0]
        self.medial = result[1]
        self.final = result[2] if(result.__len__ == 2) else  ''
        return result
