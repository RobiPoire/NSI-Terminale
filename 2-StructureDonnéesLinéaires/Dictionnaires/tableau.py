size = 25
def CREER_TABLEAU_VIDE():
    keys = [0]*(size)
    values = [0]*(size)
    T = (keys, values)
    return T

def HACHAGE(key):
    sum = 0
    for i in key:
        sum = sum + ord(i)
    SN = sum % size
    return(SN)

def AJOUTER(T, key, value):
    (keys, values) = T
    SN = HACHAGE(key)
    if key in keys and value in values :
        return print("Contact déjà existant")
    elif keys[SN] == 0:
        keys[SN] = key
        values[SN] = value
    else:
        while keys[SN] != 0:
            if SN < 25:
                SN = SN+1
            else:
                SN = 1
        keys[SN] = key
        values[SN] = value
    return T

def RECHERCHER(T, key):
    (keys, values) = T
    for i in range(size):
        if keys[i] == key:
            return print(key,":", values[i])
    else:
        return print("Contact inexistant")

def MODIFIER(T, key, value):
    (keys, values) = T
    for i in range(size):
        if keys[i] == key:
            values[i] = value
            return T
    else:
        return print("Contact inexistant")

def SUPPRIMER(T, key):
    (keys, values) = T
    for i in range(size):
        if keys[i] == key:
            keys[i] = 0
            values[i] = 0
            return T
    else:
        return print("Contact inexistant")