# from win10toast import ToastNotifier
import win10toast
# from random import randint

# def bubbleSort(array):
#     n = len(array)
#     for i in range(n):
#         already_sorted = True

#         for j in range(n - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j],  array[j + 1] = array[j + 1], array[j]
#                 already_sorted = False

#         if already_sorted:
#               break

#     return array


toaster = win10toast.ToastNotifier()
# array = [randint(-3000, 3000) for I in range(3000)]

toaster.show_toast('Bubble sort', 'The array is being sorted', icon_path=None, duration = 5, threaded = True)
# toaster.notification_active()

# while toaster.notification_active():
#     bubbleSort(array)

# toaster.show_toast('Bubble Sort', f"The array is sorted {array}", icon_path=None, duration = 10, threaded = False)

