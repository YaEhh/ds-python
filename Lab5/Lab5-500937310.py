class MyHeap():
    def __init__(self, size):
        self.original_size = size + 1
        self.arr = [None for i in range(0,size +1)]
        self.size = 0
        self.arr[0] = -1

    def swap(self, first, second):
        temp = self.arr[first]
        self.arr[first] = self.arr[second]
        self.arr[second] = temp

    def insert(self, data):
        if (self.size) >= (self.original_size - 1):
            newArr = [None for i in range(0, (self.original_size *2) - 1)]
            counter = 0
            for i in self.arr:
                if i == -1:
                    newArr[counter] = i
                    counter += 1
                else:
                    newArr[counter] = i
                    counter += 1

            self.arr = newArr
            self.original_size = len(self.arr) - 1


        self.size = self.size + 1
        self.arr[self.size] = data

        current_idx = self.size
        parentIdx = self.get_parent_node(current_idx)

        while (parentIdx and (self.arr[current_idx] > self.arr[parentIdx])):
            self.swap(current_idx, self.get_parent_node(current_idx))
            current_idx = self.get_parent_node(current_idx)
            parentIdx = self.get_parent_node(current_idx)
        # self.heapify(self.size)

    def heapify(self, idx):
        parent = self.get_parent_node(idx)
        largest = idx

        if self.arr[idx] > self.arr[parent]:
            self.swap(idx, parent)

    def extractMax(self):
        root = self.arr[1]

        for i in range(2, self.size + 2):
            self.arr[i - 1] = self.arr[i]

        self.size = self.size - 1
        self.sort()

        return root

    def sort(self):
        for i in range(self.size, 1, -1):
            self.heapify(i)


    def __len__(self):
        if self.size < 0:
            return 0
        else:
            return self.size

    def getData(self):
        newList = []
        for i in self.arr:
           if i != None:
                newList.append(i)

        return newList

    def get_parent_node(self, idx):
        if idx == 1:
            return None
        returnIdx = int(idx/2)
        return returnIdx

    def left(self, idx):
        if (2*idx < self.size):
            return (2* idx)
        else:
            return None

    def right(self, idx):
        if ((2 * idx) + 1) < self.size:
            return (2 * idx) + 1
        else:
            return None


# Test Cases Below
def heap_property_test(max_heap):
    # root = max_heap.arr[1]

    for i in range(1,5):
        # Check is left child is less than parent
        if max_heap.arr[i] > max_heap.arr[2*i + 1]:
            print(f"First Test Case - Parent node {max_heap.arr[i]} is greater than left child {max_heap.arr[2*i +1]}")
        else:
            print(f"Heap property not maintained - Test Case FAILED")
            return "FAILED"

        if max_heap.arr[i] > max_heap.arr[2*i + 2]:
            print(f"First Test Case - Parent node {max_heap.arr[i]} is greater than right child {max_heap.arr[2*i +2]}")
        else:
            print(f"First Test Case - Heap property not maintained - Test Case FAILED")
            return "FAILED"

    return "PASSED"

def run_all_test_cases():
    insert_values = [1, 11, 0, 42, 12, 54, 25, 1, 100, 75, 1, 4, 2, 8]
    print(f"The below test cases test the integrity of a Max Heap after having inserted the following keys one by one\n{insert_values}")
    max_heap = MyHeap(10)

    for i in insert_values:
        max_heap.insert(i)

    first_test_case_result = heap_property_test(max_heap)
    print(f"First test case: cheap_heap_property result - {first_test_case_result}")

    second_test_case_result = height_test(max_heap)
    print(f"Second test case: cheap_heap_property result - {second_test_case_result}")

    third_test_case_result = max_test(max_heap)
    print(f"Third test case: cheap_heap_property result - {third_test_case_result}")

def height_test(max_heap):
    if len(max_heap) == max_heap.size:
        print(f"Second Test Case - The height of {len(max_heap)} is equal to the expected value of 14")
    else:
        print(f"The height of {len(max_heap)} is incorrect - expected value is - Test Case FAILED")
        return "FAILED"

    return "PASSED"

def max_test(max_heap):
    max_heap_max = max_heap.extractMax()
    if  max_heap_max == 100:
        print(f"Third Test Case - The actual max value of {max_heap_max} matches the expected value")
    else:
        print(f"The actual max - {max_heap_max} - differs from expected value of - 100 ")

    return "PASSED"


run_all_test_cases()