# "seats" is the input file

def binary_seats(pattern:str,upper_bound_string:str,quantity):
    scan = range(quantity)
    for partition in pattern:
        mid_part = int(len(scan)/2)
        if partition == upper_bound_string:
            scan = range(min(scan)+mid_part,max(scan)+1)
#             print(scan)
        else:
            scan = range(min(scan),min(scan)+mid_part)
#             print(scan)
    assert(len(scan)) ==1 
    return scan[0]

highest_id = 0
seat_id_list =[]
for seat in seats:
    rows = seat[:-3]
    columns = seat[-3:]
    row_number = binary_seats(pattern = rows, upper_bound_string = 'B', quantity=128)
    column_number = binary_seats(pattern = columns, upper_bound_string = 'R', quantity=8)
    seat_id = row_number * 8 + column_number
    if seat_id > highest_id:
        highest_id = seat_id
    seat_id_list.append(seat_id)
print(highest_id)

possible_seats = sorted(seat_id_list)
for i in range(1,len(possible_seats)):
    if possible_seats[i]- possible_seats[i-1] == 2:
        print(possible_seats[i]-1)

