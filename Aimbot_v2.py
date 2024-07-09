import pyautogui
import keyboard
import cv2
import numpy as np

# Coordonnées de la région à analyser
x_start, y_start = 350, 300
x_end, y_end = 1553, 809

# Couleur à rechercher (en BGR)
target_color = np.array([232, 195, 149])

# Fonction pour cliquer sur la couleur spécifique lorsqu'elle est trouvée
def click_on_color(color):
    while True:
        # Capture de l'écran et conversion en format OpenCV
        screen = np.array(pyautogui.screenshot(region=(x_start, y_start, x_end-x_start, y_end-y_start)))
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        
        # Réduction de la résolution de l'image pour accélérer le traitement
        resized_screen = cv2.resize(screen, None, fx=0.5, fy=0.5)
        
        # Recherche de la couleur cible dans la région réduite
        mask = cv2.inRange(resized_screen, color, color)
        points = np.argwhere(mask > 0)
        
        if len(points) > 0:
            # Convertir les coordonnées des points trouvés dans la région réduite aux coordonnées de l'écran complet
            points = points * 2  # Retour à la taille originale
            # Clic sur le premier pixel trouvé
            pyautogui.click(points[0][1] + x_start, points[0][0] + y_start)
            if keyboard.is_pressed('ctrl+c'):  # Vérifie si Ctrl + C est enfoncé
                return  # Sort de la fonction si Ctrl + C est enfoncé
            #break  # Sort de la boucle après avoir cliqué sur le premier point

# Démarrage du bot
pyautogui.PAUSE = 0
pyautogui.click(938, 528)  # Cliquer sur une position initiale
click_on_color(target_color)
