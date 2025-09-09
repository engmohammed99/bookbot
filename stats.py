def num_returned(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    index = {}
    for char in text:
        if char in index:
            index[char] += 1
        else:
            index[char] = 1
    return index

def report_characters(dec):
    def order_key(items):
        return items["num"]
    
    list_of_dec = []                              
    for key,value in dec.items():
        list_of_dec.append({"char":key,"num":value})
    list_of_dec.sort(reverse=True,key=order_key)
    return list_of_dec