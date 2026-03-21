def is_safe(levels):
    # Calculate differences between adjacent levels
    diffs = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    
    # Check if all differences are within [1, 3] or [-3, -1]
    all_increasing = all(1 <= d <= 3 for d in diffs)
    all_decreasing = all(-3 <= d <= -1 for d in diffs)
    
    return all_increasing or all_decreasing

def solve():
    # Load your input data
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    part1_safe_count = 0
    part2_safe_count = 0

    for line in lines:
        levels = list(map(int, line.split()))
        
        # Part 1: Check if the report is safe as-is
        if is_safe(levels):
            part1_safe_count += 1
            part2_safe_count += 1
        else:
            # Part 2: Check if removing one element makes it safe
            is_dampener_safe = False
            for i in range(len(levels)):
                # Create a new list without the element at index i
                modified_levels = levels[:i] + levels[i+1:]
                if is_safe(modified_levels):
                    is_dampener_safe = True
                    break
            
            if is_dampener_safe:
                part2_safe_count += 1

    print(f"Part 1 Safe Reports: {part1_safe_count}")
    print(f"Part 2 Safe Reports: {part2_safe_count}")

if __name__ == "__main__":
    solve()
