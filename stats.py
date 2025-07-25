def get_num_words(text):
    return len(text.split())

def char_count(text):
    low_c=text.lower()
    full_count={}
    for char in low_c:
        if char in full_count:
            full_count[char]+=1
        else:
            full_count[char]=1
    return full_count


def sort_on(items):
    return items["num"]
    

def new_list(char_count):
    d_to_l=[]
    for char in char_count:
        if char.isalpha():
            d_to_l.append({"char":char, "num":char_count[char]})
    d_to_l.sort(reverse=True,key=sort_on)
    return d_to_l

   
