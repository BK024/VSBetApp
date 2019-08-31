# As deployed to BK024.pythonanywhere.com with version 0.8.

class BetParticipant:
    def __init__(self, participant, bet_prediction, bet_amount):
        self.participant = participant
        self.entry_amount = bet_amount
        self.entry_option = bet_prediction
        self.entry_date = None
        self.bet_notes = ""