def no_of_words(text):
    text = text.split()
    return len(text)

def no_of_unique_words(text):
    text = text.split()
    text = set(text)
    return len(text)

# def read_file(filenanme):
#     with open(filename, 'r', encoding='utf8') as
#         content = file1.read()
#     return len(text)

def words_repeat(text):
    text = text.split()
    my_dict = {}
    for word in text:
        if word in my_dict.keys():
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict
