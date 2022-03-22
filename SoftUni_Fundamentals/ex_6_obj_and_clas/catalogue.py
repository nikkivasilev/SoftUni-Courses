class Catalogue:

    def __init__(self, name):
        self.products = []
        self.name = name

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        first_letter_list = [item for item in self.products if item[0] == first_letter]
        return first_letter_list

    def __repr__(self):
        last_list = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{last_list}"






catalogue = Catalogue("Furniture")

catalogue.add_product("Sofa")

catalogue.add_product("Mirror")

catalogue.add_product("Desk")

catalogue.add_product("Chair")

catalogue.add_product("Carpet")

print(catalogue.get_by_letter("C"))

print(catalogue)