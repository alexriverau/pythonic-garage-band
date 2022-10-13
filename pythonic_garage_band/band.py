class Band:

    instances = []

    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        return [member.play_solo() for member in self.members]

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician:
    def __init__(self, name, instrument, solo):
        self.name = name
        self.instrument = instrument
        self.solo = solo

    def __str__(self):
        return f'My name is {self.name} and I am a musician'

    def __repr__(self):
        return f'Musician instance. Name = {self.name}'

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Guitarist(Musician):
    def __init__(self, name, instrument='guitar', solo='face melting guitar solo'):
        super().__init__(name, instrument, solo)

    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    def get_instrument(self):
        return self.instrument


class Bassist(Musician):
    def __init__(self, name, instrument='bass', solo='bom bom buh bom'):
        super().__init__(name, instrument, solo)

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    def get_instrument(self):
        return self.instrument


class Drummer(Musician):
    def __init__(self, name, instrument='drums', solo='rattle boom crash'):
        super().__init__(name, instrument, solo)

    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    def get_instrument(self):
        return self.instrument
