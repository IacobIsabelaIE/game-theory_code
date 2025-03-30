import tkinter as tk
from Ex2 import define_probability

def run_simulation():
    """
    Reads `n` and `k` from the user’s entries,
    calls define_probability, then shows the result in the GUI.
    """
    n = int(entry_n.get())
    k = int(entry_k.get())
    
    stay_prob, switch_prob = define_probability(n, k)
    
    label_result.config(
        text=(
            f"Stay Win Probability: {stay_prob:.3f}\n"
            f"Switch Win Probability: {switch_prob:.3f}"
        )
    )

root = tk.Tk()
root.title("Monty Hall Simulation")

label_n = tk.Label(root, text="Number of Doors (N):")
label_n.pack()
entry_n = tk.Entry(root)
entry_n.pack()

label_k = tk.Label(root, text="Number of Simulations (K):")
label_k.pack()
entry_k = tk.Entry(root)
entry_k.pack()

button_run = tk.Button(root, text="Run Simulation", command=run_simulation)
button_run.pack()

label_result = tk.Label(root, text="", fg="blue")
label_result.pack()

root.mainloop()
