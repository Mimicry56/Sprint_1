time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
time_parts = time_string.split(',')
total_minutes = 0

for part in time_parts:
    if 'h' in part:
        hours_str = part.split('h')[0]
        hours = int(hours_str) 
        total_minutes += hours * 60
    part = part.replace(hours_str + 'h', '')

    if 'm' in part:
        minutes_str = part.split('m')[0]
        minutes = int(minutes_str)
        total_minutes += minutes
    part = part.replace(minutes_str + 'm', '')
        
    if 's' in part:
        second_str = part.split('s')[0]
        second = int(second_str)
        total_minutes += second / 60

print(f"Общее количество минут: {total_minutes}")