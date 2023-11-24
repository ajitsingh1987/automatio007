# Without Using any Function
#txt = "Hello World"[::-1]
#print(txt)

# Reverse String Using Function:
#def my_function(x):
   # return x[::-1]
#mytxt=my_function("This is my first String")
#print(mytxt)

# Reverse string but first char should be caps:
original_string = "hello world"
reversed_string = ' '.join(word.capitalize() for word in original_string.split()[::-1])
print(reversed_string)
