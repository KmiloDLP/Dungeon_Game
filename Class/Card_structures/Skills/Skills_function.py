import random



# Damage skills
def Damage_skills(user, target, bonus):
    daño = int(user.Atk * bonus)
    result = target.Recibir_daño(daño, user)
    return {"damage": result}

# Buff Stats
def Buff_Stats(user, bonus, stat):
    base_attr = f"Base_{stat}"
    current_attr = stat

    if not hasattr(user, base_attr):
        return {"error": "invalid_stat"}

    base_value = getattr(user, base_attr)
    buff = int(base_value * bonus)

    setattr(user, current_attr, getattr(user, current_attr) + buff)

    return {"buff": buff, "stat": stat}

# Debuff Stats
def Debuff_Stats(target, bonus, stat):
    base_attr = f"Base_{stat}"
    current_attr = stat

    if not hasattr(target, base_attr):
        return {"error": "invalid_stat"}

    base_value = getattr(target, base_attr)
    debuff = int(base_value * bonus)

    setattr(target, current_attr, getattr(target, current_attr) - debuff)

    return {"debuff": debuff, "stat": stat}

# Buff + Debuff
def Buff_debuff(user, bonus1, stat1, bonus2, stat2):
    r1 = Buff_Stats(user, bonus1, stat1)
    r2 = Debuff_Stats(user, bonus2, stat2)

    return {
        "buff": r1,
        "debuff": r2
    }

# Status
def Status_modification(target, duration, state):
    target.debuff = state
    target.debuff_duration = duration

    return {"status": state, "duration": duration}

# Drain
def Drain_hp(user, target, bonus_damage, bonus_heal):
    damage = int(user.Atk * bonus_damage)
    result_damage = target.Recibir_daño(damage, user)

    heal = int(damage * bonus_heal)
    result_heal = user.Heal(heal)

    return {
        "damage": result_damage,
        "heal": result_heal
    }

#Healing
def Healings(user, bonus):
    heal = int(user.Base_HP * bonus)
    result = user.Heal(heal)

    return {"heal": result}

# Difference damage
def difference(user, target, stat, superior=True):

    if not hasattr(user, stat) or not hasattr(target, stat):
        return {"error": "invalid_stat"}

    user_val = getattr(user, stat)
    target_val = getattr(target, stat)

    if superior:
        diff = user_val - target_val
    else:
        diff = target_val - user_val

    diff = max(1, diff)

    daño = int(user.Atk * (1 + diff * 0.01))
    result = target.Recibir_daño(daño, user)

    return {"damage": result, "scale": diff}

# Debuff strike
def Debuff_stroke(user, target, stat, bonus):
    daño = int(user.Atk * bonus)
    result_damage = target.Recibir_daño(daño, user)

    result_debuff = Debuff_Stats(target, bonus, stat)

    return {
        "damage": result_damage,
        "debuff": result_debuff
    }

# steal
def steal_stats(user, target, stat, bonus):


    base_attr = f"Base_{stat}"

    if not hasattr(target, base_attr):
        return {"error": "invalid_stat"}

    steal_value = int(getattr(target, base_attr) * bonus)

    # quitar al target
    setattr(target, stat, getattr(target, stat) - steal_value)

    # dar al user
    setattr(user, stat, getattr(user, stat) + steal_value)

    return {
        "steal": steal_value,
        "stat": stat
    }


def multi_hit(user, target, bonus, limite, probabilidad):

    hits = 1

    # intenta seguir golpeando hasta el límite
    for _ in range(limite - 1):
        if random.random() <= probabilidad:
            hits += 1
        else:
            break

    total_damage = 0

    for _ in range(hits):
        daño = int(user.Atk * bonus)
        result = target.Recibir_daño(daño, user)

        if result == "dead":
            total_damage += daño
            break

        total_damage += result

    return {
        "hits": hits,
        "total_damage": total_damage
    }