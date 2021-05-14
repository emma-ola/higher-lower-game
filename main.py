from random import choice, randint
from game_data import data
from art import logo, vs
from os import system


def cls():
    system('cls')


# Todo-2: Because a Dict is nested within the list, Access the value of the Name, Description and Country Keys,
#  display this to the user
# Get that data stored in the variable and use it to display, the {Name}, {Description}, from {Country}
# Probably a function to do this.

def construct_string(choice_a, choice_b):
    # print(choice_1)
    # print(choice_2)
    # Get a hold of each value for the keys you are interested in for choice 1(A)
    name_1 = choice_a['name']
    description_1 = choice_a['description']
    country_1 = choice_a['country']
    print(f'Compare A: {name_1}, {description_1}, from {country_1}.')

    print(vs)

    # Get a hold of each value for the keys you are interested in for choice 2(B)
    name_2 = choice_b['name']
    description_2 = choice_b['description']
    country_2 = choice_b['country']
    print(f'Against B: {name_2}, {description_2}, from {country_2}.')


# Todo-4: Check if the answered correctly and then make the previous B, A and select a new B from the list.
# First check if they answered correctly
def check_answer(user_choice, choice_a, choice_b):
    # print(user_choice)
    # Get a hold of the followers_count value for the user_choice.
    if user_choice == 'A':
        user_choice = choice_a['follower_count']
    elif user_choice == 'B':
        user_choice = choice_b['follower_count']
    # print(user_choice)
    # print(choice_a)
    # print(choice_b)

    # Get a hold of the value of followers_count for both choices and store it in a List.
    followers_count = [choice_a['follower_count'], choice_b['follower_count']]
    # print(followers_count)

    # Get a Hold of the Max follower_count in the list.
    highest_followers = max(followers_count)
    # print(highest_followers)

    # Check If the users choice is equal to the highest_follower variable
    if user_choice == highest_followers:
        # print(f"You're right! Current score: {user_score}")
        return True
    else:
        return False


# If they answered correctly Make choice B become the new choice A and select a new choice B
def swap_questions(choice_a, choice_b):
    # check if the answered correctly
    correct_answer = check_answer(user_choice=user_answer, choice_a=choice_a, choice_b=choice_b)

    # This allows the function to update the initial user choices.
    global a
    global b

    # If they did Make choice B become choice A.
    if correct_answer:
        # print(choice_a)
        # print(choice_b)
        choice_a = choice_b

        # print(f'choice_a is now {choice_a}')
        print(f"Compare A: {choice_a['name']}, {choice_a['description']}, from {choice_a['country']}.")

        # Select a new choice b from the list.
        new_choice_b = choice(data)
        if choice_a == new_choice_b:
            new_choice_b = choice(data)

        # Update the initial a variable with the new a variable.
        a = choice_a

        print(vs)

        # Update the initial b variable with the new b variable
        b = new_choice_b
        # print(f'choice_b is now {new_choice_b}')
        print(f"Against B: {new_choice_b['name']}, {new_choice_b['description']}, from {new_choice_b['country']}.")
        return True
    elif not correct_answer:
        return False


# Todo-1: Get A hold of 2 random items from the list. Call it A and B
# Use the random module to select two random items from the Data.
# Store it in two different variables.
a = choice(data)
b = choice(data)
if a == b:
    b = choice(data)

# Todo-5: If the answered correctly keep track of their score and increment it.
# create a variable to keep track of scores if they answered correctly.
user_score = 0

# print(a)
# print(b)
print(logo)
# Call the function to display the data to the user.
construct_string(choice_a=a, choice_b=b)

# print(swap_questions(choice_a=A, choice_b=B))
# Todo-7: The program should keep going until they select the wrong answer.
continue_asking = True
while continue_asking:
    # Todo-3: Ask the user to pick who they think has the most followers from the two randomly selected.
    # Get the users Answer.
    user_answer = input('Who has more followers? Type "A" or "B": ')
    cls()
    if swap_questions(choice_a=a, choice_b=b):

        # Increment the user's score if they answered correctly.
        user_score += 1
        print(f"You're right! Current score: {user_score}")
        # swap_questions(choice_a=a, choice_b=b)
    #  Todo-6: Check If the user is wrong tell them they were wrong and display their final score to them.
    elif not swap_questions(choice_a=a, choice_b=b):
        print(f'Sorry, that\'s wrong. Final Score: {user_score}')
        continue_asking = False
