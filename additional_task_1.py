types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 

def delete_duplicates(tickets):
    encountered_tickets = []
    for key in tickets:
        for ticket in tickets[key]:
            if ticket not in encountered_tickets:
                encountered_tickets.append(ticket)
            else:
                tickets[key].remove(ticket)
    return tickets

def merge_dicts(types, tickets):
    tickets_by_type = {}
    for key, value in types.items():
        tickets_by_type[value] = tickets[key]
    return tickets_by_type