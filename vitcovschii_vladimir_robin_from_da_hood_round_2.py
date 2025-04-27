def strategy_round_2(opponent_id: int, my_history: dict[int, list[int]], opponents_history: dict[int, list[int]]) -> tuple[int, int]:
    my_moves = my_history.get(opponent_id, [])
    opponent_moves = opponents_history.get(opponent_id, [])
    total_rounds = len(my_moves)
    my_zeros = total_rounds - sum(my_moves)
    opp_zeros = total_rounds - sum(opponent_moves)

    last_three_ones = len(opponent_moves) >= 3 and opponent_moves[-1] == opponent_moves[-2] == opponent_moves[-3] == 1
    dynamic_gap = 0
    dynamic_gap_less = dynamic_gap + total_rounds // 4

    if last_three_ones:
        move = 1
    elif opp_zeros >= my_zeros + dynamic_gap or opp_zeros < my_zeros - dynamic_gap_less:
        move = 0
    else:
        move = 1

    # Choose next opponent: pick someone you haven't maxed 200 rounds with
    possible_opponents = [pid for pid, history in my_history.items() if len(history) < 200]

    if not possible_opponents:
        next_opponent = opponent_id  # fallback if nobody is available
    else:
        next_opponent = possible_opponents[0]  # pick first available

    return move, next_opponent