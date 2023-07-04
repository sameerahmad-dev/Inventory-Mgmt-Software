import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


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
        self.users = []
        self.current_user = None

        self.create_widgets()

    def create_widgets(self):
        self.style = ThemedStyle(self.window)
        self.style.set_theme("equilux")

        self.frame = ttk.Frame(self.window, style='Custom.TFrame')
        self.frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        self.label = ttk.Label(self.frame, text="Inventory Management Software", font=("Arial", 24))
        self.label.pack()

        self.login_btn = ttk.Button(self.frame, text="Login", command=self.open_login_window)
        self.login_btn.pack(pady=10)

        self.exit_btn = ttk.Button(self.frame, text="Exit", command=self.window.quit)
        self.exit_btn.pack(pady=10)

    def open_login_window(self):
        login_window = tk.Toplevel(self.window)
        login_window.title("Login")
        login_window.geometry("300x200")

        login_frame = ttk.Frame(login_window, style='Custom.TFrame')
        login_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        username_label = ttk.Label(login_frame, text="Username:")
        username_label.pack()
        self.username_entry = ttk.Entry(login_frame)
        self.username_entry.pack()

        password_label = ttk.Label(login_frame, text="Password:")
        password_label.pack()
        self.password_entry = ttk.Entry(login_frame, show="*")
        self.password_entry.pack()

        login_btn = ttk.Button(login_frame, text="Login", command=self.perform_login)
        login_btn.pack(pady=10)

    def perform_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            self.current_user = User(username, password)
            self.open_inventory_section()
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            return

        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                self.open_inventory_section()
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                return

        messagebox.showerror("Invalid Credentials", "Username or password is incorrect.")
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def open_inventory_section(self):
        self.window.withdraw()
        inventory_window = tk.Toplevel(self.window)
        inventory_window.title("Inventory Management")
        inventory_window.geometry("800x600")

        inventory_frame = ttk.Frame(inventory_window, style='Custom.TFrame')
        inventory_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        inventory_label = ttk.Label(inventory_frame, text=f"Welcome, {self.current_user.username}", font=("Arial", 24))
        inventory_label.pack()

        add_product_btn = ttk.Button(inventory_frame, text="Add Product", command=self.open_add_product_window)
        add_product_btn.pack(pady=10)

        remove_product_btn = ttk.Button(inventory_frame, text="Remove Product", command=self.open_remove_product_window)
        remove_product_btn.pack(pady=10)

        update_quantity_btn = ttk.Button(inventory_frame, text="Update Quantity", command=self.open_update_quantity_window)
        update_quantity_btn.pack(pady=10)

        calculate_total_btn = ttk.Button(inventory_frame, text="Calculate Total Value", command=self.calculate_total_value)
        calculate_total_btn.pack(pady=10)

        list_product_btn = ttk.Button(inventory_frame, text="List Products", command=self.list_products)
        list_product_btn.pack(pady=10)

        user_management_btn = ttk.Button(inventory_frame, text="User Management", command=self.open_user_management_window)
        user_management_btn.pack(pady=10)

        close_btn = ttk.Button(inventory_frame, text="Close", command=self.close_inventory_section)
        close_btn.pack(pady=10)

    def open_add_product_window(self):
        add_product_window = tk.Toplevel(self.window)
        add_product_window.title("Add Product")
        add_product_window.geometry("400x300")

        add_product_frame = ttk.Frame(add_product_window, style='Custom.TFrame')
        add_product_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        name_label = ttk.Label(add_product_frame, text="Name:")
        name_label.pack()
        self.name_entry = ttk.Entry(add_product_frame)
        self.name_entry.pack()

        price_label = ttk.Label(add_product_frame, text="Price:")
        price_label.pack()
        self.price_entry = ttk.Entry(add_product_frame)
        self.price_entry.pack()

        quantity_label = ttk.Label(add_product_frame, text="Quantity:")
        quantity_label.pack()
        self.quantity_entry = ttk.Entry(add_product_frame)
        self.quantity_entry.pack()

        add_btn = ttk.Button(add_product_frame, text="Add", command=self.add_product)
        add_btn.pack(pady=10)

    def add_product(self):
        name = self.name_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())

        product = Product(name, price, quantity)
        self.inventory.add_product(product)

        messagebox.showinfo("Success", "Product added successfully.")
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def open_remove_product_window(self):
        remove_product_window = tk.Toplevel(self.window)
        remove_product_window.title("Remove Product")
        remove_product_window.geometry("400x300")

        remove_product_frame = ttk.Frame(remove_product_window, style='Custom.TFrame')
        remove_product_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        products = [product.name for product in self.inventory.products]

        if len(products) == 0:
            messagebox.showinfo("No Products", "There are no products in the inventory.")
            remove_product_window.destroy()
            return

        product_label = ttk.Label(remove_product_frame, text="Select Product:")
        product_label.pack()
        self.selected_product = tk.StringVar()
        self.product_combobox = ttk.Combobox(remove_product_frame, textvariable=self.selected_product, values=products, state="readonly")
        self.product_combobox.pack()

        remove_btn = ttk.Button(remove_product_frame, text="Remove", command=self.remove_product)
        remove_btn.pack(pady=10)

    def remove_product(self):
        selected_product = self.selected_product.get()
        if selected_product:
            for product in self.inventory.products:
                if product.name == selected_product:
                    self.inventory.remove_product(product)
                    messagebox.showinfo("Success", f"Product '{selected_product}' removed successfully.")
                    self.product_combobox.set('')
                    break

    def open_update_quantity_window(self):
        update_quantity_window = tk.Toplevel(self.window)
        update_quantity_window.title("Update Quantity")
        update_quantity_window.geometry("400x300")

        update_quantity_frame = ttk.Frame(update_quantity_window, style='Custom.TFrame')
        update_quantity_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        products = [product.name for product in self.inventory.products]

        if len(products) == 0:
            messagebox.showinfo("No Products", "There are no products in the inventory.")
            update_quantity_window.destroy()
            return

        product_label = ttk.Label(update_quantity_frame, text="Select Product:")
        product_label.pack()
        self.selected_product = tk.StringVar()
        self.product_combobox = ttk.Combobox(update_quantity_frame, textvariable=self.selected_product, values=products, state="readonly")
        self.product_combobox.pack()

        quantity_label = ttk.Label(update_quantity_frame, text="New Quantity:")
        quantity_label.pack()
        self.quantity_entry = ttk.Entry(update_quantity_frame)
        self.quantity_entry.pack()

        update_btn = ttk.Button(update_quantity_frame, text="Update", command=self.update_quantity)
        update_btn.pack(pady=10)

    def update_quantity(self):
        selected_product = self.selected_product.get()
        quantity = int(self.quantity_entry.get())

        if selected_product and quantity >= 0:
            for product in self.inventory.products:
                if product.name == selected_product:
                    self.inventory.update_quantity(product, quantity)
                    messagebox.showinfo("Success", f"Quantity for product '{selected_product}' updated successfully.")
                    self.product_combobox.set('')
                    self.quantity_entry.delete(0, tk.END)
                    break

    def calculate_total_value(self):
        total_value = self.inventory.calculate_total_value()
        messagebox.showinfo("Total Value", f"The total value of all products is ${total_value:.2f}.")

    def list_products(self):
        products_window = tk.Toplevel(self.window)
        products_window.title("Product List")
        products_window.geometry("400x300")

        products_frame = ttk.Frame(products_window, style='Custom.TFrame')
        products_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        products_label = ttk.Label(products_frame, text="Product List", font=("Arial", 24))
        products_label.pack()

        for product in self.inventory.products:
            product_label = ttk.Label(products_frame, text=f"{product.name} - ${product.price:.2f} - Quantity: {product.quantity}")
            product_label.pack()

    def open_user_management_window(self):
        user_management_window = tk.Toplevel(self.window)
        user_management_window.title("User Management")
        user_management_window.geometry("400x300")

        user_management_frame = ttk.Frame(user_management_window, style='Custom.TFrame')
        user_management_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        list_users_btn = ttk.Button(user_management_frame, text="List Users", command=self.list_users)
        list_users_btn.pack(pady=10)

    def list_users(self):
        users_window = tk.Toplevel(self.window)
        users_window.title("User List")
        users_window.geometry("400x300")

        users_frame = ttk.Frame(users_window, style='Custom.TFrame')
        users_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        users_label = ttk.Label(users_frame, text="User List", font=("Arial", 24))
        users_label.pack()

        for user in self.users:
            user_label = ttk.Label(users_frame, text=f"Username: {user.username} - Password: {user.password}")
            user_label.pack()

    def close_inventory_section(self):
        self.window.deiconify()
        self.current_user = None

    def run(self):
        self.window.mainloop()


def main():
    root = tk.Tk()
    app = InventoryManagementApp(root)
    app.run()


if __name__ == "__main__":
    main()
