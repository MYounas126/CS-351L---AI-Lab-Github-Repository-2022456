import random
from collections import deque

def bfs_number_guessing_game():
    # Player selects a number
    print("Think of a number between 1 and 100, and I (the AI) will try to guess it.")
    
    numbers = list(range(1, 101))  # Create a list of numbers from 1 to 100
    random.shuffle(numbers)  # Shuffle the list to make the starting number random
    queue = deque(numbers)  # Convert the shuffled list into a queue
    attempts = 0

    # Loop until the AI guesses the number correctly
    while queue:
        guess = queue.popleft()  # AI guesses the next number in the queue
        attempts += 1
        
        print(f"AI's guess is: {guess}")
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'c':
            print(f"I (AI) guessed the number in {attempts} attempts!")
            return
        elif feedback == 'h':
            queue = deque([x for x in queue if x < guess])  # Filter out numbers higher than the guess
        elif feedback == 'l':
            queue = deque([x for x in queue if x > guess])  # Filter out numbers lower than the guess
    
    print("Something went wrong!")

# Run the BFS version with a random starting guess
bfs_number_guessing_game()
