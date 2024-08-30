# write a script that formats the dates this way: Seconds since January 2, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$

import time

print("Seconds since January 2, 1970: {:.4f}".format(time.time()))
