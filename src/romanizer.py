from jamo import h2j, j2hcj
from syllable import Syllable  
import re
from hangul_romanization_equivalents import vowels, consonants, double_consonant_final

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
        double_letter = double_consonant_final.get(syl.final)
        romanization = ''
        if(letter):
            romanization = letter.get('final')
        elif(double_letter):
            romanization = self.get_double_consonant_final(double_letter)
        return romanization

    def get_double_consonant_final(self, letter):
        romanization = ''
        for cons in letter:
            romanization += consonants.get(cons).get('final')
        return romanization

