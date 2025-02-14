import tkinter as tk
from tkinter import messagebox

def calculate_cost():
    try:
        total_cost = 0.0
        for entry in ingredient_entries:
            name = entry[0].get().strip()
            quantity = float(entry[1].get().strip())
            price = float(entry[2].get().strip())
            total_cost += quantity * price
        result_label.config(text=f"Total Cost: ₹{total_cost:.2f}")
    except Exception:
        messagebox.showerror("Error", "Invalid input. Ensure all fields are correctly filled.")

def add_ingredient_row():
    row_frame = tk.Frame(root)
    row_frame.pack(pady=5)
    
    name_entry = tk.Entry(row_frame, width=15)
    name_entry.pack(side=tk.LEFT, padx=5)
    
    quantity_entry = tk.Entry(row_frame, width=10)
    quantity_entry.pack(side=tk.LEFT, padx=5)
    
    price_entry = tk.Entry(row_frame, width=10)
    price_entry.pack(side=tk.LEFT, padx=5)
    
    ingredient_entries.append((name_entry, quantity_entry, price_entry))

# GUI Setup
root = tk.Tk()
root.title("Recipe Cost Calculator")
root.geometry("450x500")

tk.Label(root, text="Ingredients (Name, Quantity, Price in INR):", font=("Arial", 10)).pack(pady=5)

header_frame = tk.Frame(root)
header_frame.pack(pady=5)
tk.Label(header_frame, text="Ingredient", width=15, font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=5)
tk.Label(header_frame, text="Quantity (without units)", width=20, font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=5)
tk.Label(header_frame, text="Price (INR)", width=10, font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=5)

ingredient_entries = []
for _ in range(5):
    add_ingredient_row()

tk.Button(root, text="Calculate Cost", command=calculate_cost).pack(pady=10)
result_label = tk.Label(root, text="Total Cost: ₹0.00", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
