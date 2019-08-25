from flask import Flask
from PollScraper import getDemCandidatePollData as getDemData

app = Flask(__name__)

def makeTableString(name, amt, candidate, perc):
    pass


@app.route("/")
def main():
    returnString = \
    """
    ---Name----------Sum (euro)-------Candidate------
    ---{}{}{}------
    """
    return str(getDemData())




if __name__ == "__main__":
    app.run()