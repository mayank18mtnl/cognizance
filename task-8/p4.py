# first letter upper case

import pandas as pd

ser=pd.Series(['amrita','school','of','engineering','chennai','campus'])
print("Main sentence ")
print(ser)
new=(ser.str.capitalize())
print(new)
