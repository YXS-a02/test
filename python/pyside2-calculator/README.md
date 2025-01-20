# pyside2-calculator 项目说明

这是一个使用 PySide2 编写的简单计算器应用程序。该项目展示了如何使用 PySide2 创建图形用户界面，并实现基本的计算功能。

## 项目结构

```
pyside2-calculator
├── src
│   ├── main.py                # 应用程序入口点
│   ├── ui
│   │   └── calculator.ui      # 使用 Qt Designer 创建的用户界面文件
│   ├── controllers
│   │   └── calculator_controller.py  # 处理用户输入和计算逻辑
│   └── models
│       └── calculator_model.py # 存储计算器状态和数据
├── requirements.txt           # 项目所需的 Python 包
└── README.md                  # 项目文档
```

## 安装

1. 克隆该项目到本地：
   ```
   git clone <项目地址>
   cd pyside2-calculator
   ```

2. 安装所需的依赖：
   ```
   pip install -r requirements.txt
   ```

## 使用

1. 运行应用程序：
   ```
   python src/main.py
   ```

2. 使用计算器进行基本的数学运算。

## 贡献

欢迎任何形式的贡献！请提交问题或拉取请求。

## 许可证

该项目使用 MIT 许可证。有关详细信息，请参阅 LICENSE 文件。