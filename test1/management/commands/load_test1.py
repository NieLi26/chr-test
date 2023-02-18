import requests
from django.core.management.base import BaseCommand
from test1.models import Network, Payment, Location, Company, Extra, Station


class Command(BaseCommand):
    help = 'Obtiene la información de la API de BikeSantiago y la guarda en el modelo BikeSantiago'

    def handle(self, *args, **kwargs):
        Location.objects.all().delete()
        Payment.objects.all().delete()
        Company.objects.all().delete()
        Network.objects.all().delete()
        Extra.objects.all().delete()
        Station.objects.all().delete()

        # Realizar una solicitud GET a la API de BikeSantiago
        BASE_URL = 'https://api.citybik.es/v2/networks/bikesantiago'
        response = requests.get(BASE_URL)

        # Obtener los datos de la respuesta de la API
        data = response.json()

        # Crear instancia de Locacion
        location = data['network']['location']
        location = Location.objects.create(
            city=location['city'],
            country=location['country'],
            latitude=location['latitude'],
            longitude=location['longitude']
        )

        # Crear instancia de Network
        network = data['network']
        network = Network.objects.create(
            gbfs_href=network['gbfs_href'],
            href=network['href'],
            id=network['id'],
            location=location,
            name=network['name'],
        )

        # Crear instancias de Company
        companys = data['network']['company']
        for company in companys:
            Company.objects.create(
                network=network,
                name=company
            )

        # Crear instancias de Payment
        stations = data['network']['stations']
        for station in stations:
            for payment in station['extra']['payment']:
                payment, _ = Payment.objects.get_or_create(name=payment)

        # Crear instancia de Stations y Extras
        for station in stations:

            # payments = [payment for payment in Payment.objects.all() if payment.name in station['extra']['payment']]

            extra = Extra.objects.create(
                address=station['extra']['address'],
                altitude=station['extra']['altitude'],
                ebikes=station['extra']['ebikes'],
                has_ebikes=station['extra']['has_ebikes'],
                last_updated=station['extra']['last_updated'],
                normal_bikes=station['extra']['normal_bikes'],
                # payments=payments,
                payment_terminal=station['extra']['payment-terminal'],
                post_code=station['extra'].get('post_code', ''),
                renting=station['extra']['renting'],
                returning=station['extra']['returning'],
                slots=station['extra']['slots'],
                uid=station['extra']['uid']
            )

            # Crear lista de objetos Payment
            payment_names = station['extra']['payment']
            payments = Payment.objects.filter(name__in=payment_names)

            extra.payments.set(payments)

            Station.objects.create(
                network=network,
                empty_slots=station['empty_slots'],
                extra=extra,
                free_bikes=station['free_bikes'],
                id=station['id'],
                latitude=station['latitude'],
                longitude=station['longitude'],
                name=station['name'],
                timestamp=station['timestamp']
            )



        # Crear instancas de Company
        # company_name = api_data['network']['company'][0]
        #     company, _ = Company.objects.get_or_create(name=company_name)

        # print(Payment.objects.all())

        # Crear una instancia del modelo BikeSantiagoData con los datos obtenidos
        # Network.objects.create(
        #     company=data['network']['company'],
        #     gbfs_href=data['network']['gbfs_href'],
        #     href=data['network']['href'],
        #     id=data['network']['id'],
        #     location=data['network']['location'],
        #     name=data['network']['name'],
        #     stations=data['network']['stations'],
        # )

        # Imprimir un mensaje de éxito
        self.stdout.write(self.style.SUCCESS('Se ha guardado la información de BikeSantiago'))
