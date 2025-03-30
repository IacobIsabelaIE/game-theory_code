import random

def define_probability(n, k): 

    stay_win = 0
    switch_win = 0

    for i in range(0, k): 

        doors = []
        for j in range(0, n): 
            doors.append(j)

        gift_door = random.randint(0, n - 1)
        choice = random.randint(0, n - 1) 

        openable_doors = []
        for door in doors: 
            if door != gift_door and door != choice: 
                openable_doors.append(door)

        eliminated_doors = random.sample(openable_doors, n - 2)

        remaining_doors = []
        for door in doors:
            if door not in eliminated_doors:
                remaining_doors.append(door)

        for door in remaining_doors:
            if door != choice:
                other_door = door

        if choice == gift_door: 
            stay_win =stay_win + 1

        if other_door == gift_door: 
            switch_win = switch_win + 1

    return stay_win / k, switch_win / k


print(define_probability(10, 10000))
