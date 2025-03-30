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
        player_1_decisions = []
        player_2_decisions = []

        reversed_rounds = list(reversed(rounds))

        for round in reversed_rounds:
            payoffs = round.payoffs
            p1_score = payoffs.get(self.player_1, 0)
            p2_score = payoffs.get(self.player_2, 0)

            player_1_decisions.append((round.round_number, p1_score))
            player_2_decisions.append((round.round_number, p2_score))

        print("Payoffs per round (backwards):")
        for i in range(len(player_1_decisions)):
            print("Round", player_1_decisions[i][0],
                  "| Player 1:", player_1_decisions[i][1],
                  "| Player 2:", player_2_decisions[i][1])

        for i in range(len(reversed_rounds)):
            round_num = player_1_decisions[i][0]
            p1_val = player_1_decisions[i][1]
            p2_val = player_2_decisions[i][1]

            is_player_1_turn = (rounds[-1].round_number - round_num) % 2 == 0

            if is_player_1_turn:
                if p1_val >= p2_val:
                    print("\nGame stops at round", round_num, "by Player 1")
                    print("Final Payoffs: Player 1:", p1_val, ", Player 2:", p2_val)
                    return
            else:
                if p2_val >= p1_val:
                    print("\nGame stops at round", round_num, "by Player 2")
                    print("Final Payoffs : Player 1:", p1_val, ", Player 2:", p2_val)
                    return

        last_p1 = player_1_decisions[-1][1]
        last_p2 = player_2_decisions[-1][1]
        print("\nGame reaches the end .")
        print("Final Payoffs: Player 1:", last_p1, ", Player 2:", last_p2)


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
payoff = [(1, 0), (3, 2), (2, 3), (5, 6), (6, 4), (4, 7)] 

game = Game()
first_player = Player('Player 1')
second_player = Player('Player 2')

all_rounds = game.start_game(first_player, second_player, number_rounds, payoff)
game.backwards_induction(all_rounds)
