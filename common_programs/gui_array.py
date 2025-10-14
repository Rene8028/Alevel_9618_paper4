import tkinter as tk
import threading
import time
from typing import List, Sequence
from typing import Callable,Optional

# ---------- 智能数组代理类 ----------
class TrackedArray:
    def __init__(self, arr: list, callback: Optional[Callable] = None):
        self._arr = list(arr)
        self._callback = callback
        self._accessed_indices = set()
        self._modified_index = -1
        self._comparing_indices = []  # 改为列表以保持访问顺序
        self._last_operation = None
        self._old_value = None
        self._in_callback = False  # 防止递归
        self._should_trigger = True  # 控制回调触发
        self._last_compare_idx = None  # 上一个比较的索引
        
    def __len__(self):
        return len(self._arr)
        
    def get_raw_array(self):
        """返回原始数组的副本，不触发回调"""
        return list(self._arr)
        
    def clear_access_history(self):
        """清除访问历史"""
        self._accessed_indices.clear()
        self._comparing_indices.clear()
        self._modified_index = -1
        self._last_compare_idx = None
        self._should_trigger = True
        
    def get_sorted_range(self) -> int:
        """自动检测已排序范围（从前到后检查升序）"""
        if len(self._arr) <= 1:
            return 0
            
        for i in range(len(self._arr) - 1):
            if self._arr[i] > self._arr[i + 1]:
                return i
        return len(self._arr) - 1  # 全部有序
        
    def __getitem__(self, idx):
        if isinstance(idx, int):
            self._accessed_indices.add(idx)
            if self._modified_index != idx:  # 不是在设置值的过程中访问
                # 如果这是第一个比较的数
                if not self._comparing_indices:
                    self._comparing_indices.append(idx)
                    self._last_compare_idx = idx
                    self._should_trigger = False  # 暂不触发回调
                # 如果这是第二个比较的数
                elif idx != self._last_compare_idx:
                    self._comparing_indices.append(idx)
                    self._last_operation = (
                        f"Compare: {self._arr[self._comparing_indices[0]]} "
                        f"(at {self._comparing_indices[0]}) to "
                        f"{self._arr[self._comparing_indices[1]]} "
                        f"(at {self._comparing_indices[1]})"
                    )
                    self._should_trigger = True  # 现在可以触发回调
                
            if self._callback and not self._in_callback and self._should_trigger:
                self._in_callback = True
                self._callback(self)
                self._in_callback = False
                if len(self._comparing_indices) >= 2:  # 完成一次比较后清除历史
                    self.clear_access_history()
        return self._arr[idx]
        
    def __setitem__(self, idx, val):
        if isinstance(idx, int):
            self.clear_access_history()  # 在设置新值前清除历史
            self._old_value = self._arr[idx]
            self._arr[idx] = val
            self._modified_index = idx
            self._comparing_indices.clear()  # 清除比较状态
            self._last_operation = f"Edit: {val} <-- {self._old_value} (at {idx})"
            if self._callback and not self._in_callback:
                self._in_callback = True
                self._callback(self)
                self._in_callback = False
            self.clear_access_history()  # 操作完成后清除历史
        
    def __str__(self):
        return str(self._arr)
        
    def __repr__(self):
        return repr(self._arr)

