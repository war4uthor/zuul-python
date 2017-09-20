class Item:
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_weight(self):
        return self.weight

    