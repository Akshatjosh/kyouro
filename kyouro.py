import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robotic answering machine 1.0 created by Akshat")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want to say: ")
        if x == "bye" :
            y="bye bye friends"
            engine.say(y)
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
