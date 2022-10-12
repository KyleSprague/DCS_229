from code_base.String import *
import pytest
import random
import string

###############################################################################

class print_test:
    ''' Class to be used in streamlining prints of each test in "test_..."
        pytest testing functions below.  Because this class only provides
        an __init__ method, it can be used as though it was simply a
        function call, e.g.,
            print_test('String("")._chars', ...)
        Because this is a class, each call to print_test can therefore track
        the total number of calls/tests to be displayed in the printing.

        Usage syntax:

            print_test([string representing the call being tested], \
                       result =   [result of the call being tested], \
                       expected = [expected result of the call teing tested])
 
        Usage example:
            print_test('String("")._chars', 
                       result   = String("")._chars, 
                       expected = [])

    '''    

    test_number = 0  # class-level (static) variable to track number of tests

    def __init__(self, what_test: str, *args: list, **kwargs: dict):
        ''' Defining print_test as a class with __init__ will allow the user
            call print_test like a funtion, when they're actually constructing
            a print_test object (but allows us to track the total number of
            tests).

        Parameters:
            what_test: str representation of what is being tested, e.g., of the
                form 'String("")._chars' when testing the contents of an
                instance variable _chars inside a newly created String object
            kwargs['result']: type varies (typically String or str or list or None).
                The actual result of the test being conducted.  For example, this
                would be [] for a correct implementation of String("")._chars.
            kwargs['expected']: type varies (typically String or str or list or None)
                The expected result of the test being conducted. For example, this
                should be [] when testing String("")._chars.

        Returns:
            None -- this is an __init__ method
        '''

        # grab the required keyword arguments
        result   = kwargs['result']
        expected = kwargs['expected']

        # some setup for printing the test info below
        prefix = f'Test {print_test.test_number}: '
        # fish out the class name, which whould be String in this context,
        # and the argument to the String construction
        open1_idx  = what_test.index('(')
        close1_idx = what_test.index(')', open1_idx)
        class_name = what_test[0:open1_idx]
        argument1  = what_test[open1_idx + 2 : close1_idx - 1]  # account for quotes
        # create a string with string-indices for displaying 
        indices = "".join(str(i % 10) for i in range(len(argument1))) #HELPPPPPP!!!!

        argument2 = None; padding = ""
        # check whether String("...") appears twice for adding second arg's indices
        if class_name in what_test[close1_idx:]:
            open2_idx    = what_test.index('(', close1_idx)
            close2_idx   = what_test.index(')', open2_idx)
            argument2    = what_test[open2_idx + 2 : close2_idx - 1]  # account for quotes
            arg2_indices = "".join(str(i % 10) for i in range(len(argument2)))
            padding      = ' ' * (open2_idx - close1_idx + 1 + 2)     # account for quotes

        # indentation (accounting for # of tests) used in printing below
        indent = '    ' + (' ' * len(str(print_test.test_number)))

        # print the test info, a la 'Test 0: String("")._chars';
        # print indices below whenever the argument is not the empty string
        print(f'\n\n{prefix}{what_test}')
        if argument2 is None:
            if len(argument1) > 0:
                print(f'{indent}# indices: {indices} (length:{len(argument1)})')
        else:
            if len(argument1) > 0 or len(argument2) > 0:
                print(f'{indent}# indices: {indices}{padding}{arg2_indices}')

        try:
            if isinstance(result, String): result = result.__str__()
            assert(type(result) == type(expected))
        except:
            # if the provided result and expected mismatch in type,
            # let the user know...
            print(f"ERROR: mismatched list type in print_test's " + \
                  f"test #{print_test.test_number}:")
            print(f"\t result type: {type(result)}  expected type: {type(expected)}")
        else:
            if isinstance(expected, list):
                # remove spaces from between list items for compact printing
                print(f'{indent}Result:   {str(result).replace(", ", ",")}')
                print(f'{indent}Expected: {str(expected).replace(", ", ",")}')
            elif isinstance(expected, str):
                # include quotes when output is type str
                print(f'{indent}Result:   "{result}"')
                print(f'{indent}Expected: "{expected}"')
            else:
                print(f'{indent}Result:   {result}')
                print(f'{indent}Expected: {expected}')

        print_test.test_number += 1  # increment the static test count

###############################################################################

@pytest.fixture
def empty_string() -> str: 
    ''' pytest fixture to return an empty string

     Returns:
         empty string
    '''
    return ""

