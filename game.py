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

