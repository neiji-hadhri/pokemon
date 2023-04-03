class Pokémon :
    def __init__(self, nom, niveau, puissanceattaque, defense=0, pointdevie=100  ) -> None:
        self.__nom = nom
        self.__vie = pointdevie
        self.niveau = niveau
        self.attaque = puissanceattaque
        self.defense = defense

    def getnom(self):
         return self.__nom
    
    def getvie(self):
         return self.__vie

class Normal(Pokémon):
        def __init__(self, nom, niveau, puissanceattaque, defense=0, pointdevie=100) -> None:
            super().__init__(nom, niveau, puissanceattaque, defense, pointdevie)
            puissanceattaque = 27
            self.NPokemonpv = pointdevie
            self.Nattaque = puissanceattaque
        

class Feu(Pokémon):
        def __init__(self, nom, niveau, puissanceattaque, defense=0, pointdevie=100) -> None:
            super().__init__(nom, niveau, puissanceattaque, defense, pointdevie)
            puissanceattaque = 26
            self.Fpokémonpv = pointdevie
            self.Fattaque = puissanceattaque

            

class Eau(Pokémon):
        def __init__(self, nom, niveau, puissanceattaque, defense=0, pointdevie=100) -> None:
            super().__init__(nom, niveau, puissanceattaque, defense, pointdevie)
            puissanceattaque = 24
            self.Epokémonpv = pointdevie
            self.Eattaque = puissanceattaque

class Terre(Pokémon):
        def __init__(self, nom, niveau, puissanceattaque, defense=0, pointdevie=100) -> None:
            super().__init__(nom, niveau, puissanceattaque, defense, pointdevie)
            puissanceattaque = 25
            self.Tpokémonpv = pointdevie
            self.Tattaque = puissanceattaque



class Combat(Pokémon) :
    def __init__(self, nom, niveau, puissanceattaque, defense=0, pointdevie=100) -> None:
         super().__init__(nom, niveau, puissanceattaque, defense, pointdevie)
    

    def verifie(self):
        if self.__vie <= 0  :
            print("{} n'as plus de vie".format(self.__nom))
    
    def renvoie(self):
        pvnormal = getattr(Normal, 'self.NPokemonpv')
        pvfeu = getattr(Feu, 'self.FPokemonpv')
        pveau = getattr(Eau, 'self.EPokemonpv')
        pvterre = getattr(Terre, 'self.TPokemonpv')


        if self.__vie >= pvnormal or pvfeu or pveau or pvterre and self.__vie >= 0 :
            print("Le vainqueur est {}".format(self.__nom ))
        else :
            self.__vie < pvnormal or pvfeu or pveau or pvterre and self.__vie <= 0 
            print("Le perdant est {}".format(self.__nom ))

        if self.__vie <= pvnormal or pvfeu or pveau or pvterre and self.__vie <= 0 :
            print("Le perdant est {}".format(self.__nom ))
        else :
            self.__vie > pvnormal or pvfeu or pveau or pvterre and self.__vie >= 0 
            print("Le vainqueur est {}".format(self.__nom ))
        


    def recupere(self):
        #Normal
        if Normal in Feu:
             getattr('self.Nattaque') * 0.75
        if Feu in Normal:
             getattr('self.Fattaque') * 1
        if Normal in Eau:
             getattr('self.Nattaque') * 0.75
        if Eau in Normal :
             getattr('self.Eattaque') * 1
        if Normal in Terre:
             getattr('self.Fattaque') * 1
        if Terre in Normal:
             getattr('self.Nattaque') * 0.75
        if Normal in Normal :
             getattr('self.Eattaque') * 1
        if Normal in Normal :
             getattr('self.Eattaque') * 1

        
        if Eau in Eau:
             getattr('self.Eattaque') * 1
        if Eau in Feu:
             getattr('self.Eattaque') * 2
        if Feu in Eau:
             getattr('self.Fattaque') * 0.5
        if Eau in Terre :
             getattr('self.Eattaque') * 0.5
        if Terre in Eau:
             getattr('self.Tattaque') * 2


        if Feu in Feu:
             getattr('self.Fattaque') * 0.75
        if Feu in Terre :
             getattr('self.Fattaque') * 2
        if Terre in Feu :
             getattr('self.Tattaque') * 0.5

        if Terre in Terre:
             getattr('self.Tattaque') * 1

    def enleve (recupere):
        
         
         
             

Pok = Combat("js", 12, 15)
Pok.recupere()