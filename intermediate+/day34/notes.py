"""
Trivia API and The Quizzler App

"""

##################################################
# HTML Entities
# https://www.w3schools.com/html/html_entities.asp
##################################################

import html

text = html.unescape("Q.1: Valve&#039;s &quot;Portal&quot; and &quot;Half-Life&quot; " \
                    "franchises exist within the same in-game universe.")
print(text)

# Q.1: Valve&#039;s &quot;Portal&quot; and &quot;Half-Life&quot; franchises exist within the same in-game universe. (True/False): 
# Q.1: Valve's "Portal" and "Half-Life" franchises exist within the same in-game universe.

###################
# Type Hints
###################

# sets what the input type should be, and also what the returned data type will be

def greeting(name: str) -> str:
    return 'Hello ' + name


###########################
# Quiz Game Updates
#
# Uses API to get questions
#
# Has GUI to display quiz
#
# Read UI.py 
# Read Data.py
# Read Quiz_Brain.py
###########################