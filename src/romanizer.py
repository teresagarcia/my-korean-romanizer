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
    'ㅁ': {'initial': 'm', 'final': 'm'},
    'ㄴ': {'initial': 'n', 'final': 'n'},
    'ㅂ': {'initial': 'b', 'final': 'p'},
    'ㅅ': {'initial': 's', 'final': 't', 'pre_vowel': 's', 'before_i': 'sh'},
    'ㅇ': {'initial': '', 'final': 'ng'},
    'ㅈ': {'initial': 'j', 'final': 't', 'pre_vowel': 'j'},
    'ㅊ': {'initial': 'ch', 'final': 't', 'pre_vowel': 'ch'},
    'ㅋ': {'initial': 'k', 'final': 'k'},
    'ㅌ': {'initial': 't', 'final': 't', 'before_i': 'ch'},
    'ㅍ': {'initial': 'p', 'final': 'p'},
    'ㅎ': {'initial': 'h', 'final': 'h'},
    'ㄲ' : {'initial': 'kk', 'final': 'kk'},
    'ㄸ' : {'initial': 'tt', 'final': 'tt'},
    'ㅃ' : {'initial': 'pp', 'final': 'pp'},
    'ㅉ' : {'initial': 'jj', 'final': 't', 'pre_vowel': 'jj'},
    'ㅆ' : {'initial': 'ss', 'final': 't', 'pre_vowel': 'ss'},
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
    def __init__(self):
        self.text = ''

    def romanize(self, text):
        self.text = text
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
        romanization = letter.get('initial')
        return romanization

    def get_medial_rom(self, syl):
        romanization = vowels.get(syl.medial)
        return romanization

    def get_final_rom(self, syl):
        letter = consonants.get(syl.final)
        romanization = ''
        if(letter is not None):
            print(letter)
            romanization = letter.get('final')
        return romanization

