def year_prog(name,age):
    '''
    Enter your name and age as parameters. The program will Print out a message that tells you the year that they will turn 100 years old. The present year is 2019'''
    
    x = 2019 - age
    year = x + 100
    
    print(f"Hello {name}, the year you will turn 100 is:")
    return year
