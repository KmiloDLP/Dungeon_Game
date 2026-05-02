import os
import inspect
class Habilidad:
    def __init__(self, nombre, type, efecto, objetivo="enemigo", coste_mp=0, **params ):
        self.nombre = nombre
        self.efecto = efecto
        self.objetivo = objetivo
        self.coste_mp = coste_mp
        self.params = params

        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, "Skills_font")
        self.Fund = os.path.join(img_dir, f"{type}.png")    
        

    def usar(self, user, target=None):

        # 🔥 validar MP
        if user.MP < self.coste_mp:
            return {"error": "no_mp"}

        # consumir MP
        user.MP -= self.coste_mp

        # definir target
        if self.objetivo == "self":
            target = user

        sig = inspect.signature(self.efecto)
        params = list(sig.parameters.values())

        if len(params) >= 2 and params[0].name == "user" and params[1].name == "target":
            return self.efecto(user, target, **self.params)

        if len(params) >= 1 and params[0].name == "target":
            return self.efecto(target, **self.params)

        return self.efecto(user, **self.params)
    