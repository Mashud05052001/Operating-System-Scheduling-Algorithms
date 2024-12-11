# SJF
# Process : [ burst_time, arrival_time, process_id ]
# Find out the : [ complete_time, turn_around_time, waiting_time, chart ]

def sjf(process_list):
    t = 0
    gantt = []
    completed = {}

    while process_list:
        available = []
        for p in process_list:
            if p[1] <= t :   # Arrival time wise comparing & inserting
                available.append(p)
                
        if available == [] :
           t += 1
           gantt.append('Idle')
           continue
        else:
            available.sort()
            process = available[0]
            bt = process[0]
            at = process[1]
            pid = process[2]
            t += bt
            gantt.append(pid)
            ct = t
            tat = ct - at
            wt = tat - bt 
            rt = wt
            completed[pid] = [ct,tat,wt,rt]
            process_list.remove(process)



    print("\nGantt Chart : ", " -> ".join(gantt))
    print("\nProcess Completion Table:")
    print(f"{'Process':<10}{'CT':<5}{'TAT':<5}{'WT':<5}{'RT':<5}")
    for pid, values in completed.items():
        print(f"{pid:<10}{values[0]:<5}{values[1]:<5}{values[2]:<5}{values[3]:<5}")


process_list = [[2, 1, "p1"], [7, 2, "p2"], [3, 4, "p3"], [1, 3, "p4"], [5, 5, "p5"]]
sjf(process_list)
