import os
import random
import vlc
import time
import tkinter as tk
from tkinter import ttk

# Função para reproduzir arquivo de áudio
def reproduzir_audio(arquivo):
    instance = vlc.Instance('--no-video')
    player = instance.media_player_new()
    media = instance.media_new(arquivo)
    player.set_media(media)
    player.play()

# Diretório onde estão os arquivos de áudio
diretorio = 'C:\\Users\\uever\\OneDrive\\Área de Trabalho\\Elle\\audio'

# Função chamada quando o botão é pressionado
def reproduzir_novamente():
    # Lista todos os arquivos de áudio na pasta
    arquivos_audio = [os.path.join(diretorio, arquivo) for arquivo in os.listdir(diretorio) if arquivo.endswith('.mp3')]

    if arquivos_audio:
        # Escolhe aleatoriamente um arquivo de áudio
        arquivo_aleatorio = random.choice(arquivos_audio)

        # Reproduz o arquivo selecionado
        reproduzir_audio(arquivo_aleatorio)
    else:
        print("Não foram encontrados arquivos de áudio na pasta especificada.")

# Função para criar e configurar a interface gráfica
def criar_interface():
    # Cria a janela
    janela = tk.Tk()
    janela.title("Sorting Hat")
    janela.configure(background="darkred")  # Define a cor de fundo como vermelho carmesim

    # Calcula o centro da tela
    largura_janela = 300
    altura_janela = 200
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2

    # Define o tamanho e a posição da janela
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    # Cria o botão "Reproduzir Novamente"
    botao_reproduzir = ttk.Button(janela, text="Escolher a Casa", command=reproduzir_novamente, style='Botao.TButton')
    botao_reproduzir.place(relx=0.5, rely=0.5, anchor="center")

    # Define o estilo do botão
    estilo = ttk.Style()
    estilo.configure('Botao.TButton', background='cyan', foreground='black')

    # Executa a interface
    janela.mainloop()

# Chamada da função para criar a interface
criar_interface()
