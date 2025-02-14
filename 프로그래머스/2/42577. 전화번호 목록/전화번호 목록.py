def solution(phone_book):
    '''
    전화번호 길이가 1~20 -> 전화번호 길이로 key
    key안에 중복된 숫자가 있고, 해당 번호가 phone_book에 존재하면 answers = False
    '''
    
    phone_book_dict = {i:set() for i in range(1,21)}
    total_phone_dict = {i:set() for i in range(1,21)} # total number dict
    
    answers = True
    flag = False
    for number in phone_book:
        tot_len = len(number)
        total_phone_dict[tot_len].update([number])
        for i in range(1, tot_len+1): # key
            if number[:i] in total_phone_dict[i] and number[:i] in phone_book_dict[i]: # low efficiency
                answers = False
                flag = True
                break
            else:
                phone_book_dict[i].update([number[:i]])
        if flag:
            break
    
    return answers