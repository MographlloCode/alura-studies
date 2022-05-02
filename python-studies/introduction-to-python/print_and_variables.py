''' Print and Variables - Lesson 1 - Part 1 '''

# Testing print (\n to jump a line)

print("-"*30)
print("Testing print function\n")

print("Brazil has won 5 world cups\n")
print("Brazil", "has", "won", 5, "world cups\n", sep=" ") # using the parameter "sep" to separate the words
print("Brazil", "has", "won", 5, "world cups", end="\n\n") # using the parameter "end" to insert 
                                                           # two lines after the sentence
                                                                
# Setting Variables

print("-"*30)
print("Testing variables")

brazil = 5
italy = 4
germany = 3
portugal = 2
cuba = 1

print("\nBrazil has won", brazil,"world cups")
print("\nItaly has won", brazil,"world cups")
print("\nGermany has won", germany,"world cups")
print("\nPortugal has won", portugal,"world cups")
print("\nCuba has won", cuba,"world cups")

day = 15
month = 10
year = 2015

print(day, month, year, sep="/")