import pyautogui
import keyboard

# Définir les coordonnées de départ
x_start, y_start = 350, 300
# Définir les coordonnées de fin
x_end, y_end = 1553, 809
# Définir l'espacement horizontal et vertical
spacing_x = 85
spacing_y = 92

# Fonction pour cliquer sur une position donnée
def click_at(x, y):
    pyautogui.click(x, y)

# Fonction pour parcourir les coordonnées et effectuer des clics
def click_coordinates(x_start, y_start, x_end, y_end, spacing_x, spacing_y):
    pyautogui.PAUSE = 0  # Désactiver la pause de pyautogui pour accélérer les opérations
    while True:
        for y in range(y_start, y_end + 1, spacing_y):
            for x in range(x_start, x_end + 1, spacing_x):
                pyautogui.moveTo(x, y)  # Déplacer la souris à la position spécifiée
                click_at(x, y)
                if keyboard.is_pressed('ctrl+c'):  # Vérifie si Ctrl + C est enfoncé
                    return  # Sort de la fonction si Ctrl + C est enfoncé

# Appel de la fonction avec les paramètres spécifiés
click_coordinates(x_start, y_start, x_end, y_end, spacing_x, spacing_y)
