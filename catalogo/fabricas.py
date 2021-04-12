from productos import *

class Fabricas:
    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass

class FabricaCompuesta:
    def crear_montura(self):
        pass

    def crear_cuerpo(self):
        pass

class FabricaHumanos(Fabricas):
    def crear_arma(self):
        return ArmaHumanos()

    def crear_escudo(self):
        return EscudoHumanos()

class FabricaOrcos(Fabricas):
    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()
    

class FabricaElfos(Fabricas, FabricaCompuesta):
    def crear_arma(self):
        return ArmaElfos()

    def crear_escudo(self):
        return EscudoElfos()

    def crear_montura(self):
        return MonturaElfos()

    def crear_cuerpo(self):
        return CuerpoElfos()

