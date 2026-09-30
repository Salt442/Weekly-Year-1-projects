#calculator function, identifies the correct sign and returns the valid output.
def calculator(num1,num2,operator): # Uses If/Elif to check each valid operator and return the correct equation.
    if operator == "+":
        return num1+num2
    elif operator == "-":
        return num1-num2
    elif operator == "*":
            return num1*num2
    elif operator == "/":
         if num2 == 0:
              return "Cannot divide by zero!"
         else:
            return num1/num2
    elif operator == "%":
            return num1%num2
    elif operator == ">":
            return num1>num2
    elif operator == ">=":
            return num1>=num2
    elif operator == "<":
            return num1<num2
    elif operator == "<=":
            return num1<=num2
    else:
          return "Invalid operator!"
    
#Function to compare all three numbers to each other and return the highest value
def max_of_three(num1,num2,num3):
    if num1 != type(1) or num2 != type(1) or num3 != type(1):
        return None

    if num1 > num2 and num1 > num3: #Checks if num1 is greater than all others.
        return num1
    elif num2 > num3: #If num1 is not greatest, num2 is checked against num3
        return num2
    else:
        return num3 #If all else is smaller then by default num3 is the largest.
    
#Function compares guesses to winning list, adds score for
#each correct guess.
def winning_numbers(winning_list, guessed_list):
    if winning_list != type([1,1]) or guessed_list != type([1,1]):
        return None
    score = 0 # Defines score variable.
    if guessed_list[0] in winning_list: # +1 score per correct guess
        score += 1
    if guessed_list[1] in winning_list:
        score+= 1
    if guessed_list[2] in winning_list:
        score+= 1
    if score == 0: #Uses if/elif to return prize
        return "No"
    elif score == 1:
        return "Third"
    elif score == 2:
        return "Second"
    else:
        return "First"
    
#Function to take two numbers and add together all even inbetween, inclusive of the start/end.
def sum_of_evens(min_num,max_num):
    total = 0
    if min_num != type(1) or max_num != type(1):
        return None
    if min_num < 0 or max_num < 0:
        return None
    else:
        for i in range(min_num,max_num+1): #+1 to the end point to include the max_num
            if i%2 == 0: #Odd/even check, adds even to total variable.
                total+= i
            else:
                continue
        return total
    
# Function that calculates the average from a list of numbers without using len() or sum()
def calculate_average(list_of_numbers):
    pos = 0 #Tracks number of items in list
    total = 0 #Stores total.
    if list_of_numbers != type([1,1]):
        return None
    for i in list_of_numbers:
        total += list_of_numbers[pos]
        pos += 1
    return int(total / pos) #Returns the average number as an int.

#Function that calculates weekly pay + Overtime pay.
def calculate_weekly_pay(hours):
    if hours != type(1):
        return None
    if hours <= 0:
        return None #If hours is not positive/is 0, returns none.
    total_pay = 0
    pay = 12 #Pay/Overtime pay variables
    overtime = 18
    if hours <= 35: #Calculates non-overtime pay.
        total_pay += (hours * pay)
        return total_pay
    elif hours > 35:
        total_pay += (35 * pay)
        total_pay += overtime * (hours - 35) #Removes 35 from hours, uses remaining hours to calculate overtime pay.
        return total_pay
    
#Function to detect if an input is a prime number
def is_prime(pos_int):
    if pos_int != type(1):
        return None
    if pos_int <= 1: #Removes <=1 numbers
        return False
    
    # Only need to test divisors up to the square root
    for i in range(2, int(pos_int**0.5) + 1):
        if pos_int % i == 0:
            return False
    # If none == 0, returns True
    return True

# Function to check if two words are anagrams (Contain the same letters in different order)
def are_anagrams(word1,word2):
    word1_set = set(word1.lower()) #Turns words into sets, sets have no order and no order is needed.
    word2_set = set(word2.lower())# lower() changes all words into lowercase, meaning it's case insensitive.

    if word1_set > word2_set or word2_set > word1_set: #If words are not equal in length they cannot be anagrams.
        return False
    
    if word1_set == word2_set: #If sets are equal then they are anagrams.
        return True
    else:
        return False

