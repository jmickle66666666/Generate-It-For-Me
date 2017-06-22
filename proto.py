# prototype for Generate It For Me
# goals of prototype: generate simple functions that input one integer and output one integer
#                     user must provide a list of inputs and outputs to check against

# First unit test. Outputs are equal to input + 1
simple_addition_tests = {
    "name" : "Add 1",
    "input" : [0, 1, 2, -1, -2, -3, 15, 100, 99, -75, 43422, -2305],
    "output" : [1, 2, 3, 0, -1, -2, 16, 101, 100, -74, 43423, -2304]
}

double_tests = {
    "name" : "Double",
    "input" : [0, 1, 2, -1, -2, -3, 15, 100, 99, -75, 43422, -2305],
    "output" : [0, 2, 4, -2, -4, -6, 30, 200, 198, -150, 86844, -4610]
}

double_minus_one_tests = {
    "name" : "Double, Minus 1",
    "input" : [0, 1, 2, -1, -2, -3, 15, 100, 99, -75, 43422, -2305],
    "output" : [-1, 1, 3, -3, -5, -7, 29, 199, 197, -151, 86843, -4611]
}

minus_three_triple_minus_one = {
    "name" : "Minus 3, Triple, Minus 1",
    "input" : [0, 1, 2, -1, -2, -3, 15, 100, 99, -75, 43422, -2305],
    "output" : [-10, -7, -4, -13, -16, -19, 35, 290, 287, -235, 130256, -6925]
}

# First generation test. has a set of template lines of code and brute forces through them until
# it passes the unit test. outputs a string defining the function. max_lines is maximum lines of code
# for it to use
def generate_function(unit_tests, max_lines):
    # setup
    template_header = "def genfunc(inval):\n"
    template_footer = "    return inval\n"

    func_lines = ["inval $o= $v"]
    operators = ["+","-","/","*","%","**","//"]
    values = [0, 1, 2, 3]

    def build_code(code):
        output = ""
        output += template_header
        for c in code:
            output += "    "+c+"\n"
        output += template_footer
        return output

    def genlines(code, lines):
        stop = False
        for o in operators:
            for v in values:
                output = code[:]
                new_line = func_lines[0].replace("$o", o).replace("$v", str(v))
                output.append( new_line )
                if lines == 1:
                    if test_function_ok(build_code(output), unit_tests):
                        return [output, "stop"]
                else:
                    next_iter = genlines(output, lines-1)
                    if next_iter[1] == "stop":
                        return next_iter
                if stop: break
            if stop: break
        return [output,"continue"]

    for bleh in range(max_lines):
        result = genlines([], bleh+1)
        if result[1] == "stop":
            return build_code(result[0])

    return False


def test_function_ok(test_function, unit_tests):

    if type(test_function) is str:
        exec(test_function)

    # inputs a function and checks against the unit tests
    passed = True
    for i in range(len(unit_tests["input"])):
        _input = unit_tests["input"][i]
        _exp_output = unit_tests["output"][i]
        try: 
            _output = genfunc(unit_tests["input"][i])
        except Exception:
            _output = None
            passed = False
            pass


        if _output != _exp_output and passed == True:
            passed = False

    return passed

for t in [simple_addition_tests, double_tests, double_minus_one_tests, minus_three_triple_minus_one]:
    print (t["name"])
    print ("")
    print(generate_function(t, 3))

