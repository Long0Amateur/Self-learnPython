# A programs asks the user for an algebraic expression and then inserts
# multiplication symbols where appropriate

# Visit: https://stackoverflow.com/questions/35929640/
# add-multiplication-signs-between-coefficients
 
# 3x+ 4y => 3*x + 4*y
# 3(x+5) => 3*(x+5)

import re

s = input('Enter an algebraic expression:\n')

s1 = re.sub(r"((?:\d+)|(?:[a-zA-Z]\w*\(\w+\)))((?:[a-zA-Z]\w*)|\()", r"\1*\2", s)

print('The result:\n',s1)
