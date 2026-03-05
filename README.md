# 📅 Alerta de Agenda (Background Calendar Notifier)

Um aplicativo em Python que roda silenciosamente na bandeja do sistema e monitora sua conta do Google Calendar. Sempre que um evento está prestes a começar, ele exibe uma notificação nativa no desktop e toca um alerta sonoro.

Este projeto foi construído para praticar o consumo de APIs, Threading e execução em background.

## ✨ Funcionalidades

- [x] Autenticação segura com a API do Google Calendar (OAuth 2.0).
- [x] Monitoramento contínuo usando concorrência (Threads).
- [x] Sistema de "memória" para não disparar o mesmo alarme duas vezes.
- [x] Notificação visual nativa no sistema operacional.
- [x] Alerta sonoro integrado.
- [x] Interface discreta na Bandeja do Sistema com opção de encerramento seguro.
- [ ] Executável do programa.

## 🚀 Tecnologias e Bibliotecas Utilizadas

- **Linguagem:** Python 3.13
- **APIs:** Google Calendar API
- **Bibliotecas Principais:**
  - `google-api-python-client` (Comunicação com o Google)
  - `pystray` e `Pillow` (Ícone e menu na bandeja do sistema)
  - `plyer` (Notificações desktop)
  - `pygame` (Reprodutor de som)
  - `threading` (Biblioteca nativa para concorrência)

## 🛠️ Como rodar o projeto localmente

### Pré-requisitos
1. Python instalado.
2. Uma conta no Google Cloud com a **Google Calendar API** ativada.

### Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/JacundaEntorpe/NOME_DO_REPOSITORIO.git
   ```
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3. Crie suas credenciais na API do Google e baixe o arquivo credentials.json.
4. Coloque o arquivo credentials.json na raiz do projeto.
5. Adicione um arquivo de áudio chamado alarm_sound.mp3 e um icone.ico na pasta assets/.

## Uso

1. Execute o arquivo principal:
    ```bash
    python main.py
    ```
Na primeira execução, uma janela do navegador será aberta para você autorizar o aplicativo a ler sua agenda.