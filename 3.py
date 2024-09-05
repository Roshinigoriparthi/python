#Mr Stark is facing the north. Peter is in trouble, and he is facing the south. Stark being his mentor will protect him as soon as he sees that Peter is in trouble.
#Stark's suit is programmed to rotate automatically in the direction of most enemies. By analyzing the direction in which most enemies are heading, the suit provides you with the next set of suit instructions in the form of a string S.
##Write a program that reads the set of suit instructions S and determines whether Stark will be able to save Peter.
#Note
#
#10-
#11
#12-
#13
#14-
#if c
#15
#16-
#else:
#17
#pr
#The string S contains either L or R. The letter L indicates left and the letter R indicates right.
#Submit Feedback

code:
def will_stark_save_peter(S):

    current_direction = 0  

    
    for instruction in S:
        if instruction == 'L':
            current_direction = (current_direction - 1) % 4  
        elif instruction == 'R':
            current_direction = (current_direction + 1) % 4  

        if current_direction == 2:
            return "Stark will save Peter"
    
    return "Stark will not save Peter"

S = input("Enter the suit instructions (sequence of L and R): ")

result = will_stark_save_peter(S)
print(result)
