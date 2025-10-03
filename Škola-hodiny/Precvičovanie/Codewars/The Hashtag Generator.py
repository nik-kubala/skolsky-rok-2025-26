def generate_hashtag(s):
    if not s.strip():
        return False
    
    capitalized_words = [word.capitalize() for word in s.split()]
    
    final = f"#{''.join(capitalized_words)}"
    
    return final if len(final) < 141 else False



def generate_hashtag_noob(s):
    words = s.split()
    final_str = "#"
    
    if s == "":
        return False
    
    for word in words:
        final_str += word.capitalize()
    
    if len(final_str) > 140:
        return False
    else:
        return final_str