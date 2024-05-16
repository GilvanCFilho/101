import os

def executar_atalho(caminho_atalho):
    os.startfile(caminho_atalho)

if __name__ == "__main__":
    caminho_do_atalho = r"C:\Users\Public\Desktop\Firefox.lnk"  # Substitua pelo caminho do seu atalho
    executar_atalho(caminho_do_atalho)
