#amazonia.py
#Programa sobre animales de la Amazonia

animales = [
    {"nombre": "Jaguar", "dato": "Es el felino mas grande de America."},

    {"nombre": "Delfin rosado", "dato": "Vive en los rios de la Amazonia."},

    {"nombre": "Anaconda", "dato": "Es una de las serpientes mas grandes del mundo."}
]

print("=== Animales de la Amazonia ===")
for animal in animales:
    print(f"- {animal['nombre']}: {animal['dato']}")

