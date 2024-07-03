import sys
import logging
log = logging.Logger("alerta")

info = {
    "temperatura":None,
    "umidade":None
}

keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual a {key}? ").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)

temp_atual = info["temperatura"]
umidade_ar = info["umidade"]

if temp_atual > 45:
    print("ALERTA! Calor extremo!")
elif temp_atual * 3 >= umidade_ar:
    print("ALERTA! Perigo de calor úmido!")
elif temp_atual >= 10 and temp_atual <= 30:
    print("Temperatura Normal!")
elif temp_atual >= 0 and temp_atual <=10:
    print("Frio!")
elif temp_atual < 0:
    print("Frio extremo!")