class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.cart = {}

    def add(self, item):
        if item in self.cart:
            self.cart[item] += 1
        else:
            self.cart[item] = 1

    def total_Charges(self):
        total_price = 0
        for item, quantity in self.cart.items():
            if item in self.pricing_rules:
                price_info = self.pricing_rules[item]
                unit_price = price_info['unit_price']
                discount_quantity = price_info.get('discount_quantity')
                discount_price = price_info.get('discount_price')

                if discount_quantity and discount_price:
                    # Calculate the number of discounted groups and remaining items
                    discounted_groups = quantity // discount_quantity
                    remaining_items = quantity % discount_quantity

                    # Calculate the total price
                    total_price += discounted_groups * discount_price
                    total_price += remaining_items * unit_price
                else:
                    # No discount, calculate normal price
                    total_price += quantity * unit_price
            else:
                raise ValueError(f"Item {item} not found in pricing rules.")

        return total_price

# Pricing rules for the products
pricing_rules = {
    'A': {'unit_price': 50, 'discount_quantity': 3, 'discount_price': 130},
    'B': {'unit_price': 30, 'discount_quantity': 2, 'discount_price': 45},
    'C': {'unit_price': 20},
    'D': {'unit_price': 15},
}

# Example usage
checkout = Checkout(pricing_rules)

# Scanning items in any order
checkout.add('A')
checkout.add('A')
checkout.add('A')
checkout.add('B')
checkout.add('C')
checkout.add('D')

# Calculating the total price
print("Total price:", checkout.total_Charges())  
