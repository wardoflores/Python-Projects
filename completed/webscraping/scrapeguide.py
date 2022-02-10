#!/bin/zsh
# Followed Beautiful Soup Crash course by freeCodeCamp.


from bs4 import BeautifulSoup

# --- example 1 Basic Scraping

with open('/home/joey/JoeyRepositories/Portfolio-Website/index.html', 'r') as html_file: # Scrape local file
    content = html_file.read() # Prints all the html file contents
    # print(content)

    soup = BeautifulSoup(content, 'lxml') # Scrape content using lxml
    # print(soup.prettify())

    tags = soup.find('h2') # only print 1 element of the Tag  specified
    # print(tags)
    
    alltags = soup.find_all('h2') # Print all elements of the Tag specified
    # print(alltags)

    for i in alltags: # Only outputs text and dismisses the element syntax.
        # print(i.text)
        pass

# --- example 2 Printing specific div classes

with open('/home/joey/JoeyRepositories/Portfolio-Website/index.html', 'r') as html_file: # Scrape local file
    content = html_file.read() # Prints all the html file contents
    # print(content)

    soup = BeautifulSoup(content, 'lxml') # Scrape content using lxml
    div_tags = soup.find_all('div', class_='container') # Call div classes | class_ is named like it because python already has class
    for i in div_tags:
        # print(i)
        # print(i.text)
        
        i_thing = i.text # i.{tag}.{attribute}
        i_thing2 = i.text # i.{tag}.{attribute} | could add .split()[-1]

        # print(i_thing)
        # print(i_thing2)

        print(f'{i_thing} costs {i_thing2}')

    # print(div_tags)