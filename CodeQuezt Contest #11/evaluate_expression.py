import re

def evaluate_expression(expr):
    def evaluate(expr):
        # Check for a number
        if expr.isdigit():
            return int(expr)
        
        # Find the innermost function call using regex
        match = re.search(r'(\w+)\(([^()]*)\)', expr)
        while match:
            func = match.group(1)
            args = match.group(2)
            arg_list = args.split(',')
            arg_values = [evaluate(arg.strip()) for arg in arg_list]
            
            # Evaluate the function call
            if func == 'add':
                result = arg_values[0] + arg_values[1]
            elif func == 'sub':
                result = arg_values[0] - arg_values[1]
            elif func == 'mul':
                result = arg_values[0] * arg_values[1]
            elif func == 'div':
                result = arg_values[0] // arg_values[1]
            
            # Replace the evaluated function call with the result in the expression
            expr = expr[:match.start()] + str(result) + expr[match.end():]
            
            # Find the next innermost function call
            match = re.search(r'(\w+)\(([^()]*)\)', expr)
        
        return int(expr)
    
    return evaluate(expr)

# Sample Input
expr = "add(2, mul(3, 4))"
print(evaluate_expression(expr))  # Output: 14
