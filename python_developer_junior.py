import json
from bs4 import BeautifulSoup
import requests


class ParseWebsite(object):

    def __init__(self, RAW_URL='https://www.hyperia.sk', START_PAGE='/kariera/'):
        self.data = []
        self.raw_url = RAW_URL
        self.start_page = START_PAGE

    def get_data(self):

        job_offer_start_page = requests.get(f'{self.raw_url}{self.start_page}')
        start_page_soup = BeautifulSoup(job_offer_start_page.content, 'html.parser')

        job_offer_links_html = start_page_soup.find_all('a', string='viac info')

        for job_offer_link_html in job_offer_links_html:

            job_offer_url = f"{self.raw_url}{job_offer_link_html.get('href')}"
            job_offer_page = requests.get(job_offer_url)

            job_offer_soup = BeautifulSoup(job_offer_page.content, 'html.parser')

            # # shorter code
            # place, salary, contract_type = [str(job_offer_info).split(str(job_offer_info.find('br')))[-1][:-len('</p>')]
            #                                 for job_offer_info in job_offer_soup.find('div', 'hero-icons text-center col-md-12').find_all('p')]

            job_offer_info_list = []
            # loop through each job_offer info -> place, salary, contract_type
            for job_offer_info in job_offer_soup.find('div', 'hero-icons text-center col-md-12').find_all('p'):
                split_text_for_br = str(job_offer_info).split(str(job_offer_info.find('br')))
                # get relevant info without ending tags -> '</p>'
                relevant_info = split_text_for_br[1][:-len('</p>')]
                job_offer_info_list.append(relevant_info)

            title = job_offer_soup.find('div', 'hero-text col-lg-12').find('h1').text
            place, salary, contract_type = job_offer_info_list
            contact_email = job_offer_soup.find('div', 'container position-contact').find('strong').text

            self.data.append({
                'title': title,
                'place': place,
                'salary': salary,
                'contract_type': contract_type,
                'contact_email': contact_email
            })

        return self.data


parse = ParseWebsite()
data = parse.get_data()
json_data_output = json.dumps(data, ensure_ascii=False)

with open('json_data_output.json', 'w', encoding='utf-8') as f:
    f.write(json_data_output)
