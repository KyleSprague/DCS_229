class String:
    '''DCS 229 implementation of a version of the built-in str class. 
    
    PLEASE NOTE THAT THE COMMENTATION IS BY MY PROFESSOR Barry Lawson: blawson@bates.edu

    This class implements a simple version corresponding to the str class,
    where a String object consists of a sequence of characters.

    Attributes:
        __str__    : returns an str version of this String object
        len        : returns the (int) number of characters in this String
        is_empty   : returns True if this String is an empty string; False o/w
        __eq__     : allows comparison of this String vs. either a String or str
        __getitem__: allows fetching a character using [] notation
        __setitem__: allows overwriting a character using [] assignment
        __add__    : returns a new String object that is the concatenation of
                        this String object and a given String or str object
        substring  : returns a new String object by specifying substring indices
    '''

    ''' Notes on type hints below:
        - As the String class does not yet exist, the standard approach is
          to use 'String' which is understood by type checkers as a lookahead.
        - Python 3.10 allows "or" support a la 'String' | str.  To fake this
          support in the presence of < 3.10 versions of Python, we are using
          'String | str' here (rather than the suggested Union['String', str]
          approach) for convenience and brevity.
    '''

    __slots__ = ('_chars')

    #####################################################
    def __init__(self, string: str) -> None:
        ''' initialization method for the String class

        Parameters:
            string: an str type used to initialize the String

        Returns:
            None
        '''  
        if isinstance(string, str) == False:  
            raise TypeError("The object you pass to String must be of type str")
        else:   
            self._chars = [c for c in string]  # a list of characters in the str

    #####################################################
    def __str__(self) -> str:
        ''' overrides the __str__ special method for conversion to str
        
        Returns:
            an str version of the String object contents 

        '''
        
        string_val = self._chars  
        if string_val == "":   
            return string_val 
        else:  
            new_string = ""   
            for i in range(0, len(string_val)): 
                new_string = new_string + string_val[i]  
            return new_string
        
    #####################################################
    def len(self) -> int:
        ''' returns the number of characters present in the String object

        Returns:
            an int representing the number of character in the String
        '''
        string = self._chars 
        string_length = len(string) 
        return string_length

    #####################################################
    def is_empty(self) -> bool:
        ''' Boolean method indicating whether the String is an empty string

        Returns:
            True if no characters are present in the String; False o/w
        ''' 

        string = self._chars 
        if string == []: 
            return True  
        return False 


    #####################################################
    def __eq__(self, other: 'String | str') -> bool:  # faking Python 3.10 support for hints
        ''' overrides the __eq__ special method for comparing two String
            objects, or for comparing a String object and an str object

        Parameters:
            other: a separate String or str object for comparing

        Returns:
            True if the two objects contain exactly the same characters in
            the same order; False o/w
        '''

        # make sure to allow comparison when other is either String or str
        

        if isinstance(other, String) == True:
            if self._chars == other._chars: 
                return True 
            else: 
                return False 
        elif isinstance(other, str) == True: 
            string_1 = self.__str__() 
            if string_1 == other: 
                return True 
            else: 
                return False 
        else: 
            raise TypeError("The second object you evaluate using __eq__ must be str or String type")


        

    #####################################################
    def __getitem__(self, index: int) -> str:
        ''' overrides the __getitem__ special method, allowing [] access
            into a String object to access a single character (str)

        Parameters:
            index: an integer indicating the position of the character to fetch

        Returns:
            the character (a str in Python) at the indicated position

        Raises:
            IndexError: if the index value is invalid relative to String length 
        '''
        
        element = self._chars[index]  
        return element


    #####################################################
    def __setitem__(self, index: int, char: str) -> None:
        ''' overrides the __setitem__ special method, allowing one to overwrite
            a character at a specific index in the String

        Parameters:
            index: an integer indicating the position of the character to overwrite

        Returns:
            None

        Raises:
            IndexError: if the index value is invalid relative to String length
        '''
        working_string = self._chars  
        if isinstance(index, int) == False or isinstance(char, str) == False: 
            raise TypeError("Please specify your index as an integer and replacement\
                character as an str")
        if len(working_string) == 0 or index > len(working_string): 
            raise IndexError(f"Can not index into an empty string {working_string}") 
        else: 
            updated_string = working_string[:index] + [char] + working_string[index:]
            del updated_string[index + 1]
            self._chars = updated_string



    #####################################################
    def __add__(self, other: 'String | str') -> 'String':
        ''' overrides the __add__ special method, allowing one to add
            (concatenate) two String objects, or to concatenate an str object
            to a String object; this String and other should remain unchanged

        Parameters:
            other: a String or str object to append to this String

        Returns:
            a String object represent the concatenation of the two strings
        '''  

        if isinstance(other, String):
            newChars = ""
            for c in self._chars:
                newChars += c
            for d in other:
                newChars += d
            return String(newChars)
        elif isinstance(other, str):
            newChars = ""
            for c in self._chars:
                newChars += c
            for d in other:
                newChars += d
            return String(newChars)
        else:
            raise TypeError
    





    #####################################################
    def substring(self, start: int, end: int) -> 'String':
        '''
         returns a new String object that consists of the characters
            between indices start and end, both inclusive, in the current
            String object

        Parameters:
            start: an integer index between 0 and the length of the string - 1
            end: an integer index between 0 and the length of the string - 1,
                with end >= start

        Returns:
            a String object representing the corresponding substring;
            if end < start, returns an empty String

        Raises:
            TypeError if either start or end is not an integer
            IndexError if either start or end is negative or beyond the end
                of the String 
        '''
        if isinstance(start, int) == False or isinstance(end, int) == False: 
            raise TypeError(f"Either {start} or {end} is not an integer") 
        elif start < 0 or end < 0: 
            raise IndexError(f"A start value {start} less than one or end value {end} less than\
                zero is an innappropriate input") 
        elif start >= len(self._chars) or end >= len(self._chars): 
            raise IndexError(f"Indeces with exceed the length of the string can not be used")
        string = self._chars[start:end+1]
        new_string = "" 
        for i in string: 
            new_string += i 
        return String(new_string)

'''
def main():  

    string_1 = String("@abcFde")
    string_2 = String("efgh")
    new_string = string_1.substring(1,2)
    print(new_string)
main() 
'''
