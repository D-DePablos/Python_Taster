def luckylotto(raffle):
    """
    param: raffle: A list containing the Possible Outcomes
    return: Returns the outcome of the raffle
    """
    import numpy.random       # We can have imports inside functions


    picked = numpy.random.randint(len(raffle) - 1) # Random number from 0 to end of raffle
    result = raffle[picked]  # Getting the result of the raffle


    if result == 'money':

        print(f'You now have {result}: Good on you!')

    else:

        print(f'You now have {result}: Better luck next time!')


    return 'Done picking!'
