import time
import requests
import selectorlib
import smtplib, ssl
import os

URL = "https://programmer100.pythonanywhere.com/tours/"

def scrape(URL):
    """Scrape the tour data from the given URL."""
    response = requests.get(URL)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "ingenieroiansuarez@gmail.com"
    password = "ezkp ydkc zupi uhjx"

    receiver = "ingenieroiansuarez@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    print("email sent successfully!")


def store(extracted):
    """Store the extracted data in a file."""
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read(extracted):
    """Read the extracted data from the file."""
    with open("data.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    # Scrape the data
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        content = read(extracted)
        if extracted != "No upcoming tours":
            if not extracted in "data.txt":
                store(extracted)
                send_email(message= "new event was found")
        time.sleep(2)


