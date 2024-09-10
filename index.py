def get_response(option):
    responses = {
        '/name': "My name is Lucas Pritchett.",
        '/why': "I chose computer science I've always enjoyed computers/video games and have a passion to learn more.",
        '/what': "Once I graduate, I want to go into cybersercurity or possibly AI.",
        '/fact': "A fun fact about me is that I do demolition derbies."
    }
    
    return responses.get(option, "Invalid option. Please choose from /name, /why, /what, or /fact.")

def main():
    print("Available options: /name, /why, /what, /fact")
    option = input("Enter an option: ").strip()
    print(get_response(option))

if __name__ == "__main__":
    main()
    