# Function that takes a string and returns count of vowels
def count_vowels(vowel_string):
    vowels = ["a","e","i","o","u","A","E","I","O","U"] #Upper and lower vowels to make program case insensitive
    vowels_counter = 0 
    for i in vowel_string: # Loop checks if current letter is in vowels, if True adds 1 to counter.
        if i in vowels:
            vowels_counter += 1
    return vowels_counter

# Function to sort a list of numbers using bubble sort method.
def sort_list(number_list):
    pos = 0
    total = 0
    counter = 0
    if number_list != type([1,1]):
        return None

    for i in number_list:
        total += 1

    while True:
        if pos >= total-1: #If the posistion reaches the end of the list posistion is reset.
            pos = 0 
        
        if counter == total-1: #Only once counter loops through the numbers without resetting does it return the sorted list.
            return number_list
        
        if number_list[pos] > number_list[pos+1]: #Checks if current number and next number are ordered, if not they are swapped.
            number_list[pos], number_list[pos+1] = number_list[pos+1], number_list[pos]
            pos+=1
            counter = 0 #Counter is reset
        else:
            pos+=1
            counter += 1
            continue

# Function that uses lists to return the sum of a numbers digits
def sum_of_digits(num):
    total = 0
    if num != type(1):
        return None
    num_list = list(str(num))
    for i in num_list: #Adds each item in the list to total
        total+= int(i)
    return total

def is_palindrome(palindrome):
    alphabet = { #Dictionary containing entire lower and upper alphabet, used to convert uppers to lowers
        "A" : "a",
        "B" : "b",
        "C" : "c",
        "D" : "d",
        "E" : "e",
        "F" : "F",
        "G" : "g",
        "H" : "h",
        "I" : "i",
        "J" : "j",
        "K" : "k",
        "L" : "l",
        "M" : "m",
        "N" : "n",
        "O" : "o",
        "P" : "p",
        "Q" : "q",
        "R" : "r",
        "S" : "s",
        "T" : "t",
        "U" : "u",
        "V" : "v",
        "W" : "w",
        "X" : "x",
        "Y" : "y",
        "Z" : "z"
    }
    backwards = ""
    pos = 0
    true_palindrome = ""
    list_palindrome = list(palindrome) #Converts string into a list


    for i in list_palindrome: #Goes through entire word, converts capital to lower and adds to true palindrome variable.
        if list_palindrome[pos] in alphabet:
            list_palindrome[pos] = alphabet[list_palindrome[pos]]
        true_palindrome += list_palindrome[pos]
        pos+=1

    pos = 0
    for i in list_palindrome: # Goes from the end of the list, adding each letter to backwards variable, at the end returns True/False 
        if list_palindrome[pos] in alphabet:
            list_palindrome[pos] = alphabet[list_palindrome[pos]]
        backwards += list_palindrome[pos-1]
        pos-=1
    return backwards == true_palindrome

#Function takes password variable, uses a loop to record the length and check each character against the special char and upper char list.
#If found it changes the has_upper or has_special variable to True. These are then checked when deciding its strength.
def password_strength(password):
    special_char = ["@","$","£"]
    upper_char = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    length = 0
    has_upper = False
    has_special = False

    for character in password: # Checks if character is in special/Upper, turns flag to True if it is. Tracks length
        if character in special_char:
            has_special = True
            length += 1
            continue
        elif character in upper_char:
            has_upper = True
            length += 1
            continue
        else:
            length += 1
            continue

    #Checking for weak passwords, using Special/Upper flags and length
    print(has_special,has_upper,length)
    if length < 6 or has_special == False or has_upper == False:
        return "Weak"
    elif length >= 6 and length <= 10 and has_special == True and has_upper == True:
        return "Medium"
    elif length > 10 and has_special == True and has_upper == True:
        return "Strong"
    
