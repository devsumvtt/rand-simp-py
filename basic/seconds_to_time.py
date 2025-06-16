"""convert the number of seconds into the real amount of time"""

inputSecond = int(input('Enter the number of seconds: '))




day = inputSecond // 86400
remainder = inputSecond % 86400
hour = remainder // 3600
remainder = remainder % 3600
minute = remainder // 60
second = remainder % 60

print(f'{inputSecond} seconds is equal to {day}d {hour}h {minute}m {second}s.')