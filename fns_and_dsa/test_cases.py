import unittest

def square_of_number(number):
    return number ** 2

# print(area_of_number(5))

class testAddFunction(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(square_of_number(5), 25)


if __name__ == '__main__':
    unittest.main()