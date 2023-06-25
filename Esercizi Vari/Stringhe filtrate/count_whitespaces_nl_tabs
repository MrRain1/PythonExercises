def filter_whitespaces(input_str):
    return True if input_str == " " else False

def filter_tabs(input_str):
    return True if input_str == "\t" else False

def filter_newlines(input_str):
    return True if input_str == "\n" else False

if __name__=="__main__":
    with open("./lorem_ipsium.txt", "r") as text_file:
        text_content = text_file.read()
    number_of_whitespaces = len(list(filter(filter_whitespaces, text_content)))
    number_of_tabs = len(list(filter(filter_tabs, text_content)))
    number_of_newlines = len(list(filter(filter_newlines, text_content)))

    print(f"number of whitespaces: {number_of_whitespaces}")
    print(f"number of tabs: {number_of_tabs}")