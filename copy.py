# Function5.py
#
# @ author: A. N. Other
# date: September 2016

score = 4

def get_new_score(param_score):
    param_score += 1
    print("You got another point...\n"
          "Your score is now {0}.\n"
          .format(param_score))
    return param_score


# some run code
x = input("Your score is {0} points...\n\n"
          "Hit any key to get another point. "
          .format(score))
# invoking the function and using it to set the new score
score = get_new_score(score)
# test case assertion
# '''
print("Test case assertion: the current score is ",score ,
     "and it should become".format(score))
# invoking the function
#
score = get_new_score(score)


# '''

