import sys
sys.path.append('src') 
import pytest
from syllable import Syllable


def test_two_letter_syllable():
    s = Syllable('오')
    assert s.initial == 'ㅇ'
    assert s.medial == 'ㅗ'
    assert s.final == ''


def test_three_letter_syllable():
    s = Syllable('창')
    assert s.initial == 'ㅊ'
    assert s.medial == 'ㅏ'
    assert s.final == 'ㅇ'

def test_starts_with_vowel():
    s = Syllable('오')
    assert s.starts_with_vowel() == True
    s = Syllable('돈')
    assert s.starts_with_vowel() == False

    