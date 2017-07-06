#Reversing month and date

import re

str="June 10 1994, June 11 1994, June 12 1994, June 13 1994"
regex=r"([a-zA-Z]+) (\d+) (\d+)"
print(re.sub(regex,r"\3\\2\\1",str))



#End of file