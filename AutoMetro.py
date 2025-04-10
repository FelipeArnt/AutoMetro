#AutoMetro 
import pyautogui # type: ignore
import time
import json
import os

class AutoMetro: # Implementando a classe Autômetro para lidar melhor com o código.
    def __init__(self):
        self.actions = None  # Variável que armazena as ações do usuário
        self.state_machine = {
            '1': self.gravar_acoes,
            '2': self.carregar_acoes,
            '3': self.repetir_acoes,
            '4': self.sair
        }

    def gravar_acoes(self):
        self.actions = rec()
        save(self.actions)

    def carregar_acoes(self):
        filename = input("\nArquivo JSON (Enter para 'actions.json'): ").strip() or 'actions.json'
        self.actions = load(filename)

    def repetir_acoes(self):
        if self.actions:
            try:
                n = int(input("Quantas repetições? "))
                rep(self.actions, n)
            except ValueError:
                print("Digite um número válido!")
        else:
            print("Nenhuma ação carregada! Use opção 1 ou 2 primeiro.")

    def sair(self):
        print("Saindo...")
        exit()

    def run(self):
        while True:
            opt = menu_interativo()
            rodar = self.state_machine.get(opt, lambda: print("Opção inválida!"))
            rodar()





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
   autoMetro = AutoMetro()
   autoMetro.run() 
if __name__ == "__main__":
    main()
 
 
