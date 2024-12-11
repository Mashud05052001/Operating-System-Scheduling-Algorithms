# HRRN
# Process : [ burst_time, arrival_time, process_id ]
# Find out the : [ complete_time, turn_around_time, waiting_time, chart ]

def hrrn(process_list):
    t = 0
    gantt = []
    completed = {}

    while process_list:
        available = []
        for p in process_list:
            if p[1] <= t :   
                available.append(p)
        if available == [] :
           t += 1
           gantt.append('Idle')
           continue
       
        response_ration_data = []
        for process in available:
            bt = process[0]
            at = process[1]
            wt = t - at
            rr = (wt + bt) / bt
            response_ration_data.append((rr, process))
        
        response_ration_data.sort(reverse=True)
        selectedProcess = response_ration_data[0][1]
        gantt.append(selectedProcess[2])
        process_list.remove(selectedProcess)
        processId = selectedProcess[2]
        at = selectedProcess[1]
        bt = selectedProcess[0]
        t += bt
        ct = t
        tat = ct-at 
        wt = tat - bt
        rt = wt 
        completed[processId] = [ct,tat,wt,rt]


    print("\nGantt Chart : ", " -> ".join(gantt))
    print("\nProcess Completion Table:")
    print(f"{'Process':<10}{'CT':<5}{'TAT':<5}{'WT':<5}{'RT':<5}")
    for pid, values in completed.items():
        print(f"{pid:<10}{values[0]:<5}{values[1]:<5}{values[2]:<5}{values[3]:<5}")


process_list = [[5, 1, "p1"], [7, 2, "p2"], [3, 4, "p3"], [1, 3, "p4"], [2, 5, "p5"]]
hrrn(process_list)
