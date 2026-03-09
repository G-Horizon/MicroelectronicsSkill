#!/usr/bin/env python3
"""
修正的BUCK电路仿真：正确的BUCK拓扑结构
输入：12V，输出：~5V，开关频率：100kHz
"""

import os
import sys
import tempfile
import numpy as np
from simetrix_automation import SimplisAutomator

def create_correct_buck_netlist(netlist_path):
    """创建正确的BUCK电路网表"""
    netlist_content = """* Correct BUCK Converter Simulation
* Input: 12V, Output: ~5V, Switching frequency: 100kHz
* Topology: Vin -> MOSFET drain, MOSFET source -> switch node
*           Diode cathode -> switch node, anode -> ground
*           Inductor -> switch node to output
VIN 1 0 DC 12
VG 3 0 PULSE(0 5 0 1n 1n 5u 10u)
M1 1 3 2 0 NMOS W=1 L=1
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
    print(f"修正的网表已创建: {netlist_path}")
    return netlist_content

def run_simulation(automator, netlist_path):
    """运行仿真并返回输出"""
    print("检查网表语法...")
    check_cmd = f"Run /check {netlist_path}"
    check_result = automator.send_command(check_cmd, timeout=5.0)
    print(f"检查结果: {check_result[:100] if check_result else '无输出'}")

    print("运行仿真...")
    run_cmd = f"Run {netlist_path}"
    run_result = automator.send_command(run_cmd, timeout=20.0)
    print(f"仿真结果: {run_result[:200] if run_result else '无输出'}")

    return run_result

def get_simulation_data(automator):
    """获取仿真数据"""
    print("显示可用变量...")
    display_cmd = "Display"
    display_result = automator.send_command(display_cmd, timeout=3.0)
    print(f"可用变量: {display_result[:500] if display_result else '无输出'}")

    print("获取节点4电压数据（输出电压）...")
    show_cmd = "Show V(4)"
    show_result = automator.send_command(show_cmd, timeout=5.0)

    # 也获取开关节点电压
    print("获取节点2电压数据（开关节点）...")
    show_cmd2 = "Show V(2)"
    show_result2 = automator.send_command(show_cmd2, timeout=5.0)

    return show_result, show_result2

def parse_show_output(show_output):
    """解析Show命令的输出"""
    lines = show_output.strip().split('\n')
    data = []

    for line in lines:
        line = line.strip()
        if line and not line.startswith('V(') and not line.startswith('Index'):
            parts = line.split()
            if len(parts) >= 2:
                try:
                    time = float(parts[0])
                    voltage = float(parts[1])
                    data.append((time, voltage))
                except ValueError:
                    continue

    return data

def create_text_visualization(data, title="BUCK Converter Output Voltage", num_points=20):
    """创建文本可视化"""
    if not data:
        return "无数据可用"

    # 选择数据点（均匀采样）
    step = max(1, len(data) // num_points)
    sampled_data = data[::step]
    if len(sampled_data) > num_points:
        sampled_data = sampled_data[:num_points]

    # 创建ASCII图表
    output = []
    output.append(f"{title}")
    output.append("=" * 60)
    output.append("Time (s)        Voltage (V)     ASCII Chart")
    output.append("-" * 60)

    # 找到电压范围用于缩放
    voltages = [d[1] for d in sampled_data]
    min_v = min(voltages)
    max_v = max(voltages)
    range_v = max_v - min_v if max_v > min_v else 1

    for time, voltage in sampled_data:
        # 缩放电压到0-50范围
        scaled = int(((voltage - min_v) / range_v) * 50) if range_v > 0 else 25
        bar = "#" * scaled
        output.append(f"{time:<12.6e}  {voltage:<12.6f}  |{bar}")

    output.append("-" * 60)
    output.append(f"数据统计: {len(data)} 个数据点, 时间范围: {data[0][0]:.6f} 到 {data[-1][0]:.6f} s")
    output.append(f"电压范围: {min_v:.6f} 到 {max_v:.6f} V")
    output.append(f"平均电压: {sum(voltages)/len(voltages):.6f} V")

    return "\n".join(output)

def print_data_table(data, title="BUCK Converter Data", max_rows=30):
    """打印数据表格"""
    if not data:
        print(f"{title}: 无数据")
        return

    print(f"\n{title}")
    print("=" * 60)
    print(f"{'时间 (s)':<15} {'电压 (V)':<15}")
    print("-" * 60)

    # 显示前N行和后N行
    if len(data) <= max_rows:
        for time, voltage in data:
            print(f"{time:<15.6e} {voltage:<15.6f}")
    else:
        half = max_rows // 2
        for i in range(half):
            time, voltage = data[i]
            print(f"{time:<15.6e} {voltage:<15.6f}")
        print(f"... 省略 {len(data) - max_rows} 行 ...")
        for i in range(-half, 0):
            time, voltage = data[i]
            print(f"{time:<15.6e} {voltage:<15.6f}")

    print("-" * 60)
    print(f"总计: {len(data)} 个数据点")

def main():
    """主函数"""
    try:
        print("正在连接到SIMetrix...")
        automator = SimplisAutomator()
        print("连接成功!")

        # 创建临时网表文件
        netlist_path = os.path.join(os.getcwd(), "buck_correct.net")
        create_correct_buck_netlist(netlist_path)

        # 运行仿真
        run_result = run_simulation(automator, netlist_path)

        # 获取数据
        output_voltage_data, switch_node_data = get_simulation_data(automator)

        # 解析数据
        if output_voltage_data:
            data_vout = parse_show_output(output_voltage_data)
            if data_vout:
                print(f"\n解析到 {len(data_vout)} 个输出电压数据点")

                # 打印数据表格
                print_data_table(data_vout, "BUCK转换器输出电压")

                # 创建文本可视化
                text_viz = create_text_visualization(data_vout, "BUCK转换器输出电压文本可视化")
                print(f"\n{text_viz}")

                # 保存数据到文件
                with open("buck_output_data.txt", "w") as f:
                    f.write(text_viz)
                print(f"\n数据已保存到: buck_output_data.txt")
            else:
                print("未能从输出中解析输出电压数据")
                print("原始输出:", output_voltage_data[:500])

        if switch_node_data:
            data_vsw = parse_show_output(switch_node_data)
            if data_vsw:
                print(f"\n解析到 {len(data_vsw)} 个开关节点电压数据点")
                print_data_table(data_vsw, "开关节点电压", max_rows=15)

        # 清理临时文件
        if os.path.exists(netlist_path):
            os.remove(netlist_path)
            print(f"\n已清理临时文件: {netlist_path}")

    except Exception as e:
        print(f"执行失败: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())