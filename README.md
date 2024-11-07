# IntervalMerger

## Overview

`IntervalMerger` is a Python program that merges overlapping intervals entered by the user. This tool reads intervals from user input, processes them to merge any overlapping ranges, and outputs the final list of non-overlapping intervals. It’s useful for scenarios where data includes ranges that need consolidation.

## Features

- **Interactive User Input**: Enter intervals in a straightforward, space-separated format.
- **Automatic Merging**: Detects and merges overlapping intervals.
- **Easy-to-Read Output**: Returns a list of consolidated intervals, ready for further use or display.

## Getting Started

### Prerequisites

- **Python 3.x** is required to run this program.

### Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/mahditalaldev/IntervalMerger.git
    cd IntervalMerger
    ```
   
2. Open a terminal or command prompt in the project directory.

### Usage

1. Run the program:
    ```bash
    python interval_merger.py
    ```

2. Follow the prompts to enter the intervals:
    ```
    How many intervals would you like to enter? 3
    Enter an interval (start and end) separated by a space: 1 3
    Enter an interval (start and end) separated by a space: 2 4
    Enter an interval (start and end) separated by a space: 6 8
    ```

3. The program will output the merged intervals:
    ```
    Merged Intervals: [[1, 4], [6, 8]]
    ```

### Example Code

The following code snippet demonstrates how the `merge_intervals()` function works with hardcoded data:

```python
from interval_merger import merge_intervals

intervals = [[1, 3], [2, 4], [6, 8]]
merged_intervals = merge_intervals(intervals)
print("Merged Intervals:", merged_intervals)  # Output: [[1, 4], [6, 8]]
```

### Functions

- **`read_intervals_from_user()`**: Reads and returns a list of intervals provided by the user.
- **`merge_intervals(intervals)`**: Merges overlapping intervals within a list and returns the merged list.

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
