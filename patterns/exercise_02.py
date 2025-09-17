# You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', 
# represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).

def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Your code here
    pattern = []
    
    if n == 1:
        return ["*"]
        
    pattern.append("*"*n) #First Row
        
    for i in range(n-2):
        p = "*" + " "*(n-2) + "*"
        pattern.append(p)
            
    pattern.append("*"*n) #Last Row
            
    return pattern


answer = generate_square(5)
print(answer)