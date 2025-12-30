from .models import CarMake, CarModel

def initiate():
    if CarMake.objects.exists():
        return  # Prevent duplicate entries

    nissan = CarMake.objects.create(name="NISSAN", description="Japanese technology")
    mercedes = CarMake.objects.create(name="Mercedes", description="German technology")
    audi = CarMake.objects.create(name="Audi", description="German technology")
    kia = CarMake.objects.create(name="Kia", description="Korean technology")
    toyota = CarMake.objects.create(name="Toyota", description="Japanese technology")

    CarModel.objects.bulk_create([
        CarModel(name="Pathfinder", type="SUV", year=2023, car_make=nissan),
        CarModel(name="Qashqai", type="SUV", year=2023, car_make=nissan),
        CarModel(name="XTRAIL", type="SUV", year=2023, car_make=nissan),
        CarModel(name="A-Class", type="Sedan", year=2023, car_make=mercedes),
        CarModel(name="C-Class", type="Sedan", year=2023, car_make=mercedes),
        CarModel(name="E-Class", type="Sedan", year=2023, car_make=mercedes),
        CarModel(name="A4", type="Sedan", year=2023, car_make=audi),
        CarModel(name="A5", type="Sedan", year=2023, car_make=audi),
        CarModel(name="A6", type="Sedan", year=2023, car_make=audi),
        CarModel(name="Sorrento", type="SUV", year=2023, car_make=kia),
        CarModel(name="Carnival", type="SUV", year=2023, car_make=kia),
        CarModel(name="Cerato", type="Sedan", year=2023, car_make=kia),
        CarModel(name="Corolla", type="Sedan", year=2023, car_make=toyota),
        CarModel(name="Camry", type="Sedan", year=2023, car_make=toyota),
        CarModel(name="Kluger", type="SUV", year=2023, car_make=toyota),
    ])