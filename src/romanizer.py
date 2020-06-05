from jamo import h2j, j2hcj
from syllable import Syllable  
import re
from hangul_romanization_equivalents import vowels, consonants, double_consonant_final

class Romanizer(object):
    def __init__(self):
        self.text = ''  
        self.current_syllable = ''
        self.next_syllable = ''


    def romanize(self, text):
        self.text = text
        _romanized = ""
        for idx, char in enumerate(self.text):
            if(self.is_hangul(char)):
                self.current_syllable = Syllable(char)
                self.next_syllable = self.get_next_syllable(idx)
                _romanized += self.romanize_syllable(self.current_syllable)
            else:
                _romanized += char
        return _romanized


    def get_next_syllable(self, idx):
        next_char = self.text[idx+1] if(len(self.text) > (idx+1)) else None
        if(next_char and self.is_hangul(next_char)):
            return Syllable(next_char)

    def is_hangul(self, char):
        value = ord(char)
        return 0xAC00 <= value <= 0xD7A3


    def romanize_syllable(self, syl):
        initial_rom = self.get_initial_rom(syl)
        medial_rom = self.get_medial_rom(syl)
        final_rom = self.get_final_rom(syl)
        romanized_syl = initial_rom + medial_rom + final_rom
        return romanized_syl


    def get_initial_rom(self, syl):
        letter = consonants.get(syl.initial)
        if(self.current_syllable.initial_is_s() and self.current_syllable.medial_is_i()):
            romanization = letter.get('before_i')
        else:
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
            key = self.set_correct_key(letter)
            romanization = letter.get(key)
        elif(double_letter):
            romanization = self.get_double_consonant_final(double_letter)
        return romanization


    def get_double_consonant_final(self, letter):
        romanization = ''
        for cons in letter:
            consonant_entry = consonants.get(cons)
            key = self.set_correct_key(consonant_entry)
            romanization += consonant_entry.get(key)
        return romanization


    def set_correct_key(self, letter):
        key = 'final'
        if(self.next_syllable):
            if(self.next_syllable.starts_with_i() and self.changes_before_i(letter)):
                key = 'before_i'
            elif(self.next_syllable.starts_with_vowel() and self.changes_before_vowel(letter)):
                key = 'pre_vowel'
        return key


    def changes_before_vowel(self, letter):
        return letter.get('pre_vowel')

    
    def changes_before_i(self, letter):
        return letter.get('before_i')


