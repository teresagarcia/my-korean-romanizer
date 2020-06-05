import sys
sys.path.append("src") 
import pytest
from romanizer import Romanizer
from hangul_romanization_equivalents import vowels, consonants, double_consonant_final

r = Romanizer()

def test_basic_romanization():
    assert r.romanize("안녕") == "annyeong"
    assert r.romanize("바보") == "babo"
    assert r.romanize("깜짝") == "kkamjjak"
    assert r.romanize("영원에 남겨진 나를 찾는가") == "yeongwone namgyeojin nareul chatneunga"


def test_is_hangul():
    assert r.is_hangul("오") == True
    assert r.is_hangul("h") == False
    assert r.is_hangul("2") == False


def test_non_korean_characters():
    assert r.romanize("hola buenas qué tal!!") == "hola buenas qué tal!!"
    assert r.romanize("Hey señor~$ <3") == "Hey señor~$ <3"
    assert r.romanize("時が過ぎて見えてきたこと") == "時が過ぎて見えてきたこと"
    assert r.romanize("안녕이란 말 hello hello") == "annyeongiran mal hello hello"


def test_double_final_consonants():
    assert r.romanize("밝다") == "balkda"


def test_next_syllable_starts_with_vowel():
    assert r.romanize("있어") == "isseo"
    assert r.romanize("잊어줘") == "ijeojwo"


def test_s_and_t_change_before_i():
    assert r.romanize("보고 싶어") == "bogo shipeo"
    assert r.romanize("이 것이") == "i geoshi"
    assert r.romanize("같이") == "gachi"