@pytest.fixture
def empty_list() -> list: 
    ''' pytest fixture to return an empty list

     Returns:
         empty list
    '''
    return []

@pytest.fixture
def characters() -> str:
    ''' pytest fixture to provide a list of characters for generating random strings

     Returns:
         a string of characters consisting of letters, digits, and punctuation,
             but with parentheses and quotes removed (to make output comparison  
             easier in printed output)
    '''
    return string.digits + string.ascii_letters + \
           "!#$%&*+,-./:;<=>?@[\\]^_`{|}~"

@pytest.fixture
def random_string(characters: pytest.fixture) -> str: 
    ''' pytest fixture to generate a random string between length 2 and 20

    Parameters
        characters:  pytest fixture (above) for generating a random character string

    Returns:
        an str consisting of randomly-selected characters
    '''
    length = random.randint(2,20)
    return "".join(random.choice(characters) for i in range(length))

@pytest.fixture
def different_random_string(characters: pytest.fixture) -> str: 
    ''' pytest fixture to generate a different random string between length 2 and 20
        (e.g., for using random_string and different_random_string as argument to
        the same subsequent fixture)

        see RonnyPfannschmidt 1 Oct 2019 comment here:
        https://github.com/pytest-dev/pytest/issues/5896

    Parameters:
        characters:  pytest fixture (above) for generating a random character string

    Returns:
        an str consisting of randomly-selected characters
    '''
    length = random.randint(2,20)
    return "".join(random.choice(characters) for i in range(length)) 


@pytest.fixture 
def random_string_length_one(characters: pytest.fixture) -> str: 
    '''
        Pytest fixture to generate string with random character of length one 

        Parameters: 
            pytest fixture (above) for generating a random character string 

        Returns: 
            an str of length one with randomly selected characters 
    
    '''
    length = 1
    return "".join(random.choice(characters) for i in range(length))  



# NOTE: you may want/need to define more fixtures (e.g., for length-one
#   strings?).

###############################################################################

# individual pytest unit tests below

def test_empty_constructor(empty_string: pytest.fixture) -> None:
    ''' pytest test for String construction of an empty string 
        (1) stores the actual result of the construction, grabbing internal list
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(empty_string)._chars
    expected = []
    print_test(f'String("{empty_string}")._chars', \
               result = result, expected = expected)
    assert(result == expected)

def test_basic_constructor(random_string: pytest.fixture) -> None:
    ''' pytest test for String construction of a random string 
        (1) stores the actual result of the construction, grabbing internal list
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(random_string)._chars
    expected = [c for c in random_string]
    print_test(f'String("{random_string}")._chars', \
               result = result, expected = expected)
    assert(result == expected) 
    

##############################################################################
##############################################################################

# plenty more tests go here... 

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ STR TESTS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def test_str_method_on_random_string(random_string: pytest.fixture) -> None:  
    '''
        Pytest test for random string of type String given to str function. 
        (1). stores the str version of the constructed random string String object
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest
    
    '''
    result = (String(random_string)).__str__()
    expected = random_string  
    print_test(f'str(String{random_string})', 
                result  = result, 
                expected = expected) 
    assert (result == expected) 

def test_str_method_on_empty_string_(empty_string: pytest.fixture) -> None:   
    ''' 
        Pytest for empty string of type String inputed to str function 
        (1). stores str version of the given String object
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest
      
    '''
    result = (String(empty_string)).__str__()
    expected = empty_string 
    print_test(f'str(String{empty_string})', 
                result = result, 
                expected = expected) 
    assert (result == expected)   

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ LEN TESTS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 

def test_len_on_empty_string_(empty_string: pytest.fixture) -> None: 
    '''
        Pytest for len method with empty string argument 

        (1). stores the integer corresponding to the length of the String object
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  

    '''   

    result = (String(empty_string)).len()
    expected = 0
    print_test(f'(String{empty_string})._len()', 
                result = result, 
                expected = expected) 
    assert (result == expected)   

