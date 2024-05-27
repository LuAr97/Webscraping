from bs4 import BeautifulSoup
import requests

def job_seek():
    opportunities = []
    positions = []
    companies = []
    html_text = requests.get('https://www.seek.com.au/Software-Developer-jobs/in-Melbourne-VIC-3000').text
    soup = BeautifulSoup(html_text, 'lxml')
    options = soup.find_all('article')
    
    for option in options:
        opportunity = {}
        html_option = requests.get('https://www.seek.com.au'+option.div.a['href']).text
        soup_option = BeautifulSoup(html_option, 'lxml')
        option_title = soup_option.find('h1').text
        option_company = soup_option.find_all('span', class_ = 'y735df0 _1iz8dgs4y _94v4w0 _94v4w1 _94v4w21 _4rkdcp4 _94v4wa')[4].text
        opportunity['position'] = option_title
        if option_title not in opportunities : positions.append(option_title)
        opportunity['company'] = option_company
        if option_company not in companies : companies.append(option_company)
        opportunity['url'] = 'https://www.seek.com.au'+option.div.a['href']
        opportunities.append(opportunity)
    return(companies,positions,opportunities)

    

