task 0.10

def common_letters(wordx, wordy):
    wordx = wordx.lower()
    wordy = wordy.lower()
    for char in wordx and wordy:
        if char in wordx and char in wordy:
            print(char)
common_letters("sanele","mokoatle")