def test_len_on_random_length_string_(random_string: pytest.fixture) -> None: 
    '''
        Pytest for len method with random string argument 

        (1). stores the integer corresponding to the length of the String object
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  

    ''' 
    result = (String(random_string)).len()
    expected = len(random_string)
    print_test(f'(String{random_string})._len()', 
                result = result, 
                expected = expected) 
    assert (result == expected)  

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ IS_EMPTY TESTS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def test_is_empty_on_empty_string(empty_string: pytest.fixture) -> None: 
   
    '''
        Pytest for is_empty method on empty string

        (1). stores the Boolean result of the method for the empty_string String object
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  
    
    result = String(empty_string).is_empty() 
    expected = True  
    print_test(f'(String({empty_string})).is_empty()', 
                result = result, 
                expected = expected) 
    assert (result == expected) 

def test_is_empty_on_random_length_string(random_string: pytest.fixture) -> None: 

    '''
        Pytest for is_empty method on random string

        (1). stores the Boolean result of the method for the random_string String object
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''    

    result = (String(random_string)).is_empty() 
    expected = False  
    print_test(f'(String({random_string})).is_empty()', 
                result = result, 
                expected = expected) 
    assert (result == expected)   


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ EQ TESTS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 

##comparing String and str where both are empty 

def test_eq_on_empty_String_and_empty_str(empty_string: pytest.fixture) -> None: 

    '''
        Pytest for eq method on an empty String object and str object

        (1). stores the Boolean result of the method for the empty String and str
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    arg_one = String(empty_string) 
    arg_two = (String(empty_string)).__str__() 
    result = arg_one.__eq__(arg_two) 
    expected = True 
    print_test(f'(arg_one({empty_string})).__eq__({empty_string}) for String and str', 
                result = result, 
                expected = expected) 
    assert (result == expected) 


##comparing String and String where both are empty  

def test_eq_on_empty_String_and_empty_String(empty_string: pytest.fixture) -> None: 

    '''
        Pytest for eq method on an empty String object and String object

        (1). stores the Boolean result of the method for the empty String and String
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    arg_one = String(empty_string)
    arg_two = String(empty_string)
    result = arg_one.__eq__(arg_two) 
    expected = True 
    print_test(f'(arg_one({empty_string})).__eq__({empty_string}) for String and String', 
                result = result, 
                expected = expected) 
    assert (result == expected) 

##comparing String and str where both are random_string 

def test_eq_on_random_String_and_random_str(random_string: pytest.fixture) -> None: 

    '''
        Pytest for eq method on an random String object and str object

        (1). stores the Boolean result of the method for the random String and str
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    arg_one = String(random_string)
    arg_two = String(random_string).__str__()
    result = arg_one.__eq__(arg_two) 
    expected = True 
    print_test(f'(arg_one({random_string})).__eq__({random_string}) for String and str', 
                result = result, 
                expected = expected) 
    assert (result == expected) 



##Comparing String and String where both are random_string  

def test_eq_on_random_String_and_random_String(random_string: pytest.fixture) -> None: 

    '''
        Pytest for eq method on an random String object and String object

        (1). stores the Boolean result of the method for two random String objects
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    arg_one = String(random_string)
    arg_two = String(random_string)
    result = arg_one.__eq__(arg_two) 
    expected = True 
    print_test(f'(arg_one({random_string})).__eq__({random_string}) for String and String', 
                result = result, 
                expected = expected) 
    assert (result == expected) 

##Comparing  String and String where one is random_string and one is different_random_string  

def test_eq_on_random_String_and_different_random_String(random_string: pytest.fixture, different_random_string: pytest.fixture) -> None: 

    '''
        Pytest for eq method on an random String object and different random String object

        (1). stores the Boolean result of the method for a random String object and different Random String object
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    arg_one = String(random_string)
    arg_two = String(different_random_string)
    result = arg_one.__eq__(arg_two) 
    expected = False 
    print_test(f'(arg_one({random_string})).__eq__({different_random_string})) for String and String', 
                result = result, 
                expected = expected) 
    assert (result == expected)  

##Comparing String and str where one is random_string and one is different random_string 

def test_eq_on_random_String_and_different_random_str(random_string: pytest.fixture, different_random_string: pytest.fixture) -> None: 

    '''
        Pytest for eq method on an random String object and different random str object

        (1). stores the Boolean result of the method for a random String object and different random str object
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    arg_one = String(random_string)
    arg_two = String(different_random_string).__str__()
    result = arg_one.__eq__(arg_two) 
    expected = False 
    print_test(f'(arg_one({random_string})).__eq__({different_random_string})) for String and str', 
                result = result, 
                expected = expected) 
    assert (result == expected) 


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ GET ITEM TESTS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#get item that is at index 1 (String of arbitrary length) 

