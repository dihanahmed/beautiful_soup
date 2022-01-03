from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    

    soup = BeautifulSoup(content,'lxml')
    #print(soup.prettify)

    # course_html_tags = soup.find_all('h5')
    # #print(courses_html_tags)

    # for course in course_html_tags :
    #     print(course.text)

    course_cards= soup.find_all('div',class_='card')
    for course in course_cards:
        course_name=course.h5.text
        course_price= course.a.text

        print(course_name)
        print(course_price)


