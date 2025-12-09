#!/usr/bin/env python3

import subprocess
import sys

def run_code(input_data):
    """Run the code with given input and return output"""
    try:
        result = subprocess.run([sys.executable, 'Škola-hodiny/zenit/krajske/sutaz/3.py'], 
                               input=input_data, 
                               capture_output=True, 
                               text=True, 
                               timeout=5)
        return result.stdout.strip()
    except Exception as e:
        return str(e)

# Test cases from the task
print("Test 1: Input '4 20'")
output1 = run_code("4 20")
print(f"Output: '{output1}'")
print(f"Expected: '5.00000000' (or similar)")
print()

print("Test 2: Input '102 39'")
output2 = run_code("102 39")
print(f"Output: '{output2}'")
print(f"Expected: '167.213114754' (or similar)")
print()

# Edge cases
print("Test 3: Edge case '0 100' (n=0, k=100)")
output3 = run_code("0 100")
print(f"Output: '{output3}'")
print(f"Expected: Should be any number (multiple solutions exist)")
print(f"Bug: Code outputs -1, but should output a number (e.g., 0)")
print()

print("Test 4: Edge case '5 100' (n>0, k=100)")
output4 = run_code("5 100")
print(f"Output: '{output4}'")
print(f"Expected: '-1' (no solution)")
print()

print("Test 5: Edge case '0 0' (n=0, k=0)")
output5 = run_code("0 0")
print(f"Output: '{output5}'")
print(f"Expected: '0.00000000' (or similar)")
print()

print("Test 6: Edge case '100 0' (n=100, k=0)")
output6 = run_code("100 0")
print(f"Output: '{output6}'")
print(f"Expected: '100.00000000' (or similar)")
