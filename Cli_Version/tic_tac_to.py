# TODO: Quit at the start of the program & start at the end
# TODO: Some color or formatting of the text
# TODO: restart should not ask about the name and symbol again
# TODO: some doc string and clean code

class Menu:

    def start_menu(self):
        while True:
            start_quit = input(
                "Welcome For Tic-Tac-To game\n1)Start game\n2)Quit Game\n1 or 2: "
            )
            if start_quit == "1":
                return True
            elif start_quit == "2":
                return False
            else:
                print("You should Choose just 1 or 2 ")

    def end_menu(self):
        while True:
            restart_quit = input("1)Restart\n2)Quit\n1 or 2: ")
            if restart_quit == "1":
                return True
            elif restart_quit == "2":
                return False
            else:
                print("You should Choose just 1 or 2 ")


class Board:

    def __init__(self):
        print("Player 1")
        self.player1 = Player()
        print("Player 2")
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
        while True:
            if self.player1.symbol == self.player2.symbol:
                print("*" * 60)
                print("Valid symbol every player should have uniq symbol")
                print("*" * 60)
                print(f"{self.player2.name} Put your symbol again")
                self.player2.set_symbol()
            else:
                break

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

    def is_balance(self):
        for i in self.board:
            if i in "123456789":
                return False
        return True

    def winner(self):
        for combo in self._win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]):
                return self.board[combo[0]]

    def update_board(self):
        while True:
            self._choose_position(self.player1)
            if self.winner():
                return self.winner()
            if self.is_balance():
                return False

            self._choose_position(self.player2)
            if self.winner():
                return self.winner()
            if self.is_balance():
                return False

    def restart_board(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


class Player:

    def __init__(self):
        self.set_name()
        self.set_symbol()

    def set_name(self):
        while True:
            name = input("Put your name only letters: ")
            if name.isalpha():
                print(f"Hello {name} you are welcome")
                self.name = name
                break
            else:
                print(
                    f"You should write just Alpha don't write your name like that {name}."
                )

    def set_symbol(self):
        while True:
            symbol = input(f"Symbol of {self.name} is: ")
            if len(symbol) == 1 and not symbol.isdigit():
                self.symbol = symbol.upper()
                break
            else:
                print(f"You should write one character no like that {symbol}.")


class Game:

    def __init__(self):
        self.menu = Menu()

    def start_game(self):
        if self.menu.start_menu():
            self.board = Board()
            self.board.check_name()
            self.board.check_symbol()
            return True

    def middle_game(self):
        self.board.print_board()
        return self.board.update_board()

    def end_game(self):
        return self.menu.end_menu()


def main():

    my_game = Game()
    result = None

    if my_game.start_game():
        result = my_game.middle_game()

    if result:
        print(f"The {result} is Win. ")
    else:
        print("No one win.")

    if my_game.menu.end_menu():
        main()

if __name__ == "__main__":
    main()
