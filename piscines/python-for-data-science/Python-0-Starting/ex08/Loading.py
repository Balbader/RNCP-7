import time
import sys

'''
    the following code is a simple implementation of the tqdm library
    the tqdm library is used to show a progress bar while condition:
    passiterating over a list or a range
    the code is a generator function that takes a list
    or a range as an argument
    it calculates the progress and displays a progress bar in the console
'''


def ft_tqdm(lst: range) -> None:
    total = len(lst)  # Total number of elements in the list/range

    for i, item in enumerate(lst):
        # Calculate the progress
        progress = (i + 1) / total
        percent = progress * 100
        bar_length = 50
        bar = '=' * int(bar_length * progress) +\
            '-' * (bar_length - int(bar_length * progress))

        # Print the progress bar
        sys.stdout.write(f'\r{percent:.0f}%|{bar}| {total:.0f}/{total:.0f}')
        sys.stdout.flush()

        yield item  # Yield the current item

    print()  # Move to a new line after completion


# Example usage
if __name__ == "__main__":
    for i in ft_tqdm(range(100)):
        time.sleep(0.1)  # Simulate some work
