# round-robin
# Process : [ arrival_time, burst_time, process_id ]  must be in order
# Find out the : [ complete_time, turn_around_time, waiting_time ]

def round_robin(process_list, tq):
    t = 0
    gantt = []
    completed = {}
    burst_times = {}
    for item in process_list: burst_times[item[2]] = item[1]
    
    # Sort the process w.r.t. AT
    process_list.sort()

    while process_list:
        available = []
        for item in process_list:
            if item[0] <= t:
                available.append(item)
        if(available == []):
            t += 1
            gantt.append('Idle')
            continue
        else:
            process = available[0] # Work on this process
            gantt.append(process[2])
            # remove the process
            process_list.remove(process)
            remaining_bt = process[1]
            if(remaining_bt <= tq):
                t += remaining_bt
                at = process[0]
                bt = burst_times[process[2]]
                ct = t
                tat = ct - at 
                wt = tat - bt
                completed[process[2]] = [ct, tat, wt]
            else:
                t += tq
                process[1] -= tq
                process_list.append(process)
    

    print("\nGantt Chart : ", " -> ".join(gantt))
    print("\nProcess Completion Table:")
    print(f"{'Process':<10}{'CT':<5}{'TAT':<5}{'WT':<5}")
    for pid, values in completed.items():
        print(f"{pid:<10}{values[0]:<5}{values[1]:<5}{values[2]:<5}")



process_list = [[0, 5, "p1"], [1, 4, "p2"], [2, 2, "p3"], [4, 1, "p4"]]
tq = 1
round_robin(process_list, tq)