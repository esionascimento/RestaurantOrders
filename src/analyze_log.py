from collections import Counter
import csv


def maria(client, data):
    orders_maria = []
    for cur in data:
        if cur["name"] == client:
            orders_maria.append(cur["order"])
    ordened_maria = list(Counter(orders_maria).keys())[0]
    return ordened_maria


def arnold(client, order, data):
    count = 0
    for cur in data:
        if cur["name"] == client and cur["order"] == order:
            count += 1
    return count


def joao_never(client, data):
    order_joao = set()
    orders = set()
    for cur in data:
        orders.add(cur["order"])
        if cur["name"] == client:
            order_joao.add(cur["order"])
    return orders - order_joao


def joao_never_days(client, data):
    date_client = set()
    date_joao = set()
    for cur in data:
        date_joao.add(cur["date"])
        if cur["name"] == client:
            date_client.add(cur["date"])
    return date_joao - date_client


def analyze_log(path_to_file):
    listFilters = list()
    with open(path_to_file, mode="r") as file:
        data = csv.DictReader(file, fieldnames=["name", "order", "date"])
        listFilters = [row for row in data]
    with open("data/mkt_campaign.txt", mode="w") as file:
        file.writelines(
            "\n".join(
                [
                    str(maria("maria", listFilters)),
                    str(
                        arnold("arnaldo", "hamburguer", listFilters)
                    ),
                    str(joao_never("joao", listFilters)),
                    str(joao_never_days("joao", listFilters)),
                ]
            )
        )
