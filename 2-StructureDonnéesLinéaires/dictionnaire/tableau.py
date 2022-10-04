N = 25
def CREER_TABLEAU_VIDE():
    C = [0]*(N)
    V = [0]*(N)
    T = (C,V)
    return T

def HACHAGE(string):
    som = 0
    for i in string:
        som = som + ord(i)
    SN = som%N
    return(SN)

def AJOUTER(T, string, telephone):
    (C,V) = T
    SN = HACHAGE(string)
    if string in C and telephone in V :
        return print("Contact déjà existant")
    elif C[SN] == 0:
        C[SN] = string
        V[SN] = telephone
    else:
        while C[SN] != 0:
            if SN < 25:
                SN = SN+1
            else:
                SN = 1
        C[SN] = string
        V[SN] = telephone
    return T

def RECHERCHER(T, string):
    (C,V) = T
    for i in range(N):
        if C[i] == string:
            return print(string,":",V[i])
    else:
        return print("Contact inexistant")

def MODIFIER(T, string, telephone):
    (C,V) = T
    for i in range(N):
        if C[i] == string:
            V[i] = telephone
            return T
    else:
        return print("Contact inexistant")

def SUPPRIMER(T, string):
    (C,V) = T
    for i in range(N):
        if C[i] == string:
            C[i] = 0
            V[i] = 0
            return T
    else:
        return print("Contact inexistant")