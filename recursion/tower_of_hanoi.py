def tower_of_hanoi(n, source, helper, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, helper)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, helper, source, target)

if __name__ == "__main__":
    n = 3
    print(f"Tower of Hanoi with {n} disks:")
    tower_of_hanoi(n, "A", "B", "C")
