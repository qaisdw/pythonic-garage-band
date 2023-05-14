class Musician:
    def __init__(self, name = "empty", instrument = "empty", profession="empty", solo="empty"):
        """
        Initializes the Musician class with a name, instrument, profession, and solo attribute.
        
        Args:
        name (str): the name of the musician (default "empty")
        instrument (str): the instrument the musician plays (default "empty")
        profession (str): the profession of the musician (default "empty")
        solo (str): the type of solo the musician can play (default "empty")
        """
        self.name = name
        self.instrument = instrument
        self.profession = profession
        self.solo = solo

    def __str__(self):
        """
        Returns a string representation of the Musician object.
        
        Returns:
        str: the musician's name and instrument
        """
        return f"My name is {self.name} and I play {self.instrument}"
    
    def __repr__(self):
        """
        Returns a string representation of the Musician object to be used for debugging.
        
        Returns:
        str: the musician's name, instrument, and profession
        """
        return f"{self.profession} instance. Name = {self.name}"

    def get_instrument(self):
        """
        Returns the instrument the Musician plays.
        
        Returns:
        str: the musician's instrument
        """
        return self.instrument
    
    def play_solo(self):
        """
        Returns the type of solo the Musician can play.
        
        Returns:
        str: the musician's solo
        """
        return self.solo
    
class Guitarist(Musician):
    def __init__(self, name):
        """
        Initializes the Guitarist class with a name, instrument, profession, and solo attribute.
        Calls the parent class's __init__ method.
        
        Args:
        name (str): the name of the guitarist
        """
        instrument = "guitar"
        profession = "Guitarist"
        solo = "face melting guitar solo"
        super().__init__(name, instrument, profession, solo)
    
class Drummer(Musician):
    def __init__(self, name):
        """
        Initializes the Drummer class with a name, instrument, profession, and solo attribute.
        Calls the parent class's __init__ method.
        
        Args:
        name (str): the name of the drummer
        """
        instrument = "drums"
        profession = "Drummer"
        solo = "rattle boom crash"
        super().__init__(name, instrument, profession, solo)
    
class Bassist(Musician):
    def __init__(self, name):
        """
        Initializes the Bassist class with a name, instrument, profession, and solo attribute.
        Calls the parent class's __init__ method.
        
        Args:
        name (str): the name of the bassist
        """
        instrument = "bass"
        profession = "Bassist"
        solo = "bom bom buh bom"
        super().__init__(name, instrument, profession, solo)
    

class Band:
    instances = []

    def __init__(self, name, members):
        """
        Initializes a Band instance with the given name and members.

        Args:
        - name (str): The name of the band.
        - members (list): A list of Musician objects representing the members of the band.
        """
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        """
        Plays the solo of each member of the band.

        Returns:
        - A list of strings representing the solos played by each member of the band.
        """
        # lambda is an anonymous function
        get_solo = lambda member : member.play_solo()
        return list(map(get_solo, self.members))
    

    '''
      In brief, @staticmethod is used for methods that don't depend on the class or its instances,
      while @classmethod is used for methods that work with the class itself or its instances.
    '''
    
    @staticmethod
    def to_list():
        """
        Returns a list of all Band instances created.

        Returns:
        - A list of Band instances.
        """
        return Band.instances