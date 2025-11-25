def perform_operation(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return 'Not Divisible by zero'
            else:
                return num1 / num2

print(perform_operation(4, 2, '/'))