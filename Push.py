from datetime import datetime
import os

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

os.system('git add .')
os.system('git commit -m"{0}"'.format(dt_string))
os.system('git push')
