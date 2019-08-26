"""
Class that contains methods for scraping poll data from websites.
"""

import requests
from collections import OrderedDict as OD
from bs4 import BeautifulSoup


def getDemCandidatePollData():
    """
    Method that gets the latest polling data for the democratic nomination from real clear politics. It retrieves the latest real clear politics average (RCP AVG).
    It returns an OrderedDict with the candidate names as keys and their chance of winning the nomination as a percentage (float) as value.
    """
    candidate_dict = OD()
    response = requests.get('https://www.realclearpolitics.com/epolls/2020/president/us/2020_democratic_presidential_nomination-6730.html')
    soup = BeautifulSoup(response.text, 'html.parser')
    for i in soup.find("table", attrs={'class': 'data large'}).findAll('th', attrs={'class': 'diag'}):
        candidate_dict[i.find('span').text] = -1
    candidate_name_list = list(candidate_dict.keys())
    num_candidates = len(candidate_dict)
    for num, i in enumerate(soup.find("table", attrs={'class': 'data large'}).find('tr', attrs={'class': "rcpAvg"})):
        if num in [0, 1]:
            continue
        if num == (num_candidates + 2):
            break
        candidate_dict[candidate_name_list[num-2]] = float(i.text)
    return candidate_dict
