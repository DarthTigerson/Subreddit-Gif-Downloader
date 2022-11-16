def text_return_string_location(data,text_string):
    try:
        string_location = data.find(text_string)
        return string_location
    except:
        return False

def text_write_file(path, data, mode='w'):
    with open(path,mode, encoding="utf-8")as file:
        file.write(data)
        file.close()