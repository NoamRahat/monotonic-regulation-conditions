# Boolean Function Monotonicity Checker

This repository contains a Python script to check the monotonicity of a given Boolean function.
The program reads the predefined conditions from the table, ensuring the 18 rows correspond to the regulation conditions that satisfy the monotonic requirement, considering the presence or absence of activators/inhibitors.

### Program Logic:
- Read the table data.
- Implement the logic to check monotonic regulation conditions.
- Output the conditions that satisfy the monotonic requirement.

#### Explanation of How the Monotonicity Checker Program Works

The program is designed to check if a given Boolean function is monotonic. A Boolean function is monotonic if, for any pair of input vectors `a` and `b`, whenever `a <= b`, the function value at `a` is less than or equal to the function value at `b`. Here's a breakdown of how the program accomplishes this:

##### 1. **Boolean Function Representation**:
The Boolean function is represented as a dictionary where the keys are binary strings (input vectors) and the values are the function outputs (0 or 1).

##### 2. **Monotonicity Check**:
- The `is_monotonic` function takes the Boolean function dictionary `f` as input.
- It sorts the keys of the dictionary to ensure consistent order for comparison.
- For each pair of keys `a` and b` in the dictionary, it checks if ` a <= b ` using the `is_less_than` function.
- If ` a <= b ` but the function value at `a` is greater than the function value at `b`, the function is not monotonic, and the program returns `False`.
- If all pairs satisfy the monotonicity condition, the program returns `True`.

##### 3. **Comparison Function**:
- The `is_less_than` function compares two binary strings `a` and `b`.
- It returns `True` if, for each corresponding bit, the bit in `a` is less than or equal to the bit in `b`.

##### 4. **Example Conditions**:
- The dictionary `f` is filled with binary strings as keys and their corresponding function outputs (0 or 1).
- You can replace the example conditions with your actual 18 conditions.

##### 5. **Program Execution**:
- The program prints `True` if the Boolean function is monotonic and `False` otherwise.
- You can save the output to a file using command-line redirection.

## Files

- `monotonicity_check.py`: The Python script to check monotonicity.
- `output.txt`: The output of the script.

## Usage

1. **Replace**: Replace the dictionary `f` with your actual 18 conditions.
2. **Run**: Run the script using Python.
3. **Capture Output**: Save the output to a file if needed using command-line redirection.

Run the script with the command:

```bash
python monotonicity_check.py
