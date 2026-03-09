#!/usr/bin/env python3
"""
简单的SIMetrix仿真示例：RC电路瞬态分析并绘制结果
"""

import os
import sys
import tempfile
import numpy as np
import matplotlib.pyplot as plt
from simetrix_automation import SimplisAutomator

def create_netlist(netlist_path):
    """创建简单的RC电路网表"""
    netlist_content = """* Simple RC Circuit - Transient Analysis
V1 1 0 PULSE(0 1 0 1u 1u 1m 2m)
R1 1 2 1k
C1 2 0 1u
.TRAN 10u 10m
.END
"""
    with open(netlist_path, 'w') as f:
        f.write(netlist_content)
    print(f"网表已创建: {netlist_path}")

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
    run_result = automator.send_command(run_cmd, timeout=10.0)
    print(f"仿真结果: {run_result[:200] if run_result else '无输出'}")

    return run_result

def get_simulation_data(automator):
    """获取仿真数据"""
    # 首先显示当前数据组中的所有变量
    print("显示可用变量...")
    display_cmd = "Display"
    display_result = automator.send_command(display_cmd, timeout=3.0)
    print(f"可用变量: {display_result[:500] if display_result else '无输出'}")

    # 获取节点2电压数据
    print("获取节点2电压数据...")
    show_cmd = "Show V(2)"
    show_result = automator.send_command(show_cmd, timeout=3.0)
    print(f"电压数据预览: {show_result[:300] if show_result else '无输出'}")

    # 如果没有获取到，尝试V(2)的不同表示方式
    if show_result and "Cannot find vector" in show_result:
        print("尝试其他表示方式...")
        # 尝试小写v(2)
        show_cmd = "Show v(2)"
        show_result = automator.send_command(show_cmd, timeout=3.0)
        print(f"小写v(2)结果: {show_result[:300] if show_result else '无输出'}")

    return show_result

def parse_show_output(show_output):
    """解析Show命令的输出"""
    lines = show_output.strip().split('\n')
    data = []

    # 跳过标题行，寻找数据行
    for line in lines:
        line = line.strip()
        if line and not line.startswith('V(2)') and not line.startswith('Index'):
            parts = line.split()
            if len(parts) >= 2:
                try:
                    time = float(parts[0])
                    voltage = float(parts[1])
                    data.append((time, voltage))
                except ValueError:
                    continue

    return data

def plot_data(data, output_image="simulation_result.png"):
    """绘制仿真数据图表"""
    if not data:
        print("无数据可绘制")
        return

    times = [d[0] for d in data]
    voltages = [d[1] for d in data]

    plt.figure(figsize=(10, 6))
    plt.plot(times, voltages, 'b-', linewidth=2)
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Voltage V(2) (V)', fontsize=12)
    plt.title('RC Circuit Transient Response', fontsize=14)
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
        netlist_path = os.path.join(os.getcwd(), "rc_circuit.net")
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
                plot_data(data, "rc_circuit_response.png")
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