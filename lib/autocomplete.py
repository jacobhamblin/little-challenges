def possibilities_slow(query, possible):
    results = []
    for item in possible:
        if item.startswith(query):
            results.append(item)
    return results
