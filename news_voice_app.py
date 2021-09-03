from bs4 import BeautifulSoup
import requests
import colorama
import pyttsx3

#####################################
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
}
######################################
# start voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate -20)
engine.say("Hi!")
engine.say("I will read you the latest news from top sources")
engine.say("Have a coffee and relax")
engine.runAndWait()

# CBC
print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.YELLOW + "******************************")
print("CBC:")
url_cbc = "https://www.cbc.ca/news/world"
request = requests.get(url_cbc, headers=HEADERS)
soup_cbc = BeautifulSoup(request.text, "html.parser")
header_cbc = soup_cbc.find_all("div", class_="card")
# parsing description
for description_cbc in header_cbc:
    description_cbc = description_cbc.find("a", {'class': 'contentWrapper'})
    # parsing links
    if description_cbc is not None:
        link_cbc = description_cbc.get('href')
        # voice CBC
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            engine.setProperty('voice', voices[1].id)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate -20)
        engine.say("CBC")
        engine.say(description_cbc.text)
        engine.runAndWait()
        # output
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.CYAN + description_cbc.text + " \n" + (
            str("https://www.cbc.ca" + link_cbc)))
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.YELLOW + "******************************")

# NYT
print("The New York Times:")
url_nyt = "https://www.nytimes.com/section/world"
request = requests.get(url_nyt, headers=HEADERS)
soup_nyt = BeautifulSoup(request.text, "html.parser")
header_nyt = soup_nyt.find_all("li", class_="css-ye6x8s")

# parsing description
for description_nyt in header_nyt:
    description_nyt = description_nyt.find("div", {'class': 'css-1l4spti'}).find('a')
    # parsing links
    if description_nyt is not None:
        link_nyt = description_nyt.get('href')

        # voice The New York Times
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            engine.setProperty('voice', voices[1].id)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate -20)
        engine.say("The New York Times")
        engine.say(description_nyt.text)
        engine.runAndWait()
        # output
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.CYAN + description_nyt.text + " \n" + (
            str("https://www.nytimes.com/" + link_nyt)))
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.YELLOW + "******************************")

# Aljazeera
print("Aljazeera:")
url_alj = "https://www.aljazeera.com/europe/"
request = requests.get(url_alj, headers=HEADERS)
soup_alj = BeautifulSoup(request.text, "html.parser")
header_alj = soup_alj.find_all("article", class_="gc")

# parsing description
for description_alj in header_alj:
    description_alj = description_alj.find("div", {'class': 'gc__header-wrap'}).find('a')
    # parsing links
    if description_alj is not None:
        link_alj = description_alj.get('href')

        # voice Aljazeera
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            engine.setProperty('voice', voices[1].id)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate -20)
        engine.say("Aljazeera")
        engine.say(description_alj.text)
        engine.runAndWait()
        # output
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.CYAN + description_alj.text + " \n" + (
            str("https://www.aljazeera.com" + link_alj)))
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.YELLOW + "******************************")

# BBC
url_bbc = "https://www.bbc.com/news/world"
request = requests.get(url_bbc, headers=HEADERS)
soup_bbc = BeautifulSoup(request.text, "html.parser")
header_bbc = soup_bbc.find_all("div", class_="gs-c-promo-body")

# parsing description
for description_bbc in header_bbc:
    description_bbc = description_bbc.find("a", {'class': 'gs-c-promo-heading'})
    # parsing links
    if description_bbc is not None:
        link_bbc = description_bbc.get('href')

        # voice BBC
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            engine.setProperty('voice', voices[1].id)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate -20)
        engine.say("BBC")
        engine.say(description_bbc.text)
        engine.runAndWait()
        # output
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.CYAN + str(description_bbc.text) + " \n" + (
            str("https://www.bbc.com" + link_bbc)))
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.YELLOW + "******************************")

# final voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate -20)
engine.say("Whats all i have for you at this moment")
engine.say("But you can read all the top news in the terminal or follow the links")
engine.runAndWait()
