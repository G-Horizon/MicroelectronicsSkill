# BUCK电路仿真实验总结

## 概述
使用 `simetrix_skill` 完成了一个基础BUCK电路的仿真实验，并基于仿真数据绘制了输出电压波形图表。

## 电路设计
BUCK电路（降压转换器）参数：
- 输入电压：12V DC
- 开关频率：100kHz（PWM信号周期10μs，占空比50%）
- 开关元件：NMOS晶体管
- 续流二极管：普通二极管
- 电感：10μH
- 输出电容：100μF
- 负载电阻：2.5Ω
- 预期输出电压：约5V

## 仿真步骤

### 1. 连接 SIMetrix
- 使用 `simetrix_automation.py` 中的 `SimplisAutomator` 类连接到正在运行的 SIMetrix/SIMPLIS 软件
- 要求：SIMetrix 必须正在运行，且已打开 Command Shell（菜单 View -> Command Shell）

### 2. 创建BUCK电路网表
创建BUCK电路网表文件 `buck_circuit.net`：
```spice
* BUCK Converter Simulation
* Input: 12V, Output: ~5V, Switching frequency: 100kHz
VIN 1 0 DC 12
VG 3 0 PULSE(0 5 0 1n 1n 5u 10u)
M1 2 3 0 0 NMOS W=1 L=1
D1 0 2 DIODE
L1 2 4 10u
C1 4 0 100u
RLOAD 4 0 2.5
.MODEL NMOS NMOS(LEVEL=1 VTO=2.5 KP=1e-3)
.MODEL DIODE D(IS=1e-12 RS=0.01)
.TRAN 0.1u 500u
.END
```

电路元件说明：
- VIN：输入直流电压源，12V
- VG：栅极驱动脉冲源，0-5V，上升/下降时间1ns，脉冲宽度5μs，周期10μs
- M1：NMOS晶体管，作为开关元件
- D1：续流二极管
- L1：储能电感，10μH
- C1：输出滤波电容，100μF
- RLOAD：负载电阻，2.5Ω
- 瞬态分析：0.1μs步长，总时间500μs

### 3. 运行仿真
使用 SIMetrix 脚本命令：
```bash
Run buck_circuit.net
```

### 4. 获取仿真数据
使用以下命令查看和提取数据：
```bash
Display          # 显示所有可用变量
Show V(4)        # 显示节点 4（输出电压）的电压数据
```

### 5. 数据解析与绘图
- 解析 `Show V(4)` 命令输出的文本数据
- 使用 Python 的 `matplotlib` 库绘制图表
- 保存为 PNG 格式图像：`buck_circuit_response.png`

## 仿真脚本
完整仿真脚本：`buck_simulation.py`

运行脚本的命令：
```bash
cd skills/simetrix_skill
python buck_simulation.py
```

## 预期结果
仿真将生成以下文件：
1. `buck_circuit_response.png` - 输出电压波形图表
2. 控制台输出显示仿真进度和数据统计

输出电压波形应显示：
- 启动瞬态：从0V逐渐上升至稳态
- 稳态纹波：在目标电压（约5V）附近波动
- 开关纹波：反映100kHz开关频率的纹波成分

## 注意事项
1. **SIMetrix 运行状态**：运行脚本前必须确保 SIMetrix 正在运行且 Command Shell 已打开
2. **模型准确性**：当前使用简单的NMOS和二极管模型，实际BUCK电路可能需要更精确的模型
3. **仿真时间**：BUCK电路仿真可能需要较长时间，请耐心等待
4. **参数调整**：可通过修改网表中的元件值来探索不同设计参数的影响

## 扩展实验建议
1. **改变占空比**：修改VG脉冲源的脉冲宽度，观察输出电压变化
2. **调整电感电容值**：探索LC滤波器对输出电压纹波的影响
3. **改变负载电阻**：观察负载变化对输出电压的影响
4. **效率分析**：添加输入电流测量，计算转换效率

## 相关文件
1. `buck_simulation.py` - 完整的BUCK电路仿真脚本
2. `simetrix_automation.py` - SIMetrix 自动化接口
3. `SIMPLIS&SIMetrix文档/` - SIMetrix 脚本命令参考手册

---
*仿真脚本创建时间：2026-03-09*
*使用工具：simetrix_skill + Python + matplotlib*