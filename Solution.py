def process_list(input_list):
    # Check for empty list
    if not input_list:
        return "Error: The input list is empty."
    
    # Process the list (example processing)
    result = []
    for item in input_list:
        if item:  # Ignore empty lines
            result.append(item)  
    return result

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return process_list(lines)
    except FileNotFoundError:
        return "Error: The specified file was not found."

# Example Usage
if __name__ == "__main__":
    print(read_file('input.txt'))
  
