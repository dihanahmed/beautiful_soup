from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    

    soup = BeautifulSoup(content,'lxml')
    #print(soup.prettify)

    keyword = soup.find_all('h2')
    #print(courses_html_tags)

    for word in keyword:
        print(word.text)

