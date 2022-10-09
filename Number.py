class Number:

    __slots__ = ("_input_number") #integer or floating point value

    def __init__(self, value: "int or float") -> None:
        '''
            Initializes the instance variable self._input_number so long as this
            number is part of the Number class

            Parameters:
                int or float -- self: the variable that stores all our information
                int or float -- value: the variable that stores whatever our inputed
                number is

            Returns:
                None

        '''



        if isinstance(value, int) == False and isinstance(value, float) == False:
            raise TypeError(f"Your input value is not a number object")
        else:
            self._input_number = value
            #print(f"value ORIG is {value}")
            #print(f"self._input_number ORIG is {self._input_number}")
            #print("1")

    def __add__(self, value: "int or float") -> "Int | Float":




        '''
            Adds the objects of the number class stored in self._input_number
            and value._input_number

            Parameters:
                int or float -- self: the variable that stores all our information
                int or float -- value: the variable that stores whatever our inputed
                number is

            Returns:
                Integer or float sum of two inputed numbers

        '''

        if isinstance(value, Number) != True: #value we can check to see if it
        #is an instance of the Number class but value._input_number we can not
        #because value._input_number will be a float or int

        #the reason that input_numberis an int or float is that the instance variable
        #represents private data stored within the Number class. value and self
        #are non-private objects of the number class which contain specific
        #input_number data and can be operated on by Number methods

            raise TypeError(f"Your input value is not a Number object")
        else:
            #print("2")
            #print(f"self._input_number is {self._input_number}")
            #print(f"value._input_number is {value._input_number}")
            sum = self._input_number + value._input_number

             #here we
            #access the specific instantiation of self and value, which
            #are the float and integer values stored within the Number objects
            #that can then be added together

        #after creating integer or float class, come back here and check
        #whether the result of instance or float, then return an object of that class

        if isinstance(value, Integer) == True and isinstance(self, Integer) == True:
            return Integer(sum)
        else:
            #print(f"self is {self}")
            #print(f"value is {value}")
            return Float(sum)


    def __mul__(self, value: "int or float") -> "Float | Int":
        '''
            Multiplies the objects of the number class stored in self._input_number
            and value._input_number

            Parameters:
                int or float -- self: the variable that stores all our information
                int or float -- value: the variable that stores whatever our inputed
                number is

            Returns:
                Integer or float product of the two numbers

        '''

        if isinstance(value, Number) != True:
            raise TypeError(f"Your input value is not a Number object")
        else:
            product = self._input_number * value._input_number


        if isinstance(value, Integer) == True and isinstance(self, Integer) == True:
            return Integer(product)
        else:
            return Float(product)


    def __str__(self) -> str:
        '''
        Takes the value in self.input_number and returns it as a string

        int or float -- self: The variable storing our information

        Returns:
            string of whatever number type is inputed
        '''
        string = str(self._input_number)
        return string


#for str method, give back string representation of number chopped off to decimal place
#number stored inside the object


class Integer(Number):

    def __init__(self, value: "int or float") -> None:
        '''
            Stores information from the number class as an integer. Uses all
            methods from the number class by calling super

            Parameters:
                int or float -- self: the variable that stores all our information
                int or float -- value: the variable that stores whatever our inputed
                number is

            Returns:
                None

        '''
        super().__init__(int(value))
        if isinstance(value, int) == False:
            raise ValueError(f"Your input is not an integer object")

