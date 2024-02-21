import traceback

def check_assignment(student_code, test_cases):
    """
    Function to check a programming assignment.
    Returns a list of tuples (test_case, result), where result is True if the output matches the expected output, False otherwise.
    """
    results = []
    for test_input, expected_output in test_cases:
        try:
            # Execute student's code with test input
            exec(student_code)
            student_output = eval(test_input)
            result = student_output == expected_output
            results.append((test_input, result, expected_output, student_output))
        except Exception as e:
            # If an exception occurs during execution, consider it as incorrect
            results.append((test_input, False, expected_output, None))
            print(f"Error occurred for test case {test_input}: {e}")
            traceback.print_exc()
    return results

# Example usage:
test_cases = [
    ("2 + 2", 4),
    ("3 * 5", 15),
    ("'hello'", "hello"),
    ("10 / 2", 5),
    ("1 / 0", ZeroDivisionError),  # Intentionally causing an error
]

loop_test_cases = [
    ("0", 0),   # Expecting 0 as the first value of the loop variable
    ("9", 9),   # Expecting 9 as the last value of the loop variable
]

student_code = """
# Student's code goes here
for i in range(10):
    print(i)
"""

results = check_assignment(student_code, test_cases)

print("Programming assignment results:")
for idx, (test_input, result, expected_output, student_output) in enumerate(results, start=1):
    print(f"Test Case {idx}: {test_input} => {'Pass' if result else 'Fail'}")
    if not result:
        print(f"    Expected Output: {expected_output}")
        if student_output is not None:
            print(f"    Your Output: {student_output}")

loop_results = check_assignment(student_code, loop_test_cases)

print("Loop-related test results:")
for idx, (test_input, result, expected_output, student_output) in enumerate(loop_results, start=1):
    print(f"Test Case {idx}: {test_input} => {'Pass' if result else 'Fail'}")
    if not result:
        print(f"    Expected Output: {expected_output}")
        if student_output is not None:
            print(f"    Your Output: {student_output}")
