# 📅 Alerta de Agenda (Background Calendar Notifier)

Um aplicativo em Python que roda silenciosamente na bandeja do sistema (System Tray) e monitora sua conta do Google Calendar. Sempre que um evento está prestes a começar, ele exibe uma janela pop-up interativa e estilizada no centro da tela, exigindo confirmação, e toca um alerta sonoro contínuo.

Este projeto foi construído para praticar o consumo de APIs, Threading, criação de interfaces gráficas customizadas e execução em background.

## ✨ Funcionalidades

- [x] Autenticação segura com a API do Google Calendar (OAuth 2.0).
- [x] Monitoramento contínuo usando concorrência (Threads).
- [x] Sistema de "memória" para não disparar o mesmo alarme duas vezes.
- [x] **Janela Pop-up Customizada:** Interface "Frameless" (sem as bordas padrão do Windows) com design aconchegante (Cozy/Pastel).
- [x] Alerta sonoro integrado em loop até a confirmação do usuário.
- [x] Interface discreta na Bandeja do Sistema com opção de encerramento seguro.
- [ ] Executável do programa (.exe).

## 🚀 Tecnologias e Bibliotecas Utilizadas

- **Linguagem:** Python 3.13
- **APIs:** Google Calendar API
- **Bibliotecas Principais:**
  - `google-api-python-client` (Comunicação segura com o Google)
  - `tkinter` (Biblioteca nativa para a criação da Interface Gráfica / Pop-up)
  - `pystray` e `Pillow` (Ícone na bandeja do sistema e manipulação de imagens na UI)
  - `pygame` (Motor de áudio para o alarme em loop)
  - `threading` (Biblioteca nativa para rodar o monitoramento sem travar a interface)

## 🛠️ Como rodar o projeto localmente

### Pré-requisitos
1. Python instalado na sua máquina.
2. Uma conta no Google Cloud com a **Google Calendar API** ativada.

### Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/JacundaEntorpe/NOME_DO_REPOSITORIO.git
   ```
2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    # No Windows: venv\Scripts\activate
    # No Linux/Mac: source venv/bin/activate
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Crie suas credenciais na API do Google e baixe o arquivo credentials.json.
5. Coloque o arquivo credentials.json na raiz do projeto.
6. Adicione um arquivo de áudio chamado alarm_sound.mp3 e um icone.ico na pasta assets/.

## Uso

1. Execute o arquivo principal:
    ```bash
    python main.py

    ou

    python main.pyw
    ```
Para rodar em modo silencioso no Windows

Na primeira execução, uma janela do navegador será aberta para você autorizar o aplicativo a ler sua agenda.