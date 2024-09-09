import random
import math

def simulated_annealing_number_guessing_game():
    # Player selects a number
    print("Think of a number between 1 and 100, and I (the AI) will try to guess it.")
    
    current_guess = random.randint(1, 100)  # Start with a random guess
    attempts = 0
    temperature = 100.0  # Initial temperature (high value to allow exploration)
    cooling_rate = 0.95  # Rate at which temperature decreases

    # Loop until the AI guesses the number correctly or temperature gets too low
    while temperature > 1:
        attempts += 1
        print(f"AI's guess is: {current_guess}")
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()
        
        if feedback == 'c':
            print(f"I (AI) guessed the number in {attempts} attempts!")
            return
        elif feedback == 'h':
            next_guess = random.randint(1, current_guess - 1)  # Explore lower numbers
        elif feedback == 'l':
            next_guess = random.randint(current_guess + 1, 100)  # Explore higher numbers
        
        # Probability of accepting a worse guess decreases as temperature lowers
        if next_guess < current_guess or random.uniform(0, 1) < math.exp((current_guess - next_guess) / temperature):
            current_guess = next_guess  # Accept the new guess based on probability
        
        temperature *= cooling_rate  # Cool down the temperature

    print("AI couldn't guess the number before cooling down completely!")

# Run the Simulated Annealing version
simulated_annealing_number_guessing_game()
