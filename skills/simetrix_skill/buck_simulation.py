#!/usr/bin/env python3
"""
BUCK电路仿真示例：使用SIMetrix仿真BUCK转换器并绘制结果
"""

import os
import sys
import tempfile
import numpy as np
import matplotlib.pyplot as plt
from simetrix_automation import SimplisAutomator

def create_netlist(netlist_path):
    """创建BUCK电路网表"""
    netlist_content = """* BUCK Converter Simulation
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
"""
    with open(netlist_path, 'w') as f:
        f.write(netlist_content)
    print(f"网表已创建: {netlist_path}")
    return netlist_content

def run_simulation(automator, netlist_path):
    """运行仿真并返回输出"""
    # 首先检查网表语法
    print("检查网表语法...")
    check_cmd = f"Run /check {netlist_path}"
    check_result = automator.send_command(check_cmd, timeout=5.0)
    print(f"检查结果: {check_result[:100] if check_result else '无输出'}")

    # 运行仿真
    print("运行仿真...")
    run_cmd = f"Run {netlist_path}"
    run_result = automator.send_command(run_cmd, timeout=20.0)  # 可能需要更长时间
    print(f"仿真结果: {run_result[:200] if run_result else '无输出'}")

    return run_result

def get_simulation_data(automator):
    """获取仿真数据"""
    # 首先显示当前数据组中的所有变量
    print("显示可用变量...")
    display_cmd = "Display"
    display_result = automator.send_command(display_cmd, timeout=3.0)
    print(f"可用变量: {display_result[:500] if display_result else '无输出'}")

    # 获取节点4电压数据（输出电压）
    print("获取节点4电压数据...")
    show_cmd = "Show V(4)"
    show_result = automator.send_command(show_cmd, timeout=3.0)
    print(f"电压数据预览: {show_result[:300] if show_result else '无输出'}")

    # 如果没有获取到，尝试其他表示方式
    if show_result and "Cannot find vector" in show_result:
        print("尝试其他表示方式...")
        # 尝试小写v(4)
        show_cmd = "Show v(4)"
        show_result = automator.send_command(show_cmd, timeout=3.0)
        print(f"小写v(4)结果: {show_result[:300] if show_result else '无输出'}")

    return show_result

def parse_show_output(show_output):
    """解析Show命令的输出"""
    lines = show_output.strip().split('\n')
    data = []

    # 跳过标题行，寻找数据行
    for line in lines:
        line = line.strip()
        if line and not line.startswith('V(4)') and not line.startswith('Index'):
            parts = line.split()
            if len(parts) >= 2:
                try:
                    time = float(parts[0])
                    voltage = float(parts[1])
                    data.append((time, voltage))
                except ValueError:
                    continue

    return data

def plot_data(data, output_image="buck_circuit_response.png"):
    """绘制仿真数据图表"""
    if not data:
        print("无数据可绘制")
        return

    times = [d[0] for d in data]
    voltages = [d[1] for d in data]

    plt.figure(figsize=(12, 7))
    plt.plot(times, voltages, 'b-', linewidth=2)
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Output Voltage V(4) (V)', fontsize=12)
    plt.title('BUCK Converter Transient Response', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    # 保存图像
    plt.savefig(output_image, dpi=150)
    print(f"图表已保存: {output_image}")

    # 显示图像（在非交互式环境中可能无效）
    try:
        plt.show()
    except:
        pass

    return output_image

def main():
    """主函数"""
    try:
        # 连接到SIMetrix
        print("正在连接到SIMetrix...")
        automator = SimplisAutomator()
        print("连接成功!")

        # 创建临时网表文件
        netlist_path = os.path.join(os.getcwd(), "buck_circuit.net")
        create_netlist(netlist_path)

        # 运行仿真
        run_result = run_simulation(automator, netlist_path)

        # 获取数据
        show_result = get_simulation_data(automator)

        # 解析数据
        if show_result:
            data = parse_show_output(show_result)
            if data:
                print(f"解析到 {len(data)} 个数据点")
                print(f"时间范围: {data[0][0]:.6f} 到 {data[-1][0]:.6f} s")
                print(f"电压范围: {min(v[1] for v in data):.6f} 到 {max(v[1] for v in data):.6f} V")

                # 绘制图表
                plot_data(data, "buck_circuit_response.png")
            else:
                print("未能从输出中解析数据")
                print("原始输出:", show_result[:500])
        else:
            print("未获取到仿真数据")

        # 清理临时文件
        if os.path.exists(netlist_path):
            os.remove(netlist_path)
            print(f"已清理临时文件: {netlist_path}")

    except Exception as e:
        print(f"执行失败: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())