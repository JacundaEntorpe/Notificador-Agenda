from plyer import notification
import pygame
import time
import sys
import ctypes

if sys.platform == "win32":
    app_id = 'Notificador Agenda' 
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

def set_alarm(event_title):

    notification.notify(
        title=event_title,
        message="Hora de beber água.",
        app_name="Notificador",
        app_icon='assets/icone.ico',
        timeout=5
    )

    pygame.mixer.init()
    pygame.mixer.music.load('assets/alarm_sound.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


if __name__ == "__main__":
    set_alarm("Teste: Hora do Café ☕")