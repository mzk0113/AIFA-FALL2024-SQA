import random
import string

# Example methods to fuzz
def method_one(input_data):
    # Example implementation: simply returns the input
    return input_data

def method_two(input_data):
    # Example implementation: raises an exception for a specific input
    if input_data == "error":
        raise ValueError("Intentional error for testing")
    return input_data

def method_three(input_data):
    # Example implementation: processes input as an integer
    return int(input_data)

def method_four(input_data):
    # Example implementation: raises an exception for input length
    if len(input_data) > 5:
        raise IndexError("Input too long")
    return input_data

def method_five(input_data):
    # Example implementation: raises an exception for empty input
    if not input_data:
        raise AssertionError("Empty input not allowed")
    return input_data

def generate_random_input(size=10):
    """Generate a random string of fixed size."""
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=size))

def fuzz_method(method):
    """Fuzz a given method with random inputs."""
    for _ in range(100):  # Number of fuzzing iterations
        input_data = generate_random_input()
        try:
            method(input_data)
        except Exception as e:
            print(f"Bug found in {method.__name__} with input '{input_data}': {e}")

if __name__ == "__main__":
    methods_to_fuzz = [method_one, method_two, method_three, method_four, method_five]
    for method in methods_to_fuzz:
        print(f"Fuzzing {method.__name__}...")
        fuzz_method(method)