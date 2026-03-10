import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pygame
import time
import sys
import ctypes

if sys.platform == "win32":
    app_id = 'Notificador Agenda' 
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

def set_alarm(event_title):
    """Cria uma janela pop-up centralizada e toca um som até ser fechada."""
    
    pygame.mixer.init()
    try:
        pygame.mixer.music.load('assets/alarm_sound.mp3')
        pygame.mixer.music.play(-1) # -1 pra ser infinito
    except Exception as e:
        print(f"Erro ao carregar o som: {e}")

    COR_FUNDO = "#FAF3E0"
    COR_TEXTO = "#5C4D42"
    COR_DESTAQUE = "#D4A373"
    COR_BOTAO = "#CCD5AE"
    COR_BOTAO_HOVER = "#E9EDC9"
    COR_FECHAR_HOVER = "#E07A5F"
    FONTE_PADRAO = "Segoe UI"

    janela = tk.Tk()
    janela.overrideredirect(True)

    janela.configure(bg=COR_TEXTO, highlightthickness=1, highlightbackground=COR_TEXTO)

    largura_janela = 450
    altura_janela = 300
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)

    janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    janela.attributes("-topmost", True)

    barra_titulo = tk.Frame(janela, bg=COR_FUNDO, relief="flat", bd=0)
    barra_titulo.pack(side="top", fill="x") 

    try:
        img_original = Image.open('assets/icone.png')
        img_redimensionada = img_original.resize((20, 20), Image.Resampling.LANCZOS)
        icone_tk = ImageTk.PhotoImage(img_redimensionada)
        
        lbl_imagem_icone = tk.Label(barra_titulo, image=icone_tk, bg=COR_FUNDO)
        lbl_imagem_icone.image = icone_tk 
        lbl_imagem_icone.pack(side="left", padx=(10, 0), pady=5)
    except Exception as e:
        print(f"Aviso: Não foi possível carregar o ícone da barra: {e}")

    lbl_titulo = tk.Label(barra_titulo, text=" Lembrete de Agenda", bg=COR_FUNDO, fg=COR_TEXTO, font=(FONTE_PADRAO, 10, "bold"))
    lbl_titulo.pack(side="left", pady=5)

    def stop_alarm():
        """O que acontece quando clicamos no botão."""
        pygame.mixer.music.stop()
        janela.destroy()

    btn_fechar = tk.Button(barra_titulo, text=" ✕ ", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 12), 
                           relief="flat", bd=0, activebackground=COR_FECHAR_HOVER, activeforeground="white", cursor="hand2",
                           command=stop_alarm)
    btn_fechar.pack(side="right", padx=5)

    btn_fechar.bind("<Enter>", lambda e: btn_fechar.config(bg=COR_FECHAR_HOVER, fg="white"))
    btn_fechar.bind("<Leave>", lambda e: btn_fechar.config(bg=COR_FUNDO, fg=COR_TEXTO))

    def iniciar_arrasto(event):
        janela.x = event.x
        janela.y = event.y

    def arrastar_janela(event):
        x = janela.winfo_x() - janela.x + event.x
        y = janela.winfo_y() - janela.y + event.y
        janela.geometry(f"+{x}+{y}")

    barra_titulo.bind("<Button-1>", iniciar_arrasto)
    barra_titulo.bind("<B1-Motion>", arrastar_janela)
    lbl_titulo.bind("<Button-1>", iniciar_arrasto)
    lbl_titulo.bind("<B1-Motion>", arrastar_janela)

    frame = tk.Frame(janela, bg=COR_FUNDO)
    frame.pack(expand=True, fill='both')

    lbl_icone = tk.Label(frame, text="☕✨", font=(FONTE_PADRAO, 28), bg=COR_FUNDO, fg=COR_DESTAQUE)
    lbl_icone.pack(pady=(10, 5))

    lbl_aviso = tk.Label(frame, text="Está na hora do seu compromisso:", font=(FONTE_PADRAO, 11, "italic"), bg=COR_FUNDO, fg=COR_TEXTO)
    lbl_aviso.pack()

    lbl_evento = tk.Label(frame, text=event_title, font=(FONTE_PADRAO, 16, "bold"), bg=COR_FUNDO, fg=COR_TEXTO, wraplength=400, justify="center")
    lbl_evento.pack(pady=(10, 20))

    btn_ok = tk.Button(frame, text="Tudo certo, vou lá!", font=(FONTE_PADRAO, 11, "bold"),
                       bg=COR_BOTAO, fg=COR_TEXTO, relief="flat", borderwidth=0, 
                       activebackground=COR_BOTAO_HOVER, activeforeground=COR_TEXTO, cursor="hand2",
                       padx=30, pady=8, command=stop_alarm)
    btn_ok.pack()

    btn_ok.bind("<Enter>", lambda e: btn_ok.config(bg=COR_BOTAO_HOVER))
    btn_ok.bind("<Leave>", lambda e: btn_ok.config(bg=COR_BOTAO))

    janela.mainloop()


if __name__ == "__main__":
    set_alarm("Teste: Hora do Café ☕")