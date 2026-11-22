# this prompet is for plus and minus with time
import datetime
now = datetime.datetime.now()
# we use this two datetime for point the exact datetime and now() for function
two_week_later = now + datetime.timedelta(weeks=2)
print(f"یک هقته یغد: {two_week_later}")
