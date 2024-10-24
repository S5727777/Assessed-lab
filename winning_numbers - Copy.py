def winning_numbers(user_list, winning_list):
    """
    This function checks if the user's numbers match the predefined winning numbers.

    Parameters:
    user_list (list): A list of three integers representing the user's chosen numbers.
    winning_list (list): A list of integers representing the winning numbers.

    Returns:
    str: A string indicating the prize won:
        - "First" if all three numbers match the winning numbers.
        - "Second" if two numbers match the winning numbers.
        - "Third" if one number matches the winning numbers.
        - "No" if none of the numbers match the winning numbers.

    Example:
    --------
    winning_list = [5, 14, 17]
    user_list = [3, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since one number, 5, matches the winning numbers)

    user_list = [14, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since two numbers, 14 and 5, match the winning numbers)

    The function also prints a message indicating the prize won.
    """

    # Function implementation here ...
   

    #Winner_roll= winning_list & user_list

    user_set = set(user_list)
    Winning_set= set(winning_list)
    Consumer_list = winning_list + user_list
    consumer_set = set(Consumer_list)
    if len(consumer_set)== 3:
       prize="Bingo!/ First"
       print(f"Congratulations, you won {prize} prize!")
    else:
        Consumer_list = winning_list + user_list
        consumer_set = set(Consumer_list)
        if len (consumer_set)== 3:
           prize = "first"
        elif len(consumer_set)== 4 and 14 and 17 in consumer_set:
           prize ="second"
        elif len (consumer_set)== 4 and 5 and 14 in consumer_set:
           prize ="second"
        elif len (consumer_set)== 4 and 17 and 5 in consumer_set:
           prize ="second"
        elif len (consumer_set) == 5 and 17 in consumer_set:
           prize ="third"
        elif len (consumer_set) == 5 and 14 in consumer_set:
           prize ="third"
        elif len(consumer_set) == 5 and 5 in consumer_set:
           prize ="third"
       
        print(f"Congratulations, you won {prize} prize!")
        return prize

winning_list=[5,14,17]
user_list=[5,14,20]
prize= "first"
prize= "second"
prize= "third"
winning_numbers(user_list,winning_list)
   

  

    # Print the result
   # print(f"Congratulations, you won {prize} prize!")
    #return prize
    #if len (user_set&Winning_set)== 3:
       #    prize = "first"
       ## elif len(consumer_set&Winning_set)== 4 and 14 and 17 in consumer_set:
       #    prize ="second"
       # elif len (user_set&Winning_set)== 4 and 5 and 14 in consumer_set:
       #    prize ="second"
       # elif len (user_set&Winning_set)== 4 and 17 and 5 in consumer_set:
       #    prize ="second"
       # elif len (user_set&Winning_set) == 5 and 17 in consumer_set:
       #    prize ="third"
       ## elif len (user_set&Winning_set) == 5 and 14 in consumer_set:
       #    prize ="third"
       # elif len(user_set&Winning_set) == 5 and 5 in consumer_set:
       #    prize ="third"