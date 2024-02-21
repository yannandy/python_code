def addTime(current_time, time_to_be_added, day = False):
    current_time = current_time.split(' ')
    period = ['AM', 'PM']
    x = period.index(current_time[1])
    print(x)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    current_time_hour_minutes = current_time[0].split(':')
    time_to_be_added_hour_minutes = time_to_be_added.split(':')
    result = {'hour':0, 'minutes': 0, 'period': 'PM', 'day_offset': 0}
    y = int(current_time_hour_minutes[0]) + int(time_to_be_added_hour_minutes[0]) + (int(current_time_hour_minutes[1]) + int(time_to_be_added_hour_minutes[1])) // 60
    offset_period = y // 12
    new_index = (x + offset_period) % 2
    result['day_offset'] = (y+12)//24 if x ==1 else y//24
    result['hour'] = y % 12
    result['minutes'] = (int(current_time_hour_minutes[1]) + int(time_to_be_added_hour_minutes[1])) % 60
    result['period'] = period[new_index]
    if day:
        index_day = days.index(day)
        new_index_day = (index_day + result['day_offset']) % 7
        jour = days[new_index_day]
        print(jour)
    print(result)
addTime("11:43 PM", "24:20")