import winsound
import random
import time
import keyboard
morse = {"A":"._",
         "B":"_...",
         "C":"_._.",
         "D":"_..",
         "E":".",
         "F":".._.",
         "G":"__.",
         "H":"....",
         "I":"..",
         "J":".___",
         "K":"_.__",
         "L":"_._",
         "M":"__",
         "N":"_.",
         "O":"___",
         "P":".__.",
         "Q":"__._",
         "R":"._.",
         "S":"...",
         "T":"_",
         "U":".._",
         "V":"..._",
         "W":".__",
         "X":"_.._",
         "Y":"_.__",
         "Z":"__.."
         }

def test_morse(inp):
    for i in range(inp):
        if(keyboard.is_pressed('q')):
            exit()
        key=random.choice(list(morse))
        print(key, end="->")
        time.sleep(1)
        for i in morse[key]:
            if i==".":
                winsound.PlaySound('sound/dot.wav', 0)
                print(i ,end="")
            else:
                winsound.PlaySound('sound/dash.wav', 0)
                print("_", end="")
        time.sleep(2)        
        winsound.PlaySound(f'sound/{key}.wav', 0)
        print("\n")
        


def learn_morse():
        for key in morse:
            print(key, end="->")
            winsound.PlaySound(f'sound/{key}.wav', 0)
            for i in morse[key]:
                if i==".":
                    winsound.PlaySound('sound/dot.wav', 0)
                    print(i ,end="")
                else:
                    winsound.PlaySound('sound/dash.wav', 0)
                    print("_", end="")
            print("\n")
            if(keyboard.is_pressed('q')):
                quit()


def eng_to_morse():
    word = input("Enter the word(exclude symbols): ")
    for letter in word:
        if(letter == " "):
            print("", end="   ")
            continue
        print(morse[letter.upper()], end=" ")
    esc = input("\nPress q to exit:\nPress any key to continue: ")
    if(esc.lower() != 'q'):
        eng_to_morse()
    else:
        quit()    



ipt = input("Enter 1: To Learn Morse Code\nEnter 2: To Test Morse Code\nEnter 3: English to MorseCode converter\n")
if ipt=="1":
    learn_morse()
elif ipt == "2":
    inp = int(input("Select a number from 1 to 26: "))
    test_morse(inp)
elif ipt=="3":
    eng_to_morse()    