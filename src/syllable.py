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
