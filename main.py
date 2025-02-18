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
    start_cli()

    
    