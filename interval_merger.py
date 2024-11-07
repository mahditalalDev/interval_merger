"""
Function: merge_intervals(intervals)
Description:
This function takes a list of intervals (each interval represented as a list with a start and end).
For example, intervals = [[1, 3], [2, 4], [6, 8]].
The function merges overlapping intervals and returns a list of the merged intervals.
Example:
Given the input intervals = [[1, 3], [2, 4], [6, 8]], the function should return [[1, 4], [6, 8]].
Merge Rules:
Two intervals overlap if the start of one interval is less than the end of another,
and the end of the first interval is greater than the start of the second.
This function reads a list of intervals from user input and merges overlapping ones.
Note: No input validation is not performed.

"""