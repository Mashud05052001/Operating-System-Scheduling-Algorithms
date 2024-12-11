# FCFS
# Process : [ arrival_time , burst_time, process_id ]
# Find out the : [ complete_time, turn_around_time, waiting_time, chart ]

def fcfs(process_list):
    t=0
    gantt = []
    completed = {}
    process_list.sort() 
    while process_list:
        if process_list[0][0] > t:
            t += 1
            gantt.append('Idle')
            continue
        else:
            process = process_list.pop(0)
            gantt.append(process[2])
            t+=process[1]
            process_id = process[2]
            ct = t
            tat = ct - process[0]
            wt = tat -  process[1]
            rt = wt
            completed[process_id] = [ct,tat,wt,rt]

    print("\nGantt Chart : ", " -> ".join(gantt))
    print("\nProcess Completion Table:")
    print(f"{'Process':<10}{'CT':<10}{'TAT':<10}{'WT':<10}{'RT':<10}")
    for pid, values in completed.items():
        print(f"{pid:<10}{values[0]:<10}{values[1]:<10}{values[2]:<10}{values[3]:<10}")
    



process_list = [[0,5,"p1"],[2,3,"p2"],[1,4,"p3"],[3,1,"p4"],[4,2,"p5"]]
fcfs(process_list)

