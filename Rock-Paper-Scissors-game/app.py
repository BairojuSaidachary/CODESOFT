import sys
import random
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QMessageBox,
)
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtCore import Qt


class RockPaperScissorsGame(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize game variables
        self.user_score = 0
        self.computer_score = 0
        self.continuous_wins_user = 0
        self.continuous_wins_computer = 0

        # Initialize the user interface
        self.init_ui()

    def init_ui(self):
        # Create a vertical layout for the widgets
        layout = QVBoxLayout()

        # Instruction label for the user
        self.instruction_label = QLabel("Choose rock, paper, or scissors:")
        self.instruction_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.instruction_label)

        # Display label for game results
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)

        # Score label to show the current scores
        self.score_label = QLabel()
        self.score_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.score_label)

        # Buttons for user choices (rock, paper, scissors)
        rock_button = QPushButton("Rock")
        rock_button.clicked.connect(lambda: self.play_game("rock"))
        rock_button.setIcon(self.create_icon("rock.png"))
        layout.addWidget(rock_button)

        paper_button = QPushButton("Paper")
        paper_button.clicked.connect(lambda: self.play_game("paper"))
        paper_button.setIcon(self.create_icon("paper.png"))
        layout.addWidget(paper_button)

        scissors_button = QPushButton("Scissors")
        scissors_button.clicked.connect(lambda: self.play_game("scissors"))
        scissors_button.setIcon(self.create_icon("scissors.png"))
        layout.addWidget(scissors_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle("Rock-Paper-Scissors Game")
        self.setGeometry(100, 100, 400, 300)
        self.setFixedSize(400, 300)

        # Show the main window
        self.show()

    def play_game(self, user_choice):
        # Determine computer's choice
        computer_choice = self.get_computer_choice()

        # Determine the winner and update scores
        winner = self.determine_winner(user_choice, computer_choice)
        self.display_result(user_choice, computer_choice, winner)

        # Update scores and check for continuous wins
        if winner == "user":
            self.user_score += 1
            self.continuous_wins_user += 1
            self.continuous_wins_computer = 0
        elif winner == "computer":
            self.computer_score += 1
            self.continuous_wins_computer += 1
            self.continuous_wins_user = 0
        else:
            self.continuous_wins_user = 0
            self.continuous_wins_computer = 0

        # Update the score label
        self.update_score_label()

        # Display final result if someone reaches three continuous wins
        if self.continuous_wins_user == 3:
            self.display_final_result(
                "✨Congratulations!✨ You have demonstrated exceptional skill by winning 3 times in a row. You are the undisputed overall winner!",
                QColor("white"),
                QColor("green"),
            )
        elif self.continuous_wins_computer == 3:
            self.display_final_result(
                "🥺Apologies🥺, but the computer has proven to be a formidable opponent by winning 3 times in a row. Better luck next time!",
                QColor("white"),
                QColor("red"),
            )

    def get_computer_choice(self):
        # Randomly choose rock, paper, or scissors for the computer
        return random.choice(["rock", "paper", "scissors"])

    def determine_winner(self, user_choice, computer_choice):
        # Determine the winner based on user and computer choices
        if user_choice == computer_choice:
            return "tie"
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "scissors" and computer_choice == "paper")
            or (user_choice == "paper" and computer_choice == "rock")
        ):
            return "user"
        else:
            return "computer"

    def display_result(self, user_choice, computer_choice, winner):
        # Display the result of the game
        self.result_label.setText(
            f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {winner}"
        )
        self.result_label.setStyleSheet(
            "background-color: lightyellow; border: 2px solid #333; border-radius: 5px;"
        )
        self.result_label.setFont(QFont("Arial", 12, QFont.Bold))

    def update_score_label(self):
        # Update the score label with current scores
        self.score_label.setText(
            f"Score - You: {self.user_score} | Computer: {self.computer_score}"
        )
        self.score_label.setStyleSheet(
            "background-color: lightblue; border: 2px solid #333; border-radius: 5px;"
        )
        self.score_label.setFont(QFont("Arial", 12, QFont.Bold))

    def display_final_result(self, message, background_color, text_color):
        # Display the final result in a pop-up message box
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Game Over")
        msg_box.setText(message)
        msg_box.setStyleSheet(
            f"background-color: {background_color.name()}; color: {text_color.name()};"
        )
        msg_box.setFont(QFont("Arial", 12, QFont.Bold))
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

        # Reset the game after displaying the final result
        self.reset_game()
        self.result_label.setStyleSheet(
            f"background-color: {background_color.name()}; border: 2px solid #333; border-radius: 5px;"
        )
        self.result_label.setFont(QFont("Arial", 14, QFont.Bold))

    def reset_game(self):
        # Reset game variables and update the score label
        self.user_score = 0
        self.computer_score = 0
        self.continuous_wins_user = 0
        self.continuous_wins_computer = 0
        self.update_score_label()

    def create_icon(self, filename):
        # Create QIcon from a QPixmap loaded from an image file
        pixmap = QPixmap(filename)
        icon = QIcon(pixmap)
        return icon


if __name__ == "__main__":
    # Run the application
    app = QApplication(sys.argv)
    game_window = RockPaperScissorsGame()
    sys.exit(app.exec_())
