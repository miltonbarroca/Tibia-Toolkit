import os
import json

def criar_script_json():
    nome_hunt = input("Qual é o nome da hunt? ")
    if not nome_hunt:
        print("Nome da hunt inválido. Por favor, insira um nome válido.")
        return

    num_boxes = int(input("Quantas boxes são (de 1 a 20)? "))
    if not 1 <= num_boxes <= 20:
        print("Número de boxes inválido. Por favor, escolha um número entre 1 e 20.")
        return

    tempo_entre_boxes = 7  # Definindo o tempo padrão entre as boxes

    script = []
    for i in range(num_boxes):
        flag_number = i
        path = f"img/flags/flag_{flag_number}.png"
        box = {
            "path": path,
            "down_hole": 0,
            "up_hole": 0,
            "wait": tempo_entre_boxes
        }
        script.append(box)

    script_dir = "scripts"
    if not os.path.exists(script_dir):
        os.makedirs(script_dir)

    with open(os.path.join(script_dir, f"{nome_hunt}.json"), "w") as json_file:
        json.dump(script, json_file, indent=4)

    print(f"Script JSON para a hunt '{nome_hunt}' criado com sucesso em '{script_dir}'.")

criar_script_json()
