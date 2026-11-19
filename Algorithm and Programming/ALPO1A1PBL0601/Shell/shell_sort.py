import time

def show_step(text, delay):
    # \r moves the cursor back to the start of the line, so each new message overwrites the last one
    print(f"\r{text:<60}", end="", flush=True)
    time.sleep(delay)

def shell_sort(arr, delay):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                show_step(f"Gap {gap}: moving {arr[j - gap]} from index {j - gap} to {j}", delay)
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
            show_step(f"Gap {gap}: placing {temp} at index {j}", delay)

        print()  # new line after each gap round
        gap //= 2

numbers = [98, 254, 344, 171, 13, 19, 44, 366, 108, 515, 173, 91, 480, 217, 927, 445, 119, 807, 122, 819, 749, 679, 185, 899, 955, 791, 476, 564, 241, 469, 488, 695, 155, 371, 752, 130, 657, 553, 615, 90, 487, 770, 528, 406, 406, 615, 180, 400, 692, 679]

shell_sort(numbers, delay=0.05)
print("Final:", numbers)