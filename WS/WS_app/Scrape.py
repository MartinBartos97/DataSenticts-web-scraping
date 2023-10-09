from bs4 import BeautifulSoup as BS
import requests
from WS_app.models import Car


def scrape():
    cars = []
    for i in range(0, 100, 20):
        source = requests.get("https://auto.bazos.cz/"+str(i)+"/")
        parsed_source = BS(source.text, "html.parser")
        cars_part = parsed_source.find("div", class_="maincontent").find_all("div", class_="inzeraty inzeratyflex")
        cars += cars_part

    car_instances = []
    for car in cars:
        title = car.find("div", class_="inzeratynadpis").find("h2", class_="nadpis").find("a").text
        image_url = car.find("div", class_="inzeratynadpis").find("a").find("img").get("src")
        price = car.find("div", class_="inzeratycena").find("b").text
        location = car.find("div", class_="inzeratylok").text

        existing_instance = Car.objects.filter(title=title).first()
        if not existing_instance:
            car_instance = Car(title=title, img_url=image_url, location=location, price=price)
            car_instances.append(car_instance)
        else:
            continue

    Car.objects.bulk_create(car_instances)
