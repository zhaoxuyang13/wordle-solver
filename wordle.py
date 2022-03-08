
import re
import random
def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def filter_words(words, pattern):
    left_words = [word for word in words if re.match(r'pattern', word)]
    return left_words
def get_candidate_words(words):
    return random.choice(words)
def remove_letter(words, letter):
    return [word for word in words if letter not in word]
def filter_more_letter(words, letter, num):
    return [word for word in words if word.count(letter) >= num] 
def filter_pos(words, letter, pos):
    return [word for word in words if word[pos] == letter] 
def filter_letter_num(words, letter, num):
    return [word for word in words if  word.count(letter) == num] 
def remove_letter_pos(words, letter, pos):
    return [word for word in words if word[pos] != letter]  
if __name__ == '__main__':
    english_words_set = load_words()
    len6_words_set = [word for word in english_words_set if len(word) == 6]
    candidate_set = len6_words_set
    turn = 0
    while(1):
        turn += 1
        candidate = get_candidate_words(candidate_set)
        if len(candidate_set) == 1 :
            print("haha, the word must be ", candidate)
            break
        size = len(candidate_set)
        if size <= 5:
            print("I guess it maybe ", candidate, "? (left candidates:",candidate_set, ")")
        else:
            print("I guess it maybe ", candidate, "?")
        result = input ( "The result is :" ) # 1 - correct, 0 - wrong,  X - wrong pos
        if(result == 'Yes'):
            print("Thank you")
            break
        if(len(result) != 6):
            print("not corrent input. plz try again")
            continue
        for i in range(6):
            letter = candidate[i]
            res = result[i]
            if res == '1':
                candidate_set = filter_pos(candidate_set, letter, i)
            if res == 'X': 
                candidate_set = remove_letter_pos(candidate_set,letter, i)
                count = 0
                for j in range(6):
                    if (result[j] == '1' or result[j] == 'X') and candidate[j] == letter:
                        count = count + 1
                candidate_set = filter_more_letter(candidate_set,letter,count)
            if res == '0':
                candidate_set = remove_letter_pos(candidate_set,letter, i)
                count = 0
                for j in range(6):
                    if (result[j] == '1' or result[j] == 'X') and candidate[j] == letter: 
                        count = count + 1
                if count > 0:
                    candidate_set = filter_letter_num(candidate_set,letter, count)
        


