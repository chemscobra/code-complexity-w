class Ave:
    nombre = ''
    no_vuela = False
    es_extinto = False

    def get_speed(self):
        if self.es_extinto:
            return -1  # no nos interesa saber la velocidad de un ave extinta
        else:
            if self.no_vuela:
                if self.name == 'Avestruz':
                    return 15
                elif self.name == 'Gallina':
                    return 7
                elif self.name == 'Pingüino':
                    return 8
                else:
                    return -1  # ave no tiene nombre
            else:
                if self.name == 'Cardenal':
                    return 12
                elif self.name == 'Chuchube':
                    return 10
                elif self.name == 'Guacamayo':
                    return 14
                elif self.name == 'Colibrí':
                    return 16
                else:
                    return -1
