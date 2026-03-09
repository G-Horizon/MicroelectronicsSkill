#!/usr/bin/env python3
"""
优化BUCK电路仿真：调整参数以获得正确的输出电压(~5V)
输入：12V，输出：~5V，开关频率：100kHz
"""

import os
import sys
import numpy as np
from simetrix_automation import SimplisAutomator

def create_optimized_buck_netlist(netlist_path):
    """创建优化参数的BUCK电路网表"""
    # 目标输出电压：5V，占空比 D = Vout/Vin = 5/12 ≈ 0.4167
    # 脉冲宽度 = D * 周期 = 0.4167 * 10μs ≈ 4.167μs
    netlist_content = """* Optimized BUCK Converter Simulation
* Input: 12V, Target Output: ~5V, Switching frequency: 100kHz
* Topology: Vin -> MOSFET drain, MOSFET source -> switch node
*           Diode cathode -> switch node, anode -> ground
*           Inductor -> switch node to output
* Optimized parameters:
*   MOSFET: VTO=1.0V (lower threshold), KP=10m (higher transconductance)
*   Inductor: 100uH (larger for better filtering)
*   Capacitor: 470uF (larger for lower ripple)
*   Load: 10Ω (higher load resistance)
*   Duty cycle: 41.67% (5V/12V = 0.4167)
VIN 1 0 DC 12
VG 3 0 PULSE(0 5 0 1n 1n 4.167u 10u)
M1 1 3 2 0 NMOS W=10 L=1
D1 0 2 DIODE
L1 2 4 100u
C1 4 0 470u
RLOAD 4 0 10
.MODEL NMOS NMOS(LEVEL=1 VTO=1.0 KP=10e-3)
.MODEL DIODE D(IS=1e-12 RS=0.01)
.TRAN 0.1u 1m
.END
"""
    with open(netlist_path, 'w') as f:
        f.write(netlist_content)
    print(f"优化网表已创建: {netlist_path}")
    return netlist_content

def run_simulation(automator, netlist_path):
    """运行仿真并返回输出"""
    print("检查网表语法...")
    check_cmd = f"Run /check {netlist_path}"
    check_result = automator.send_command(check_cmd, timeout=5.0)
    print(f"检查结果: {check_result[:100] if check_result else '无输出'}")

    print("运行仿真...")
    run_cmd = f"Run {netlist_path}"
    run_result = automator.send_command(run_cmd, timeout=30.0)  # 更长仿真时间
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

    print("获取节点2电压数据（开关节点）...")
    show_cmd2 = "Show V(2)"
    show_result2 = automator.send_command(show_cmd2, timeout=5.0)

    print("获取输入电流数据...")
    show_cmd3 = "Show I(VIN)"
    show_result3 = automator.send_command(show_cmd3, timeout=5.0)

    return show_result, show_result2, show_result3

def parse_show_output(show_output):
    """解析Show命令的输出"""
    lines = show_output.strip().split('\n')
    data = []

    for line in lines:
        line = line.strip()
        if line and not line.startswith('V(') and not line.startswith('I(') and not line.startswith('Index'):
            parts = line.split()
            if len(parts) >= 2:
                try:
                    time = float(parts[0])
                    value = float(parts[1])
                    data.append((time, value))
                except ValueError:
                    continue

    return data

def create_text_visualization(data, title="BUCK Converter Output Voltage", num_points=25):
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
    output.append("Time (s)        Value (V/A)     ASCII Chart")
    output.append("-" * 60)

    # 找到值范围用于缩放
    values = [d[1] for d in sampled_data]
    min_val = min(values)
    max_val = max(values)
    range_val = max_val - min_val if max_val > min_val else 1

    for time, value in sampled_data:
        # 缩放值到0-50范围
        scaled = int(((value - min_val) / range_val) * 50) if range_val > 0 else 25
        bar = "#" * scaled
        output.append(f"{time:<12.6e}  {value:<12.6f}  |{bar}")

    output.append("-" * 60)
    output.append(f"数据统计: {len(data)} 个数据点, 时间范围: {data[0][0]:.6f} 到 {data[-1][0]:.6f} s")
    output.append(f"值范围: {min_val:.6f} 到 {max_val:.6f}")
    if 'Voltage' in title:
        output.append(f"平均值: {sum(values)/len(values):.6f} V")
        output.append(f"峰值纹波: {(max_val - min_val):.6f} V")
    elif 'Current' in title:
        output.append(f"平均值: {sum(values)/len(values):.6f} A")

    return "\n".join(output)

