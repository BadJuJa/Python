import datetime
import time
import os



if __name__ == "__main__":
    with open('last_parse_time.txt', 'w') as lpt:
        lpt.write(str(datetime.datetime.now()))
    date = ""
    with open('last_parse_time.txt', 'r') as lpt:
        date = lpt.read()
    date = datetime.datetime.fromisoformat(date)