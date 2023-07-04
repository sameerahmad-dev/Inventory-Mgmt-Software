import tkinter as tk

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def update_quantity(self, product, quantity):
        product.quantity = quantity

    def calculate_total_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.price * product.quantity
        return total_value


class InventoryManagementApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Inventory Management Software")
        self.window.geometry("800x600")

        self.inventory = Inventory()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.window, text="Inventory Management Software", font=("Arial", 24))
        self.label.pack(pady=20)

        self.add_product_btn = tk.Button(self.window, text="Add Product", command=self.add_product)
        self.add_product_btn.pack(pady=10)

        self.remove_product_btn = tk.Button(self.window, text="Remove Product", command=self.remove_product)
        self.remove_product_btn.pack(pady=10)

        self.update_quantity_btn = tk.Button(self.window, text="Update Quantity", command=self.update_quantity)
        self.update_quantity_btn.pack(pady=10)

        self.calculate_total_value_btn = tk.Button(self.window, text="Calculate Total Value", command=self.calculate_total_value)
        self.calculate_total_value_btn.pack(pady=10)

        self.product_list_label = tk.Label(self.window, text="Product List", font=("Arial", 16))
        self.product_list_label.pack(pady=10)

        self.product_listbox = tk.Listbox(self.window, width=80, height=10)
        self.product_listbox.pack()

        self.exit_btn = tk.Button(self.window, text="Exit", command=self.window.quit)
        self.exit_btn.pack(pady=10)

    def add_product(self):
        add_product_window = tk.Toplevel(self.window)
        add_product_window.title("Add Product")

        name_label = tk.Label(add_product_window, text="Name:")
        name_label.pack()
        self.name_entry = tk.Entry(add_product_window)
        self.name_entry.pack()

        price_label = tk.Label(add_product_window, text="Price:")
        price_label.pack()
        self.price_entry = tk.Entry(add_product_window)
        self.price_entry.pack()

        quantity_label = tk.Label(add_product_window, text="Quantity:")
        quantity_label.pack()
        self.quantity_entry = tk.Entry(add_product_window)
        self.quantity_entry.pack()

        add_btn = tk.Button(add_product_window, text="Add", command=self.perform_add_product)
        add_btn.pack(pady=10)

    def perform_add_product(self):
        name = self.name_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())
        product = Product(name, price, quantity)
        self.inventory.add_product(product)
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        print("Product added successfully!")
        self.update_product_list()

    def remove_product(self):
        remove_product_window = tk.Toplevel(self.window)
        remove_product_window.title("Remove Product")

        name_label = tk.Label(remove_product_window, text="Name:")
        name_label.pack()
        self.remove_name_entry = tk.Entry(remove_product_window)
        self.remove_name_entry.pack()

        remove_btn = tk.Button(remove_product_window, text="Remove", command=self.perform_remove_product)
        remove_btn.pack(pady=10)

    def perform_remove_product(self):
        name = self.remove_name_entry.get()
        for product in self.inventory.products:
            if product.name == name:
                self.inventory.remove_product(product)
                self.remove_name_entry.delete(0, tk.END)
                print("Product removed successfully!")
                self.update_product_list()
                return
        print("Product not found!")

    def update_quantity(self):
        update_quantity_window = tk.Toplevel(self.window)
        update_quantity_window.title("Update Quantity")

        name_label = tk.Label(update_quantity_window, text="Name:")
        name_label.pack()
        self.update_name_entry = tk.Entry(update_quantity_window)
        self.update_name_entry.pack()

        quantity_label = tk.Label(update_quantity_window, text="New Quantity:")
        quantity_label.pack()
        self.new_quantity_entry = tk.Entry(update_quantity_window)
        self.new_quantity_entry.pack()

        update_btn = tk.Button(update_quantity_window, text="Update", command=self.perform_update_quantity)
        update_btn.pack(pady=10)

    def perform_update_quantity(self):
        name = self.update_name_entry.get()
        new_quantity = int(self.new_quantity_entry.get())
        for product in self.inventory.products:
            if product.name == name:
                self.inventory.update_quantity(product, new_quantity)
                self.update_name_entry.delete(0, tk.END)
                self.new_quantity_entry.delete(0, tk.END)
                print("Quantity updated successfully!")
                self.update_product_list()
                return
        print("Product not found!")

    def calculate_total_value(self):
        total_value = self.inventory.calculate_total_value()
        print("Total inventory value:", total_value)

    def update_product_list(self):
        self.product_listbox.delete(0, tk.END)
        for product in self.inventory.products:
            self.product_listbox.insert(tk.END, f"Name: {product.name} | Price: {product.price} | Quantity: {product.quantity}")


def main():
    window = tk.Tk()
    app = InventoryManagementApp(window)
    window.mainloop()


if __name__ == '__main__':
    main()