#A function that accepts a dictionary with scores and credits, uses a loop to calculate the numerator and denominator
#Uses numerator and denominator to calculate average. Checks average against grade criteria, returns grade and average
#Scalable, will accept less or more dictionary items without changing code.#
def letter_grade(data_input):
        if data_input != type({}):
               return None

        numerator = 0
        denominator = 0
        for item in data_input: #Uses formula to calculate the num/den. *'s items on num and adds items to the den.#
                numerator += item["score"] * item["credits"]
                denominator += item["credits"]
        
        average = numerator / denominator #Calculates average
        if average < 50:
            return "Grade F", average
        elif average >= 50 and average < 60:
               return "Grade D", average
        elif average >= 60 and average < 70:
               return "Grade C", average
        elif average >= 70 and average < 90:
               return "Grade B", average
        elif average >= 90:
               return "Grade A", average

# Function that calculates the largest possible gap between two numbers, each from one list.
def maximum_gap(list1,list2):
    if list1 == None or list2 == None or list1 != type([]) or list2 != type([]): #Does not allow for empty lists.
        return None
    smallest = 0
    largest = 0
    if max(list1) > max(list2): #Checks to see if list1 has the largest number, if True uses list2's smallest number.
        largest = max(list1)
        smallest = min(list2)
    else: # If list1 does not have the largest number, performs the same operation in reverse.
        largest = max(list2)
        smallest = min(list1)
    
    return largest - smallest #Calculates the gap.

# Function to decipher a specific cipher
def cipher_text(input_text,key):
    if key != type(1) or input_text != type(""):
        return None
    solved_text = ""
    for i in input_text: #Converts current char to ASCII number, removes the key number and converts back to a char.
        char = ord(i)
        char -= key
        solved_text+= chr(char)
    return solved_text

# Function to calculate total annual income minus tax
def net_annual_income(gross_salary):
    tax = 0
    if gross_salary != type(1):
        return None
    # If salary is greater than 12571 - 50270, it calculates the tax for the money in the range
    # If the salary is within range but does not exceed it, calculates the tax based on salary - lower end of catagory
    if gross_salary > 12571 and gross_salary > 50270: 
        tax += (50270-12571) * 0.2 
    elif gross_salary > 12571:
        tax += (gross_salary-12571) * 0.2
    if gross_salary > 50270 and gross_salary > 125140:
        tax += (125140 - 50270) * 0.4
    elif gross_salary > 50270:
        tax += (gross_salary - 50270) * 0.4
    if gross_salary > 125140:
        tax += (gross_salary - 125140) * 0.45

    return int(gross_salary - tax)

# A function that takes a string and seperator, then creates a list using that seperator.
def my_split(my_str,sep):
    my_str += sep #Adds extra seperator to end, ensures last item is added to the list.
    output_list = []
    string_item = ""
    for i in my_str:
        if i == sep: #When sep is found, adds item to output list and clears the current string item.
            output_list += [string_item]
            string_item = ""
            continue
        else:
            string_item += i # Adds current letter to string.
            print(string_item)
            continue
            
    return output_list

# Function that takes a string and outputs the longest repeated letter without break (eg, "eerreeei" = e, 3)
def longest_repitition(string):
    current_letter = ""
    current_streak = 0
    highest_streak = -999
    highest_letter = ""

    for i in string: # starts a streak for each letter, if streak is the highest it is saved
    
        if i == current_letter:
            current_streak += 1 # Adds score each time current letter matches the previous
        else:
            current_letter = i #Sets new letter to current, resets streak
            current_streak = 1

        if current_streak > highest_streak: #Sets current streak to highest if it is greater than current highest.
            highest_streak = current_streak
            highest_letter = current_letter

    return (highest_letter, highest_streak)

# Function to find two items that together spend the most of the budget.
def closest_pair_under_budget(prices,budget):
    if prices != type([]) or budget != type(1):
        return None
    item1 = (None, 0)
    item2 = (None, 0)

# Loops for length of the item list checking to see if each item is greater than the current two saved, if it is and is under budget
# it is replaced.
    for i in range(len(prices)): 
        #If current item > saved item1 and total is smaller than the budget, the saved item is replaced.
        if prices[i][1] > item1[1] and prices[i][1] + item2[1] <= budget: 
            item1 = prices[i]
            continue
        #Same as previous check, except for item2
        elif prices[i][1] > item2[1] and prices[i][1] + item1[1] <= budget:
            item2 = prices[i]
            continue
    
    # If no items are given, returns none.
    if item1[0] == None and item2[0] == None: 
        return None
    else:
        return [item1[0],item2[0]]