class Float(Number):

    __slots__ = ("_round") #we only need new slots if our instance variable is new
    #as opposed to inherited

    def __init__(self, value: "int or float", decimal_places:int = 2) -> None: #decimal_places  = 2 represents a
        '''
            Stores information from the number class as a float. Uses all
            methods from the number class by calling super

            Parameters:
                int or float -- self: the variable that stores all our information
                int or float -- value: the variable that stores whatever our inputed
                number is
                int -- decimal_places: the number of decimals as an integer

            Returns:
                None

        '''

    #default parameter that changes when we add another input value
        super().__init__(float(value))

        if isinstance(value, float) == False:
            raise ValueError(f"Your input is not a float object")

        #print(f" 1 in Float self._input_number is {self._input_number}")
        else:
            self._round = decimal_places

    def __str__(self) -> str:
        '''
            Grabs the float version of a given number and returns the rounded version

            Parameters:
                int or float -- self:  the variable that stores all our information

            Returns:
                Rounded string

        '''
        decimals = self._round
        return f"{self._input_number:.{self._round}f}"

    def changeFormat(self, decimal_places: int) -> str:
        '''
            Enables us to change the number of decimal places in the string function

            Paramaters:
                int or float -- self:  the variable that stores all our information
                int -- decimals: the number of decimal places we want to round to

            Returns:
                updated string with correct number of decimal places

        '''
        #maybe we need to use the format method here???
        self._round = decimal_places
        return str(self)

