import Assignment6_1
import utils

records = [
    dict(year='1988', intro='Jun-88'),
    dict(year='1989', intro='May-89'),
    dict(year='2005', intro='5-May'),
    dict(year='2013', intro='13-Nov'),
    dict(year='2014', intro='14-Jan')
]


for row in records:
    print('Input Record - ', row)
    print('Date joined -', Assignment6_1.get_date_joined(row['year'], row['intro']))
    print('Days since joined -', Assignment6_1.days_since_joined(row['year'], row['intro']))

    print()
