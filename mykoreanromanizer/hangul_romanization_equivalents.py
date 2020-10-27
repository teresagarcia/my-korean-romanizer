# -*- coding: utf-8 -*-

vowels = {
    'ㅏ' : 'a',
    'ㅓ' : 'eo',
    'ㅗ' : 'o',
    'ㅜ' : 'u',
    'ㅡ' : 'eu',
    'ㅣ' : 'i',
    'ㅐ' : 'ae',
    'ㅔ' : 'e',
    'ㅚ' : 'oe',
    'ㅟ' : 'wi',
    
  
    'ㅑ' : 'ya',
    'ㅕ' : 'yeo',
    'ㅛ' : 'yo',
    'ㅠ' : 'yu',
    'ㅒ' : 'yae',
    'ㅖ' : 'ye',
    'ㅘ' : 'wa',
    'ㅙ' : 'wae',
    'ㅝ' : 'wo',
    'ㅞ' : 'we',
    'ㅢ' : 'ui', 
}

consonants = { 
    'ㄱ': {'initial': 'g', 'final': 'k', 'before_vowel': 'g'},
    'ㄷ': {'initial': 'd', 'final': 't', 'before_vowel' : 'd'},
    'ㄹ': {'initial': 'r', 'final': 'l', 'before_vowel': 'r', 'before_h' : 'r'},
    'ㅁ': {'initial': 'm', 'final': 'm'},
    'ㄴ': {'initial': 'n', 'final': 'n'},
    'ㅂ': {'initial': 'b', 'final': 'p', 'before_n': 'm', 'before_vowel' : 'b'},
    'ㅅ': {'initial': 's', 'final': 't', 'before_vowel': 's', 'before_i': 'sh', 'before_s': 's', 'before_wi' : 'sh'},
    'ㅇ': {'initial': '', 'final': 'ng'},
    'ㅈ': {'initial': 'j', 'final': 't', 'before_vowel': 'j', 'before_h' : 'j'},
    'ㅊ': {'initial': 'ch', 'final': 't', 'before_vowel': 'ch', 'before_h' : 'ch'},
    'ㅋ': {'initial': 'k', 'final': 'k'},
    'ㅌ': {'initial': 't', 'final': 't', 'before_i': 'ch'},
    'ㅍ': {'initial': 'p', 'final': 'p'},
    'ㅎ': {'initial': 'h', 'final': 'h'},
    'ㄲ' : {'initial': 'kk', 'final': 'kk'},
    'ㄸ' : {'initial': 'tt', 'final': 'tt'},
    'ㅃ' : {'initial': 'pp', 'final': 'pp'},
    'ㅉ' : {'initial': 'jj', 'final': 't', 'before_vowel': 'jj', 'before_h' : 'jj'},
    'ㅆ' : {'initial': 'ss', 'final': 't', 'before_vowel': 'ss', 'before_s': 's'},
}

double_consonant_final = {
    'ㄳ' : {'complete' : ['ㄱ', 'ㅅ'], 'reduced' : 'ㄱ'},
    'ㄵ' : {'complete' : ['ㄴ', 'ㅈ'], 'reduced' : 'ㄴ'},
    'ㄶ' : {'complete' : ['ㄴ', 'ㅎ'], 'reduced' : 'ㄴ'},
    'ㄺ' : {'complete' : ['ㄹ', 'ㄱ'], 'reduced' : 'ㄹ'},
    'ㄻ' : {'complete' : ['ㄹ', 'ㅁ'], 'reduced' : 'ㄹ'},
    'ㄼ' : {'complete' : ['ㄹ', 'ㅂ'], 'reduced' : 'ㄹ'},
    'ㄽ' : {'complete' : ['ㄹ', 'ㅅ'], 'reduced' : 'ㄹ'},
    'ㄾ' : {'complete' : ['ㄹ', 'ㅌ'], 'reduced' : 'ㄹ'},
    'ㄿ' : {'complete' : ['ㄹ', 'ㅍ'], 'reduced' : 'ㄹ'},
    'ㅀ' : {'complete' : ['ㄹ', 'ㅎ'], 'reduced' : 'ㄹ'},
    'ㅄ' : {'complete' : ['ㅂ', 'ㅅ'], 'reduced' : 'ㅂ'},
}
