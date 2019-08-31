from datetime import date
from collections import OrderedDict as OD
import Participant
from collections import Counter
from TableToHtml import Table
import BetParticipant, Participant

class Bet:
    def __init__(self, name, bet_participant_OD, bet_data_OD):
        self.name = ""
        self.start_date = date(year=2019, month=8, day=24)
        self.end_date = date(year=2020, month=7, day=16)
        self.bet_cluster_id = 1
        self.is_dynamic = True
        self.bet_data_OD = bet_data_OD
        self.bet_participant_OD = bet_participant_OD
        self.payout_str_dict = self.make_payout_dict()
        self.payout_calculator = None
        self.table = self.get_html_table()

    def get_html_table(self):
        header_OD = OD([("Position", 8), ("Participant", 20), ("Candidate (%)", 20), ("Payout (profit)", 10)])
        rows = self.make_row_OD_list_for_html()
        return Table(header_OD, rows, name="Dem nomination bet.", row_size=len(header_OD), num_rows=len(rows))

    def make_row_OD_list_for_html(self):
        row_OD_list = []
        cnt = 0
        for k, v in self.bet_participant_OD.items():
            v: BetParticipant
            row = OD()
            cnt += 1
            row["Position"] = cnt
            row["Participant"] = k
            row["Candidate"] = v.entry_option
            row["Payout"] = self.payout_str_dict[v.participant.name]
            row_OD_list.append(row)
        return row_OD_list

    def make_payout_dict(self):
        total_euro = 0
        entry_euro = 0
        payout_dict = {}
        profit_symbol = ""
        winning_participant = self.determine_winner()
        for name, b_p in self.bet_participant_OD.items():
            total_euro += b_p.entry_amount
            entry_euro = b_p.entry_amount

        for name, b_p in self.bet_participant_OD.items():
            total_payout = total_euro if name == winning_participant else 0
            profit = total_payout-entry_euro
            profit_symbol = "+" if profit >= 0 else ""
            payout_dict[name] = "{} ({})".format(total_payout, profit_symbol+str(profit))

        return payout_dict

    def determine_winner(self):
        winning_option = list(self.bet_data_OD.keys())[0]
        return [x.participant.name for x in self.bet_participant_OD.values() if x.entry_option == winning_option][0]