
def Multi_Bracket_Validation(str):

    open_brackect_list = ["(","[","{"]
    close_brackect_list= [")","]","}"]
    stack = []
    for bracket in str:
        if bracket in open_brackect_list:
            stack.append(bracket)
        elif bracket in close_brackect_list:
            index_bracket = close_brackect_list.index(bracket)
            if ((len(stack) > 0) and (open_brackect_list[index_bracket] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False



if __name__ == "__main__":

    print(Multi_Bracket_Validation('()}})'))
    print(Multi_Bracket_Validation('{}{Code}[Fellows](())'))
    print(Multi_Bracket_Validation('{)'))
    print(Multi_Bracket_Validation('{}(){}'))
    print(Multi_Bracket_Validation('{}'))
