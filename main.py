def count_letters(text):
    
    
    numw=0
    for word in range(0,len(text)):
        for letter in letters:
            if text[word]==letter:
                letters[letter] += 1
                    #print(letters[letter])
    return letters

def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        words = file_contents.split()
        text = file_contents.lower()
    count_letters(text)
    for letter in letters:
        print(f"The '{letter}' character was found {letters[letter]} times")

letters={"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0, "w":0, "x":0,"y":0,"z":0}
letters_all={"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0, "w":0, "x":0,"y":0,"z":0,
             " ":0, ",":0, ".":0, "!":0, "?":0, ";":0, "#":0, "(":0, ")":0}
alphabet=("abcdefghijklmnopqrstuvwxyz,;:?!.#() ")
main()