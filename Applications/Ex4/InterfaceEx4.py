import tkinter as tk
from tkinter import messagebox
from Ex4 import Game, Player
import random

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Simulator")

        self.rounds_var = tk.StringVar()
        self.mode_var = tk.StringVar(value="random")

        self.entries = []

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Number of Rounds:").grid(row=0, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.rounds_var).grid(row=0, column=1)

        tk.Radiobutton(self.root, text="Random Payoffs", variable=self.mode_var, value="random", command=self.clear_entries).grid(row=1, column=0, sticky="w")
        tk.Radiobutton(self.root, text="Manual Payoffs", variable=self.mode_var, value="manual", command=self.prepare_manual_input).grid(row=2, column=0, sticky="w")

        self.manual_frame = tk.Frame(self.root)
        self.manual_frame.grid(row=3, column=0, columnspan=2, pady=10)

        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.grid(row=4, column=0, columnspan=2)

    def clear_entries(self):
        for widget in self.manual_frame.winfo_children():
            widget.destroy()
        self.entries = []

    def prepare_manual_input(self):
        self.clear_entries()

        n = int(self.rounds_var.get())
        if n <= 0:
            raise ValueError
    

        tk.Label(self.manual_frame, text="Enter Payoffs for Each Round").grid(row=0, column=0, columnspan=2)

        for i in range(n):
            p1_entry = tk.Entry(self.manual_frame, width=5)
            p2_entry = tk.Entry(self.manual_frame, width=5)
            tk.Label(self.manual_frame, text=f"Round {i+1}: P1").grid(row=i+1, column=0, sticky="e")
            p1_entry.grid(row=i+1, column=1)
            tk.Label(self.manual_frame, text="P2").grid(row=i+1, column=2, sticky="e")
            p2_entry.grid(row=i+1, column=3)
            self.entries.append((p1_entry, p2_entry))

    def start_game(self):

        n = int(self.rounds_var.get())
        if n <= 0:
            raise ValueError


        if self.mode_var.get() == "manual":
            payoffs = []
            for p1_entry, p2_entry in self.entries:
                p1 = int(p1_entry.get())
                p2 = int(p2_entry.get())
                payoffs.append((p1, p2))

        else:
            payoffs = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(n)]
            payoff_text = "\n".join([f"Round {i+1}: Player 1 = {p1}, Player 2 = {p2}" for i, (p1, p2) in enumerate(payoffs)])
            messagebox.showinfo("Generated Random Payoffs", payoff_text)

        game = Game()
        p1 = Player("Player 1")
        p2 = Player("Player 2")

        rounds = game.start_game(p1, p2, n, payoffs)

        result = self.get_game_result(game, rounds)
        messagebox.showinfo("Game Result", result)


    def get_game_result(self, game, rounds):

        player_1_decisions = []
        player_2_decisions = []

        reversed_rounds = list(reversed(rounds))

        for round in reversed_rounds:
            payoffs = round.payoffs
            p1_score = payoffs.get(game.player_1, 0)
            p2_score = payoffs.get(game.player_2, 0)

            player_1_decisions.append((round.round_number, p1_score))
            player_2_decisions.append((round.round_number, p2_score))

        for i in range(len(reversed_rounds)):
            round_num = player_1_decisions[i][0]
            p1_val = player_1_decisions[i][1]
            p2_val = player_2_decisions[i][1]

            is_player_1_turn = (rounds[-1].round_number - round_num) % 2 == 0

            if is_player_1_turn:
                if p1_val >= p2_val:
                    return f"Game stops at round {round_num} by Player 1.\nFinal Payoffs:\nPlayer 1: {p1_val}\nPlayer 2: {p2_val}"
            else:
                if p2_val >= p1_val:
                    return f"Game stops at round {round_num} by Player 2.\nFinal Payoffs:\nPlayer 1: {p1_val}\nPlayer 2: {p2_val}"

        last_p1 = player_1_decisions[-1][1]
        last_p2 = player_2_decisions[-1][1]
        return f"Game reaches the end.\nFinal Payoffs:\nPlayer 1: {last_p1}\nPlayer 2: {last_p2}"

if __name__ == "__main__":
    root = tk.Tk()
    app = GameGUI(root)
    root.mainloop()
