class variables_hd():
    hd_zone = []
    decision = []
    mutex = 0
    
    for i in range(2):
        decision[i] = Lock()
        hd_zone.append(False)
