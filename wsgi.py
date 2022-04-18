# This is the WSGI Python script that will be called by the web server.
from AppCode import app
def main():
    app.run(host='localhost')


if __name__== "__main__":
    main()