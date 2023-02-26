import threading

def reverse_string(input_str):
    reversed_str = input_str[::-1]
    print("Reversed string:", reversed_str)

input_str = input("Enter a string: ")

thread = threading.Thread(target=reverse_string, args=(input_str,))
thread.start()

# Wait for the thread to complete before exiting the program
thread.join()
