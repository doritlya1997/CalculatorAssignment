# Assignment Calculator

This calculator can solve the following assignments, and return the final values of the variables:
    
    valid input:
    a = 40 - ( 4 + 6 / 2 ) * 5
    i = 0
    j = ++i
    x = i++ + 5
    y = 5 + 3 * 10 
    i += y

    output: 
    {i=37, j=1, x=6, y=35, a=5}

This project contains unit testing module to test the above supported calculations and invalid input, such as:

    invalid input:
    no assignment "2 + 3"
    assignment into number "9 = 3"
    division by zero " a = 7 / 0"
    using variable before definition "b = a" / "x *= 7" / "++j"

### The AssignmentCalculator supports:

* arithmetic operations by order: `(), *, /, +, -` 
* different types of assignment: `=, +=, -+, *=, /=`
* using variables to calculate right wing value: `x = y`
* using incrementing/decrementing variables: `x = i++ * --j`

### Arithmetic calculation explanation:

Sign Hierarcy
(upper to lower)

- `(`
- `* /`
- `+ -`

We calculate the arithmetic operations using `operandsStack` and `operatorsStack`. Operators and Operands are all given in string format at first.

* We split by spaces `" "`  and go over the items.
* If the item is a number we push it into `operandsStack`. 
* If the item is an operator we must follow these actions:
  * If the item is `(` push it into `operatorsStack`. 
  * If the item is `)` pop the operators from `operatorsStack` until `(` character. 
    * For every operator we pop, we also pop two operands (numbers or variables) from `operandsStack`.
    * We calculate the result of the `operand1 operator operand2` and push into `operandsStack`. 
  * If the item is one of these `[+, -, *, /]` we look at the previous operator (which is at the top of `operatorsStack`). 
    * If the new sign (`=item`) is in lower class in hierarchy compared to the previous operator:
      * Pop the signs from `operatorsStack` that have the upper class. 
      * For every operator we pop, we also pop two operands (numbers or variables) from `operandsStack`.
      * We calculate the result of the `operand1 operator operand2` and push into `operandsStack`.
    * If the new sign (`=item`) in upper class or equivalent compared to the previous operator (which is at the top of `operatorsStack`):
      * push the new sign to the `operatorsStack`.
* After finishing reading the string expression, calculate the result of the remaining elements in the stacks.
* When the `operatorsStack` is empty, the result of the entire calculation is the only number left in the `operandsStack`.

### Debug prints of arithmetic calculation:

For example: `i = 40 - ( 4 + 6 / 2 ) * 5`


* operandsStack: ['40']
operatorsStack: []

* operandsStack: ['40']
operatorsStack: ['-']

* operandsStack: ['40']
operatorsStack: ['-', '(']

* operandsStack: ['40', '4']
operatorsStack: ['-', '(']

* operandsStack: ['40', '4']
operatorsStack: ['-', '(', '+']

* operandsStack: ['40', '4', '6']
operatorsStack: ['-', '(', '+']

* operandsStack: ['40', '4', '6']
operatorsStack: ['-', '(', '+', '/']

* operandsStack: ['40', '4', '6', '2']
operatorsStack: ['-', '(', '+', '/']

* operandsStack: ['40', '4', '6', '2']
operatorsStack: ['-', '(', '+']

* operandsStack: ['40', '4', 3.0]
operatorsStack: ['-', '(']

* operandsStack: ['40', 7.0]
operatorsStack: ['-']

* operandsStack: ['40', 7.0]
operatorsStack: ['-', '*']

* operandsStack: ['40', 7.0, '5']
operatorsStack: ['-', '*']

* operandsStack: ['40', 7.0, '5']
operatorsStack: ['-']

* operandsStack: ['40', 35.0]
operatorsStack: []

* operandsStack: [5.0]
operatorsStack: []

output: `{'i': 5.0}`

## Run requirements

Open the project in Pycharm and run the `testCalculator` module.

