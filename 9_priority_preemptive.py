# Priority : Non Preemptive
# Process : [ priority, arrival_time, burst_time,  process_id ]
# Find out the : [ complete_time, turn_around_time, waiting_time ]

def preemtive_priority(process_list):
    t = 0
    gantt = []
    completed = {}
    burst_times = {}
    for item in process_list:
        burst_times[item[3]] = item[2]
    while process_list:
        available = []
        for item in process_list : 
            if item[1] <= t : 
                available.append(item)
        if(item==[]):
            gantt.append('Idle')
            t += 1
            continue
        else:
            available.sort()
            process = available[0]
            gantt.append(process[3])
            process_list.remove(process)
            bt = process[2]
            if(bt>1):
                process[2] -= 1
                process_list.append(process)
                t += 1
            else:
                t += 1
                gantt.append(f"|{t}|")
                ct = t
                at = process[1]
                bt = burst_times[process[3]]
                tat = ct - at 
                wt = tat - bt 
                completed[process[3]] = [ct, tat, wt]


    
    print("\nGantt Chart : ", " -> ".join(gantt))
    print("\nProcess Completion Table:")
    print(f"{'Process':<10}{'CT':<5}{'TAT':<5}{'WT':<5}")
    for pid, values in completed.items():
        print(f"{pid:<10}{values[0]:<5}{values[1]:<5}{values[2]:<5}")





process_list = [
    [5, 2, 6, "p1"], 
    [2, 5, 2, "p2"], 
    [4, 1, 8, "p3"], 
    [1, 0, 3, "p4"], 
    [3, 4, 4, "p5"]
]
preemtive_priority(process_list)