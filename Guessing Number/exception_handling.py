# file name is "text_file.txt" but we entered "textfile.txt" so it goes to except

try:
    f = open("textfile.txt")
except Exception:
    print("Sorry. This file doesnot exist!")

# -----------------------------------------------------------------------------------------------------------------

# not the problem with above is that it will always print same thing even for different exceptions
# like if we have set bad variable  then also it will print "Sorry. This file doesnot exist!"

try:
    f = open("text_file.txt")
    var = bad_var
except Exception:
    print("Sorry. This file doesnot exist!")

# -----------------------------------------------------------------------------------------------------------------

# to overcome this let's try specific exception specific to "FileNotFoundError"
# now it will give normal python error since file is found the error is in variable but we havn't specified any exception handling for bad variable

try:
    f = open("test_file.txt")
    var = bad_var
except FileNotFoundError:
    print("Sorry. This file doesnot exist!")

# -----------------------------------------------------------------------------------------------------------------

# now let's handle bad variable exception
# for this we can add another except with general "Exception"
# NOTE: always put more specific exception at the top and more general exception at the bottom
#              because if we put more general exception at top then it will always excecute that only and not more specific exception

try:
    f = open("test_file.txt")
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

# -----------------------------------------------------------------------------------------------------------------

# "else" get excecuted when try doesn't raise any exception

try:
    f = open("test_file.txt")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()

# -----------------------------------------------------------------------------------------------------------------

# "finally" runs no matter what. wheather the code is successful or wheather it is not it will always run!!!
# these are useful if you are working with database then this would be the area to close down the database.

try:
    f = open("test_file.txt")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally...!!")

# -----------------------------------------------------------------------------------------------------------------

# we can raise exception of our own!

try:
    f = open("corrupt_file.txt")
    if f.name == "corrupt_file.txt":
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Error!")
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally...!!")

    # **************************************************************************
