import time
import datetime
from datetime import timezone
from notifier import set_alarm
from calendar_api import get_next_events
import pystray
from pystray import Menu, MenuItem
from themes import TEMAS
import config
import threading
from PIL import Image
import pystray


PREVIOUS_WARNING_TIME = 1
CHECKING_INTERVAL = 60

def checking_loop():

    notified_events = set()

    print("Loop iniciado... Checando agenda a cada minuto.")

    while True:
            
            local_now = datetime.datetime.now(timezone.utc).astimezone()
            
            try:

                next_events = get_next_events(quant=5)
                
                for event in next_events:
                    event_id = event['id']
                    event_name = event['nome']
                    event_time = event['horario']
                    
                    if event_id in notified_events:
                        continue

                    time_diference = event_time - local_now
                    minutes_to_event = time_diference.total_seconds() / 60
                    
                    if -2 <= minutes_to_event <= PREVIOUS_WARNING_TIME:
                        print(f"\n[ALERTA] Evento '{event_name}' está prestes a começar!")
                        
                        set_alarm(event_name)

                        notified_events.add(event_id)
                        
            except Exception as e:
                print(f"Erro ao checar a agenda: {e}")
                
            time.sleep(CHECKING_INTERVAL)

def exit_program(icon, item):
    print("Encerrando o Notificador de Agenda...")
    icon.stop()

def testar_notif():
    set_alarm("Teste de Notificação")

if __name__ == "__main__":
    print("Iniciando o sistema...")

    checking_thread = threading.Thread(target=checking_loop, daemon=True)
    
    checking_thread.start()

    try:
        imagem_icone = Image.open("assets/icone.ico") 
    except FileNotFoundError:
        print("ERRO: Arquivo 'assets/icone.ico' não encontrado!")
        print("Coloque uma imagem lá ou o ícone não vai aparecer.")
        exit()

    tema_selecionado = config.ler_tema_atual()

    def mudar_tema(icon, item):
        """Função chamada quando o usuário clica em um tema na bandeja."""
        global tema_selecionado
        tema_selecionado = item.text
        config.salvar_tema(tema_selecionado)
        print(f"Tema alterado para: {tema_selecionado}")

    def checar_tema_ativo(item):
        """Diz ao pystray qual bolinha (radio button) deve ficar marcada."""
        return tema_selecionado == item.text

    # Cria uma lista de botões gerados dinamicamente a partir do themes.py
    # O 'radio=True' cria aquela bolinha de seleção do lado do nome
    itens_de_tema = []
    for nome_do_tema in TEMAS.keys():
        botao = MenuItem(nome_do_tema, mudar_tema, checked=checar_tema_ativo, radio=True)
        itens_de_tema.append(botao)

    submenu_temas = Menu(*itens_de_tema)

    menu_principal = Menu(
        MenuItem("Temas", submenu_temas),
        MenuItem("Testar Notificação", testar_notif),
        MenuItem("Sair", exit_program)
    )

    tray_icon = pystray.Icon(
        "NotificadorAgenda", 
        imagem_icone, 
        "Notificador de Agenda", 
        menu_principal
    )

    print("Minimizando para a bandeja do sistema...")
    tray_icon.run()