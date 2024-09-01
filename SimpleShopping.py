grocery_items = [
    ("Apples", 0.50), ("Bananas", 0.30), ("Bread", 2.00), ("Milk", 2.50),
    ("Eggs", 3.00), ("Cheese", 4.00), ("Cereal", 3.50), ("Pasta", 1.50),
    ("Tomatoes", 1.00), ("Onions", 0.75), ("Potatoes", 1.25), ("Chicken", 5.00),
    ("Beef", 6.00), ("Fish", 7.00), ("Rice", 2.00), ("Beans", 1.00),
    ("Carrots", 0.75), ("Lettuce", 1.50), ("Yogurt", 2.00), ("Ice Cream", 4.50),
    ("Coffee", 5.00), ("Tea", 3.00), ("Juice", 2.50), ("Soda", 1.50),
    ("Chips", 2.00), ("Cookies", 2.50), ("Candy", 1.00), ("Chocolate", 2.00),
    ("Soap", 1.50), ("Shampoo", 3.50)
]

TAX_RATE = 0.09
BAG_COST = 0.08
ITEMS_PER_BAG = 5

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name:<15} {self.item_quantity:>2} @ ${self.item_price:>5.2f} = ${total:>6.2f}")

def print_store_menu():
    print("\n" + "="*40)
    print("Welcome to the Simple Grocery Store!")
    print("="*40)
    for i, (item, price) in enumerate(grocery_items, 1):
        print(f"{i:2}. {item:<15} ${price:.2f}")
        if i % 6 == 0:
            print()

def get_user_selection():
    while True:
        try:
            selection = input("Enter the numbers of the items you want (comma-separated): ")
            return [int(x.strip()) for x in selection.split(",") if 1 <= int(x.strip()) <= len(grocery_items)]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

def calculate_bags_needed(total_items):
    return max(1, (total_items + ITEMS_PER_BAG - 1) // ITEMS_PER_BAG)

def main():
    print_store_menu()
    selected_items = get_user_selection()
    
    cart = []
    total_items = 0
    for item_num in selected_items:
        item_name, item_price = grocery_items[item_num - 1]
        quantity = int(input(f"How many {item_name} do you want? "))
        cart.append(ItemToPurchase(item_name, item_price, quantity))
        total_items += quantity
    
    print("\n" + "="*40)
    print("Your Receipt")
    print("="*40)
    subtotal = 0
    for item in cart:
        item.print_item_cost()
        subtotal += item.item_price * item.item_quantity
    
    bags_needed = calculate_bags_needed(total_items)
    bag_charge = bags_needed * BAG_COST
    tax = subtotal * TAX_RATE
    total_cost = subtotal + bag_charge + tax
    
    print("-"*40)
    print(f"Subtotal:     ${subtotal:>6.2f}")
    print(f"Bag Charge:   ${bag_charge:>6.2f} ({bags_needed} bag{'s' if bags_needed > 1 else ''} @ ${BAG_COST:.2f} each)")
    print(f"Tax (9%):     ${tax:>6.2f}")
    print(f"Total:        ${total_cost:>6.2f}")
    print("="*40)
    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main()
