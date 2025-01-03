def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        else:
        	#스택이 빈 경우
            if stack == []:
                return False
         	#올바른 괄호 
            else:
                stack.pop()
    
    #'(' 남아있는 경우
    if stack != []:
        return False
    
    return True