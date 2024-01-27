Python Import & Modules
Modules 
- File containing set of functions you want to include in your application
- When using a function from a module, use the syntax: _module_name.function_name_.
-  You can create an alias when you import a module by using the as keyword

			import mymodule as mx
- if the module name is followed by `as`, then the name following `as` is bound directly to the imported module.

- There is a built in function to list all the function names(or variable names) in a module:

		     x = dir(platform)

- The ***dir()  function can be used on _all_ modules, also the ones you create yourself.

- You can choose to import only parts from a module, by using from keyword.

			from mymodule import person!
