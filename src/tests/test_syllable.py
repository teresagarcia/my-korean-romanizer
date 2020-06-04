import sys
sys.path.append('src') 
import pytest
from syllable import Syllable


def test_is_hangul():
    s = Syllable('오')
    assert s.is_hangul() == True
    s_not_hangul = Syllable('h')
    assert s_not_hangul.is_hangul() == False
    s_number = Syllable('2')
    assert s_number.is_hangul() == False


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

    