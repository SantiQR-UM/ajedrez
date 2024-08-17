# En la BD almaceno las instancias de pieza y los espacios para buscarlos.
class BD():
    def __init__(self):
        self.__base_datos__ = {}

    # Añade una cosa a la BD, con key como su var, que lo busca con var().
    def add(self, cosa):
        self.__base_datos__[str(cosa.var())] = cosa

    def search(self, var):
        return self.__base_datos__[var]

