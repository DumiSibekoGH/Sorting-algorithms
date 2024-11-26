import bubbleSort
import insertionSort
import quickSort
import time

# dictionary for sorting algorithms

list = ['x','a','t','b','j','y','d', 'n', 'b', 'f', 'y', 'q']

def get_algorithms(arg):
    algorithms = {
        1: lambda: insertionSort.sort(list),
        2: lambda: bubbleSort.sort(list),
        3: lambda: quickSort.sort(list)
    }

    return algorithms.get(arg)


option = input("Choose one:\n"
               "1. Insertion Sort\n"
               "2. Bubble sort\n"
               "3. Quick Sort\n")

sort = get_algorithms(int(option))


start_time = time.time()
sorted_list = sort()
end_time = time.time()

print(f"Sorted List: {sorted_list}")
print(f"Time Taken: {end_time - start_time:.10f} seconds")