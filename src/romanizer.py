from jamo import h2j, j2hcj
from syllable import Syllable  
import re

vowels = {
    'ㅏ' : 'a',
    'ㅓ' : 'eo',
    'ㅗ' : 'o',
    'ㅜ' : 'u',
    'ㅡ' : 'eu',
    'ㅣ' : 'i',
    'ㅐ' : 'ae',
    'ㅔ' : 'e',
    'ㅚ' : 'oe',
    'ㅟ' : 'wi',
    
  
    'ㅑ' : 'ya',
    'ㅕ' : 'yeo',
    'ㅛ' : 'yo',
    'ㅠ' : 'yu',
    'ㅒ' : 'yae',
    'ㅖ' : 'ye',
    'ㅘ' : 'wa',
    'ㅙ' : 'wae',
    'ㅝ' : 'wo',
    'ㅞ' : 'we',
    'ㅢ' : 'ui', 
}

consonants = { 
    'ㄱ': {'initial': 'g', 'final': 'k'},
    'ㄷ': {'initial': 'd', 'final': 't'},
    'ㄹ': {'initial': 'r', 'final': 'l'},
    'ㅁ': {'all': 'm'},
    'ㄴ': {'all': 'n'},
    'ㅂ': {'initial': 'b', 'final': 'p'},
    'ㅅ': {'initial': 's', 'final': 't', 'pre_vocal': 's', 'before_i': 'sh'},
    'ㅇ': {'initial': '', 'final': 'ng'},
    'ㅈ': {'initial': 'j', 'final': 't', 'pre_vocal': 'j'},
    'ㅊ': {'initial': 'ch', 'final': 't', 'pre_vocal': 'ch'},
    'ㅋ': {'all': 'k'},
    'ㅌ': {'all': 't'},
    'ㅍ': {'all': 'p'},
    'ㅎ': {'all': 'h'},
    'ㄲ' : {'all': 'kk'},
    'ㄸ' : {'all': 'tt'},
    'ㅃ' : {'all': 'pp'},
    'ㅉ' : {'all': 'jj'},
    'ㅆ' : {'initial': 'ss', 'final': 't', 'pre_vocal': 'ss'},
}

double_consonant_final = {
    'ㄳ' : ('ㄱ', 'ㅅ'),
    'ㄵ' : ('ᆫ', 'ㅈ'), 
    'ᆭ' : ('ᆫ', 'ᇂ'),
    'ㄺ' : ('ㄹ', 'ㄱ'), 
    'ㄻ' : ('ㄹ', 'ㅁ'), 
    'ㄼ' : ('ㄹ', 'ㅂ'), 
    'ㄽ' : ('ㄹ', 'ㅅ'), 
    'ㄾ' : ('ㄹ', 'ㅌ'), 
    'ㄿ' : ('ㄹ', 'ㅍ'),
    'ㅀ' : ('ㄹ', 'ᇂ'), 
    'ㅄ' : ('ㅂ', 'ㅅ'), 
    'ㅆ' : ('ㅅ', 'ㅅ')
}


class Romanizer(object):
    def __init__(self, text):
        self.text = text

    def romanize(self):
        _romanized = ""
        for char in self.text:
            if(char.isspace() is False):
                syl = Syllable(char)
                _romanized += self.romanize_syllable(syl)
            else:
                _romanized += ' '
        return _romanized

    def romanize_syllable(self, syl):
        initial_rom = self.get_initial_rom(syl)
        medial_rom = self.get_medial_rom(syl)
        final_rom = self.get_final_rom(syl)
        romanized_syl = initial_rom + medial_rom + final_rom
        return romanized_syl

    def get_initial_rom(self, syl):
        letter = consonants.get(syl.initial)
        print(letter)
        romanization = letter.get('all') if(letter.get('all') is not None) else letter.get('initial')
        return romanization

    def get_medial_rom(self, syl):
        romanization = vowels.get(syl.medial)
        return romanization

    def get_final_rom(self, syl):
        letter = consonants.get(syl.final)
        romanization = ''
        if(letter is not None):
            print(letter)
            romanization = letter.get('all') if(letter.get('all') is not None) else letter.get('final')
        return romanization

r = Romanizer("오빠 나빠")

print(r.romanize())