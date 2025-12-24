def count_word(content):
    return len(content.split())

def count_letter(content):
    dict_words = {}
    for i in content.lower():
        dict_words[i] = dict_words.get(i,0) + 1
    return dict_words

def letters_from_greatest(characters_dict):
    list_dict = [{"letter": k, "count": v} for k, v in characters_dict.items() if k.isalpha()]
    
    list_dict.sort(reverse=True, key=lambda item: item["count"])
    
    return list_dict