import requests
import platform
from os import system
from bs4 import BeautifulSoup

urls = ['https://arstechnica.com', 'https://www.bbc.com/news', 'https://www.ndtv.com', 'https://assamtribune.com']


def fetchNews(keyword):
    articles_list = []
    article_matches = []
    length = len(urls)

    for i in range(length):
        response = requests.get(urls[i])
        soup = BeautifulSoup(response.text, 'html.parser')

        system('clear') if platform.system() == 'Linux' else system('cls')  # CLEAR SCREEN
        print('Fetching articles from : ', end='')
        print(urls[i], sep='')

        # find all headlines
        if (urls[i] == "https://www.bbc.com/news") or (urls[i] == "https://www.ndtv.com"):
            html_class = 'h3'

        else:
            html_class = 'h2'

        headlines = soup.find('body').find_all(html_class)

        for x in headlines:
            articles_list.append(x.text.strip() + ' [source: ' + urls[i] + ']')

        for j, title in enumerate(articles_list):
            title_lower = title.lower()
            if keyword.lower() in title_lower:
                article_matches.append(title)

    # remove duplicates from list
    newList = [ii for n, ii in enumerate(article_matches) if ii not in article_matches[:n]]
    no_of_news = len(newList)

    # Prints the Titles of the articles that contain the keywords
    system('clear') if platform.system() == 'Linux' else system('cls')  # CLEAR SCREEN
    print(f'\n--------- Total mentions of "{keyword}" = {no_of_news} ---------')
    for i, title in enumerate(newList):
        print(i + 1, ')', title)


def main():
    print('=============================== NEWS SEARCH ===============================')
    print('')
    search_keyword = input('Enter search keyword: ')
    fetchNews(search_keyword)
    print('')
    print('https://github.com/Prajnadeep')
    print('')
    raw_input = input('Press any key to quit')


if __name__ == "__main__":
    main()
