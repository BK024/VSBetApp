
class BettingGoal:
    def __init__(self):
        self.betting_goal_id = -1
        self.name = "Democratic Nominee."
        self.informal_description = "The person that will be the democratic candidate for the 2020 elections."
        self.formal_description = "The last name of the person that receives more then 1885 votes for becoming the democratic nominee at the democratic convention that is held from 13-07-2020 until 16-07-2020 in Milwaukee, Wisconsin."
        self.option_data_type = "String"
        self.options = ['Biden', 'Sanders', 'Warren', 'Harris', 'Buttigieg', 'Yang', 'Booker', "O'Rourke", 'Gabbard', 'Castro', 'Klobuchar', 'Bullock', 'Williamson']
        self.resolver = None
