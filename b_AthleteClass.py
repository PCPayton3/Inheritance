
class Athlete:
    def __init__(self, ht, wt, bodyfat):
        self.__ht = ht
        self.__wt = wt
        self.__bf = bodyfat

    def get_ht(self):
        return self.__ht

    def get_wt(self):
        return self.__wt

    def get_bf(self):
        return self.__bf


class Football_Player(Athlete):

    def __init__(self, ht, wt, bodyfat, position, team):

        Athlete.__init__(self, ht, wt, bodyfat)

        self.__position = position
        self.__team = team

    def get_position(self):
        return self.__position

    def get_team(self):
        return self.__team


class Basketball_Player(Athlete):
    def __init__(self, ht, wt, bodyfat, spot, team, number):

        Athlete.__init__(self, ht, wt, bodyfat)
        self.__spot = spot
        self.__team = team
        self.__number = number

    def get_spot(self):
        return self.__spot

    def get_team(self):
        return self.__team

    def get_number(self):
        return self.__number
