#Testing some regular expressions

import re

regex = r"([a-zA-Z]+) (\d+)"
date_string = "June 10,1994"

search_obj = re.search(regex,date_string)
print(search_obj.start(),search_obj.end())


regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   June
    #   August
    #   Dec
    print ("Match month: %s" % (match))