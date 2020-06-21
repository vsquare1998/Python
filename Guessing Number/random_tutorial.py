import random

value = random.random()
print(f"Floating point random number between 0 and 1: {value}")

value2 = random.uniform(1, 10)
print(f"floating point random number between 0 to 10: {value2}")

value3 = random.randint(1, 6)
print(f"Random number between 1 and 6(inclusive) and ot floating: {value3}")

# random.choice() chooses one from multiple choices:
greeting = ["Hey", "Hello", "Hi", "Hola", "Howdy"]
value4 = random.choice(greeting)
print(value4 + " vaibhav!")

# random.choices() : getting multiple value from list
# k means how many times we want to pick the value
# in this every color is "equally likely" to be selected
colors = ["Red", "Black", "Green"]
value5 = random.choices(colors, k=10)
print(value5)

# we can weight the value to be selected from colors by using "weight"
# 18 for red, 18 for black,2 for green
value6 = random.choices(colors, weights=[18, 18, 2], k=10)
print(value6)

# random.shuffle(): shuffles the value in place we don't need to assign it to different variable
deck = list(range(1, 53))
random.shuffle(deck)
print(deck)

# now we wanna select 5 cards but we will not use choice because it may select same card multiple times
# but we want unique cards so we will use:
# random.sample()
hand = random.sample(deck, k=5)
print(hand)
