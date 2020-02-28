#n = 12345
#print(max(str(n)))
"""def descending_order(num):

    def descending_order_str(s):
        if len(s) == 1:
            return s
        else:
            return max(s) + descending_order_str(s.replace(max(s), '', 1))

    return int(descending_order_str(str(num)))
"""
def descending_order(num):
    return (int(''.join(sorted(str(num), reverse = True))))
print(descending_order(1357526))