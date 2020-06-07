# -*- coding: utf-8 -*-

import sys
import pytest
from mykoreanromanizer.syllable import Syllable


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
    t = Syllable('돈')
    assert t.starts_with_vowel() == False


def test_starts_with_i():
    s = Syllable('입') 
    assert s.starts_with_i() ==  True
    t = Syllable('꽃')
    assert t.starts_with_i() == False

def test_initial_is_s():
    s = Syllable('손') 
    assert s.initial_is_s() ==  True
    t = Syllable('꽃')
    assert t.initial_is_s() == False



    