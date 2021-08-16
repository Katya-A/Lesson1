for i in range(10):
    duration = int(input('duration sec:  '))
    if 60 > duration > 0:
        print('in sec =', duration)
    elif 60 <= duration < 3600:
        minute: int = duration // 60
        second: int = duration % 60
        print('in minute = ', minute, 'in second = ', second)
    elif 86400 > duration >= 3600:
        hour: int = duration // 3600
        second: int = duration % 60
        minute: int = (duration - hour * 3600) // 60
        print('in hour =', hour, 'in minute = ', minute, 'in second = ', second)
    else:
        print("false")
