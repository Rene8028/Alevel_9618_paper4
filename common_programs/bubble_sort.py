import random

from gui_array import gui_array
@gui_array(delay=0.8)  # 可以调整延迟时间来控制动画速度

def bubble_sort(arr):
    """
    冒泡排序算法
    通过重复遍历列表，比较并交换相邻的元素来实现排序。
    每次遍历后，最大的元素会"浮"到序列的末尾。
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # 比较相邻元素
            if arr[j] > arr[j + 1]:
                # 交换它们
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 如果没有发生交换，说明已经排序完成
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    data = [random.randint(5, 99) for _ in range(15)]
    print("原始数组:", data)
    
    bubble_sort(data.copy())
