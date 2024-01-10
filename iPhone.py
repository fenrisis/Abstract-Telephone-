from telephone import Telephone


class iPhone(Telephone):
    def __init__(self, model, color, battery_capacity) :
        super().__init__("Apple", model, "iOS", color, battery_capacity)

    def make_call(self, number):
        return f"iPhone calling {number}"

    def send_message(self, number, message):
        return f"iPhone sending message to {number}: {message}"

