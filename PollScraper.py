# As deployed to BK024.pythonanywhere.com with version 0.8.
"""
Class that contains methods for scraping poll data from websites.
"""

import requests
from collections import OrderedDict as OD
from bs4 import BeautifulSoup


def getDemCandidatePollData(no_access_to_outside=True):
    """
    Method that gets the latest polling data for the democratic nomination from real clear politics. It retrieves the latest real clear politics average (RCP AVG).
    It returns an OrderedDict with the candidate names as keys and their chance of winning the nomination as a percentage (float) as value.
    """

    if no_access_to_outside:
        return OD([('Biden', 28.9), ('Sanders', 17.1), ('Warren', 16.5), ('Harris', 7.0), ('Buttigieg', 4.6), ('Yang', 2.5), ('Booker', 2.4), ("O'Rourke", 2.4), ('Gabbard', 1.4), ('Castro', 1.1), ('Klobuchar', 0.9), ('Bullock', 0.8), ('Williamson', 0.8)])
    else:
        candidate_dict = OD()
        response = requests.get('https://www.realclearpolitics.com/epolls/2020/president/us/2020_democratic_presidential_nomination-6730.html')
        soup = BeautifulSoup(response.text, 'html.parser')
        for i in soup.find("table", attrs={'class': 'data large'}).findAll('th', attrs={'class': 'diag'}):
            candidate_dict[str(i.find('span').text).strip()] = -1
        candidate_name_list = list(candidate_dict.keys())
        num_candidates = len(candidate_dict)
        for num, i in enumerate(soup.find("table", attrs={'class': 'data large'}).find('tr', attrs={'class': "rcpAvg"})):
            if num in [0, 1]:
                continue
            if num == (num_candidates + 2):
                break
            candidate_dict[candidate_name_list[num-2]] = float(i.text)
        print(candidate_dict)
        return candidate_dict
