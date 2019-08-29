from flask import Flask, render_template
from PollScraper import getDemCandidatePollData as getDemData

app = Flask(__name__)

@app.route("/")
def home():
    dem_data = getDemData()
    candidate_participant_dict = {"Sanders ": "Bart", "Warren ": "Fransje", "Harris ": "Koen", "Biden ": "Rob"}
    row_list = []
    cnt = 0
    for candidate_name , percentage_polled in dem_data.items():
        if not candidate_name in candidate_participant_dict.keys():
            continue
        cnt += 1
        if cnt == 1:
            return_euro = 4
            win_euro = 3
        else:
            return_euro = 0
            win_euro = -1
        win_euro_symbol = "+" if win_euro >= 0 else ""

        row_list.append("{} - {}({}%)...............{} ({}{})".format(candidate_participant_dict[candidate_name], candidate_name, percentage_polled, return_euro, win_euro_symbol, win_euro))


    return render_template('home.html', row_list=row_list)

@app.route("/about")
def about():
    return "Build by BK024."


if __name__ == "__main__":
    app.run(debug=True)