# ---------- 自动可视化装饰器 ----------
def gui_array(delay: float = 1.0,
              width: int = 60,
              height: int = 60,
              spacing: int = 10,
              top_margin: int = 20,
              bottom_margin: int = 20):
    """智能可视化装饰器：自动追踪数组访问和修改"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            root = tk.Tk()
            root.geometry("200x200")
            root.title("Array Visualizer – " + func.__name__)
            canvas = tk.Canvas(root, bg="white")
            canvas.pack(fill="both", expand=True)

            rects: List[int] = []
            texts: List[int] = []
            old_arr: Sequence[int] = []

            # ---------- 动态计算所需窗口大小 ----------
            def compute_geometry(arr):
                w = len(arr) * (width + spacing) + spacing
                h = top_margin + height + bottom_margin + 60  # 增加空间来显示操作说明
                return max(w, 300), max(h, 250)  # 增加最小高度

            # ---------- 窗口居中 ----------
            def center_window(w, h):
                sw = root.winfo_screenwidth()
                sh = root.winfo_screenheight()
                x = (sw - w) // 2
                y = (sh - h) // 2
                root.geometry(f"{w}x{h}+{x}+{y}")

            # ---------- 可视化状态 ----------
            class VisualizerState:
                def __init__(self):
                    self.sorted_range = -1
                    self.current_key_idx = -1
                    self.comparing_idx = -1
                    self.accessed_indices = set()
                    self.operation_text = ""

                def update(self, arr_state: TrackedArray):
                    self.current_key_idx = arr_state._modified_index
                    self.accessed_indices = set(arr_state._accessed_indices)
                    self.sorted_range = arr_state.get_sorted_range()
                    self.operation_text = arr_state._last_operation or ""
                    
                    # 更新比较状态
                    if len(arr_state._comparing_indices) >= 2:
                        self.comparing_idx = arr_state._comparing_indices[1]  # 显示第二个比较的元素
                        self.accessed_indices.add(arr_state._comparing_indices[0])  # 第一个元素显示为访问过
                    elif len(arr_state._comparing_indices) == 1 and not arr_state._should_trigger:
                        # 如果只有一个比较元素且不应触发回调，不显示任何比较状态
                        self.comparing_idx = -1
                        self.accessed_indices.clear()
                    else:
                        self.comparing_idx = -1

            # ---------- 绘制数组 ----------
            def draw_array(arr: Sequence[int], state: VisualizerState):
                canvas.delete("all")
                rects.clear()
                texts.clear()

                # 1. 标题
                canvas.create_text(
                    canvas.winfo_width() // 2, 12,
                    text=func.__name__,
                    font=("Arial", 20, "bold"),
                    fill="black"
                )

                # 2. 数组元素
                x0 = spacing
                y0 = top_margin + 25
                for i, v in enumerate(arr):
                    # 根据状态决定颜色
                    color = "lightblue"  # 默认颜色
                    if i <= state.sorted_range:
                        color = "#90EE90"  # 浅绿色：已排序部分
                    if i == state.current_key_idx:
                        color = "#FF9999"  # 红色：当前修改的元素
                    if i == state.comparing_idx:
                        color = "yellow"   # 黄色：正在比较的元素
                    elif i in state.accessed_indices:
                        color = "#FFE5B4"  # 浅橙色：被访问过的元素
                    
                    r = canvas.create_rectangle(
                        x0, y0, x0 + width, y0 + height,
                        fill=color, outline="black")
                    t = canvas.create_text(
                        x0 + width // 2, y0 + height // 2,
                        text=str(v), font=("Arial", 18))
                    rects.append(r)
                    texts.append(t)
                    x0 += width + spacing

                # 3. 操作说明文本
                if state.operation_text:
                    canvas.create_text(
                        canvas.winfo_width() // 2,
                        y0 + height + 30,
                        text=state.operation_text,
                        font=("Arial", 14),
                        fill="black"
                    )
                
                root.update_idletasks()

            # ---------- 回调和状态管理 ----------
            visualizer_state = VisualizerState()
            
            def update_gui(arr: Sequence[int], key_idx: int = -1, comparing_idx: int = -1):
                nonlocal old_arr
                
                # 获取要显示的数组
                display_arr = arr.get_raw_array() if isinstance(arr, TrackedArray) else list(arr)
                
                if not old_arr:
                    ww, wh = compute_geometry(display_arr)
                    center_window(ww, wh)
                
                if isinstance(arr, TrackedArray):
                    visualizer_state.update(arr)
                else:
                    visualizer_state.current_key_idx = key_idx
                    visualizer_state.comparing_idx = comparing_idx
                    
                old_arr = display_arr
                root.after(0, draw_array, display_arr, visualizer_state)
                time.sleep(delay)

            # ---------- 启动算法线程 ----------
            def run_algo():
                # 将输入数组包装成可追踪数组
                if args:
                    tracked_arr = TrackedArray(args[0], update_gui)
                    new_args = (tracked_arr,) + args[1:]
                else:
                    new_args = args
                
                func(*new_args, **kwargs)

            threading.Thread(target=run_algo, daemon=True).start()
            root.mainloop()

        return wrapper
    return decorator


"""
数组算法可视化模块

这个模块提供了一个装饰器，可以为操作数组的算法添加实时可视化功能。
它能自动追踪数组的访问、比较和修改操作，并以图形化方式展示算法的执行过程。

使用示例:
    from gui_array import gui_array
    
    @gui_array()
    def your_sort_algorithm(arr):
        # 你的算法代码
        pass
        
    # 调用你的算法
    your_sort_algorithm([64, 34, 25, 12, 22, 11, 90])

颜色说明:
    - 浅蓝色: 默认颜色，未处理的元素
    - 浅绿色: 已排序/处理完成的部分
    - 红色: 当前正在修改的元素
    - 黄色: 正在比较的元素
    - 浅橙色: 已经访问过的元素
"""

if __name__ == "__main__":
    print("This is a module for visual array operations, please use through import.")