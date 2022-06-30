class Ave:
    nombre = ''
    no_vuela = False
    extinto = False

    def get_speed(self):
        raise NotImplementedError


class Guacamayo(Ave):
    nombre = 'Guacamayo'

    def get_speed(self):
        return 14


class Cardenal(Ave):
    nombre = 'Cardenal'

    def get_speed(self):
        return 12


class Avestruz(Ave):
    nombre = 'Avestruz'
    no_vuela = True

    def get_speed(self):
        return 15


class Archaeopteryx(Ave):
    nombre = 'Archaeopteryx'
    extinto = True

    def get_speed(self):
        return -1
