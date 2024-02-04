morse_code={'A':'.-', 'B':'-...',
'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..',
'1':'.----', '2':'..---', '3':'...--',
'4':'....-', '5':'.....', '6':'-....',
'7':'--...', '8':'---..', '9':'----.',
'0':'-----', ', ':'--..--', '.':'.-.-.-',
'?':'..--..', '/':'-..-.', '-':'-....-',
'(':'-.--.', ')':'-.--.-'}

run=True
while run:
    user_input = input("Type the string for morse code conversion").upper()
    string = ""
    string_check = ""
    for word in user_input:
        if word in morse_code:
            string += morse_code[word]
            string_check += "a"
        else:
            print("No special characters are allowed, "
                  "please use English alphabets and numbers fom 1 to 9 only, sry please try again.")
    if len(user_input) == len(string_check):
        print(string)
    user_input_two = input("try again").upper()
    if user_input_two == "NO":
        run=False

