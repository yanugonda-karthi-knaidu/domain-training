from datetime import datetime
import pytz
b=pytz.timezone('Asia/Kolkata')
res=datetime.now(b)
print(res)
