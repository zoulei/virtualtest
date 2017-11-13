from hunlgame import Poker
from pokerweb import handsengine

class DealerFromHistory(Poker):
    def __init__(self, handsdata):
        self.m_handsengine = handsengine(handsdata)
        playerquantity = self.m_handsengine.getplayerquantity()
        Poker.__init__(playerquantity)

    def getFlop(self):
        return self.m_handsengine.getboard()[:3]

    def getTurn(self):
        return self.m_handsengine.getboard()[3]

    def getRiver(self):
        return self.m_handsengine.getboard()[4]

    def distribute(self):
        return self.m_handsengine.m_privatehands

    def distributehand(self, pos):
        return self.m_handsengine.gethand(pos)

    def updateaction(self, action , value):
        self.m_handsengine.executenextaction()

    def getboard(self):
        return self.m_handsengine.getcurboard()

    def getcurrentturn(self):
        return self.m_handsengine.m_curturn

class Dealer(Poker):
    # the first element of pokeragentlist is button
    # and the last element of pokeragentlist is small blind
    def __init__(self):
        Poker.__init__(self)

        self.m_actionhis = []

    # def distribute(self):
    #     hands = Poker.distribute(self)
    #     for agent, hand in zip(self.m_agents[::-1],hands):
    #         agent.sethand(hand)

    def distributehand(self, pos):
        pass

    def updateaction(self):
        pass

    def getcurrentturn(self):
        pass
