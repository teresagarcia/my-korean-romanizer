# -*- coding: utf-8 -*-

import sys
import pytest
from mykoreanromanizer.enhacer import Enhacer
from mykoreanromanizer.hangul_romanization_equivalents import vowels, consonants, double_consonant_final

e = Enhacer()

def test_substitute_with_ll():
    assert e.enhace_romanization("ilnyeon") == "illyeon"
    assert e.enhace_romanization("julrae") == "jullae"
    assert e.enhace_romanization("chanranhan") == "challanhan"


def test_substitute_with_gn():
    assert e.enhace_romanization("chokseokru") == "chokseognu"
    assert e.enhace_romanization("jongro") == "jogno"


def test_add_apostrophe():
    assert e.enhace_romanization("kaeeona") == "kae'eona"

