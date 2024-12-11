# LRTF
# Process : [ burst_time, arrival_time, process_id ]
# Find out the : [ complete_time, turn_around_time, waiting_time ]


def lrtf(process_list):
    t = 0
    gantt = []
    completed = {}
    burst_times = {}
    # Storing the burst time in object
    for item in process_list:   
        burst_times[item[2]] = item[0]
    while process_list:
        available = []
        for item in process_list:
            if(item[1] <= t):
                available.append(item)
        
        
        if(available==[]):
            gantt.append('Idle')
            t += 1
            continue
        else:
            t += 1
            available.sort(key=lambda x: (-x[0], x[1]))
            process = available[0]
            copy_process = available.pop(0)
            gantt.append(process[2])
            process[0] -= 1 
            process_list.remove(copy_process)
            
            if(process[0]==0):
                at = process[1]
                ct = t
                tat = ct - at
                initial_bt = burst_times[process[2]]
                wt = tat - initial_bt
                completed[process[2]] = [ct, tat, wt]
                continue
            else:
                process_list.append(process)

    
    print("\nGantt Chart : ", " -> ".join(gantt))
    print("\nProcess Completion Table:")
    print(f"{'Process':<10}{'CT':<5}{'TAT':<5}{'WT':<5}")
    for pid, values in completed.items():
        print(f"{pid:<10}{values[0]:<5}{values[1]:<5}{values[2]:<5}")



process_list = [[5, 0, "p1"], [3, 1, "p2"], [1, 3, "p3"], [4, 2, "p4"], [2, 5, "p5"]]
lrtf(process_list)