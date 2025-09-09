# strftime stands for "string format time" - it converts a datetime object into a formatted string.

# Basic Concept:
datetime import datetime

now = datetime.now()  # datetime object: 2025-09-05 14:30:45.123456
formatted = now.strftime("%Y-%m-%d")  # string: "2025-09-05"

# Common Format Codes:
pythonnow = datetime.now()  # Let's say it's Sept 5, 2025, 2:30:45 PM

# DATE FORMATS
print(now.strftime("%Y"))      # 2025       (4-digit year)
print(now.strftime("%y"))      # 25         (2-digit year)
print(now.strftime("%m"))      # 09         (month as number)
print(now.strftime("%B"))      # September  (full month name)
print(now.strftime("%b"))      # Sep        (abbreviated month)
print(now.strftime("%d"))      # 05         (day of month)
print(now.strftime("%A"))      # Friday     (full weekday name)
print(now.strftime("%a"))      # Fri        (abbreviated weekday)

# TIME FORMATS
print(now.strftime("%H"))      # 14         (24-hour format hour)
print(now.strftime("%I"))      # 02         (12-hour format hour)
print(now.strftime("%M"))      # 30         (minutes)
print(now.strftime("%S