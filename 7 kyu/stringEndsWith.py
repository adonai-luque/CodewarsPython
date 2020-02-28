def solution(string, ending):
    return True if ending == '' else string.split(ending)[-1] == ''

def solution(string, ending):
    return ending == string[len(string)-len(ending):]