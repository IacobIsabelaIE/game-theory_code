class Game:
    def __init__(self):
        pass

    def start_game(self, first_player, second_player, number_rounds, payoffs):
        player_1 = Player(first_player)
        player_2 = Player(second_player)
        all_rounds = []

        for i in range(number_rounds):
            new_round = Round(round_number=i)
            first_tuple = payoffs[i]
            new_round.payoffs[player_1] = first_tuple[0]
            new_round.payoffs[player_2] = first_tuple[1]
            all_rounds.append(new_round)

        self.player_1 = player_1
        self.player_2 = player_2

        return all_rounds

    def backwards_induction(self, rounds):
        n = len(rounds)
        optimal_path = [None] * n  
        final_payoffs = [None] * n  

        last_round = rounds[-1]
        final_payoffs[-1] = (last_round.payoffs[self.player_1], last_round.payoffs[self.player_2])
        optimal_path[-1] = 'stop'

        for i in range(n - 2, -1, -1):
            current_round = rounds[i]
            is_p1_turn = (i % 2 == 0)
            stop_payoff = (current_round.payoffs[self.player_1], current_round.payoffs[self.player_2])
            continue_payoff = final_payoffs[i + 1]

            if is_p1_turn:
                if stop_payoff[0] >= continue_payoff[0]:
                    final_payoffs[i] = stop_payoff
                    optimal_path[i] = 'stop'
                else:
                    final_payoffs[i] = continue_payoff
                    optimal_path[i] = 'continue'
            else:
                if stop_payoff[1] >= continue_payoff[1]:
                    final_payoffs[i] = stop_payoff
                    optimal_path[i] = 'stop'
                else:
                    final_payoffs[i] = continue_payoff
                    optimal_path[i] = 'continue'

        for i in range(n):
            if optimal_path[i] == 'stop':
                stopping_player = self.player_1 if (i % 2 == 0) else self.player_2
                print(f"\nGame stops at round {i+1} by {stopping_player.player_name}")
                print(f"Final Payoffs: Player 1: {final_payoffs[i][0]}, Player 2: {final_payoffs[i][1]}")
                return

        print("\nGame reaches the end.")
        print(f"Final Payoffs: Player 1: {final_payoffs[-1][0]}, Player 2: {final_payoffs[-1][1]}")


class Player:
    def __init__(self, player_name):
        self.player_name = player_name

    def __repr__(self):
        return f"Player({self.player_name})"

    def __eq__(self, other):
        return isinstance(other, Player) and self.player_name == other.player_name

    def __hash__(self):
        return hash(self.player_name)


class Round:
    def __init__(self, round_number=0, payoffs=None, direction=None):
        self.round_number = round_number
        self.payoffs = payoffs if payoffs is not None else {}
        self.direction = direction

    def __repr__(self):
        return f"Round({self.round_number}, {self.payoffs})"



number_rounds = 6
payoff = [
    (5, 0),
    (6, 1),
    (7, 2),
    (8, 3),
    (6, 0),
    (4, 1),

]

game = Game()
first_player = Player('Player 1')
second_player = Player('Player 2')

all_rounds = game.start_game(first_player, second_player, number_rounds, payoff)
game.backwards_induction(all_rounds)
