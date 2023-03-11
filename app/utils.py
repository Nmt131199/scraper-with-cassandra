import datetime

def uuid1_time_to_datetime(time:int):
    """
    Start datetime is on October 15th, 1582
    add the time from uuid.uui1().time 
    divided by 10
    """
    return datetime.datetime(1582, 10, 15) + datetime.timedelta(microseconds=time//10)