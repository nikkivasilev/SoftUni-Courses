total_of_pages = int(input())
pages_per_hour = int(input())
days_to_read = int(input())
total_hours_to_read = total_of_pages / pages_per_hour
hours_per_day = total_hours_to_read / days_to_read
print(int(hours_per_day))