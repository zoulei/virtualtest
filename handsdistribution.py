
class HandsDisQuality:
    def __init__(self,dis = None):
        if dis is None:
            self.m_handsdis = {}
        else:
            self.m_handsdis = dis

    def __add__(self, other):
        for key in self.m_handsdis.keys():
            self.m_handsdis[key] += other.m_handsdis.get(key,0)
        for key in other.m_handsdis.keys():
            if key in self.m_handsdis:
                continue
            self.m_handsdis[key] = other.m_handsdis[key]
        return self

    # make the sum of probability be 1
    def normalize(self):
        total = sum(self.m_handsdis.values())
        for key in self.m_handsdis.keys():
            self.m_handsdis[key] /= total

    def calquality(self):
        pass

    def getquality(self):
        pass