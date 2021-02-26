class Meteo:
    def __init__(self,temp,wind):
        self.temp=temp
        self.wind=wind
    
    def __lt__(self,m):
        return self.temp<m.temp
    def __eq__(self,m):
        return self.temp==m.temp

m_yesterday=Meteo(-5.0,25.00)
m_today=Meteo(-5.0,15.00)


if m_yesterday< m_today:
    print("It's getting warmer")
elif m_yesterday==m_today:
    print("It's the same")
else:
    print("It's getting colder")