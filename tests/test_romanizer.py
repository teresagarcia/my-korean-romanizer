# -*- coding: utf-8 -*-

import sys
import pytest
from mykoreanromanizer.romanizer import Romanizer
from mykoreanromanizer.hangul_romanization_equivalents import vowels, consonants, double_consonant_final

r = Romanizer()

def test_basic_romanization():
    assert r.romanize("안녕하세요") == "annyeonghaseyo"
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
    assert r.romanize("잃어") == "irheo"
    assert r.romanize("모습이") == "moseubi"
    assert r.romanize("믿었어") == "mideosseo"


def test_s_and_t_change_before_i():
    assert r.romanize("보고 싶어") == "bogo shipeo"
    assert r.romanize("이 것이") == "i geoshi"
    assert r.romanize("같이") == "gachi"
    assert r.romanize("같아") == "gata"
    assert r.romanize("이 것 아니야") == "i geot aniya"
    assert r.romanize("않아") == "anha"


def test_s_before_wi():
    assert r.romanize("쉬다") == "shwida"


def test_mn_instead_of_pn():
    assert r.romanize("감사합니다") == "gamsahamnida"


def test_ss_changes_before_s():
    assert r.romanize("있습니다") == "isseumnida"


def test_transform_ps_ss():
    assert r.romanize("없어") == "eobseo"
    assert r.romanize("없다") == "eopta"
    assert r.romanize("있으면") == "isseumyeon"
    assert r.romanize("있다") == "itta"
    assert r.romanize("없나요") == "eomnayo"


def test_enhacement():
    assert r.romanize("일년 후") == "illyeon hu"
    assert r.romanize("대답해 줄래") == "daedaphae jullae"  
    assert r.romanize("마지막이 찬란한 노을처럼") == "majimagi challanhan noeulcheoreom"
    assert r.romanize("Oh 네가 나를 부를 때 깨어나") == "Oh nega nareul bureul ttae kkae'eona"


def test_multiline():
    assert r.romanize("어떡해 어쩌면 좋아 \n 내가 이렇게 아픈데") == "eotteokhae eojjeomyeon joha \n naega ireohke apeunde"


def test_j_ch_r_before_h():
    assert r.romanize("잊혀") == "ijhyeo"
    assert r.romanize("잃어") == "irheo"
    assert r.romanize("잊어요") == "ijeoyo"
