class TrackOrders:
    def __init__(self):
        self.orders = []

    """ tamanho """
    def __len__(self):
        return len(self.orders)

    """ novos dados """
    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    """ prato mais pedido """
    def get_most_ordered_dish_per_costumer(self, costumer):
        obj = {}

        for order in self.orders:
            if costumer in order:
                if order[1] not in obj:
                    obj[order[1]] = 1
                else:
                    obj[order[1]] += 1
        return max(obj, key=lambda k: obj[k])

    """ Pratos nunca pedidos por cada cliente """
    def get_never_ordered_per_costumer(self, costumer):
        print(costumer)
        dishes = set()
        ordered_dishes = set()

        for order in self.orders:
            dishes.add(order[1])

            if costumer in order:
                ordered_dishes.add(order[1])
        return dishes.difference(ordered_dishes)

    """ dias que a pessoa nunca visitou """
    def get_days_never_visited_per_costumer(self, costumer):
        days_funf = set()
        go_cafeteria = set()

        for order in self.orders:
            days_funf.add(order[2])

            if costumer in order:
                go_cafeteria.add(order[2])

        return days_funf.difference(go_cafeteria)

    """ Dia mais movimentado """
    def get_busiest_day(self):
        day_absent = {}
        for order in self.orders:
            if order[2] not in day_absent:
                day_absent[order[2]] = 1
            else:
                day_absent[order[2]] += 1

        return max(day_absent, key=day_absent.get)

    """ Dia menos movimentado """
    def get_least_busy_day(self):
        day_absent = {}

        for order in self.orders:
            if order[2] not in day_absent:
                day_absent[order[2]] = 1
            else:
                day_absent[order[2]] += 1

        return min(day_absent, key=day_absent.get)
