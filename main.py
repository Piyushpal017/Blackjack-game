import art
import random

again = True
while again:
    def play_game():
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ").lower()
        if play == "y":
            print(art.logo)
            your_card = [random.randint(1, 11), random.randint(1, 11)]
            computer_first_card = [random.randint(1, 11)]
            if 11 in your_card and sum(your_card) > 21:
                your_card.remove(11)
                your_card.append(1)
            if 11 in computer_first_card and sum(computer_first_card) > 21:
                computer_first_card.remove(11)
                computer_first_card.append(1)

            def print_score():
                current_score = 0
                computer_score = 0
                for score in your_card:
                    current_score += score
                for point in computer_first_card:
                    computer_score += point

                def result():
                    print(f"    Your final hand: {your_card}, final score: {current_score}")
                    print(f"    computer's final hand: {computer_first_card}, final score: {computer_score}")

                print(f"    Your cards {your_card}, Current score = {current_score}")
                print(f"    computer's first card: {computer_first_card}")
                if current_score > 21:
                    result()
                    print("You went over. You lose 😭")
                    play_game()
                elif current_score == 2 and len(your_card) == 2:
                    result()
                    print("Win with a Blackjack 😎")
                    play_game()

            def print_computer_score():
                current_score = 0
                computer_score = 0
                for score in your_card:
                    current_score += score
                for point in computer_first_card:
                    computer_score += point

                def answer():
                    print(f"    Your final hand: {your_card}, final score: {current_score}")
                    print(f"    computer's final hand: {computer_first_card}, final score: {computer_score}")

                if computer_score > 21:
                    answer()
                    print("opponent went over. you win 😁")
                    play_game()
                elif computer_score == 21 and len(computer_first_card) == 2:
                    answer()
                    print("lose, opponent has Blackjack 😱")
                    play_game()
                elif computer_score > current_score:
                    answer()
                    print("You lose 😤")
                    play_game()
                elif current_score > computer_score:
                    answer()
                    print("You Win 😃")
                    play_game()
                else:
                    answer()
                    print("Draw 🙃")
                    play_game()

            print_score()
            again_again = True
            while again_again:
                play_again = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if play_again == "y":
                    your_card += [random.randint(1, 10)]
                    print_score()
                else:

                    while sum(computer_first_card) < 17:
                        computer_first_card += [random.randint(1, 10)]
                    print_computer_score()


    play_game()
