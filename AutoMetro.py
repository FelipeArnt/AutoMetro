#AutoMetro 

import pyautogui # type: ignore
import time
import sys
import json
import subprocess

# Utilizando "with" para fechar automaticamente os "Open" utilizados nas defs.
# Talvez implementar uma padronização para substituir o "actions.json". Salvando as rotinas de acordo com o nome do software utilizado no ensaio.
# json para manipular arquivos .json (Onde as ações serão armazenadas!).
# time para colocar delay entra os blocos de código e ações. (usei pelo fato de ter uma tela só e precisar colocar em tela cheia o software de ensaio) 
# sys serve para acessar argumentos na linha de comando sys.argv e encerrar o script com sys.exit(1). 



def rec():
    print("Você tem 5 segundos para ir a tela do software de ensaio.")
    time.sleep(5)
    # Registra ações do usuário (cliques do mouse ou pressionamentos de teclas).

    actions = []
    print("\n--- Modo de Gravação ---")
    print("Clique onde deseja repetir a ação. Pressione 'Ctrl+C' para parar.")
    # Loop while.
    try:
        while True:
            # Tipo de ação.
            action_type = input("O próximo clique é do teclado, mouse ou texto? (k/m/t): ").strip().lower()
            if action_type == 'm':
                x, y = pyautogui.position()
                actions.append(('mouse', x, y))
                print(f"Posição do clique registrada: ({x}, {y})")
                actions.append(("mouse", x, y))
            elif action_type == "m2":
                x, y = pyautogui.position()
                actions.append(("mouse2", x, y))
            elif action_type == 'k':
                key = input("Pressione a tecla desejada: ").strip().lower()
                if key in pyautogui.KEYBOARD_KEYS:
                    actions.append(('keyboard', key))
                    print(f"Tecla registrada: {key}")
                else:
                    print("Tecla inválida. Por favor, tente novamente.")
            elif action_type == 't':
                text = input("Digite o texto desejado: ")
                actions.append(('text', text))
                print(f"Texto registrado: {text}")
            else:
                print("Entrada inválida. Por favor, digite 'k' para teclado, 'm' para mouse ou 't' para texto.")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nGravação de ações interrompida.")
    return actions
 
# Manipulação de Arquivos
nome_arquivo = input("Digite o nome do software utilizado: (ex metersoft.json)")
def save(actions, filename=nome_arquivo):
    # Salva as ações em um arquivo JSON.
    with open(filename, 'w') as file: # modo escrita "w".
        json.dump(actions, file)
    print(f"\nAções salvas em {filename}.")
# Manipulação de Arquivos 
def load(filename='actions.json'):
    # Carrega as ações de um arquivo JSON.
    try:
        with open(filename, 'r') as file: # modo leitura "r".
            actions = json.load(file)
        print(f"\nAções carregadas de {filename}.")
        return actions
    except FileNotFoundError:
        print(f"\nArquivo {filename} não encontrado.")
        return None
 
def rep(actions, n):
    # Repete as ações registradas 'n' vezes.
    print(f"\nRepetindo ações {n} vezes...")
    for _ in range(n):
        for action in actions:
            if action[0] == 'mouse':
                pyautogui.click(action[1], action[2])
            elif action[0] == "mouse2":
                pyautogui.doubleClick(action[1], action[2])
            elif action[0] == 'keyboard':
                pyautogui.press(action[1])
            elif action[0] == 'text':
                pyautogui.write(action[1])
            time.sleep(1)
 
def menu_interativo():
    # Exibe o menu interativo
    print("\n--- AutoMetro ---")
    print("1. Gravar ações")
    print("2. Carregar ações de um arquivo")
    print("3. Repetir ações")
    print("4. Sair")
    print("--- AutoMetro ---")
    opt = input("Escolha uma opção: ").strip()
    return opt
 
def main():
    actions = None
    while True:
        opt = menu_interativo()
 
        if opt == '1':  # Grava as ações realizadas no software de ensaio.
            actions = rec()
            save(actions)
 
        elif opt == '2':  # Carrega as ações do arquivo .json
            filename = input("Digite o nome do arquivo (ou pressione Enter para usar 'actions.json'): ").strip()
            if not filename: 
                filename = 'actions.json'
            actions = load(filename)
 
        elif opt == '3':  # Repete as ações e pede o número de repetições.
            if actions:
                try:
                    n = int(input("Quantas vezes deseja repetir as ações? "))
                    time.sleep(2)
                    rep(actions, n)
                except ValueError:
                    print("Entrada inválida. Digite um número.")
            else:
                print("Nenhuma ação carregada. Por favor, grave ou carregue ações primeiro.")
 
        elif opt == '4':  # Finaliza o script.
            print("Saindo...")
            break
 
        else:
            print("Opção inválida. Tente novamente.")
 
if __name__ == "__main__":
    main()
 
 
