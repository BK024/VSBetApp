from datetime import date
from collections import OrderedDict as OD
import Participant
from collections import Counter


class Bet:
    def __init__(self):
        self.name = ""
        self.start_date = date(year=2019, month=8, day=24)
        self.end_date = date(year=2020, month=7, day=16)
        self.bet_cluster_id = 1
        self.is_dynamic = True
        self.participant_id_list = [1, 2, 3, 4]
        self.participant_OD = OD()
        self.ledger = {}
        self.payout_calculator = None

    def set_participant_in_participantOD(self, participant_list):
        for participant_to_set in participant_list:
            self.participant_OD[participant_to_set.participant_id] = participant_to_set

        assert compare(self.participant_id_list, self.participant_OD.keys())

@staticmethod
def compare(x, y):
    return Counter(x) == Counter(y)
