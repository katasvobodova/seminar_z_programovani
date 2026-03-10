def fce_na_odstranovani_prebytecnych_mezer(text:str):
    text = text.strip()
    text = text.split()
    text = " ".join(text)
    return text

def fce_na_odstranovani_prebytecnych_mezer_2(text:str):
    return " ".join(text.strip().split())

text =  input("Vložte text, u kterého chcete opravit mezery: ")

print(fce_na_odstranovani_prebytecnych_mezer(text))
