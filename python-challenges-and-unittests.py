# Question 1: write a function that returns all prime numbers from a given list of integers where the max value in the list cannot exceed 101
                                  
def prime_numbers(integer_list):
    
    # raise error if list is not provided
    if (type(integer_list) != list):
        raise TypeError(f'{"must provide a list"}')
    
    # raise error if list is empty
    if (integer_list == []):
        raise ValueError(f'{"list is empty"}')
    
    # raise error is list contains non-integers
    if (all([isinstance(i, int) for i in integer_list])) == False:
        raise ValueError(f'{"list contains non-integers"}')
        
    primes = []
    
    for integer in integer_list:
        # raise error if max value exceeds 101
        if (integer > 101):
            raise ValueError(f'{"max value in list must not exceed 101"}')
        
        # 1 is not a prime number
        elif integer > 1:  
            # check if integer is a prime number
            for i in range (2, integer):  
                if (integer % i) == 0:  
                    break  
            else: 
                primes.append(integer)
                
    # return prime numbers
    return primes
  
    
# unit testing
import unittest

class PrimeTests(unittest.TestCase):
    
    # error message should be raised if list is not provided
    def test_prime_list(self):
        with self.assertRaises(TypeError) as error:
            x = 10
            prime_numbers(x)
        self.assertEqual(str(error.exception), 'must provide a list')
    
    # error message should be raised if list is empty
    def test_prime_empty(self):
        with self.assertRaises(ValueError) as error:
            x = []
            prime_numbers(x)
        self.assertEqual(str(error.exception), 'list is empty')
    
    # error message should be raised if list contains non-integers
    def test_prime_integer(self):
        with self.assertRaises(ValueError) as error:
            x = ['a','b','c']
            prime_numbers(x)
        self.assertEqual(str(error.exception), 'list contains non-integers')
    
    # error message should be raised if max value in list is greater than 101
    def test_prime_max(self):
        with self.assertRaises(ValueError) as error:
            x = [5,10,150]
            prime_numbers(x)
        self.assertEqual(str(error.exception), 'max value in list must not exceed 101')
        
    # only prime numbers should be printed
    def test_prime_numbers(self):
        x = [1,2,3,4,5]
        output = prime_numbers(x)
        self.assertEqual(output, [2,3,5])
    
if __name__ == '__main__':
    unittest.main()

                    
# Question 2: write a function that takes an integer between negative one billion and positive one billion, including zero, 
# and returns the english-language equivalent

def to_word(integer, index):
    
    # assign words to numbers less than ten
    ones = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')

    # assign words to numbers between ten and nineteen
    twos = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')

    # assign words to numbers between twenty and hundred
    tens = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred')

    # assign words to suffixes
    suffixes = ('', 'Thousand', 'Million', 'Billion')
    
    # if integer is negative, remove negative sign
    integer = integer.replace("-",'')
    
    # assign word zero to zero integer
    if integer == '0':
        return 'Zero'
    
    # processing numbers less than 100
    if(len(integer) > 3):
        return False
    
    # assign leading zero to numbers less than 100
    integer = integer.zfill(3)
    words = ''
    
    first = int(integer[0])
    second = int(integer[1])
    third = int(integer[2])
    
    words += '' if integer[0] == '0' else ones[first]
    words += ' Hundred ' if not words == '' else ''
    
    if(second > 1):
        words += tens[second - 2]
        words += ' '
        words += ones[third]
    
    elif(second == 1):
        words += twos[(int(second + third) % 10) - 1]
        
    elif(second == 0):
        words += ones[third]

    if(words.endswith('Zero')):
        words = words[:-len('Zero')]
    else:
        words += ' '
     
    if(not len(words) == 0):    
        words += suffixes[index]
        
    return words
    
def get_word(integer):
    
    # raise error is non-integer is provided by user
    if (isinstance(integer, int)) == False:
        raise ValueError(f'{"must provide an integer"}')
    
    # raise error if integer is not within negative or positive one billion
    if len(str(integer)) > 11:
        raise ValueError(f'{"integer must be between negative one billion and positive one billion"}')
    
    count = len(str(integer)) // 3 if len(str(integer)) % 3 == 0 else len(str(integer)) // 3 + 1
    copy = count
    words = []
 
    for i in range(len(str(integer)) - 1, -1, -3):
        words.append(to_word(str(integer)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))
        count -= 1;

    final_word = ''
    for s in reversed(words):
        temp = s + ' '
        final_word += temp
        
    if ((integer < 0) & (len(final_word.split()) != 4 or len(final_word.split()) != 6)):
        final_word = final_word.split()
        final_word.insert(0, 'Negative')
        final_word = ' '.join(final_word)
        
    elif ((integer < 0) & (len(final_word.split()))) == 4:
        final_word = final_word.split()
        final_word.insert(0, 'Negative')
        #final_word.insert(3, 'and')
        final_word = ' '.join(final_word)
        
    elif ((integer < 0) & (len(final_word.split()))) == 6:
        final_word = final_word.split()
        final_word.insert(0, 'Negative')
        #final_word.insert(5, 'and')
        final_word = ' '.join(final_word)        

    # include necessary and's
    elif ((integer > 0) & (len(final_word.split()))) == 3:
        final_word = final_word.split()
        #final_word.insert(2, 'and')
        final_word = ' '.join(final_word)
        
    elif ((integer > 0) & (len(final_word.split()))) == 5:
        final_word = final_word.split()
        #final_word.insert(4, 'and')
        final_word = ' '.join(final_word)
        
    else: final_word
    
    return final_word.rstrip()


