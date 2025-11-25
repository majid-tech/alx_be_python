def perform_operation(num1, num2, operation = ['add', 'subtract', 'multiply', 'divide']):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return 'Not Divisible by zero'
            else:
                return num1 / num2

print(perform_operation(4, 2, 'subtract'))