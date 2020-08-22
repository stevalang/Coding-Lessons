class Catalog:

    def __init__(self,name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        return [p for p in self.products if p[0] == first_letter]

    def __repr__(self):
        res = f"Items in the {self.name} catalogue:\n"
        res += '\n'.join(sorted(self.products))
        return res


catalogue = Catalog("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