# unit testing
class WordTests(unittest.TestCase):
      
    # error message should be raised if user provides non-integer
    def test_get_word_integer(self):
        with self.assertRaises(ValueError) as error:
            get_word('one thousand')
        self.assertEqual(str(error.exception), 'must provide an integer')
    
    # error message should be raised if value is greater than one billion
    def test_get_word_max(self):
        with self.assertRaises(ValueError) as error:
            get_word(100000000000000000)
        self.assertEqual(str(error.exception), 'integer must be between negative one billion and positive one billion')
        
    # error message should be raised if value is less than one billion
    def test_get_word_min(self):
        with self.assertRaises(ValueError) as error:
            get_word(-100000000000000000)
        self.assertEqual(str(error.exception), 'integer must be between negative one billion and positive one billion')
        
    # the number 0 should be converted to the word 'Zero'
    def test_get_word_zero(self):
        output = get_word(0)
        self.assertEqual(output, 'Zero')
            
    # the number 1 should be converted to 'One'
    def test_get_word_one(self):
        output = get_word(1)
        self.assertEqual(output, 'One')
        
    # the number 10 should be converted to 'Ten'
    def test_get_word_ten(self):
        output = get_word(10)
        self.assertEqual(output, 'Ten')
        
    # the number 100 should be converted to 'One Hundred'
    def test_get_word_hundred(self):
        output = get_word(100)
        self.assertEqual(output, 'One Hundred')
        
    # the number 1000 should be converted to 'One Thousand'
    def test_get_word_thousand(self):
        output = get_word(1000)
        self.assertEqual(output, 'One Thousand')
        
    # the number 1000000 should be converted to 'One Million'
    def test_get_word_million(self):
        output = get_word(1000000)
        self.assertEqual(output, 'One Million')
        
    # the number 1000000000 should be converted to 'One Billion'
    def test_get_word_billion(self):
        output = get_word(1000000000)
        self.assertEqual(output, 'One Billion')
        
    # the number -1000000000 should be converted to 'Negative One Billion'
    def test_get_word_negative(self):
        output = get_word(-1000000000)
        self.assertEqual(output, 'Negative One Billion')
    
if __name__ == '__main__':
    unittest.main()


# Question 3: write a function that takes a list character sequences, removes all non-alphanumeric characters from these,
# one-hot encodes the sequences and returns the result

import re

def encode(sequence):
    
    # raise error if list is not provided
    if (type(sequence) != list):
        raise TypeError(f'{"must provide a list"}')
    
    # raise error if list is empty
    if (sequence == []):
        raise ValueError(f'{"list is empty"}')
    
    # raise error is list contains non-integers
    if (all([isinstance(i, str) for i in sequence])) == False:
        raise ValueError(f'{"list must contain character sequences"}')
    
    #sequence = re.sub(r'\W+', '', str(sequence))
    out = [re.sub(r'[^a-zA-Z0-9]','',string) for string in sequence]

    mapping = {}
    for x in range(len(out)):
      mapping[out[x]] = x
      
    return mapping


# unit testing
class EncodeTests(unittest.TestCase):
    
    # error message should be raised if list is not provided
    def test_encode_list(self):
        with self.assertRaises(TypeError) as error:
            x = 10
            encode(x)
        self.assertEqual(str(error.exception), 'must provide a list')
    
    # error message should be raised if list is empty
    def test_encode_empty(self):
        with self.assertRaises(ValueError) as error:
            x = []
            encode(x)
        self.assertEqual(str(error.exception), 'list is empty')
    
    # error message should be raised if list contains integers
    def test_encode_integer(self):
        with self.assertRaises(ValueError) as error:
            x = [1,2,3]
            encode(x)
        self.assertEqual(str(error.exception), 'list must contain character sequences')
        
    # function should remove special characters and one-hot encode sequence
    def test_encode_special(self):
        x = ['red&blue', 'red/green', 'red@orange', 'red%yellow']
        output = encode(x)
        self.assertEqual(output, {'redblue': 0, 'redgreen': 1, 'redorange': 2, 'redyellow': 3}) 
        
if __name__ == '__main__':
    unittest.main()

