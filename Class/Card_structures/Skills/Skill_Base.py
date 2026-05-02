class Habilidad:
    def __init__(self, nombre, efecto, objetivo="enemigo", coste_mp=0, **params):
        self.nombre = nombre
        self.efecto = efecto
        self.objetivo = objetivo
        self.coste_mp = coste_mp
        self.params = params

    def usar(self, user, target=None):

        # 🔥 validar MP
        if user.MP < self.coste_mp:
            return {"error": "no_mp"}

        # consumir MP
        user.MP -= self.coste_mp

        # definir target
        if self.objetivo == "self":
            target = user

        return self.efecto(user, target, **self.params)