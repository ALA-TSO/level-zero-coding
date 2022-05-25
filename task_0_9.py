def vowels(text):
    text = text.lower()
    vowels = ["a","e","i","o","u"]
    for char in text:
        if char in vowels:
            print(char)
vowels("uSanelE")
