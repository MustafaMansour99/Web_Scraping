import requests
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/History_of_Mexico"
"""
this function to return the count of the citation letter
"""
def get_citations_needed_count(url):
    page = requests.get(url)
    #convert from byte to html
    soup=BeautifulSoup(page.content,'html.parser')
    all_post=soup.find_all('sup',class_="noprint")
    return print("The citation nedded count is : ",len(all_post))
"""
this function to get the paragraph contan the citation
"""

def  get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_tags = soup.find_all('sup', class_='noprint')
    citations = [response.find_previous('p').text.strip() for response in citation_tags]
    result = '\n'.join(citations)
    return print(result)
get_citations_needed_count(url)
get_citations_needed_report(url)