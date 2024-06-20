from time import perf_counter
import csv
from faker import Faker
import random


def get_fake_data():
    # Initialize the Faker instance
    fake = Faker('es_ES')  # Spanish locale

    # Define the number of products to generate
    num_products = 100

    # Define the CSV file name
    csv_file = 'data/productos_falsos.csv'

    # List of possible product names and descriptions
    product_names = {
        "Limpiador Multiusos": 0,
        "Desinfectante": 0,
        "Detergente para Ropa": 0, 
        "Limpiador de Baños":0,
        "Limpiavidrios":0,
        "Limpiador de Pisos":0, 
        "Jabón Líquido":0,
        "Limpiador de Cocina":0,
        "Desengrasante":0, 
        "Limpiador de Muebles":0
    }

    product_descriptions = [
        "eficaz en la eliminación de gérmenes y bacterias.",
        "proporciona una limpieza profunda y duradera.",
        "ideal para todo tipo de superficies.",
        "especialmente formulado para la limpieza.",
        "deja impecable y sin manchas.",
        "perfecto para mantener limpio.",
        "aroma agradable.",
        "elimina la suciedad",
        "potente para suciedad difícil.",
        "limpia y protege."
    ]

    # Open the CSV file for writing
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(['id', 'nombre', 'descripcion', 'precio', 'stock'])

        # Generate and write fake data for products
        product_names_list = list(product_names.keys())
        for i in range(1, num_products + 1):
            id = i
            nombre = random.choice(product_names_list)
            id_nombre = product_names[nombre]
            nombre = nombre + "_" + str(id_nombre)
            descripcion = random.choice(product_descriptions)
            descripcion = nombre + " " + descripcion
            precio = round(random.uniform(1.0, 100.0), 2)  # Precio entre 1.0 y 100.0
            stock = random.randint(0, 1000)  # Stock entre 0 y 1000
            # eScribir producto en csv
            writer.writerow(["('" + nombre + "'", "'" + descripcion + "'", precio, str(stock) + ")"])
            # Incrementar conteo de producto usado
            product_names[nombre] = id_nombre + 1

    print(f"Fichero CSV con datos falsos generado: {csv_file}")


if __name__ == '__main__':
    t1 = perf_counter()
    get_fake_data()
    t2 = perf_counter()
    dt = t2 - t1
    print(f"Elapsed time: {dt} (s) = {dt / 60} (min) = {dt / 3600} ()")