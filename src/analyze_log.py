import csv
from collections import Counter


def get_csv_data(path_to_file):
    if not path_to_file.strip().lower().endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    try:
        with open(path_to_file, 'r', encoding='utf8') as file:
            return list(csv.DictReader(
                file, fieldnames=['customer', 'dish', 'days'], delimiter=','
            ))

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


class ClientsInfo():
    def __init__(self, name) -> None:
        self.name = name

    def get_most_requested_dish(self, data):
        return Counter([
            info['dish'] for info in data if info['customer'] == self.name
        ]).most_common()[0][0]

    def get_how_many_times(self, data, dish):
        return Counter([
            info['dish']
            for info in data
            if info['customer'] == self.name and info['dish'] == dish
        ]).most_common()[0][1]

    def get_dish_never_ordered(self, data):
        dishes = {info['dish'] for info in data}
        return dishes.difference({
                info['dish']
                for info in data
                if self.name == info['customer']
        })

    def get_days_never_went_to_the_cafeteria(self, data):
        opened = {info['days'] for info in data}
        return opened.difference({
            info['days']
            for info in data
            if self.name == info['customer']
        })


def analyze_log(path_to_file):
    data = get_csv_data(path_to_file)

    # - Qual o prato mais pedido por 'maria'?
    maria = ClientsInfo("maria")
    most_requested_dish_by_maria = maria.get_most_requested_dish(data)

    # - Quantas vezes 'arnaldo' pediu 'hamburguer'?
    arnaldo = ClientsInfo("arnaldo")
    many_times_order_of_hamburguer = arnaldo.get_how_many_times(
        data, 'hamburguer')

    # - Quais pratos 'joao' nunca pediu?
    joao = ClientsInfo("joao")
    dish_never_ordered = joao.get_dish_never_ordered(data)

    # - Quais dias 'joao' nunca foi à lanchonete?
    days_joao_never_went = joao.get_days_never_went_to_the_cafeteria(data)

    with open('data/mkt_campaign.txt', 'w', encoding='utf-8') as file:
        result = (
            f"{most_requested_dish_by_maria}\n"
            + f"{many_times_order_of_hamburguer}\n"
            + f"{dish_never_ordered}\n"
            + f"{days_joao_never_went}\n"
        )
        file.write(result)
