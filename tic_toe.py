battlefield = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Введите имена игроков...")
gamer_one = input("Имя первого игрока: ")
gamer_two = input("Имя второго игрока: ")
print(f"{gamer_one} играет за Х, {gamer_two} играет за О")
print()


def battlefield_zero():
    for i in battlefield:
        print(*i)
    return " "


print("Выберите цифру, куда хотите сделать ход:")
battlefield_zero()
print()


def winner():
    if (battlefield[0][0] == "X" and battlefield[0][1] == "X" and battlefield[0][2] == "X") or \
            (battlefield[1][0] == "X" and battlefield[1][1] == "X" and battlefield[1][2] == "X") or \
            (battlefield[2][0] == "X" and battlefield[2][1] == "X" and battlefield[2][2] == "X") or \
            (battlefield[0][0] == "X" and battlefield[1][0] == "X" and battlefield[2][0] == "X") or \
            (battlefield[0][1] == "X" and battlefield[1][1] == "X" and battlefield[2][1] == "X") or \
            (battlefield[0][2] == "X" and battlefield[1][2] == "X" and battlefield[2][2] == "X") or \
            (battlefield[0][0] == "X" and battlefield[1][1] == "X" and battlefield[2][2] == "X") or \
            (battlefield[0][2] == "X" and battlefield[1][1] == "X" and battlefield[2][0] == "X"):
        print(f"Победил {gamer_one}, X!")
        return True
    elif (battlefield[0][0] == "O" and battlefield[0][1] == "O" and battlefield[0][2] == "O") or \
            (battlefield[1][0] == "O" and battlefield[1][1] == "O" and battlefield[1][2] == "O") or \
            (battlefield[2][0] == "O" and battlefield[2][1] == "O" and battlefield[2][2] == "O") or \
            (battlefield[0][0] == "O" and battlefield[1][0] == "O" and battlefield[2][0] == "O") or \
            (battlefield[0][1] == "O" and battlefield[1][1] == "O" and battlefield[2][1] == "O") or \
            (battlefield[0][2] == "O" and battlefield[1][2] == "O" and battlefield[2][2] == "O") or \
            (battlefield[0][0] == "O" and battlefield[1][1] == "O" and battlefield[2][2] == "O") or \
            (battlefield[0][2] == "O" and battlefield[1][1] == "O" and battlefield[2][0] == "O"):
        print(f"Победитель {gamer_two}, O")
        return True
    return False


def game():
    counter_step = 1
    while (counter_step < 9) and (winner() == False):
        game_one = input(f"Ходит {gamer_one} (X): ")
        if game_one == "1":
            battlefield[0][0] = "X"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_one == "2":
            battlefield[0][1] = "X"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_one == "3":
            battlefield[0][2] = "X"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_one == "4":
            battlefield[1][0] = "X"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_one == "5":
            battlefield[1][1] = "X"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_one == "6":
            battlefield[1][2] = "X"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_one == "7":
            battlefield[2][0] = "X"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                 break
        elif game_one == "8":
            battlefield[2][1] = "X"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_one == "9":
            battlefield[2][2] = "X"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break

        game_two = input(f"Ходит {gamer_two} (O): ")
        if game_two == "1":
            battlefield[0][0] = "O"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_two == "2":
            battlefield[0][1] = "O"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_two == "3":
            battlefield[0][2] = "O"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_two == "4":
            battlefield[1][0] = "O"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_two == "5":
            battlefield[1][1] = "O"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_two == "6":
            battlefield[1][2] = "O"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_two == "7":
            battlefield[2][0] = "O"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_two == "8":
            battlefield[2][1] = "O"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        elif game_two == "9":
            battlefield[2][2] = "O"
            yield battlefield_zero()
            counter_step += 1
            if winner():
                break
        if counter_step == 9:
            return "Ничья"


for i in game():
    print(i)