def test_getitem_on_random_String_(random_string: pytest.fixture) -> None: 

    '''
        Pytest for __getitem__ method using random String object 

        (1). stores the correct character of the String object that is being indexed into as str
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    working_object = String(random_string)
    result = working_object[-1]
    expected = (random_string)[-1] 
    print_test(f'String({random_string})[-1]', 
                result = result, 
                expected = expected)  
    assert (result == expected) 

#get item that is at index 0 (on String object of length 1) 

def test_getitem_on_random_String_length_one(random_string_length_one: pytest.fixture) -> None: 

    '''
        Pytest for __getitem__ method using random String of length one object

        (1). stores the correct character of the String object that is being indexed into as str
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    working_object = String(random_string_length_one)
    result = working_object[0]
    expected = random_string_length_one[0]
    print_test(f'String({random_string_length_one})[0]', 
                result = result, 
                expected = expected) 
    assert (result == expected) 

#get item that is at index 49 for String object with length 0 

def test_getitem_on_another_empty_string(empty_string: pytest.fixture) -> None: 

    '''
        Pytest for __getitem__ method using empty String object

        (1). stores the correct character of the String object that is being indexed into as str
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  
    with pytest.raises(IndexError) as exception_info:
        String(empty_string)[49]             # this should raise an IndexError
    result   = type(exception_info.value)   # if correct, result should be IndexError
    expected = IndexError
    print_test(f'String("{empty_string}")[49]', \
               result = result, expected = expected)
    assert(result == expected) 

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ SET ITEM TESTS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  

#test set item by replacing an index in a random length string

def test_setitem_on_random_String_(random_string: pytest.fixture, characters: pytest.fixture) -> None: 

    '''
        Pytest for __setitem__ method using random String

        (1). stores the replacement string value and the updated string
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    expected = [c for c in random_string] 
    length = len(expected)
    
    random_index = random.randint(0, length)
    random_char = random.choice(characters) 

    #result = String(random_string)._chars)[random_index] = random_char 

    my_string = String(random_string)
    my_string[random_index] = random_char
    result = my_string._chars[random_index]
    expected = random_char 

    print_test(f'String({random_string})[{random_index}] = \'{random_char}\'', 
                result = result, 
                expected = expected) 
    assert (result == expected) 

#test set item by replacing index in string of length 1  

def test_setitem_on_length_one_random_String_(random_string_length_one: pytest.fixture, characters: pytest.fixture) -> None: 

    '''
        Pytest for __setitem__ method using random length one string

        (1). stores the replacement string value and the updated string
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    expected = [c for c in random_string_length_one] 
    
    index_val = 0
    random_char = random.choice(characters) 

    #result = String(random_string)._chars)[random_index] = random_char 

    my_string = String(random_string_length_one)
    my_string[index_val] = random_char
    result = my_string._chars[index_val]
    expected = random_char 

    print_test(f'String({random_string_length_one})[0] = \'{random_char}\'', 
                result = result, 
                expected = expected) 
    assert (result == expected) 


#test set item by changing index at invalid index (e.g. 5000)

def test_setitem_invalid_index_on_length_one_random_String_(random_string_length_one: pytest.fixture, characters: pytest.fixture) -> None: 

    '''
        Pytest for __setitem__ method using random length one string and index 500

        (1). stores the replacement string value and the updated string
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    
    index_val = 500
    random_char = random.choice(characters) 

    #result = String(random_string)._chars)[random_index] = random_char  

    with pytest.raises(IndexError) as exception_info:
        my_string = String(random_string_length_one) 
        my_string[index_val] = random_char #raises index error
    
    result = type(exception_info.value)  #if correct, is an index error
    expected = IndexError

    print_test(f'String({random_string_length_one})[500] = \'{random_char}\'', 
                result = result, 
                expected = expected) 
    assert (result == expected) 

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ADD TESTS ############################################# 

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ SUBSTR @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   

#take a random substring from a random String

