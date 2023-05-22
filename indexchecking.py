'''def print_indexes(arr):
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            print("Index:", i, "Value:", arr[i])

arr = [7, 2, 8, 4, 3, 9, 1]
print_indexes(arr)'''



'''def hey(a):
    for i in range(len(a)):
        if i == 0:
            if a[i] > a[i+1]:
                print(i)
        elif i == len(a)-1:
            if a[i] > a[i-1]:
                print(i)
        else:
            if a[i] > a[i-1] and a[i] > a[i+1]:
                print(i)

a = [7, 2, 8, 4, 3, 9, 1]
hey(a)'''



void print_indexes_of_greater_neighbors(int a[], int n) {
    for (int i = 0; i < n; i++) {
        if (i == 0) {
            if (a[i] > a[i+1]) {
                printf("%d ", i);
            }
        } else if (i == n-1) {
            if (a[i] > a[i-1]) {
                printf("%d ", i);
            }
        } else {
            if (a[i] > a[i-1] && a[i] > a[i+1]) {
                printf("%d ", i);
            }
        }
    }
}

