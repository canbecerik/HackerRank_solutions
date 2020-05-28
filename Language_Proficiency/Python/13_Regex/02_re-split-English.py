regex_pattern = r"[\,\.]{1}"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))