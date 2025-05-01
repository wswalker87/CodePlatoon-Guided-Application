#Write a function that checks if all the phone numbers in the below dictionary are United States numbers (country code +1).  If a number is not, that customer should be moved to a new dictionary called "foreign_customers".  A number with no country code is assumed to be in the United States IF the phone number is ten digits.

#Additionally, the United States numbers should be formatted as XXX-XXX-XXXX.

customers = {
    "John Doe": "123.456.7890",
    "Jane Smith": "(123) 456-7890",
    "Jim Brown": "123 456 7890",
    "Jake White": "1234567890",
    "Jill Black": "+1 123 456 7890"
}
# The below is the answer with Roger
def phone_book_scrubber(phone_number_dict : dict):
    # iterate through the data structure, to access the values
    
    for name, number in phone_number_dict.items():
        # format the value to only have digits
        formatted_number = ""
        for num in number:
            # check if num is a number or not
            if num.isdigit():
                formatted_number + num
                #print(num, True)
                #print(formatted_number)
            else:
                continue
        print(name, num)
        
        if len(formatted_number) > 10:
            formatted_number = formatted_number[-10:]
        phone_number_dict[name] = formatted_number
            #print(name, num) # iterate over each and list the name with it to visualize it. 
        #print(name, number)
    return phone_number_dict


print(phone_book_scrubber(customers))



















































#.isdigit()
#remove_var = ['.', ' ', '-', '+1', '(', ')']

# for name, number in customers.items():
#     if not number.isdigit():
#         for digit in number:
#             if digit.isdigit():
#                 digit.replace('.', '-')
#                 digit.replace(' ', '-')
#                 print(digit)
#                 print(customers)

                
        #print(number)

    #s#crubbed = number.replace(remove_var, "")
    #print(number)
    #print(scrubbed)

    


# alien_0 = ['color:' 'green', 'red',
#            'heads:' '4']

# for color in alien_0:
#     print(color)