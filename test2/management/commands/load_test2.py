import json
import requests
from django.core.management.base import BaseCommand
from test2.models import Servicio
from bs4 import BeautifulSoup


class Command(BaseCommand):
    help = 'Obtiene la información de la pagina Servicio de Evaluación Ambiental, almacenarla en un archivo json y luego cargarla al modelo servicio'

    def handle(self, *args, **kwargs):
        Servicio.objects.all().delete()

        page_number = 1
        data = []
        while True:
            # Hacer la petición GET a la URL
            BASE_URL = f'https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?_paginador_fila_actual={page_number}'
            response = requests.get(BASE_URL)

            # Crear el objeto BeautifulSoup con el contenido HTML
            soup = BeautifulSoup(response.content, 'lxml')

            # Extraer información de la tabla y agregarla a la lista 'data'
            table = soup.find('table', {'class': 'tabla_datos'})

            # Verificar si hay más páginas para consultar
            if not table or page_number == 3:
                break

            # Encontrar todas las filas de la tabla, filtramos por el tipo de etiqueta
            rows = table.find_all('tr')

            # Recorrer las filas e imprimir el contenido de cada celda
            for row in rows[2:]:
                cols = row.find_all('td')
                mapa = None
                texto = cols[9].find('a').get('onclick') if cols[9].find('a') else None
                if texto:
                    url = texto[texto.find('/mapa'):texto.find('\'', texto.find('/mapa'))]
                    mapa = f"https://seia.sea.gob.cl{url}"
                data.append({
                    'numero': cols[0].get_text(),
                    'nombre': cols[1].get_text(),
                    'link': cols[1].find('a').get('href') if cols[1].find('a') else None,
                    'tipo': cols[2].get_text(),
                    'region': cols[3].get_text(),
                    'tipologia': cols[4].get_text(),
                    'titular': cols[5].get_text(),
                    'inversion': cols[6].get_text(),
                    'fecha_ingreso': cols[7].get_text(),
                    'estado': cols[8].get_text(),
                    'mapa': mapa,
                })

            page_number += 1
        # Escribir los datos en un archivo JSON
        with open('data.json', 'w', encoding='UTF-8') as f:
            json.dump(data, f)

        # Leer data.json
        with open('data.json', 'r', encoding='UTF-8') as f:
            datos = json.load(f)

        servicios = [
            Servicio(
                numero=d['numero'],
                nombre=d['nombre'],
                link=d['link'],
                tipo=d['tipo'],
                region=d['region'],
                tipologia=d['tipologia'],
                titular=d['titular'],
                inversion=d['inversion'],
                fecha_ingreso=d['fecha_ingreso'],
                estado=d['estado'],
                mapa=d['mapa'],
            ) for d in datos
        ]

        Servicio.objects.bulk_create(servicios)

        self.stdout.write(self.style.SUCCESS('Se ha guardado la información de Servicios'))