class Complex(Number): #15 +3i 7.8+ 0i

    __slots__ = ("_imaginary_part", "_decimals")


    def __init__(self, value: "int or float", complex: "int or float", decimals = 1) -> None:
        '''
            Stores information from the number class as a complex. Uses all
            methods from the number class by calling super

            Parameters:
                int or float -- self: the variable that stores all our information
                int or float -- value: the variable that stores whatever our inputed
                number is
                int -- decimal_places: the number of decimals as an integer

            Returns:
                None

        '''
        super().__init__(value)
        self._decimals = decimals
        self._input_number = value
        self._imaginary_part = complex


    def changeFormat(self, decimals: int) -> str:
        '''
            Enables us to change the number of decimal places in the string function

            Paramaters:
                int or float -- self:  the variable that stores all our information
                int -- decimals: the number of decimal places we want to round to

            Returns:
                updated string with correct number of decimal places

        '''
        self._decimals =  decimals
        return str(self)

    def __str__(self) -> str:
        '''
            Grabs the complex version of a given number and returns the rounded version
            with varying formating depending on whether the input complex number
            is positive, negative, or zero

            Parameters:
                int or float -- self:  the variable that stores all our information

            Returns:
                Rounded string

        '''
        decimal_value = self._decimals
        real = self._input_number
        print(f"real = {real}")
        imag = self._imaginary_part
        print(f"imag = {imag}")

        if isinstance(real, int) == True:
            real_part = Integer(real)
            #imaginary_part = Integer(imag)
            #return f"{real_part} + {imaginary_part}i"
        elif isinstance(real, float) == True:
            real_part = Float(real, decimal_value)
            #imaginary_part = Float(imag, decimal_value)

        if isinstance(imag, int) == True:
            imaginary_part = Integer(imag)
        elif isinstance(imag, float) == True:
            imaginary_part = Float(imag, decimal_value)


        if real == 0 and imag == 0:
            return "0"

        if real == 0 and imag < 0 and imag != -1:
             #remove negative sign from imaginary value
            return f"{imag}i"

        if real == 0 and (imag == 1 or imag == -1):
            if imag == 1:
                return "i"
            if imag == -1:
                return "-i"

        if real == 0 and imag > 1: #CHECK!!!
            return f"+{imag}i"


        if real < 0 and imag < 1 and real != -1:
            imaginary_string = str(imaginary_part).strip("-")
            return f"{real_part} - {imaginary_string}i"

        if real < 0 and imag > 1:
            return f"{real_part} + {imaginary_part}i"

        if real > 0 and imag > 1:
            return f"{real_part} + {imaginary_part}i"

        if real > 0 and imag < 0:
            imaginary_string = str(imaginary_part).strip("-")
            return f"{real_part} - {imaginary_string}i"

        if real > 0 and imag == 0:
            return f"{real_part}"

        if real < 0 and imag == 0:
            return f"{real_part}"



    def __add__(self, value: "int or float") -> "Complex":

        '''
            Adds the two given complex numbers. Note that constituent
            components can be int or float

            Parameters:
                int or float -- self: the value we are storing one of our complex numbers in

                int or float --self: the number we are storing the other complex number in

            Returns:
                sum of two input values as int or float

        '''

        if isinstance(value, Number) == False:
            raise ValueError("your object is not of the number class")

        num_1_real = self._input_number
        num_1_imag = self._imaginary_part
        print(f"num_1_real = {num_1_real}")
        print(f"num_1_imag = {num_1_imag}")

        num_2_real = value._input_number
        print(f"num_2_real = {num_2_real}")
        num_2_imag = value._imaginary_part
        print(f"num_2_imag = {num_2_imag}")

        decimals = self._decimals

        #if isinstance(num_1_real, int) == True and isinstance(num_2_real, int) == True:
            #real_sum = num_1_real + num_2_real
        #if isinstance(num_1_real, float) == True or isinstance(num_2_real, float) == True:
            #real_sum = Float(num_1_real, decimals) + Float(num_2_real, decimals)
        #if isinstance(num_1_imag, int) == True and isinstance(num_2_imag, int) == True:
            #imag_sum = num_1_imag + num_2_imag
        #if isinstance(num_1_imag, int) == True or isinstance(num_2_imag, int) == True:
            #imag_sum = Float(num_1_imag, decimals) + Float(
            ##num_2_imag, decimals
            #)

        real_sum = num_1_real + num_2_real
        print(real_sum)
        imag_sum = num_1_imag + num_2_imag
        print(imag_sum)

        return Complex(real_sum, imag_sum)



    def __mul__(self, value: "int or float") -> "Complex":
        '''
            Takes the input value and multiples by another given value

            Parameters:
                int or float -- self: the variable that contains all the information for a given number for all classes
                int or float -- value: another variable that we use along with our instance variable to get a product

            Returns:
                product of the two given complex numbers

        '''

        if isinstance(value, Number) == False:
            raise ValueError("your object is not of the number class")



        '''
        if real_part_1 != 0 and imag_part_1 == 0:
            #scalar = real_part_1
            if isinstance(real_part_1, float) == True or isinstance(real_part_2, float) == True:
                r_val = real_part_1 * real_part_2
                r_val = changeFormat(r_val, decimals)
                #r_val_fin = Float(r_val, decimals)
            elif isinstance(real_part_1, int) == True and isinstance(real_part_2, int) == True:
                r_val = real_part_1 * real_part_2
                #r_val_fin = Integer(r_val)

            if isinstance(real_part_1, float) == True or isinstance(real_part_2, float) == True:
                s_val = real_part_1 * imag_part_2
                s_val = changeFormat(s_val, decimals)
            elif isinstance(real_part_1, int) == True and isinstance(real_part_2, int) == True:
                s_val = real_part_1 * imag_part_2
                #s_val_fin = Integer(s_val)

            return Complex(r_val, s_val)

        elif real_part_1 == 0 and real_part_2 == 0:
            r_val = 0

            if isinstance(imag_part_1, float) == True or isinstance(imag_part_2, float) == True:
                s_val = imag_part_1*imag_part_2
                s_val = changeFormat(s_val, decimals)
                #s_val_fin = Float(s_val, decimals)
            elif isinstance(imag_part_1, int) == True and isinstance(imag_part_2, int) == True:
                if imag_part_1 == 1 and imag_part_2 == 1:
                    s_val = -(imag_part_1*imag_part_2)
                else:
                    s_val = imag_part_1*imag_part_2
                #s_val_fin = Integer(s_val)

            return Complex(r_val, s_val)

        elif real_part_2 != 0 and imag_part_2 == 0:
            #scalar = real_part_2
            if isinstance(real_part_1, float) == True or isinstance(real_part_2, float) == True:
                r_val = real_part_1 * real_part_2
                r_val = changeFormat(r_val, decimals)
                #r_val_fin = Float(r_val, decimals)
            elif isinstance(real_part_1, int) == True and isinstance(real_part_2, int) == True:
                r_val = real_part_1 * real_part_2
                #r_val_fin = Integer(r_val)

            if isinstance(real_part_2, float) == True or isinstance(imag_part_1, float) == True:
                s_val = real_part_2 * imag_part_1
                s_val = changeFormat(s_val, decimals)
                #s_val_fin = Float(s_val, decimals)
            elif isinstance(real_part_1, int) == True and isinstance(real_part_2, int) == True:
                s_val = real_part_2 * imag_part_1
                #s_val_fin = Integer(s_val)

            return Complex(r_val, s_val)

        else:

            a = real_part_1
            b = real_part_2
            c = imag_part_1
            d = imag_part_2

            if isinstance(a, float) == True or isinstance(c, float) == True:
                a_c = a*c
                a_c_final = changeFormat(a_c, decimals)
            else:
                print("hi1")
                print(f"a is {a}")
                print(f"c is {c}")
                a_c_final = a*c
                print(f"a_c_final is {a_c_final}")

            if isinstance(b, float) == True or isinstance(d, float) == True:
                b_d = b*d
                b_d_final = changeFormat(b_d, decimals)
            else:
                print("hi2")
                print(f"b is {b}")
                print(f"d is {d}")
                b_d_final = b*d
                print(f"b_d_final is {b_d_final}")

            r_final = a_c_final - b_d_final

            if isinstance(a, float) == True or isinstance(d, float) == True:
                a_d = a*d
                a_d_final = changeFormat(a_d, decimals)
            else:
                print("hi3")
                print(f"a is {a}")
                print(f"d is {d}")
                a_d_final = a*d
                print(f"a_d_final is {a_d_final}")

            if isinstance(b, float) == True or isinstance(c, float) == True:
                b_c = b*c
                b_c_final = changeFormat(b_c, decimals)
            else:
                print("hi4")
                print(f"b is {b}")
                print(f"d is {d}")
                b_c_final = b*c
                print(f"b_c_final is {b_c_final}")

            s_final = a_d_final + b_c_final

            return Complex(r_final, s_final)

            '''

        #ALTERNATIVE
        decimals = self._decimals

        if isinstance(value, Complex) == True:

            a = self._input_number
            b = self._imaginary_part
            c = value._input_number
            d = value._imaginary_part


            if isinstance(a, float) == True or isinstance(c, float) == True:
                a_c = a*c
                a_c_final = changeFormat(a_c, decimals)
            else:
                print("hi1")
                print(f"a is {a}")
                print(f"c is {c}")
                a_c_final = a*c
                print(f"a_c_final is {a_c_final}")

            if isinstance(b, float) == True or isinstance(d, float) == True:
                b_d = b*d
                b_d_final = changeFormat(b_d, decimals)
            else:
                print("hi2")
                print(f"b is {b}")
                print(f"d is {d}")
                b_d_final = b*d
                print(f"b_d_final is {b_d_final}")

            r_final = a_c_final - b_d_final

            if isinstance(a, float) == True or isinstance(d, float) == True:
                a_d = a*d
                a_d_final = changeFormat(a_d, decimals)
            else:
                print("hi3")
                print(f"a is {a}")
                print(f"d is {d}")
                a_d_final = a*d
                print(f"a_d_final is {a_d_final}")

            if isinstance(b, float) == True or isinstance(c, float) == True:
                b_c = b*c
                b_c_final = changeFormat(b_c, decimals)
            else:
                print("hi4")
                print(f"b is {b}")
                print(f"d is {d}")
                b_c_final = b*c
                print(f"b_c_final is {b_c_final}")

                s_final = a_d_final + b_c_final

            return Complex(r_final, s_final)

        else:

            a = self._input_number
            b = self._imaginary_part #probably nonzero
            c = value._input_number

            r_val = a*c
            s_val = c*b

            return Complex(r_val, s_val)







