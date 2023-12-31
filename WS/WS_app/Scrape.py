from bs4 import BeautifulSoup as BS
import requests
from WS_app.models import Car


def scrape():

    car_offers = []
    for i in range(0, 100, 20):
        source = requests.get("https://auto.bazos.cz/"+str(i)+"/")
        parsed_source = BS(source.text, "html.parser")
        car_offer = parsed_source.find("div", class_="maincontent").find_all("div", class_="inzeraty inzeratyflex")
        car_offers += car_offer

    existing_instances = Car.objects.values_list("title", flat=True)

    car_instances = []
    for car in car_offers:
        title = car.find("div", class_="inzeratynadpis").find("h2", class_="nadpis").find("a").text
        if not title in existing_instances:
            image_url = car.find("div", class_="inzeratynadpis").find("a").find("img").get("src")
            price = car.find("div", class_="inzeratycena").find("b").text
            location = car.find("div", class_="inzeratylok").text
            car_instance = Car(title=title, img_url=image_url, location=location, price=price)
            car_instances.append(car_instance)
        else:
            continue

    Car.objects.bulk_create(car_instances)
