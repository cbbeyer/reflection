# Assignment: Reflection

For this assignment, you'll need to know two principles.  Read about these principles if you need to.

* Reflection is a type of programming that investigates objects for fields and methods at runtime.  It allows all sorts of dynamic programming to be done.
* Serialization is converting an object to data so it can be stored or transferred.

For this assignment, use reflection to create a method that can serialize objects to JSON -- without knowing the fields beforehand.  You need to support these types of fields:

* null
* boolean
* float
* integer
* string
* user-defined objects (BirthDate, Person)

The to_json() method should print the JSON to the console.

## JSON Format

Be sure the check the rules of the JSON format.  Here are a couple of hints:

* JSON specifies the use of double-quotes, not single quotes.
* The last item in a given level should not have a comma after it.
* Be sure to escape double-quotes and backslashes in string values.  You are not required to support other special characters like backspace, newline, etc.
* null/None/nil is listed as `null` in JSON.
* Booleans are listed as `false` or `true` in JSON.
* You are not required to support lists or dictionaries as fields values (you *do* need to worry about embedded objects).
* You are not required to support circular references in objects.

## Recursive Behavior

When your algorithm encounters a field value that is another object, store a dictionary of its values.  In other words, recursively call your serializer, setting the return value under that field.  Increase the tab spacing each time your recurse to a deeper level.


## Test Code

Create unit tests as needed to test your functions as you code.


## Submitting the Assignment

Run your program and store the output to `output.json`.  It should match `sample_output.json`.

Submit your code as a single zip file (even if they are not together in your actual program).  Submit this file on Learning Suite.
