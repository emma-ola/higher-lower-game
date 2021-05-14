from random import choice
from game_data import data
from art import logo, vs
from os import system


def cls():
    system('cls')


# Get that data stored in the variable and use it to display, the {Name}, {Description}, from {Country}
def construct_string(start_choice):
    """Takes the game data and returns the printable format."""

    # Get a hold of each value for the keys you are interested in.
    name = start_choice['name']
    description = start_choice['description']
    country = start_choice['country']

    return f'{name}, {description}, from {country}.'


# First check if they answered correctly
def check_answer(user_choice, choice_a, choice_b):
    """Takes the user_choice, and the generated choices and returns True if right or False if wrong."""

    # Get a hold of the followers_count value for the user_choice.
    if user_choice == 'A':
        user_choice = choice_a['follower_count']
    elif user_choice == 'B':
        user_choice = choice_b['follower_count']

    # Get a hold of the value of followers_count for both choices and store it in a List.
    followers_count = [choice_a['follower_count'], choice_b['follower_count']]

    # Get a Hold of the Max follower_count in the list.
    highest_followers = max(followers_count)

    # Check If the users choice is equal to the highest_follower variable
    if user_choice == highest_followers:
        # print(f"You're right! Current score: {user_score}")
        return True
    else:
        return False


# If they answered correctly Make choice B become the new choice A and select a new choice B
def swap_questions(choice_a, choice_b):
    """Swaps the questions and generate a new question to display if the user gets it right, and returns True or False
    if wrong."""
    # check if the answered correctly
    correct_answer = check_answer(user_choice=user_answer, choice_a=choice_a, choice_b=choice_b)

    # This allows the function to update the initial user choices.
    global a
    global b

    # If they did Make choice B become choice A.
    if correct_answer:
        choice_a = choice_b

        # Update the initial a variable with the new a variable.
        a = choice_a

        # Select a new choice b from the list.
        new_choice_b = choice(data)

        # Make sure choice b and a are not the same
        while choice_a == new_choice_b:
            new_choice_b = choice(data)

        # Update the initial b variable with the new b variable
        b = new_choice_b

        print(logo)
        print(f"Compare A: {choice_a['name']}, {choice_a['description']}, from {choice_a['country']}.")
        print(vs)
        print(f"Against B: {new_choice_b['name']}, {new_choice_b['description']}, from {new_choice_b['country']}.")
        return True
    elif not correct_answer:
        return False


# Use the random module to select two random items from the Data.
# Store it in two different variables.
a = choice(data)
b = choice(data)

# Make sure they are different
while a == b:
    b = choice(data)

# create a variable to keep track of scores if they answered correctly.
user_score = 0

print(logo)

# Call the function to display the data to the user.
print(f'Compare A: {construct_string(start_choice=a)}')
print(vs)
print(f'Against B: {construct_string(start_choice=b)}')

continue_asking = True
while continue_asking:
    # Get the users Answer.
    user_answer = input('Who has more followers? Type "A" or "B": ').upper()
    cls()
    if swap_questions(choice_a=a, choice_b=b):

        # Increment the user's score if they answered correctly.
        user_score += 1
        print(f"You're right! Current score: {user_score}")

    # Check If the user is wrong tell them they were wrong and display their final score to them.
    elif not swap_questions(choice_a=a, choice_b=b):
        print(f'Sorry, that\'s wrong. Final Score: {user_score}')
        continue_asking = False
