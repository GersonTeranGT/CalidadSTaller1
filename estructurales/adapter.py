
class ReproductorMP3:
    """Reproductor moderno digital"""
    def reproducir_mp3(self, cancion):
        return f"Reproduciendo MP3: {cancion}"


class TocadiscosVinilo:
    """Tocadiscos antiguo analogico"""
    def girar_vinilo(self, disco):
        return f"Girando vinilo: {disco}"



class AdaptadorViniloMP3:

    def __init__(self, tocadiscos):
        self._tocadiscos = tocadiscos

    def reproducir_mp3(self, cancion):
        #convierte: mp3 a vinilo
        resultado = self._tocadiscos.girar_vinilo(cancion)
        return f"[Convertido a MP3] {resultado}"



def escuchar_musica(reproductor, cancion):
    """El cliente solo sabe usar reproducir_mp3"""
    print(reproductor.reproducir_mp3(cancion))


print(" \nReproductor moderno ")
mp3 = ReproductorMP3()
escuchar_musica(mp3, "Bohemian Rhapsody")

print(" \nTocadiscos con adaptador ")
vinilo = TocadiscosVinilo()
adaptador = AdaptadorViniloMP3(vinilo)
escuchar_musica(adaptador, "Abbey Road - The Beatles")