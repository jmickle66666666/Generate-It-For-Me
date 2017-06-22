Generate It For Me
 ----------------

A prototype tool for generating code automatically using provided unit tests.

Current state of the tool is very simple:
It can generate a function that takes in one integer, and outputs one integer.
You provide a list of inputs and outputs, and it'll attempt to generate a function that satisfies all of them.
You can choose how many lines of code it will generate. Too few and it can't solve it, too many and it'll take a long time. (It should, however, stop once it finds a working solution)

Next steps for this prototype:

Generalize the way it does unit tests to a function instead of lists.
Support more operations instead of just inline operators. Any built-in function that takes a number and outputs a number.
Support conditions
Support more than one input
Support more variable types
clean it up and organise it into modular parts

Other things to do:

Instead of working with strings and exec(), use template functions. Maybe there's a library that can help.
Add more ways of getting code, not just brute-force generation. For instance, scour github/stackoverflow a la https://gkoberger.github.io/stacksort/

