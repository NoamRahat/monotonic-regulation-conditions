#######################################################################################
# Usage                                                                               # 
# Replace: Replace the dictionary f with your actual 18 conditions.                   #
# Run: Run the script using Python.                                                   #
# Capture Output: Save the output to a file if needed using command-line redirection. #
# Example: python monotonicity_check.py > output.txt                                  #
#######################################################################################

def is_monotonic(f):
    """
    Checks if the given Boolean function f is monotonic.
    The function f should be provided as a dictionary with keys as binary strings.
    """
    keys = sorted(f.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if is_less_than(keys[i], keys[j]) and f[keys[i]] > f[keys[j]]:
                return False
    return True

def is_less_than(a, b):
    """
    Returns True if binary string a is less than binary string b in the Boolean lattice.
    """
    for k in range(len(a)):
        if a[k] > b[k]:
            return False
    return True

# Example with 18 conditions (replace these with your actual conditions)
f = {
    '000000': 0,
    '000001': 0,
    '000010': 0,
    '000011': 1,
    '000100': 0,
    '000101': 1,
    '000110': 1,
    '000111': 1,
    '001000': 0,
    '001001': 0,
    '001010': 1,
    '001011': 1,
    '001100': 1,
    '001101': 1,
    '001110': 1,
    '001111': 1,
    '010000': 0,
    '010001': 0,
    # Add all 18 rows here
}

print(is_monotonic(f))
