def create_phone_number(n):
    nStr = [str(i) for i in n]
    return '(' + ''.join(nStr[0:3]) + ') ' + ''.join(nStr[3:6]) + '-' + ''.join(nStr[6:10])

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))

"""def create_phone_number(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)"""

"""def create_phone_number(n):
  str1 =  ''.join(str(x) for x in n[0:3])
  str2 =  ''.join(str(x) for x in n[3:6])
  str3 =  ''.join(str(x) for x in n[6:10])


  return '({}) {}-{}'.format(str1, str2, str3)"""