#NEGATIVE FLOATS ARE NOT WORKING
#FOR LOOP BARRY HAD IS NOT WORKING

def main():
    '''

    print("----------------------------- NUMBER CLASS TESTS ---------------------------------")

    n1 = Number(8675309)
    n2 = Number(3.14159)

    n3 = Number(7.22334)
    #n4 = Number("3.42")
    #n5 = Number(3)
    #n6 = Number(2)

    print("########################### GENERIC ADD TESTS ####################################")
    print(f"sum of {n1} and {n2} is {n1 + n2} and expected is 8675312.14")
    #print(f"sum of {n3} and {n4} is {n3 + n4} and expected is TypeError")
    #print(f"sum of {n5} and {n6} is {n5 + n6} and expected is 5")

    print("########################## GENERIC MUL TESTS ##################################")
    print(f"product of {n1} and {n2} is {n1*n2} and expected is 27254264")
    #print(f"product of {n3} and {n4} is {n3*n4} and expected is TypeError")


    print("--------------------------- INTEGER CLASS TESTS ---------------------------------")



    n5 = Integer(44.5)
    n6 = Integer(23.22222233342)

    n7 = Integer(22.2434)
    n8 = Integer(34)

    n9 = Integer(33.22223)

    print("########################## ADD TESTS #############################")

    print(f"The sume of {n7} and {n5} is {n5 + n7} and expected is 66")


    print("############################# MUL TESTS ###################################")
    print(f"The product of {n5} and {n6} as an integer is {n5*n6} and expected is 1012")
    print(f"The product of {n7} and {n8} as an integer is {n7*n8} and expected is 748")


    print("########################## STRING FUNCTION TESTS ##########################")
    print(f"type of {n9} is {type(n9)} and expected is integer")


    print("----------------------------- FLOAT CLASS TESTS ----------------------------")

    print("##################### DECIMAL TESTS ################################")

    n10 = Float(5.3321, 3)

    print(f"Expected result of printing 5.3321 to three decimal places is\
    5.332 and actual result is {n10}")
    n11 = Float(6, 2)
    print(f"Expected result of printing 6 to two decimal places is\
    6.00 and actual result is {n11}")

    n12 = Float(3.445, 3)
    n13 = Float(2.1, 0)

    print("#################### ADD TESTS ########################")

    print(f"expected result of {n10} + {n11} is 11.332 and result is {n10 + n11}")
    print(f"expected result of {n12} + {n13} is 5.445 and result is {n12 + n13}")


    print(f"-----------------------COMPLEX CLASS TESTS---------------------")

    a = Complex(1, 0)
    b = Complex(-1, 0)
    c = Complex(0, 1)
    d = Complex(0, -1)
    e = Complex(0, 0)
    f = Complex(0, -2)
    g = Complex(3, 2)
    h = Complex(3, -2) #works, fix spacing
    i = Complex(3.1, 2)
    j = Complex(3.1, -2)
    k = Complex(3, 2.1) #works
    l = Complex(3, -2.1) #works, fix spacing
    m = Complex(-3, -2.1)

    print(a), print(b), print(c), print(d), print(e)
    print(f), print(g), print(h), print(i), print(j)
    print(k), print(l), print(m)

    print("########################## ADD TESTS ###############################")

    addend_1 = Complex(0, 0)
    addend_2 = Complex(0, 1)
    print(f"expected result is i and result is {addend_1 + addend_2}")

    addend_3 = Complex(30, 9999.7)
    addend_4 = Complex(479, 0.235)
    print(f"expected result is 509 + 9999.9i and result is {addend_3 + addend_4}")

    addend_5 = Complex(39.9, 2890)
    addend_6 = Complex(1, 0)
    print(f"expected result is 40.9 + 2890 and actual result is {addend_5 + addend_6}")

    '''

    print("######################## MUL TESTS ##############################")

    #multiple_1 = Complex(321, 0)
    #scalar_1 = Complex(1, 0)

    #print(f"expected result of 321,0  and 1,0 is 321 and result is {multiple_1.__mul__(scalar_1)}")

    #multiple_3 = Complex(3, 4)
    #multiple_4 = Complex(4, 7)

    multiple_5 = Complex(0, 1)
    multiple_6 = Complex(0, 1)

    #print(f"{multiple_3*multiple_4}")
    print(f"result is {multiple_5*multiple_6}")




if __name__ == "__main__":
    main()
