from telephone import Telephone


class Android(Telephone):
    def __init__(self, brand, model, color, battery_capacity) :
        super().__init__(brand, model, "Android", color, battery_capacity)

    def make_call(self, number) :
        return f"Android phone calling {number}"

    def send_message(self, number, message) :
        return f"Android phone sending message to {number}: {message}"
