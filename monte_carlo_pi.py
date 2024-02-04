import random
import math

def estimate_pi_forever(print_interval=100000000):
    """
    Estimate the value of pi using Monte Carlo simulation in a forever loop.
    Prints the current estimation every 'print_interval' iterations.

    Args:
    print_interval: The interval at which to print the current estimation of pi
    """

    # Initialize count of points inside the circle and total points 
    # These numbers are from previous run (allows for saving progress)
    # TODO: incorporate reduction
    inside_circle = 620071539914
    total_points = 789500000000

    # Start an infinite loop for generating random points
    while True:
        x, y = random.random(), random.random()  # Random point between [0,1)
        distance_to_center = math.sqrt(x**2 + y**2)
        if distance_to_center <= 1:
            inside_circle += 1
        total_points += 1

        # Print current estimate every 'print_interval' iterations
        if total_points % print_interval == 0:
            pi_estimate = (inside_circle / total_points) * 4
            print(f"Estimation of PI after {total_points:,} samples: {pi_estimate}")
            print(f"inside_circle: {inside_circle:,};  total_points: {total_points:,}")
            print("---")

# Example usage:
estimate_pi_forever()
