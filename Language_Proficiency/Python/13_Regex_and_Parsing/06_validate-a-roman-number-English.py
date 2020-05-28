thousand = r'M{0,3}'
hundred = r'(C[MD]|D?C{0,3})'
ten = r'(X[CL]|L?X{0,3})'
digit = r'(I[VX]|V?I{0,3})'
regex_pattern = thousand + hundred + ten + digit +'$'
import re
print(str(bool(re.match(regex_pattern, input()))))