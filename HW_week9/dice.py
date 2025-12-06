import random


def roll_two_dice():
    """Simulate rolling two six-sided dice and return their sum."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2


def simulate_dice_rolls(num_rolls):
    frequency = {sum_value: 0 for sum_value in range(2, 13)}
    for _ in range(num_rolls):
        dice_sum = roll_two_dice()
        frequency[dice_sum] += 1

    return frequency


def display_results(frequency, num_rolls):
    """Display the frequency results in a user-friendly format."""

    print("\n" + "="*50)
    print("Hello Sam. Let's play Dice Roll Simulator")
    print("="*50)
    print(f"Total rolls: {num_rolls:,}")
    print("-"*50)

    # Table header
    print(f"{'Sum':<6} {'Frequency':<12} {'Percentage':<12} {'Graph'}")
    print("-"*50)

    # Calculate and display each sum's statistics
    for dice_sum in sorted(frequency.keys()):
        count = frequency[dice_sum]
        percentage = (count / num_rolls) * 100 if num_rolls > 0 else 0

        # Create a simple ASCII bar graph
        bar_length = int(percentage / 2)  # Scale the bar
        bar = "█" * bar_length

        print(f"{dice_sum:<6} {count:<12,} {percentage:>8.2f}%    {bar}")

    print("="*50)


def display_probability_table():
    """Display the theoretical probability table for reference."""

    print("\n" + "="*50)
    print("THEORETICAL PROBABILITIES FOR TWO DICE")
    print("="*50)
    print(f"{'Sum':<6} {'Ways':<10} {'Probability':<15} {'Percentage'}")
    print("-"*50)

    # Theoretical probabilities for two dice
    theoretical_ways = {
        2: 1,   # 1+1
        3: 2,   # 1+2, 2+1
        4: 3,   # 1+3, 2+2, 3+1
        5: 4,   # 1+4, 2+3, 3+2, 4+1
        6: 5,   # 1+5, 2+4, 3+3, 4+2, 5+1
        7: 6,   # 6+6, 2+5, 3+4, 4+3, 5+2, 6+1
        8: 5,   # 2+6, 3+5, 4+4, 5+3, 6+2
        9: 4,   # 3+6, 4+5, 5+4, 6+3
        10: 3,  # 4+6, 5+5, 6+4
        11: 2,  # 5+6, 6+5
        12: 1   # 6+6
    }

    total_ways = 36  # 6 sides × 6 sides

    for dice_sum in sorted(theoretical_ways.keys()):
        ways = theoretical_ways[dice_sum]
        probability = ways / total_ways
        percentage = probability * 100

        print(f"{dice_sum:<6} {ways:<10} {probability:<15.4f} {percentage:>8.2f}%")

    print("="*50)


def visualize_results(frequency, num_rolls):
    """Create a bar chart visualization of the results."""
    try:
        sums = list(sorted(frequency.keys()))
        counts = [frequency[sum_val] for sum_val in sums]
        percentages = [(count / num_rolls * 100) if num_rolls >
                       0 else 0 for count in counts]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        # Bar chart for counts
        bars1 = ax1.bar([str(s) for s in sums], counts,
                        color='skyblue', edgecolor='black')
        ax1.set_xlabel('Dice Sum')
        ax1.set_ylabel('Frequency')
        ax1.set_title(f'Frequency of Dice Sums ({num_rolls:,} rolls)')
        ax1.grid(True, alpha=0.3)

        # Add value labels on bars
        for bar in bars1:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                     f'{int(height):,}', ha='center', va='bottom')

        # Bar chart for percentages
        bars2 = ax2.bar([str(s) for s in sums], percentages,
                        color='lightcoral', edgecolor='black')
        ax2.set_xlabel('Dice Sum')
        ax2.set_ylabel('Percentage (%)')
        ax2.set_title('Percentage Distribution')
        ax2.grid(True, alpha=0.3)

        # Add value labels on bars
        for bar in bars2:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                     f'{height:.1f}%', ha='center', va='bottom')

        plt.tight_layout()
        plt.show()

    except ImportError:
        print("\nNote: matplotlib is not installed. Visualization skipped.")
        print("Install it with: pip install matplotlib")


def save_results_to_file(frequency, num_rolls, filename="dice_results.txt"):
    """Save the simulation results to a text file."""
    try:
        with open(filename, 'w') as file:
            file.write("="*50 + "\n")
            file.write("DICE ROLLING SIMULATION RESULTS\n")
            file.write("="*50 + "\n")
            file.write(f"Total rolls: {num_rolls:,}\n")
            file.write("-"*50 + "\n")
            file.write(f"{'Sum':<6} {'Frequency':<12} {'Percentage':<12}\n")
            file.write("-"*50 + "\n")

            for dice_sum in sorted(frequency.keys()):
                count = frequency[dice_sum]
                percentage = (count / num_rolls) * 100 if num_rolls > 0 else 0
                file.write(f"{dice_sum:<6} {count:<12,} {percentage:>8.2f}%\n")

            file.write("="*50 + "\n")

        print(f"\nResults saved to '{filename}'")

    except Exception as e:
        print(f"Error saving to file: {e}")


def main():
    """Main program function."""

    print("🎲 DICE ROLLING SIMULATOR 🎲")
    print("="*40)

    while True:
        try:
            # Get number of rolls from user
            num_rolls_input = input(
                "\nHow many times would you like to roll the dice? (Enter 'q' to quit): ")

            if num_rolls_input.lower() == 'q':
                print("\nThanks for using the Dice Rolling Simulator! Goodbye! 🎲")
                break

            num_rolls = int(num_rolls_input)

            if num_rolls <= 0:
                print("Please enter a positive number!")
                continue

            if num_rolls > 1000000:
                confirm = input(
                    f"Warning: {num_rolls:,} rolls might take a while. Continue? (y/n): ")
                if confirm.lower() != 'y':
                    continue

            # Run the simulation
            print(f"\nRolling two dice {num_rolls:,} times...")

            frequency = simulate_dice_rolls(num_rolls)

            # Display results
            display_results(frequency, num_rolls)

            # Show theoretical probabilities for comparison
            if num_rolls >= 100:
                display_probability_table()

            # Ask about visualization
            if num_rolls >= 10:
                viz_choice = input(
                    "\nWould you like to see a visualization? (y/n): ")
                if viz_choice.lower() == 'y':
                    visualize_results(frequency, num_rolls)

            # Ask about saving results
            save_choice = input(
                "\nWould you like to save the results to a file? (y/n): ")
            if save_choice.lower() == 'y':
                filename = input(
                    "Enter filename (default: dice_results.txt): ").strip()
                if not filename:
                    filename = "dice_results.txt"
                save_results_to_file(frequency, num_rolls, filename)

            # Ask if user wants to run another simulation
            again = input(
                "\nWould you like to run another simulation? (y/n): ")
            if again.lower() != 'y':
                print("\nThanks! It was funny!")
                break

        except ValueError:
            print("Please enter a valid number!")
        except KeyboardInterrupt:
            print("\n\nSimulation interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


def run_quick_example():
    """Run a quick example without user input for demonstration."""
    print("Quick Example: Rolling two dice 1000 times")
    print("-" * 40)

    frequency = simulate_dice_rolls(1000)
    display_results(frequency, 1000)

    # Show individual dice rolls for first 10 rolls
    print("\nFirst 10 rolls (die1 + die2 = sum):")
    print("-" * 40)
    for i in range(10):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"Roll {i+1}: {die1} + {die2} = {die1 + die2}")


# Run the program
if __name__ == "__main__":
    # Uncomment one of the following lines:

    # Run the full interactive program:
    main()

    # Or run a quick example:
    # run_quick_example()
