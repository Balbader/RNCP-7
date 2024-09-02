import time
import sys


def ft_tqdm(lst: range) -> None:
    total = len(lst)  # Total number of elements in the list/range
    start_time = time.time()  # Record the start time

    for i, item in enumerate(lst):
        # Calculate the progress
        elapsed_time = time.time() - start_time
        progress = (i + 1) / total
        percent = progress * 100
        bar_length = 50
        bar = '=' * int(bar_length * progress) + '-' * (bar_length - int(bar_length * progress))

        # Print the progress bar
        sys.stdout.write(f'\r{percent:.2f}%|{bar}|Elapsed Time: {elapsed_time:.2f}s')
        sys.stdout.flush()

        yield item  # Yield the current item

    print()  # Move to a new line after completion


# Example usage
if __name__ == "__main__":
    for i in ft_tqdm(range(100)):
        time.sleep(0.1)  # Simulate some work
