# SIMetrix 简单仿真尝试总结

## 概述
成功使用 `simetrix_skill` 完成了一次简单的仿真尝试，并基于仿真数据绘制了图表。

## 仿真步骤

### 1. 连接 SIMetrix
- 使用 `simetrix_automation.py` 中的 `SimplisAutomator` 类连接到正在运行的 SIMetrix/SIMPLIS 软件
- 要求：SIMetrix 必须正在运行，且已打开 Command Shell（菜单 View -> Command Shell）

### 2. 创建电路网表
创建了一个简单的 RC 电路网表文件 `rc_circuit.net`：
```spice
* Simple RC Circuit - Transient Analysis
V1 1 0 PULSE(0 1 0 1u 1u 1m 2m)
R1 1 2 1k
C1 2 0 1u
.TRAN 10u 10m
.END
```

电路参数：
- 电压源 V1：脉冲源，0V 到 1V，上升/下降时间 1μs，脉冲宽度 1ms，周期 2ms
- 电阻 R1：1kΩ
- 电容 C1：1μF
- 瞬态分析：10μs 步长，总时间 10ms

### 3. 运行仿真
使用 SIMetrix 脚本命令：
```bash
Run rc_circuit.net
```

### 4. 获取仿真数据
使用以下命令查看和提取数据：
```bash
Display          # 显示所有可用变量
Show V(2)        # 显示节点 2 的电压数据
```

### 5. 数据解析与绘图
- 解析 `Show V(2)` 命令输出的文本数据
- 使用 Python 的 `matplotlib` 库绘制图表
- 保存为 PNG 格式图像：`rc_circuit_response.png`

## 仿真结果

### 数据统计
- 数据点数量：207 个
- 时间范围：0.000000 到 0.010000 秒
- 电压范围：0.000000 到 0.731832 伏特

### 图表说明
图表显示了 RC 电路的瞬态响应：
- X 轴：时间（秒）
- Y 轴：节点 2 电压（伏特）
- 曲线呈现典型的 RC 充电曲线特征

### 生成的文件
1. `rc_circuit_response.png` - 仿真结果图表
2. `simple_simulation.py` - 完整的仿真脚本
3. `simulation_summary.md` - 本总结文件

## 关键代码片段

### 连接到 SIMetrix
```python
from simetrix_automation import SimplisAutomator
automator = SimplisAutomator()
```

### 发送命令
```python
result = automator.send_command("Run rc_circuit.net", timeout=10.0)
```

### 获取数据
```python
data_output = automator.send_command("Show V(2)", timeout=3.0)
```

## 注意事项

1. **SIMetrix 运行状态**：运行脚本前必须确保 SIMetrix 正在运行且 Command Shell 已打开
2. **命令语法**：SIMetrix 脚本命令对参数格式要求严格，需参考官方文档
3. **错误处理**：网表语法错误会导致仿真失败，可使用 `Run /check netlist.net` 检查语法
4. **数据访问**：仿真后使用 `Display` 查看所有可用变量，再使用 `Show` 提取具体数据

## 扩展应用

此示例可扩展用于：
- 参数扫描分析（改变 R、C 值）
- 频率响应分析（.AC 分析）
- 蒙特卡洛分析
- 自定义测量和数据处理

## 相关文档

- `SIMPLIS&SIMetrix文档/SIMetrix Script Manual/` - 完整的脚本命令参考
- `simetrix_automation.py` - SIMetrix 自动化接口
- `SKILL.md` - simetrix_skill 使用说明

---
*仿真完成时间：2026-03-09*
*使用工具：simetrix_skill + Python + matplotlib*