from jamo import h2j, j2hcj
from syllable import Syllable

syl = Syllable("삼")
print(syl.initial)   

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
    'ㄱ': {'initial': 'g', 'final': 'k'},
    'ㄷ': {'initial': 'd', 'final': 't'},
    'ㄹ': {'initial': 'r', 'final': 'l'},
    'ㅁ': {'all': 'm'},
    'ㄴ': {'all': 'n'},
    'ㅂ': {'initial': 'b', 'final': 'p'},
    'ㅅ': {'initial': 's', 'final': 't', 'pre_vocal': 's', 'before_i': 'sh'},
    'ㅇ': {'initial': '', 'final': 'ng'},
    'ㅈ': {'initial': 'j', 'final': 't', 'pre_vocal': 'j'},
    'ㅊ': {'initial': 'ch', 'final': 't', 'pre_vocal': 'ch'},
    'ㅋ': {'all': 'k'},
    'ㅌ': {'all': 't'},
    'ㅍ': {'all': 'p'},
    'ㅎ': {'all': 'h'},
    'ᄁ' : {'all': 'kk'},
    'ᄄ' : {'all': 'tt'},
    'ᄈ' : {'all': 'pp'},
    'ᄍ' : {'all': 'jj'},
    'ᄊ' : {'initial': 'ss', 'final': 't', 'pre_vocal': 'ss'},
}

double_consonant_final = {
    'ㄳ' : ('ㄱ', 'ㅅ'),
    'ㄵ' : ('ᆫ', 'ㅈ'), 
    'ᆭ' : ('ᆫ', 'ᇂ'),
    'ㄺ' : ('ㄹ', 'ㄱ'), 
    'ㄻ' : ('ㄹ', 'ㅁ'), 
    'ㄼ' : ('ㄹ', 'ㅂ'), 
    'ㄽ' : ('ㄹ', 'ㅅ'), 
    'ㄾ' : ('ㄹ', 'ㅌ'), 
    'ㄿ' : ('ㄹ', 'ㅍ'),
    'ㅀ' : ('ㄹ', 'ᇂ'), 
    'ㅄ' : ('ㅂ', 'ㅅ'), 
    'ㅆ' : ('ㅅ', 'ㅅ')
}

