import random
# TODO: Some color or formatting of the text X by the color and O by the color
# TODO: make the message of the app more bigger or asci
# TODO: some doc string and clean code

class Menu:

    @staticmethod
    def start_menu():
        while True:
            start_quit = input(
                "Welcome For Tic-Tac-To game\n1)Start game\n2)Quit Game\n1 or 2: "
            )
            if start_quit == "1":
                return True
            elif start_quit == "2":
                return False
            else:
                print("\nYou should Choose 1 or 2\n")

    @staticmethod
    def end_menu():
        while True:
            restart_quit = input("1)Restart\n2)Quit\n1 or 2: ")
            if restart_quit == "1":
                return True
            elif restart_quit == "2":
                return False
            else:
                print("\nYou should Choose 1 or 2\n")


class Board:

    def __init__(self):
        print("\nPlayer 1")
        self.player1 = Player()
        print("\nPlayer 2")
        self.player2 = Player()
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self._win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]

    def check_name(self):
        while True:
            if self.player1.name == self.player2.name:
                print("*" * 60)
                print("Valid name every player should have uniq name")
                print("*" * 60)
                print("Player2 Put your name again")
                self.player2.set_name()
            else:
                break

    def check_symbol(self):
        if self.player1.symbol == "O":
            self.player2.symbol = "X"
        elif self.player1.symbol == "X":
            self.player2.symbol = "O"

    def print_board(self):
        for i in range(0, 9, 3):
            print(" ", self.board[i], "|", self.board[i + 1], "|", self.board[i + 2])
            print(" ", "--|---|--")

    def _choose_position(self, player):
        while True:
            position = input(
                f"Now {player.name} choose number from 1..9 to put your symbol: "
            )
            if position in self.board:
                self.board[int(position) - 1] = player.symbol
                self.print_board()
                break
            else:
                print("Invalid")

    def is_board_full(self):
        for i in self.board:
            if i.isdigit():
                return False
        return True

    def winner(self):
        for combo in self._win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]):
                return True

    def update_board(self):
        while True:

            self._choose_position(self.player1)
            is_player1_win = self.winner()
            if is_player1_win:
                return self.player1.name
            if self.is_board_full():
                return False

            self._choose_position(self.player2)
            is_player2_win = self.winner()
            if is_player2_win:
                return self.player2.name
            if self.is_board_full():
                return False

    def reset(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


class Player:

    def __init__(self):
        self.set_name()
        self.set_symbol()

    def set_name(self):
        while True:
            name = input("Put your name only letters: ")
            if name.isalpha():
                print(f"\nHello {name} you are welcome\n")
                self.name = name
                break
            else:
                print(
                    f"You should write just Alpha don't write your name like that {name}."
                )

    def set_symbol(self):
        random_index = random.randint(0, 1)
        self.symbol = ["X", "O"][random_index]


class Game:

    def init_game(self):
        if Menu.start_menu():
            self.board = Board()
            self.board.check_name()
            self.board.check_symbol()
            return True

    def play_game(self):
        self.board.print_board()
        return self.board.update_board()

    def end_game(self):
        return Menu.end_menu()


def main():

    my_game = Game()
    result = None

    init_game = my_game.init_game()

    while True:
        if init_game:
            result = my_game.play_game()
        else:
            break

        if result:
            print(f"{result} is The Winner. ")
        else:
            print("No one win.")

        if not Menu.end_menu():
            print("\n" * 100)
            break
        else:
            my_game.board.reset()
            print("\n" * 100)

if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print()
    finally:
        print("\nEnd The Game.")
