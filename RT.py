import re
import sys
txt = sys.stdin.read()
m = re.findall(r'[^\w]([A-Za-z]{1,4}\d{3,7}[a-zA-Z]*)[^\w]', txt)
m = sorted(set(_.strip() for _ in m))
print('\n'.join(m))
