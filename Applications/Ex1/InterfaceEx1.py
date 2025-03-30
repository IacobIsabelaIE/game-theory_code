import tkinter as tk
from tkinter import messagebox
import random

from Ex1 import find_NE


class NashApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pure Nash Equilibria Finder")

        self.label1 = tk.Label(root, text="Number of strategies for Player 1:")
        self.label1.pack()
        self.entry1 = tk.Entry(root)
        self.entry1.pack()

        self.label2 = tk.Label(root, text="Number of strategies for Player 2:")
        self.label2.pack()
        self.entry2 = tk.Entry(root)
        self.entry2.pack()

        self.random_var = tk.IntVar()
        self.random_checkbox = tk.Checkbutton(root, text="Generate random payoffs (1–10)", variable=self.random_var)
        self.random_checkbox.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.get_strategy_input)
        self.submit_button.pack()

    def get_strategy_input(self):
            
        m = int(self.entry1.get())
        n = int(self.entry2.get())


        if self.random_var.get():

            payoff_p1 = [[random.randint(1, 10) for _ in range(n)] for _ in range(m)]
            payoff_p2 = [[random.randint(1, 10) for _ in range(n)] for _ in range(m)]
            self.display_results(m, n, payoff_p1, payoff_p2)
        else:
            self.create_payoff_inputs(m, n)

    def create_payoff_inputs(self, m, n):
        self.payoff_window = tk.Toplevel(self.root)
        self.payoff_window.title("Enter Payoffs (row by row)")

        self.entries_p1 = []
        self.entries_p2 = []

        tk.Label(self.payoff_window, text="Player 1 Payoffs").grid(row=0, column=0, columnspan=n)
        for i in range(m):
            row = []
            for j in range(n):
                e = tk.Entry(self.payoff_window, width=3)
                e.grid(row=i+1, column=j)
                row.append(e)
            self.entries_p1.append(row)

        offset = m + 2
        tk.Label(self.payoff_window, text="Player 2 Payoffs").grid(row=offset, column=0, columnspan=n)
        for i in range(m):
            row = []
            for j in range(n):
                e = tk.Entry(self.payoff_window, width=3)
                e.grid(row=i+offset+1, column=j)
                row.append(e)
            self.entries_p2.append(row)

        submit_btn = tk.Button(self.payoff_window, text="Compute Nash Equilibria",
                               command=lambda: self.collect_manual_payoffs(m, n))
        submit_btn.grid(row=2*offset+1, column=0, columnspan=n)

    def collect_manual_payoffs(self, m, n):
        
        payoff_p1 = [[int(self.entries_p1[i][j].get()) for j in range(n)] for i in range(m)]
        payoff_p2 = [[int(self.entries_p2[i][j].get()) for j in range(n)] for i in range(m)]
    
        self.display_results(m, n, payoff_p1, payoff_p2)

    def display_results(self, m, n, p1, p2):
        NE = find_NE(m, n, p1, p2)
        result_window = tk.Toplevel(self.root)
        result_window.title("Result")

        tk.Label(result_window, text="Combined Payoff Matrix (Player 1, Player 2):").pack()
        for i in range(m):
            row_text = "  ".join([f"({p1[i][j]},{p2[i][j]})" for j in range(n)])
            tk.Label(result_window, text=row_text).pack()

        tk.Label(result_window, text="Pure Nash Equilibria:").pack()
        if NE:
            formatted = ', '.join([f"({i}, {j})" for i, j in NE])
            tk.Label(result_window, text=formatted).pack()
        else:
            tk.Label(result_window, text="No Pure Nash Equilibria found.").pack()



if __name__ == "__main__":
    root = tk.Tk()
    app = NashApp(root)
    root.mainloop()
