from copy import copy

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
    meeting_combos = []
    for index in xrange(len(meetings)):
        if index == 0:
            meeting_combos += [[meetings[0].get('duration')], [0]]
        else:
            for row_i in xrange(len(meeting_combos)):
                copied_row = list(meeting_combos[row_i])
                copied_row.append(0)
                meeting_combos[row_i].append(meetings[index].get('duration'))
                meeting_combos.append(copied_row)
    best = [0, 0]
    for index in xrange(len(meeting_combos)):
        summed = sum(meeting_combos[index]) 
        if summed > best[1] and summed <= availability:
            best[1] = summed
            best[0] = index
    if best[1] == 0: return []
    return [
        meetings[i] for i in xrange(len(meeting_combos[best[0]]))
        if meeting_combos[best[0]][i]
    ]

def most_time_more_natural(meetings, availability):
    def helper(meetings, avail, combos, cur_combo):
        if avail == 0 or not len(meetings):
            combos.append(cur_combo)
        for meeting in meetings:
            if avail - meeting.get('duration') >= 0:
                new_meetings = list(meetings)
                new_meetings.remove(meeting)
                new_cur_combo = list(cur_combo)
                new_cur_combo.append(meeting)
                new_avail = avail - meeting.get('duration')
                helper(new_meetings, new_avail, combos, new_cur_combo)
            else:
                new_meetings = list(meetings)
                new_meetings.remove(meeting)
                helper(new_meetings, avail, combos, cur_combo)
    combos = []
    cur_combo = []
    helper(meetings, availability, combos, cur_combo)
    if not len(combos): return combos
    durations = [
        [meeting.get('duration') for meeting in combo] for combo in combos
    ]
    best = [0, 0]
    for index in xrange(len(durations)):
        summed = sum(durations[index]) 
        if summed > best[1] and summed <= availability:
            best[1] = summed
            best[0] = index
    return combos[best[0]]

def most_time_dp(meetings, availability):
    optimals = [{'meetings': [], 'value': 0, 'id_set': set()}]
    for index in xrange(1, availability + 1):
        best = [0, 0]
        for meeting in meetings:
            if index - meeting.get('duration') >= 0:
                prior = optimals[index - meeting.get('duration')]
                if meeting.get('id') in prior.get('id_set'):
                    continue
                new_sum = meeting.get('duration') + prior.get('value')
                if new_sum > best[0] and new_sum <= availability:
                    best[0] = new_sum
                    best[1] = meeting
        if best[1] is not 0:
            last_best = optimals[index - best[1].get('duration')]
            new_meetings = list(last_best.get('meetings'))
            new_meetings.append(best[1])
            id_set = copy(last_best.get('id_set'))
            id_set.add(best[1].get('id'))
            next_item = {'meetings': new_meetings, 'value': best[0], 'id_set': id_set}
            optimals.append(next_item)
        else:
            optimals.append(optimals[index - 1])
    return optimals[availability].get('meetings')