def print_summary_statistics(vout_data, vsw_data, iin_data):
    """打印仿真结果摘要统计"""
    if not vout_data:
        print("无输出电压数据")
        return

    vout_values = [d[1] for d in vout_data]
    vout_avg = sum(vout_values) / len(vout_values)
    vout_min = min(vout_values)
    vout_max = max(vout_values)
    ripple = vout_max - vout_min

    print("\n" + "="*60)
    print("BUCK转换器仿真结果摘要")
    print("="*60)
    print(f"输出电压统计:")
    print(f"  平均值: {vout_avg:.6f} V")
    print(f"  最小值: {vout_min:.6f} V")
    print(f"  最大值: {vout_max:.6f} V")
    print(f"  峰峰值纹波: {ripple:.6f} V")
    print(f"  纹波系数: {(ripple/vout_avg)*100:.2f}%")

    if vsw_data:
        vsw_values = [d[1] for d in vsw_data]
        vsw_min = min(vsw_values)
        vsw_max = max(vsw_values)
        print(f"\n开关节点电压:")
        print(f"  最小值: {vsw_min:.6f} V")
        print(f"  最大值: {vsw_max:.6f} V")

    if iin_data:
        iin_values = [d[1] for d in iin_data]
        iin_avg = sum(iin_values) / len(iin_values)
        iin_min = min(iin_values)
        iin_max = max(iin_values)
        print(f"\n输入电流统计:")
        print(f"  平均值: {iin_avg:.6f} A")
        print(f"  最小值: {iin_min:.6f} A")
        print(f"  最大值: {iin_max:.6f} A")

        # 计算效率（粗略估算）
        # P_out = Vout_avg² / R_load
        # P_in = Vin * Iin_avg (Vin = 12V)
        if vout_avg > 0:
            p_out = (vout_avg ** 2) / 10.0  # R_load = 10Ω
            p_in = 12.0 * iin_avg
            if p_in > 0:
                efficiency = (p_out / p_in) * 100
                print(f"  输出功率: {p_out:.6f} W")
                print(f"  输入功率: {p_in:.6f} W")
                print(f"  估算效率: {efficiency:.2f}%")

    print("="*60)

def main():
    """主函数"""
    try:
        print("正在连接到SIMetrix...")
        automator = SimplisAutomator()
        print("连接成功!")

        # 创建优化网表文件
        netlist_path = os.path.join(os.getcwd(), "buck_optimized.net")
        create_optimized_buck_netlist(netlist_path)

        # 运行仿真
        run_result = run_simulation(automator, netlist_path)

        # 获取数据
        output_voltage_data, switch_node_data, input_current_data = get_simulation_data(automator)

        # 解析数据
        data_vout, data_vsw, data_iin = None, None, None

        if output_voltage_data:
            data_vout = parse_show_output(output_voltage_data)
            if data_vout:
                print(f"\n解析到 {len(data_vout)} 个输出电压数据点")
                text_viz = create_text_visualization(data_vout, "优化BUCK转换器输出电压")
                print(f"\n{text_viz}")

                with open("buck_optimized_output.txt", "w") as f:
                    f.write(text_viz)
                print(f"\n输出电压数据已保存到: buck_optimized_output.txt")

        if switch_node_data:
            data_vsw = parse_show_output(switch_node_data)
            if data_vsw:
                print(f"\n解析到 {len(data_vsw)} 个开关节点电压数据点")

        if input_current_data:
            data_iin = parse_show_output(input_current_data)
            if data_iin:
                print(f"\n解析到 {len(data_iin)} 个输入电流数据点")
                text_viz_i = create_text_visualization(data_iin, "优化BUCK转换器输入电流", num_points=15)
                print(f"\n{text_viz_i}")

        # 打印摘要统计
        print_summary_statistics(data_vout, data_vsw, data_iin)

        # 保存详细数据
        if data_vout:
            with open("buck_detailed_data.csv", "w") as f:
                f.write("Time(s),Voltage(V)\n")
                for time, voltage in data_vout:
                    f.write(f"{time:.12e},{voltage:.12f}\n")
            print(f"\n详细CSV数据已保存到: buck_detailed_data.csv")

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