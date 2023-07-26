def adding_even_numbers():
    total = 0
    
    for number in range(2, 101, 2):
        total += number
        
    print(f"Answer: {total}")
    

def add_even_numbers_diff_solution():
    new_total = 0
    
    for number in range(1, 100):
        if number % 2 == 0:
            new_total += number
            
    print(f"Answer: {new_total}")