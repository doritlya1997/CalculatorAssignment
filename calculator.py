class Calculator:
    def __init__(self, assignmentExpressions):
        self.values = {}
        self.operandsStack = []
        self.operatorsStack = []
        self.assignmentExpressions = assignmentExpressions

    def _stacksPrinter(self):
        print(f"operandsStack: {self.operandsStack}")
        print(f"operatorsStack: {self.operatorsStack}")

    def _value(self, num):
        def _pre_post_compute(num, isPreCompute):
            # This function calculates the value of increment (i++/++i) and decrement (i--/--i)
            if type(num) not in [int, float] and not num.isnumeric():
                # handle increment (i++/++i)
                if num.find("++") > -1:
                    isPrefix = (num.find("++") == 0)
                    varName = num.strip("+")

                    # handle prefix (i++) and postfix (++i), like this:
                    #
                    # ++i: not(isPrefix=True  ^ isPreCompute=True)  = True -> change value before operation
                    # i++: not(isPrefix=False ^ isPreCompute=False) = True -> change value after operation
                    #
                    # ++i: not(isPrefix=True  ^ isPreCompute=False) = False -> do not change value after operation
                    # i++: not(isPrefix=False ^ isPreCompute=True)  = False -> do not change value before operation
                    if not (isPrefix ^ isPreCompute):
                        self._assign(varName, "+=", 1)
                    return varName
                # handle decrement (i--/--i)
                elif num.find("--") > -1:
                    isPrefix = (num.find("--") == 0)
                    varName = num.strip("-")

                    # handle prefix (i--) and postfix (--i)
                    if not (isPrefix ^ isPreCompute):
                        self._assign(varName, "-=", 1)
                    return varName
                else:
                    # No increment or decrement signs - just (i)
                    return num
        if type(num) in [int, float]:
            return num
        elif num.isnumeric():
            return float(num)

        # It is a variable
        varName = _pre_post_compute(num, isPreCompute=True)
        val = self.values.get(varName, None)
        _pre_post_compute(num, isPreCompute=False)
        if val:
            return val
        else:
            raise Exception("Variable not assigned")

    # returns calculation result
    def _compute(self, num1, num2, operator):
        match operator:
            case '+':
                # _pre_post_compute(num1, num2, isPreCompute=True)
                result = self._value(num1) + self._value(num2)
                # _pre_post_compute(num1, num2, isPreCompute=False)
                return result
            case '-':
                # _pre_post_compute(num1, num2, isPreCompute=True)
                result = self._value(num1) - self._value(num2)
                # _pre_post_compute(num1, num2, isPreCompute=False)
                return result
            case '*':
                # _pre_post_compute(num1, num2, isPreCompute=True)
                result = self._value(num1) * self._value(num2)
                # _pre_post_compute(num1, num2, isPreCompute=False)
                return result
            case '/':
                # _pre_post_compute(num1, num2, isPreCompute=True)
                num2_val = self._value(num2)
                if num2_val == 0:
                    raise Exception("ERROR: division by zero")
                result = self._value(num1) / num2_val
                # _pre_post_compute(num1, num2, isPreCompute=False)
                return result

    def _assign(self, outputVarName, assignOperation, outputVarValue):
        match assignOperation:
            case "=":
                self.values[outputVarName] = outputVarValue
            case "+=":
                prevVal = self.values.get(outputVarName, None)
                if prevVal:
                    self.values[outputVarName] = prevVal + outputVarValue
                else:
                    raise Exception("ERROR: variable does not exist")
            case "-=":
                prevVal = self.values.get(outputVarName, None)
                if prevVal:
                    self.values[outputVarName] = prevVal - outputVarValue
                else:
                    raise Exception("ERROR: variable does not exist")
            case "*=":
                prevVal = self.values.get(outputVarName, None)
                if prevVal:
                    self.values[outputVarName] = prevVal * outputVarValue
                else:
                    raise Exception("ERROR: variable does not exist")
            case "/=":
                prevVal = self.values.get(outputVarName, None)
                if prevVal:
                    if outputVarValue == 0:
                        raise Exception("ERROR: division by zero")
                    self.values[outputVarName] = prevVal / outputVarValue
                else:
                    raise Exception("ERROR: VarDoesNotExistError")
        print(f"{self.values}")

    # pops two number from operand stack and pushes result back
    def _pushAndCalculate(self, operator):
        num2 = self.operandsStack.pop()
        num1 = self.operandsStack.pop()
        self.operandsStack.append(self._compute(num1, num2, operator))

    def _calculate(self, exprArr):
        for op in exprArr:
            if op.isnumeric():
                self.operandsStack.append(op)
                self._stacksPrinter()

            elif op == ')':
                operator = self.operatorsStack.pop()
                self._stacksPrinter()

                # pops values until '(' sign comes
                while (operator != '('):
                    self._pushAndCalculate(operator)
                    operator = self.operatorsStack.pop()
                    self._stacksPrinter()

            elif op == '(':
                self.operatorsStack.append(op);
                self._stacksPrinter()

            elif op in ['*', '/']:
                prevOp = ''
                if len(self.operatorsStack) > 0:
                    prevOp = self.operatorsStack[len(self.operatorsStack) - 1]
                if prevOp in ['*', '/']:
                    operator = self.operatorsStack.pop()
                    self._stacksPrinter()
                    self._pushAndCalculate(operator)

                self.operatorsStack.append(op);
                self._stacksPrinter()

            elif op in ['+', '-']:
                prevOp = ''
                if len(self.operatorsStack) > 0:
                    prevOp = self.operatorsStack[len(self.operatorsStack) - 1]
                if prevOp in ['*', '/', '+', '-']:
                    operator = self.operatorsStack.pop()
                    self._stacksPrinter()
                    self._pushAndCalculate(operator)

                self.operatorsStack.append(op)
                self._stacksPrinter()
            else:
                # means it is var like (i, i++, ++i, etc)
                self.operandsStack.append(op)
                self._stacksPrinter()

        # after finishing reading the string expression, calculate the result of the remaining elements in the stacks
        while len(self.operatorsStack) > 0:
            operator = self.operatorsStack.pop()
            self._stacksPrinter()
            self._pushAndCalculate(operator)
        self._stacksPrinter()
        return self._value(self.operandsStack.pop())

    def evaluate(self):
        try:
            for assignment in self.assignmentExpressions:
                exprArr = assignment.split(' ')

                if exprArr[1] not in ['=','+=','-=','*=','/=']:
                    raise Exception("ERROR: Invalid expression contains numeric value in left side wing")

                if exprArr[0].isnumeric():
                    raise Exception("ERROR: Invalid expression contains numeric value in left side wing")

                val = self._calculate(exprArr[2:])
                self._assign(exprArr[0], exprArr[1], val)

            return self.values
        except Exception as error:
            print(error)
            return {}
