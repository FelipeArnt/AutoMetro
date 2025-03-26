# AutoMetro - LABELO / VSW

<br>

# 01 - Propósito
- Script de automação para ensaios de Metrologia Legal.
- A ideia inicial é utilizar o script para tarefas repetitivas e cansativas, como geração de logs na memória de um dispositivo, buffer overflow e afins.

<br>

# 02 - Tecnologias empregadas 
 - Foi utilizado a linguagem de programação python3 para o código do script, assim como as seguintes bibliotecas:  "pyautogui" para mapear e gravar as ações produzidas no software de ensaio. "Json" para enviar as ações em um arquivo ".json" para ser repetido n vezes. E "time" para aplicação do delay em segundos entre cada ação.

<br>

 # 03 - Utilização do script

 - Pré-requisitos : biblioteca pyautogui.
 
 - Para iniciar o script digite o comando "py .\AutoMetro.py", você terá que escrever o nome do arquivo ( nome do software utilizado + .json no final, exemplo: "Metersoft.json"). 
 
 Após isso, será exibido um menu interativo com as seguintes opções:

 - `Opção 1:` Gravar ações. 
 - `Opção 2:` Carregar ações de um arquivo.  
 - `Opção 3:` Repetir ações.  
 - `Opção 4:` Sair.  

