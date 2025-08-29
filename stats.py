
def count_words(text):
    words = text.split()
    count = len(words)
    return count

def count_characters(text):
    count_dict = {}
    characters = text.lower()

    for i in characters:
        if count_dict.get(i):
            count_dict.update({i:count_dict.get(i)+1})
        else:
            count_dict.update({i:1})
        
    return count_dict

def make_report(count_dict):
    keypairs = []
    for keypair in count_dict:
        #print(keypair)
        keypairs.append({"char":keypair, "num":count_dict.get(keypair)})
    keypairs.sort(reverse = True, key=sort_on)
    return keypairs

def sort_on(items):
    return items["num"]
    
    