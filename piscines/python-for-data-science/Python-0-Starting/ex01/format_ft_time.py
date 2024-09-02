import time
from datetime import date

print(f"Seconds since January 1, 1970: {int(time.time()):,.4f} or {time.time():.2e} in scientific notation")

print(f"{date.today():%B %d, %Y}")
