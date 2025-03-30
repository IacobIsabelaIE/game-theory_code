def find_NE(number_strategies_player_1, number_strategies_player_2, payoff_p1, payoff_p2): 
    NE = []

    for i in range(number_strategies_player_1):
        for j in range(number_strategies_player_2): 

            p1_val = payoff_p1[i][j]
            p2_val = payoff_p2[i][j]

            best_response_p1 = True
            for z in range(number_strategies_player_1):
                if payoff_p1[z][j] > p1_val:
                    best_response_p1 = False
                    break

            best_response_p2 = True
            for y in range(number_strategies_player_2):
                if payoff_p2[i][y] > p2_val:
                    best_response_p2 = False
                    break

            if best_response_p1 and best_response_p2:

                NE.append((p1_val, p2_val))

    return NE



number_strategies_player_1 = 2 
number_strategies_player_2 = 3

payoff_p1 = [
    [3, 1, 2],
    [0, 2, 1]
]

payoff_p2 = [
    [2, 0, 3],
    [3, 1, 0]
]

nash_equilibria = find_NE(number_strategies_player_1, number_strategies_player_2, payoff_p1, payoff_p2)

print("Pure Nash Equilibria:", nash_equilibria)
