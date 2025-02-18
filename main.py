import sys
from ui import main as cli_main
from api import app 

def start_cli():
    ## start the cli
    cli_main()

def start_api():
    ## start the api
    print("Starting API...")
    app.run(debug=True)

if (__name__ == "__main__"):

    print("1. Start CLI")
    print("2. Start API")

    choice = input("Do you want to start the CLI or the API? (1 or 2): ")

    if choice == "1":
        start_cli()

    elif choice == "2":
        start_api()

    else:
        print("Invalid choice. Please try again.")  
    