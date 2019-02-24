def most_meetings(meetings, availability):
    def get_duration(meeting):
        return meeting.get('duration')
    shortest_first = sorted(meetings, key=get_duration)
    i = 0
    time_spent = 0
    while i < len(meetings):
        duration = shortest_first[i].get('duration')
        if time_spent + duration <= availability:
            time_spent += duration
            i += 1
        else:
            break
    return shortest_first[:i]

def most_time(meetings, availability):
    return meetings
