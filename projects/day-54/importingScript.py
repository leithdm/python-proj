'''

https://www.freecodecamp.org/news/whats-in-a-python-s-name-506262fe61e8/

The __name__ variable (two underscores before and after) is a special Python
variable. It gets its value depending on how we execute the
containing script.

Sometimes you write a script with functions that might be useful
in other scripts as well. In Python, you can import that script
as a module in another script.

Thanks to this special variable, you can decide whether you want
to run the script. Or that you want to import the functions
defined in the script

1. When you run your script, the __name__ variable equals __main__.
2. When you import the containing script, it will contain the name of
the script.

'''

import nameScript as ns

ns.myFunction()

# The value of __name__ is nameScript