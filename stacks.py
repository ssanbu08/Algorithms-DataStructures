class FixedCapacityStack:
    """Implementation of FixedCapacityStack."""

    def __init__(self, capacity):
        """Initialize the stack."""
        self.stack = [None] * capacity
        self.N = 0

    def push(self, item):
        """Push an item into stack.
           N - Index position of the list for adding an item
           Increment the index s
        """
        self.stack[self.N] = item
        self.N += 1

    def pop(self):
        """Pop an item from stack."""
        if self.is_empty():
            return None
        else:
            item = self.stack[self.N - 1]
            self.stack[self.N - 1] = None
            self.N -= 1
            return item

    def is_empty(self):
        """Check if the stack is empty."""
        if self.N == 0:
            return True
        else: 
            return False

    def size(self):
        """Check the size of stack at any point of time."""
        return self.N


def balanced_parenthesis():
    """Main Function"""
    capacity = 100
    input_string = '( ( ) ) ( ) ( ) ( ( ( ) ) )'
    input_string = input_string.split()
    fixed_stack = FixedCapacityStack(capacity)
    for item in input_string:
        if item == '(':
            fixed_stack.push(item)
        else:
            result = fixed_stack.pop()
            if result is None:
                break

    if fixed_stack.is_empty():
        print('The string is perfectly balanced')
    else:
        print('The string is not perfectly balanced ')


def first_offending_parenthesis():
    """Identify the index of first offending parenthesis.
       When the input string of parenthesis is not properly nested 
       and balanced,find the position of the first symbol that is 
       not balanced.

       Logic:
            Insert the index of string into the stack instead of the actual symbol.

    """
    capacity = 100
    sample_input = ['( ( ) ) ( ) ( ) ( ( ( ) ) )', ') ( ) )', '( ( ) (', '( ) ( ) ( (']
    sample_input = [sample.split() for sample in sample_input]
    

    for sample in sample_input:
        print("Evaluating Sample", sample)
        fixed_stack = FixedCapacityStack(capacity)
        for ix, item in enumerate(sample):
            
            if item == '(':
                fixed_stack.push(ix)
            else:
                result = fixed_stack.pop()
                if result is None:
                    # Edge case when the first symbol itself 
                    # is the offending symbol
                    print('First offending string position', result)
                    break
        if fixed_stack.is_empty():
            print('The string is perfectly balanced')
        else:
            print('The string is not perfectly balanced ')
            result_pos = fixed_stack.stack[0]
            print('First offending string position', result_pos)
    

if __name__ == '__main__':
    #balanced_parenthesis()
    first_offending_parenthesis()