def test_substring_on_String_(random_string: pytest.fixture) -> None: 

    '''
        Pytest for substring method using random length String object and random length substring

        (1). stores the result of taking a subsection of a random substring
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    length = len(random_string)  
    sub_str_start = random.randint(2,length) 
    sub_str_end = random.randint(sub_str_start, length) 

    result = (String(random_string)).substring(sub_str_start, sub_str_end)
    
    expected = [c for c in random_string]
    expected = expected[sub_str_start: sub_str_end]

    print_test(f'String({random_string})[{sub_str_start}:{sub_str_end}] = \'{expected}\'', 
                result = result, 
                expected = expected) 
    assert (result == expected) 

#raise index error if accessing into list with length 0 with any start or stop > 0  

def test_substring_on__empty_String_w_bad_indexing_(empty_string: pytest.fixture) -> None: 

    '''
        Pytest for substring method using empty string and indeces larger than zero

        (1). stores the replacement result of taking a subsection of an empty String
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    sub_str_start = 0
    sub_str_end = 55 

    result = (String(empty_string)).substring(sub_str_start, sub_str_end)
    
    expected = []

    print_test(f'String({empty_string})[{sub_str_start}:{sub_str_end}] = \'{expected}\'', 
                result = result, 
                expected = expected) 
    assert (result == expected) 


#index into random String of length one with invalid indeces 

def test_substring_on_random_String_length_one_(random_string_length_one: pytest.fixture) -> None: 

    '''
        Pytest for substring method on random string of length one with invalid indeces

        (1). uses 'with pytest.raises' to look for appropriate raised exception,
            which is raised by the indented code
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    length = 1
    sub_str_start = "37"
    sub_str_end = "43"

    string = String(random_string_length_one)  # first need a construction...
    with pytest.raises(TypeError) as exception_info:
        (String(random_string_length_one)).substring(sub_str_start, sub_str_end)            # this should raise an IndexError 
    result = type(exception_info.value)
    expected = TypeError
    print_test(f'String({random_string_length_one})[{sub_str_start}:{sub_str_end}] = \'TypeError\'', 
                result = result, 
                expected = expected) 
    assert(result == expected)

#raise index error if start value is higher than stop value 

def test_substring_on_different_random_String_where_stop_greater_than_start(different_random_string: pytest.fixture) -> None:      
    '''    
        Pytest for substring method on random String where stop index higher that start index

        (1). uses 'with pytest.raises' to look for appropriate raised exception,
            which is raised by the indented code
        (2) calls print_test with string version of test, result of the actual
        test, and expected result
        (3) assert required by pytest  
    '''  

    length = len(different_random_string)  
    sub_str_end = random.randint(1, length-1)  
    sub_str_start = length

    with pytest.raises(IndexError) as exception_info:
        (String(different_random_string)).substring(sub_str_start, sub_str_end)            # this should raise an IndexError 
    result = type(exception_info.value)
    expected = IndexError
    print_test(f'String({different_random_string})[{sub_str_start}:{sub_str_end}] = \'IndexError\'', 
                result = result, 
                expected = expected) 
    assert(result == expected)




 
##############################################################################
##############################################################################

##############################################################################
# this test gives an example of how to look for accessing-element exceptions
#
def test_getitem_first_on_empty_String(empty_string: pytest.fixture) -> None:
    ''' pytest test for accessing [0] entry in an empty string
        (1) uses 'with pytest.raises' to look for appropriate raised exception,
            which is raised by the indented code
        (2) stores the type of the value of the raised exception
        (3) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    with pytest.raises(IndexError) as exception_info:
        String(empty_string)[0]             # this should raise an IndexError
    result   = type(exception_info.value)   # if correct, result should be IndexError
    expected = IndexError
    print_test(f'String("{empty_string}")[0]', \
               result = result, expected = expected)
    assert(result == expected)

##############################################################################
##############################################################################

# plenty more tests go here... 

##############################################################################
##############################################################################

##############################################################################
# this test gives an example of how to look for modifiying-element exceptions
#
def test_setitem_first_on_empty_String(empty_string: pytest.fixture) -> None:
    ''' pytest test for setting [0] entry in an empty string
        (1) uses 'with pytest.raises' to look for appropriate raised exception,
            which is raised by the indented code
        (2) stores the type of the value of the raised exception
        (3) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    string = String(empty_string)  # first need a construction...
    with pytest.raises(IndexError) as exception_info:
        string[0] = '❤'            # this should raise an IndexError
    result   = type(exception_info.value)
    expected = IndexError
    print_test(f'String("{empty_string}")[0] = \'❤\'', \
               result = result, expected = expected)
    assert(result == expected)

##############################################################################
##############################################################################

# plenty more tests go here...

##############################################################################
##############################################################################
