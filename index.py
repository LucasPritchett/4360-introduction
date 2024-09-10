import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python index.py /option")
        return

    option = sys.argv[1]

    if option == "/name":
        print("My name is Lucas Pritchett.")
    elif option == "/why":
        print("I chose computer science because I've always enjoyed computers/video games and have a passion to learn more.")
    elif option == "/what":
        print("Once I 'graduate', I want to go into cybersercurity or possibly AI.")
    elif option == "/fact":
        print("One fun fact about me is that I  is that I do demolition derbies.")
    else:
        print("Unknown option. Please use one of the following options: /name, /why, /what, /fact")

if __name__ == "__main__":
    main()

