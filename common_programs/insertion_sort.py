import random

from gui_array import gui_array
@gui_array(delay=0.8)  # 可以调整延迟时间来控制动画速度

def insertion_sort(arr):
    """
    插入排序算法
    从第一个元素开始，该元素可以认为已经被排序
    取下一个元素，在已经排序的元素序列中从后向前扫描
    如果已排序的元素大于新元素，将该元素移到下一位置
    重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
    将新元素插入到该位置后
    重复步骤2~5
    """
    for i in range(1, len(arr)):
        # 当前要插入的元素
        key = arr[i]
        # 已排序部分的最后一个位置
        j = i - 1
        
        # 从后向前扫描已排序部分，寻找插入位置
        while j >= 0 and arr[j] > key:
            # 将大于key的元素都向后移动一位
            arr[j + 1] = arr[j]
            j -= 1
        
        # 找到了插入位置，将key放入
        arr[j + 1] = key
    
    return arr


if __name__ == "__main__":
    data = [random.randint(5, 99) for _ in range(15)]
    print("原始数组:", data)
    
    insertion_sort(data.copy())
