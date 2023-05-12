class Musician:
    def __init__(self, name = "empty", instrument = "empty", profession="empty", solo="empty"):
        self.name = name
        self.instrument = instrument
        self.profession = profession
        self.solo = solo

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
    
    def __repr__(self):
        return f"{self.profession} instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument
    
    def play_solo(self):
        return self.solo
    
class Guitarist(Musician):
    def __init__(self, name):
        instrument = "guitar"
        profession = "Guitarist"
        solo = "face melting guitar solo"
        super().__init__(name, instrument, profession, solo)
    
class Drummer(Musician):
    def __init__(self, name):
        instrument = "drums"
        profession = "Drummer"
        solo = "rattle boom crash"
        super().__init__(name, instrument, profession, solo)
    
class Bassist(Musician):
    def __init__(self, name):
        instrument = "bass"
        profession = "Bassist"
        solo = "bom bom buh bom"
        super().__init__(name, instrument, profession, solo)
    

class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        # anonymous function
        get_solo = lambda member : member.play_solo()
        return list(map(get_solo, self.members))
    
    @staticmethod
    def to_list():
        return Band.instances