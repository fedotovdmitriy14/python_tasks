import time

def make_readable(seconds):
    full_hours = seconds // 86400
    print(full_hours)
    rest_time = seconds % 86400
    if full_hours == 0:
        return time.strftime('%H:%M:%S', time.gmtime(rest_time))
    else: 
        result = time.strftime('%H:%M:%S', time.gmtime(rest_time)).split(':')
        result[0] = int(result[0]) + 24 * full_hours
        result[0] = str(result[0])
        return ':'.join(result)


print(make_readable(3467856))
print(make_readable(86400))
print(make_readable(86400))
