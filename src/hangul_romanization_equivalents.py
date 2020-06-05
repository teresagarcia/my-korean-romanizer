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
    'ㄷ': {'initial': 'd', 'final': 't'},
    'ㄹ': {'initial': 'r', 'final': 'l', 'before_vowel': 'r'},
    'ㅁ': {'initial': 'm', 'final': 'm'},
    'ㄴ': {'initial': 'n', 'final': 'n'},
    'ㅂ': {'initial': 'b', 'final': 'p', 'before_n': 'm'},
    'ㅅ': {'initial': 's', 'final': 't', 'before_vowel': 's', 'before_i': 'sh', 'before_s': 's'},
    'ㅇ': {'initial': '', 'final': 'ng'},
    'ㅈ': {'initial': 'j', 'final': 't', 'before_vowel': 'j'},
    'ㅊ': {'initial': 'ch', 'final': 't', 'before_vowel': 'ch'},
    'ㅋ': {'initial': 'k', 'final': 'k'},
    'ㅌ': {'initial': 't', 'final': 't', 'before_i': 'ch'},
    'ㅍ': {'initial': 'p', 'final': 'p'},
    'ㅎ': {'initial': 'h', 'final': 'h'},
    'ㄲ' : {'initial': 'kk', 'final': 'kk'},
    'ㄸ' : {'initial': 'tt', 'final': 'tt'},
    'ㅃ' : {'initial': 'pp', 'final': 'pp'},
    'ㅉ' : {'initial': 'jj', 'final': 't', 'before_vowel': 'jj'},
    'ㅆ' : {'initial': 'ss', 'final': 't', 'before_vowel': 'ss', 'before_s': 's'},
}

double_consonant_final = {
    'ㄳ' : ['ㄱ', 'ㅅ'],
    'ㄵ' : ['ㄴ', 'ㅈ'], 
    'ᆭ' : ['ㄴ', 'ㅎ'],
    'ㄺ' : ['ㄹ', 'ㄱ'], 
    'ㄻ' : ['ㄹ', 'ㅁ'], 
    'ㄼ' : ['ㄹ', 'ㅂ'], 
    'ㄽ' : ['ㄹ', 'ㅅ'], 
    'ㄾ' : ['ㄹ', 'ㅌ'], 
    'ㄿ' : ['ㄹ', 'ㅍ'],
    'ㅀ' : ['ㄹ', 'ㅎ'], 
    'ㅄ' : ['ㅂ', 'ㅅ'], 
}