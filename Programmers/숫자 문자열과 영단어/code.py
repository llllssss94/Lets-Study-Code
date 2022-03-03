def solution(s):
    answer = 0
    
    alphabet = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    c_word = ''
    for c in s:
        if c > 'a':
            c_word += c
        else:
            answer = answer * 10 + int(c)
    
        # word number detect
        if c_word in alphabet:
            word_num = alphabet.index(c_word)
            answer = answer * 10 + word_num
            c_word = ''
    return answer