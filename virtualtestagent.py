from pokerweb import handsengine

class VirtualTestAgent(handsengine):
    def __init__(self, handsinfo,pokeragent):
        handsengine.__init__(self,handsinfo)
        self.m_pokeragent = pokeragent

    def test(self):
        pass