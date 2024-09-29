# Explicação das mudanças:
## Interface gráfica com tkinter:

### Usei o tkinter para criar uma janela simples com três botões: Iniciar Combo, Pausar/Retomar Combo, e Finalizar Programa.
## A função iniciar_combo() inicia o combo, rodando o loop do auto_combo em uma thread separada para evitar que a interface congele.
## A função pausar_combo() alterna entre pausar e retomar o combo, modificando a variável pause_programa.
## A função finalizar_combo() define a variável finalizar_programa como True, o que interrompe o loop do combo.
## Status atualizado na interface:

## O status_label exibe o status atual (se o combo foi iniciado, pausado ou finalizado).
### Threading para evitar congelamento:

## Como o combo roda em um loop contínuo, ele é executado em uma thread separada para garantir que a interface gráfica permaneça responsiva.
Finalização correta:

## A função finalizar_combo() aguarda o término da thread antes de atualizar a interface, garantindo que tudo seja finalizado corretamente.
# Como usar:
## Iniciar Combo: O botão "Iniciar Combo" começará a execução do combo automático.
## Pausar/Retomar: O botão "Pausar/Retomar Combo" permite alternar entre pausar e retomar a execução.
## Finalizar Programa: O botão "Finalizar Programa" interrompe a execução do combo e encerra o programa.