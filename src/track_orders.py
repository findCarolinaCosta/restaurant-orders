from typing import Counter


class TrackOrders:
    def __init__(self) -> None:
        self.data = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        return Counter([
            info[1] for info in self.data if info[0] == customer
            ]).most_common()[0][0]

    def get_never_ordered_per_customer(self, customer):
        dishes = {info[1] for info in self.data}
        return dishes.difference({
                info[1]
                for info in self.data
                if customer == info[0]
            })

    def get_days_never_visited_per_customer(self, customer):
        opened = {info[2] for info in self.data}
        return opened.difference({
            info[2]
            for info in self.data
            if customer == info[0]
        })

    def get_busiest_day(self):
        return Counter([
            info[2] for info in self.data
        ]).most_common()[0][0]

    def get_least_busy_day(self):
        return Counter([
            info[2] for info in self.data
        ]).most_common()[-1][0]
