EXPECTED_BAKE_TIME = 40 
def bake_time_remaining(elapsed_bake_time):
    """this functions returns the remaining bake time
    """
    result = EXPECTED_BAKE_TIME - elapsed_bake_time
    return result
def preparation_time_in_minutes(number_of_layers):
    """this function returns the preparation time
    """
    return number_of_layers*2
    
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """it returns the elapsed time
    """
    return number_of_layers*2 + elapsed_bake_time
    
    
    
    