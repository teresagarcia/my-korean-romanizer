import sys
sys.path.append('src') 
import pytest
from romanizer import Romanizer

r = Romanizer()

def test_basic_romanization():
    assert r.romanize('안녕') == 'annyeong'
    assert r.romanize('바보') == 'babo'
    assert r.romanize('깜짝') == 'kkamjjak'
    assert r.romanize('영원에 남겨진 나를 찾는가') == 'yeongwone namgyeojin nareul chatneunga'


def test_double_final_consonants():
    pass