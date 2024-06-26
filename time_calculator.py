def add_time(start, duration, starting_day=None):
  # Parse the start time
  start_time = start.split(":")
  start_hour = int(start_time[0])
  start_minutes = int(start_time[1].split(" ")[0])
  start_am_pm = str(start_time[1].split(" ")[1])
  #splitting the duration into hours and minutes
  duration_time = duration.split(":")
  duration_hour = int(duration_time[0])
  duration_minutes = int(duration_time[1])
  am_pm = {"AM": 0, "PM": 1}
  days = [
      "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
      "Sunday"
  ]
  total_minutes = (start_hour + duration_hour) * 60 + (start_minutes +
                                                       duration_minutes)
  end_hour = total_minutes // 60 % 12
  end_minutes = total_minutes % 60
  end_am_pm = am_pm[start_am_pm] + total_minutes // (12 * 60)
  days_later = total_minutes // (12 * 60)
  if end_hour == 0:
    end_hour = 12
  if end_am_pm == 0:
    end_am_pm = "AM"
  else:
    end_am_pm = "PM"
  if starting_day:
    starting_day = starting_day.capitalize()
    starting_day_index = days.index(starting_day)
    end_day_index = (starting_day_index + days_later) % 7
    end_day = days[end_day_index]
    day_output = f", {end_day}"
  else:
    day_output = ""
  time_output = f"{end_hour}:{end_minutes:02d} {end_am_pm}"
  if days_later == 0:
    return time_output + day_output
  elif days_later == 1:
    return time_output + day_output + " (next day)"
  else:
    return time_output + day_output + f"({days_later} days later)"
