from cleaner import Cleaner
from environment import Environment
import time,os,random


def main():
    n=50
    # Define the dirty squares
    dirty_squares = []   
    for _ in range(n):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        dirty_squares.append((x, y))  # Coordinated of dirty squares
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    initial_position = (x, y)  # Initial position of the cleaner

    # Create an object of the Cleaner class
    cl = Cleaner()

    # Create an object of the Environment class with the dirty squares and initial position
    environment = Environment(dirty_squares, initial_position)

    # Get the initial perception from the environment
    perception = environment.get_perception()
    matrice=cl.draw_letter_A(environment.print_state()[0],environment.print_state()[1])
    os.system('cls')
    for i in matrice:
        print(i,"\n")
    time.sleep(5) # wait for you to see the cleaner
    os.system('cls')# delete the console

    while not environment.is_clean():
        matrice=cl.draw_letter_A(environment.print_state()[0],environment.print_state()[1])
        for i in matrice:
            print(i,"\n")
        # Update the cleaner's memory with the current perception
        cl.update_memory(perception)

        # Choose the best action based on the perception
        action = cl.choose_best_action()
        # Perform the action in the environment and get the next perception
        perception = environment.perform_action(action)
        print("Next Action:", action)
        time.sleep(1)  # Delay for 2 seconds before displaying the next map
        os.system('cls')  # delete the console
        
    print("\n","All squares are clean.")


if __name__ == "__main__":
    main()