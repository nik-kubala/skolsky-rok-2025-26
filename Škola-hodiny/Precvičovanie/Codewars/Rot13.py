def rot13(message):
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    final_message = []
    for character in message:
        if character in lower_alphabet:
            old_index = lower_alphabet.find(character)
            new_index = (old_index - 13) % 26
            final_message.append(lower_alphabet[new_index])
        
        elif character in upper_alphabet:
            old_index = upper_alphabet.find(character)
            new_index = (old_index - 13) % 26
            final_message.append(upper_alphabet[new_index])
        
        else:
            final_message.append(character)
        
    return ("").join(final_message)

def rot13_slaba(message):
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    final_message = ""
    for character in message:
        if character in lower_alphabet:
            for index, char_in_alpha in enumerate(lower_alphabet):
                if char_in_alpha == character:
                    if index < 13:
                        final_message += lower_alphabet[index + 13]
                    else:
                        temp = index - 13
                        final_message += lower_alphabet[temp]
    
        elif character in upper_alphabet:
            for index, char_in_alpha in enumerate(upper_alphabet):
                if char_in_alpha == character:
                    if index < 13:
                        final_message += upper_alphabet[index + 13]
                    else:
                        temp = index - 13
                        final_message += upper_alphabet[temp]
        else:
            final_message += character
    return final_message