"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jaroslav Brodacky
email: jbrodacky@gmail.com
"""

#definition of variables

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = ('bob', 'ann', 'mike', 'liz')
passwords = ['123', 'pass123', 'password123', 'pass123']
separator = '-'*50

# -------------

# getting user's username and password

print(separator)
user_name = input ('username:')
user_pass = input('password:') 
print(separator)

# checking if user exists
if user_name not in users:
    print ('unregistered user, terminating the program..')
    exit ()
else:
    index = users.index(user_name) #getting index for the username - to check corresponding pw later

# checking if password is correct
if user_pass != passwords[index]:
    print ('incorrect password, terminating the program...')
    exit ()


# App welcome
print (f'''Welcome to the app, {user_name}.
We have 3 texts to be analyzed.''')
print(separator)

# Text selection
text_selection = input('Enter a number btw. 1 and 3 to select:')
print(separator)

# Check if selection is a number
if not text_selection.isdigit():
    print ('Selection needs to be a number in the range 1 to 3, terminating program...')
    exit ()
# Check is the number is within the range
elif int(text_selection) not in range (1,4) :
    print ('Just numbers 1 to 3 are allowed in the selection, terminating program...')
    exit ()

#selection of the actual text to analyze - from the original list of strings
text_to_analyze = TEXTS[int(text_selection)-1]

#removal of fullstops and commas
text_to_analyze = text_to_analyze.replace(',','')
text_to_analyze = text_to_analyze.replace('.','')


#printout of the text to analyze
#print ('Text to analyze:')
#print (separator)
#print (text_to_analyze)
#print (separator)


# Determining word count of the text
word_count = len(text_to_analyze.split())
print ('There are', word_count, 'words in the selected text.')
print (separator)

# Definition of individual counters

uppercase_words=0
lowercase_words=0
titlecase_words=0
numeric_string=0
numeric_sum=0
#x=0  #auxiliary variable 

# Splitting the selected text to list
lst=text_to_analyze.split()


# find count of titlecase, lowercase, uppercase words and number of digits 
for x in range (word_count):
    if lst[x-1][0].isupper() and not lst[x-1][1].isupper() :
        titlecase_words=titlecase_words+1   #counting titlecase words
        #print (lst[x-1])
    elif lst[x-1].isupper():
        uppercase_words = uppercase_words+1   #counting uppercase words
    elif lst[x-1].islower():
        lowercase_words = lowercase_words+1   #counting lowercase words
    elif lst[x-1].isdigit():
        numeric_string = numeric_string+1     #counting numeric strings 
        numeric_sum = numeric_sum + int(lst[x-1])   #counting sum of nummeric strings
        
    

print ('There are', titlecase_words,'titlecase words.')
print (separator)
print ('There are', uppercase_words,'uppercase words.')
print (separator)
print ('There are', lowercase_words,'lowercase words.')
print (separator)
print ('There are', numeric_string,'numeric strings.')
print (separator)
print ('The sum of all the numbers is: ', numeric_sum)


# create new list made of lenghts of individual words in the analyzed text
new_list=[]

for item in lst:
    new_list.append(len(item))


# find the length of the longest word
highest_number = max(new_list)
#print (highest_number)


#print the star bar table with number of occurences 
print (separator)
print ('LEN|  OCCURENCES                |NR.')
print (separator)

for x in range(1,highest_number+1):
    stars = '*' * new_list.count(x)
    if x in range (1, 10):   # adjusting formatting of 1-9
        print(x, ' |', stars, ' '* (25-new_list.count(x)),'|',new_list.count(x))
    else:  # adjusting formatting of 10 and onwards
        print(x, '|', stars, ' '* (25-new_list.count(x)),'|',new_list.count(x))
