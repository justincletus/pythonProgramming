def TowerofHanoi(n, from_rod, to_rod, aux_rod):
    if n==1:
        print("move disk 1", from_rod , "to 2 ", to_rod)
        return
    TowerofHanoi(n-1, from_rod, aux_rod, to_rod)
    print("move to disk ", n, "from rod", from_rod, "to_rod", to_rod)
    TowerofHanoi(n-1, aux_rod, to_rod, from_rod)

n = 4

TowerofHanoi(n, \'A\', \'C\', \'B\')
