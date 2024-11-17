from faker import Faker
import pandas as pd

seed_value = 42
fake = Faker('es_ES')  
fake.seed_instance(seed_value)
num_records = 10000  # Número de filas que queremos generar

data = {
    "Nombre": [fake.name() for _ in range(num_records)],
    "Dirección": [fake.address() for _ in range(num_records)],
    "Correo": [fake.email() for _ in range(num_records)],
    "Teléfono": [fake.phone_number() for _ in range(num_records)],
    "Fecha de nacimiento": [fake.date_of_birth(minimum_age=18, maximum_age=90) for _ in range(num_records)],
    "Empresa": [fake.company() for _ in range(num_records)],
    "Número de tarjeta": [fake.credit_card_number() for _ in range(num_records)],
    "Fecha de vencimiento": [fake.credit_card_expire() for _ in range(num_records)],
    "Código postal": [fake.postcode() for _ in range(num_records)],
}

df = pd.DataFrame(data)

df.to_csv('dataset_falso.csv', index=False, encoding='utf-8')
