def text_with_no_spaces(text):
    new_text = ""
    for char in text:
        if char == ' ':
            res = char + new_text
            #print(res)
        else:
            new_text += char

    return new_text


text = "New Document"
print(text_with_no_spaces(text))