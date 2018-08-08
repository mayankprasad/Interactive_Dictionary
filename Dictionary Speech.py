import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:                           #simply return on availability
        return data[w]

    elif w.title() in data:                 #in case user have words like Delhi or any word starting with Captial Letter
        return data[w.title()]

    elif w.upper() in data:                 #in case user enters words in capital
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])

        if yn == "Y" or yn == "y":
            return data[get_close_matches(w, data.keys())[0]]

        elif yn == "N" or yn == "n":
            return "The word doesn't exist. Please double check it."

        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist. Please double check it."

word=""
choice=int(input("Select Option \n1. Google Speech\n2. Manual Input\n"))
if choice==1:
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak: ")
        audio = r.listen(source)
    try:
        word=(str(r.recognize_google(audio)))
        print("\nWord Detected: "+word)

    except sr.UnknownValueError:
        print("No audio")
        exit(0)
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        exit(0)
elif choice ==2:
    word = input("Enter word: ")

else:
    print("Wrong Choice.. Exiting...")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)