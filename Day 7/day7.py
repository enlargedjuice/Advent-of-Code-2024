import itertools

with open('Day 7/puzinp.txt', 'r') as file:
    samp_inp = file.read()

problems = samp_inp.splitlines()

answers = []
numbers = []
#putting everything into a nice dictionary! finally get to use one :), nvm dictionaries are evil for this problem
for item in problems:
    refined = item.split(":")
    refined[1] = refined[1].split()
    answers.append(refined[0])
    numbers.append(refined[1])


#ignore order of operations
def order_ignorer(items):
    result = int(items[0])
    for i in range(1, len(items), 2):
        operator = items[i]
        number = int(items[i + 1])
        if operator == '+':
            result += number
        elif operator == '*':
            result *= number
    return result

def problem_checker(ans,num):
    #first get all possible combinations of operations, a lot simpler than I originally thought!
    correct_keys = []
    ops = "+*"
    for key in ans:
        ind = ans.index(key)
        #so many combinations!
        op_comb = list(itertools.product(ops,repeat = len(num[ind])-1))
        #quick way to check if everything is a power of 2
        #print(len(op_comb))

        #combine numbers and operators, also formats it!
        expression = []
        for operators in op_comb:
            exp = []
            for number, operator in zip(num[ind], operators + (None,)):
                    exp.append(number)
                    if operator is not None:
                        exp.append(operator)
            expression.append(exp)
            
   
        #check if they're right
        for exp in expression:
            result = order_ignorer(exp)
            #print(f"{exp} = {result}, {key}")
            fin_result = int(result)
            test_key = int(key)
            #print(f"{exp} = {fin_result}, {key}")
            
            if fin_result == test_key:
                
                #print(f"{dict[key]} is correct!")
                correct_keys.append(fin_result)
                break
            else:
                continue
    return correct_keys

print(f"Sum of correct values: {sum(problem_checker(answers,numbers))}")
#DICTIONARY FUCKED ME
 

