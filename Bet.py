from datetime import datetime
from collections import OrderedDict as OD


class Bet:
    def __init__(self):
        self.name = ""
        self.start_date = ""
        self.end_date = ""
        self.bet_cluster_id = -1
        self.is_dynamic = True
        self.participant_OD = OD()
        self.ledger = {}
        self.payout_calculator = None

