
import random
from datetime import date, timedelta

def get_random_date(start_year, end_year):
    start_date = date(start_year, 1, 1)
    end_date = date(end_year, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    return random_date

# random_date = get_random_date(2000, 2024)
# print(random_date)
