"""
NSI Archicture, Systèmes d'exploitation
Interblocage dans un robot.
"""

# Librairies utilisées
from threading import Thread 
from threading import Lock
import time
import random


# Les ressources utilisées par le robot
R1_moteurs = Lock()
R2_wifi = Lock()
R3_camera = Lock()

# Variable partagée par les 3 threads
fin = False


def P1_pilotage_manuel():    
    """Fonction embarquée dans le thread P1"""
    while fin == False:
        print("P1 : demande de R1_moteurs...")
        R1_moteurs.acquire()
        print("P1 : demande de R2_wifi...")
        R2_wifi.acquire()
        print("P1 : début travail")
        time.sleep(random.random()/100.0)
        print("P1 : fin travail")
        print("P1 : libération de R1_moteurs...")
        R1_moteurs.release()
        print("P1 : libération de R2_wifi...")
        R2_wifi.release()

def P2_envoi_flux_video():
    """Fonction embarquée dans le thread P2"""
    while fin == False:
        print("P2 : demande de R2_wifi...")
      

def P3_auto_tests_materiels():
    """Fonction embarquée dans le thread P1"""
    while fin == False:
        print("P3 : demande de R3_camera...")
     
        


if __name__ == '__main__':
    # Création des threads
    t1 = Thread(target=P1_pilotage_manuel)
    t2 = Thread(target=P2_envoi_flux_video)
    t3 = Thread(target=P3_auto_tests_materiels)

    # Lancement des threads
    t1.start()
    t2.start()
    t3.start()

    # Attente de la fin du travail
    t1.join()
    t2.join()
    t3.join()
