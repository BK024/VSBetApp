# As deployed to BK024.pythonanywhere.com with version 0.8.

from flask import Flask, render_template
from PollScraper import getDemCandidatePollData as getDemData
from Participant import Participant
from BetParticipant import BetParticipant
from TableToHtml import Table
from Bet import Bet
from collections import OrderedDict as OD
make_link = Table.make_html_hyper_link

app = Flask(__name__)

@app.route("/")
def home():
    dem_data = getDemData(no_access_to_outside=True)
    ordered_candidate_list = [x for x in dem_data.keys()]
    table_list = []
    cnt = 0
    bet = make_bet(make_bet_participant_OD(ordered_candidate_list), dem_data)
    table_list.append(bet.get_html_table())

    return render_template('home.html', table_list=table_list)

@app.route("/about")
def about():
    return "A Python WebApp for tracking bets regarding the 2020 USA presidential elections.\nBuild by BK024.\nFor the source code look at {}".format(make_link("https://github.com/BK024/VSBetApp", "my GitHub account."))


def make_bet(participant_OD, bet_data):
    new_bet = Bet("Bet 1: Dem Nomination", participant_OD, bet_data)
    return new_bet


def make_bet_participant_OD(bet_data_name_list):
    candidate_participant_dict = {"Sanders": "Bart", "Warren": "Fransje", "Harris": "Koen", "Biden": "Rob"}
    b_P_OD = OD()
    for cnt, item in enumerate(sorted(candidate_participant_dict.items(), key=lambda x: bet_data_name_list.index(x[0]))):
        bet_prediction, name = item
        p = Participant(name, cnt)
        bp = BetParticipant(p, bet_prediction, 1)
        b_P_OD[name] = bp
    return b_P_OD


if __name__ == "__main__":
    app.run(debug=True)

