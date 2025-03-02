#看到我证明可以从vs上更改代码
import tkinter as tk
from tkinter import ttk
import random

class SugarReductionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("果糖含量检测与减糖预估")
        self.root.geometry("800x600")  # 设置窗口大小

        # 创建并放置标签和输入框
        self.create_widgets()

    def create_widgets(self):
        # 果汁种类
        ttk.Label(self.root, text="果汁种类:").grid(column=0, row=0, padx=10, pady=5)
        self.juice_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.juice_var).grid(column=1, row=0, padx=10, pady=5)

        # 检测到的果糖含量
        ttk.Label(self.root, text="检测到的果糖含量 (g):").grid(column=0, row=1, padx=10, pady=5)
        self.fructose_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.fructose_var).grid(column=1, row=1, padx=10, pady=5)

        # 预估减糖后的果糖含量
        ttk.Label(self.root, text="预估减糖后的果糖含量 (g):").grid(column=0, row=2, padx=10, pady=5)
        self.reduced_fructose_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.reduced_fructose_var).grid(column=1, row=2, padx=10, pady=5)

        # 预估减糖时间
        ttk.Label(self.root, text="预估减糖时间 (分钟):").grid(column=0, row=3, padx=10, pady=5)
        self.reduction_time_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.reduction_time_var).grid(column=1, row=3, padx=10, pady=5)

        # 用户身高
        ttk.Label(self.root, text="用户身高 (cm):").grid(column=0, row=4, padx=10, pady=5)
        self.height_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.height_var).grid(column=1, row=4, padx=10, pady=5)

        # 用户体重
        ttk.Label(self.root, text="用户体重 (kg):").grid(column=0, row=5, padx=10, pady=5)
        self.weight_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.weight_var).grid(column=1, row=5, padx=10, pady=5)

        # 用户性别
        ttk.Label(self.root, text="用户性别:").grid(column=0, row=6, padx=10, pady=5)
        self.gender_var = tk.StringVar()
        self.gender_var.set("男")  # 默认值
        ttk.Combobox(self.root, textvariable=self.gender_var, values=["男", "女"]).grid(column=1, row=6, padx=10, pady=5)

        # BMI
        ttk.Label(self.root, text="BMI:").grid(column=0, row=7, padx=10, pady=5)
        self.bmi_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.bmi_var, state='readonly').grid(column=1, row=7, padx=10, pady=5)

        # 计算BMI按钮
        ttk.Button(self.root, text="计算BMI", command=self.calculate_bmi).grid(column=2, row=5, padx=10, pady=5)

        # 日志框
        ttk.Label(self.root, text="日志:").grid(column=0, row=8, padx=10, pady=5)
        self.log_text = tk.Text(self.root, height=15, width=80)  # 增加高度和宽度
        self.log_text.grid(column=0, row=9, columnspan=3, padx=10, pady=5)

        # 添加数据到日志按钮
        ttk.Button(self.root, text="添加到日志", command=self.add_to_log).grid(column=2, row=10, padx=10, pady=5)

        # DeepSeek智能健康指南输出框
        ttk.Label(self.root, text="DeepSeek智能健康指南:").grid(column=0, row=11, padx=10, pady=5)
        self.health_guide_text = tk.Text(self.root, height=10, width=80)  # 增加高度和宽度
        self.health_guide_text.grid(column=0, row=12, columnspan=3, padx=10, pady=5)

        # 随机生成数据按钮
        ttk.Button(self.root, text="随机生成数据", command=self.generate_random_data).grid(column=2, row=11, padx=10, pady=5)

    def calculate_bmi(self):
        try:
            height = float(self.height_var.get()) / 100  # 转换为米
            weight = float(self.weight_var.get())
            bmi = weight / (height ** 2)
            self.bmi_var.set(f"{bmi:.2f}")
        except ValueError:
            self.bmi_var.set("输入无效")

    def add_to_log(self):
        log_entry = (
            f"果汁种类: {self.juice_var.get()}, "
            f"果糖含量: {self.fructose_var.get()}g, "
            f"减糖后果糖含量: {self.reduced_fructose_var.get()}g, "
            f"减糖时间: {self.reduction_time_var.get()}分钟, "
            f"身高: {self.height_var.get()}cm, "
            f"体重: {self.weight_var.get()}kg, "
            f"性别: {self.gender_var.get()}, "
            f"BMI: {self.bmi_var.get()}\n"
        )
        self.log_text.insert(tk.END, log_entry)

    def generate_random_data(self):
        fruits = ["哈密瓜", "苹果", "草莓", "蓝莓", "香蕉", "梨子", "桃子", "柠檬", "桑葚", "葡萄", "橙子", "菠萝", "猕猴桃", "西瓜", "火龙果", "芒果", "荔枝", "杨梅"]
        for _ in range(10):
            # 随机生成数据
            juice = random.choice(fruits)
            fructose = random.uniform(8, 18)
            height = random.randint(155, 190)
            weight = random.randint(40, 100)
            gender = random.choice(["男", "女"])
            reduction_time = random.randint(60, 120)  # 1小时到2小时
            reduced_fructose_percentage = random.uniform(0.55, 0.70)
            reduced_fructose = fructose * reduced_fructose_percentage

            # 计算BMI
            bmi = weight / ((height / 100) ** 2)

            # 创建日志条目
            log_entry = (
                f"果汁种类: {juice}, "
                f"果糖含量: {fructose:.2f}g, "
                f"减糖后果糖含量: {reduced_fructose:.2f}g, "
                f"减糖时间: {reduction_time}分钟, "
                f"身高: {height}cm, "
                f"体重: {weight}kg, "
                f"性别: {gender}, "
                f"BMI: {bmi:.2f}\n"
            )

            # 将日志条目添加到日志框
            self.log_text.insert(tk.END, log_entry)

if __name__ == "__main__":
    root = tk.Tk()
    app = SugarReductionApp(root)
    root.mainloop()