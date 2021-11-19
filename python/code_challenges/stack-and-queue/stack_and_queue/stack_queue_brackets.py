from stack_and_queue.stack_and_queue  import Stack
def Multi_Bracket_Validation(str):

    open_brackect_list = ["(","[","{"]
    close_brackect_list= [")","]","}"]
    stack = Stack()
    for bracket in str:
        if bracket in open_brackect_list:
            stack.push(bracket)
        elif bracket in close_brackect_list:
            if not stack.is_empty():
                index_bracket = stack.pop()
                if (open_brackect_list.index(index_bracket) != close_brackect_list.index(bracket)):
                    return False
                else:
                    continue
            else:
                return False
    if stack.is_empty() :
        return True
    else:
        return False


if __name__ == "__main__":

    print(Multi_Bracket_Validation('()}})')) # false
    print(Multi_Bracket_Validation('{}{Code}[Fellows](())'))  #true
    print(Multi_Bracket_Validation('{)'))
    print(Multi_Bracket_Validation('{}(){}'))
    print(Multi_Bracket_Validation('{}'))
