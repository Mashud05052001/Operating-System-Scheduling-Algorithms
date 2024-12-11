# Priority : Non Preemptive
# Process : [ priority, arrival_time, burst_time,  process_id ]
# Find out the : [ complete_time, turn_around_time, waiting_time ]

def non_preemtive_priority(process_list):
    t = 0
    gantt = []
    completed = {}
    process_list.sort()

    while process_list:
        available = []
        for item in process_list:
            if(item[1] <= t): available.append(item)
        print(available, t)
        if(available == []):
            t += 1
            continue
        else:
            process = available[0]
            process_list.remove(process)
            gantt.append(process[3])
            t += process[2]
            at = process[1]
            bt = process[2]
            ct = t
            tat = ct - at
            wt = tat - bt
            completed[process[3]] = [ct,tat,wt]

    
    print("\nGantt Chart : ", " -> ".join(gantt))
    print("\nProcess Completion Table:")
    print(f"{'Process':<10}{'CT':<5}{'TAT':<5}{'WT':<5}")
    for pid, values in completed.items():
        print(f"{pid:<10}{values[0]:<5}{values[1]:<5}{values[2]:<5}")





process_list = [
    [5, 2, 6, "p1"], 
    [4, 5, 2, "p2"], 
    [1, 1, 8, "p3"], 
    [2, 0, 3, "p4"], 
    [3, 4, 4, "p5"]
]
non_preemtive_priority(process_list)