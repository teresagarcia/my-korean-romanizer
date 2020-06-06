# -*- coding: utf-8 -*-

import re

class Enhacer(object):
    def __init__(self):
        self.text = ""


    def enhace_romanization(self, text):
        self.text = text
        self.substitute_with_ll()
        self.substitute_with_gn()
        self.add_apostrophe()
        return self.text


    def substitute_with_ll(self):
        self.text = re.sub('nr|ln|lr', 'll', self.text)


    def substitute_with_gn(self):
        self.text = re.sub('ngr|kr', 'gn', self.text)


    def add_apostrophe(self):
        replacements = [
            ("aeeo", "ae'eo"),
            ("eoo", "eo'o"),
            ("eoe", "eo'e")
        ]
        for old, new in replacements:
            self.text = re.sub(old, new, self.text)
