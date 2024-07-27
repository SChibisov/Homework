import multiprocessing


class WarehouseManager:
    def __init__(self):
        self.data = multiprocessing.Manager().dict()

    def process_request(self, request):
        product_name, action, quantity = request

        if action == "receipt":
            current_quantity = self.data.get(product_name, 0)
            self.data[product_name] = current_quantity + quantity

        elif action == "shipment":
            current_quantity = self.data.get(product_name, 0)
            if current_quantity > 0:
                new_quantity = max(current_quantity - quantity, 0)
                self.data[product_name] = new_quantity

    def run(self, requests):
        processes = []
        for request in requests:
            p = multiprocessing.Process(target=self.process_request, args=(request,))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()


if __name__ == "__main__":
    manager = WarehouseManager()
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    manager.run(requests)
    print(dict(manager.data))