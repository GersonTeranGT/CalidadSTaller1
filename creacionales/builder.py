class Habilidad:
    def __init__(self, nombre, costo_mana, danio):
        self._nombre = nombre
        self._costo_mana = costo_mana
        self._danio = danio

    def obtener_costo_mana(self):
        return self._costo_mana

    def obtener_danio(self):
        return self._danio

    def __str__(self):
        return f"  - {self._nombre} (Mana: {self._costo_mana}, Daño: {self._danio})"


class Personaje:
    def __init__(self):
        self._habilidades = []
        self._nombre = "Sin nombre"
        self._clase = "Aventurero"
        self._nivel = 1
        self._vida = 100

    def agregar_habilidad(self, habilidad):
        self._habilidades.append(habilidad)

    def establecer_nombre(self, nombre):
        self._nombre = nombre

    def establecer_clase(self, clase):
        self._clase = clase

    def establecer_nivel(self, nivel):
        self._nivel = nivel

    def establecer_vida(self, vida):
        self._vida = vida

    def obtener_poder_total(self):
        return sum(hab.obtener_danio() for hab in self._habilidades)

    def __str__(self):
        texto = f" \nPersonaje: {self._nombre}\n"
        texto += f"  Clase: {self._clase}\n"
        texto += f"  Nivel: {self._nivel}\n"
        texto += f"  Vida: {self._vida} HP\n"
        texto += "  Habilidades:\n"
        texto += "\n".join(str(hab) for hab in self._habilidades)
        texto += f"\n Poder total: {self.obtener_poder_total()}"
        return texto


class ConstructorPersonaje:
    def __init__(self):
        self._personaje = Personaje()

    def llamado(self, nombre):
        self._personaje.establecer_nombre(nombre)
        return self

    def de_clase_guerrero(self):
        self._personaje.establecer_clase("Guerrero")
        self._personaje.establecer_vida(200)
        return self

    def de_clase_mago(self):
        self._personaje.establecer_clase("Mago")
        self._personaje.establecer_vida(120)
        return self

    def de_clase_espadachin(self):
        self._personaje.establecer_clase("Espadachin")
        self._personaje.establecer_vida(100)
        return self

    def de_clase_arquero(self):
        self._personaje.establecer_clase("Arquero")
        self._personaje.establecer_vida(150)
        return self

    def de_nivel(self, nivel):
        self._personaje.establecer_nivel(nivel)
        return self

    def con_espada_legendaria(self):
        self._personaje.agregar_habilidad(Habilidad("Espada Legendaria", 20, 150))
        return self

    def con_bola_de_fuego(self):
        self._personaje.agregar_habilidad(Habilidad("Bola de fuego", 50, 200))
        return self

    def con_rayo_helado(self):
        self._personaje.agregar_habilidad(Habilidad("Rayo helado", 30, 120))
        return self

    def con_flecha_multiple(self):
        self._personaje.agregar_habilidad(Habilidad("Flecha multiple", 15, 90))
        return self

    def con_espada_fantasma(self):
        self._personaje.agregar_habilidad(Habilidad("Espada fantasma", 10, 80))
        return self

    def con_clon_sombra(self):
        self._personaje.agregar_habilidad(Habilidad("Clon sombra", 50, 150))
        return self

    def con_curacion(self):
        self._personaje.agregar_habilidad(Habilidad("Curacion", 40, 0))
        return self

    def obtener_personaje(self):
        return self._personaje


constructor = ConstructorPersonaje()
guerrero = (constructor
            .llamado("Thor")
            .de_clase_guerrero()
            .de_nivel(10)
            .con_espada_legendaria()
            .con_curacion()
            .obtener_personaje())
print(guerrero)

constructor2 = ConstructorPersonaje()
espadachin = (constructor2.llamado("Vergil").de_clase_espadachin().de_nivel(999).con_espada_legendaria().con_espada_fantasma().con_curacion().con_clon_sombra().obtener_personaje())
print(espadachin)