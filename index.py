import sys

def handle_name():
    print("My name is Lucas Pritchett.")

def handle_why():
    print("I chose computer science because I've always enjoyed computers/video games and have a passion to learn more.")

def handle_what():
    print("Once I graduate, I want to go into cybersercurity or possibly AI.")

def handle_fact():
    print("A fun fact about me is that I do demolition derbies.")

def handle_default():
    print("Choose from /name, /why, /what, or /fact.")

def main():
    if len(sys.argv) != 2:
        handle_default()
        return

    option = sys.argv[1]

    if option == "/name":
        handle_name()
    elif option == "/why":
        handle_why()
    elif option == "/what":
        handle_what()
    elif option == "/fact":
        handle_fact()
    else:
        handle_default()

if __name__ == "__main__":
    main()

