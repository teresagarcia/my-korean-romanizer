# -*- coding: utf-8 -*-

from .syllable import Syllable  
from .enhacer import Enhacer  
from .hangul_romanization_equivalents import vowels, consonants, double_consonant_final

class Romanizer(object):
    def __init__(self):
        self.text = ''  
        self.current_syllable = ''
        self.next_syllable = ''
        self.rom_next_initial_as_final = False


    def romanize(self, text):
        self.text = text
        romanized = ""
        tmp_romanized = ""
        all_romanized = ""
        enhacer = Enhacer()
        for idx, char in enumerate(self.text):
            if(self.is_hangul(char)):
                self.current_syllable = Syllable(char)
                self.next_syllable = self.get_next_syllable(idx)
                tmp_romanized += self.romanize_syllable(self.current_syllable)
                self.set_rom_next_initial_as_final()
            else:
                tmp_romanized = enhacer.enhace_romanization(tmp_romanized)
                all_romanized += tmp_romanized + char
                tmp_romanized = ""
        tmp_romanized = enhacer.enhace_romanization(tmp_romanized)
        all_romanized += tmp_romanized
        romanized = tmp_romanized if not (all_romanized) else all_romanized
        return romanized


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
        elif(self.rom_next_initial_as_final):
            romanization = letter.get('final')
            self.rom_next_initial_as_final = False
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


    def get_double_consonant_final(self, double_letter):
        romanization = ''
        double_cons_key = self.set_double_cons_key()
        for one_char in double_letter.get(double_cons_key):
            letter = consonants.get(one_char)
            key = self.set_correct_key(letter)
            romanization += letter.get(key)
        return romanization


    def set_double_cons_key(self):
        key = 'complete'
        if(self.change_to_reduced()):
            key = 'reduced'
            self.rom_next_initial_as_final = True
        return key


    def set_correct_key(self, letter):
        key = 'final'
        if(self.next_syllable):
            possible_keys = self.next_syllable.search_key()
            for possible_key in possible_keys:
                if(letter.get(possible_key)):
                    key = possible_key
                    break
        return key


    def set_rom_next_initial_as_final(self):
        self.rom_next_initial_as_final = self.change_initial_to_final()


    def change_to_reduced(self):
        return (self.current_syllable.final_is_ps() and not self.next_syllable.starts_with_vowel())


    def change_initial_to_final(self):
        is_case_ps_ss = ((self.current_syllable.final_is_ps() or self.current_syllable.final_is_ss()) and self.next_syllable.initial_is_d())
        is_case_hk = self.current_syllable.final_is_h() and self.next_syllable.initial_is_g()
        return is_case_hk or is_case_ps_ss