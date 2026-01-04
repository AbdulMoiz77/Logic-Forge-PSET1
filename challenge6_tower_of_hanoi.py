def towerOfHanoi(N, from_rod, to_rod, aux_rod ):
    if N == 1:
        print(f"Disk {N} moved from {from_rod} to {to_rod}")
        return

    towerOfHanoi(N-1, from_rod, aux_rod, to_rod)
    print(f"Disk {N} moved from {from_rod} to {to_rod}")
    towerOfHanoi(N-1, aux_rod, to_rod, from_rod)

if __name__ == "__main__":
    print("\nTower of Hanoi (Disks = 2):")
    towerOfHanoi(2, "A", "C", "B")

    print("\nTower of Hanoi (Disks = 3):")
    towerOfHanoi(3, "A", "C", "B")

    print("\nTower of Hanoi (Disks = 4):")
    towerOfHanoi(4, "A", "C", "B")        


