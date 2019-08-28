from flask import Flask, render_template
from PollScraper import getDemCandidatePollData as getDemData

app = Flask(__name__)

@app.route("/")
def home():
    demData = getDemData()
    return render_template('home.html', demData=demData)

@app.route("/about")
def about():
    return "Build by bSOFT."


if __name__ == "__main__":
    app.run(debug=True)