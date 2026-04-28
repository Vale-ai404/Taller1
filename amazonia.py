#amazonia.py
#Programa sobre animales de la Amazonia

animales = [
    {"nombre": "Jaguar", "dato": "Es el felino mas grande de America."},
]

print("=== Animales de la Amazonia ===")
for animal in animales:
    print(f"- {animal['nombre']}: {animal['dato']}")
