#!/usr/bin/env python3
"""
最终BUCK电路优化仿真：使用极端参数确保正确输出电压
输入：12V，目标输出：~5V，开关频率：100kHz
"""

import os
import sys
import numpy as np
from simetrix_automation import SimplisAutomator

def create_final_buck_netlist(netlist_path):
    """创建最终优化参数的BUCK电路网表"""
    netlist_content = """* FINAL Optimized BUCK Converter Simulation
* Input: 12V, Target Output: ~5V, Switching frequency: 100kHz
* EXTREME PARAMETER OPTIMIZATION:
*   MOSFET: VTO=0.5V (very low threshold), KP=500m (very high transconductance)
*   MOSFET Width: W=1000 (very wide)
*   Inductor: 220uH (large for good filtering)
*   Capacitor: 1000uF (very large for minimal ripple)
*   Load: 10Ω
*   Duty cycle: 41.67% (5V/12V)
*   Simulation time: 10ms (long for steady-state)
VIN 1 0 DC 12
VG 3 0 PULSE(0 5 0 1n 1n 4.167u 10u)
M1 1 3 2 0 NMOS W=1000 L=1
D1 0 2 DIODE
L1 2 4 220u
C1 4 0 1000u
RLOAD 4 0 10
.MODEL NMOS NMOS(LEVEL=1 VTO=0.5 KP=500e-3)
.MODEL DIODE D(IS=1e-12 RS=0.01)
.TRAN 0.1u 10m
.END
"""
    with open(netlist_path, 'w') as f:
        f.write(netlist_content)
    print(f"最终优化网表已创建: {netlist_path}")
    return netlist_content

def run_simulation(automator, netlist_path):
    """运行仿真并返回输出"""
    print("检查网表语法...")
    check_cmd = f"Run /check {netlist_path}"
    check_result = automator.send_command(check_cmd, timeout=5.0)
    print(f"检查结果: {check_result[:100] if check_result else '无输出'}")

    print("运行仿真（可能需要较长时间）...")
    run_cmd = f"Run {netlist_path}"
    run_result = automator.send_command(run_cmd, timeout=60.0)  # 更长超时时间
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
    show_result = automator.send_command(show_cmd, timeout=10.0)

    print("获取节点2电压数据（开关节点）...")
    show_cmd2 = "Show V(2)"
    show_result2 = automator.send_command(show_cmd2, timeout=10.0)

    print("获取输入电流数据...")
    show_cmd3 = "Show I(VIN)"
    show_result3 = automator.send_command(show_cmd3, timeout=10.0)

    print("获取电感电流数据...")
    show_cmd4 = "Show I(L1)"
    show_result4 = automator.send_command(show_cmd4, timeout=10.0)

    return show_result, show_result2, show_result3, show_result4

def parse_show_output(show_output):
    """解析Show命令的输出"""
    lines = show_output.strip().split('\n')
    data = []

    for line in lines:
        line = line.strip()
        if line and not any(line.startswith(x) for x in ['V(', 'I(', 'Index']):
            parts = line.split()
            if len(parts) >= 2:
                try:
                    time = float(parts[0])
                    value = float(parts[1])
                    data.append((time, value))
                except ValueError:
                    continue

    return data

def analyze_steady_state(data, start_ratio=0.8):
    """分析稳态数据"""
    if not data:
        return None

    # 使用后20%的数据作为稳态
    start_idx = int(len(data) * start_ratio)
    steady_data = data[start_idx:]

    if not steady_data:
        return None

    values = [d[1] for d in steady_data]
    times = [d[0] for d in steady_data]

    avg_value = sum(values) / len(values)
    min_value = min(values)
    max_value = max(values)
    ripple = max_value - min_value

    # 计算纹波频率相关统计
    return {
        'average': avg_value,
        'min': min_value,
        'max': max_value,
        'ripple': ripple,
        'ripple_percent': (ripple / avg_value * 100) if avg_value != 0 else 0,
        'num_points': len(steady_data),
        'time_range': (times[0], times[-1])
    }

def create_final_report(vout_data, vsw_data, iin_data, il_data):
    """创建最终仿真报告"""
    report = []
    report.append("=" * 70)
    report.append("BUCK转换器最终优化仿真报告")
    report.append("=" * 70)

    if vout_data:
        vout_stats = analyze_steady_state(vout_data)
        if vout_stats:
            report.append("\n输出电压分析 (稳态):")
            report.append(f"  平均值: {vout_stats['average']:.6f} V")
            report.append(f"  最小值: {vout_stats['min']:.6f} V")
            report.append(f"  最大值: {vout_stats['max']:.6f} V")
            report.append(f"  峰峰值纹波: {vout_stats['ripple']:.6f} V")
            report.append(f"  纹波系数: {vout_stats['ripple_percent']:.2f} %")

            # 检查是否接近目标值
            target = 5.0
            error = abs(vout_stats['average'] - target) / target * 100
            report.append(f"  目标电压: {target} V")
            report.append(f"  误差: {error:.2f} %")

            if error < 10:
                report.append("  ✅ 输出电压接近目标值!")
            else:
                report.append("  ⚠️ 输出电压偏离目标值较大")

    if vsw_data:
        vsw_stats = analyze_steady_state(vsw_data)
        if vsw_stats:
            report.append("\n开关节点电压分析 (稳态):")
            report.append(f"  平均值: {vsw_stats['average']:.6f} V")
            report.append(f"  最小值: {vsw_stats['min']:.6f} V")
            report.append(f"  最大值: {vsw_stats['max']:.6f} V")

    if iin_data and vout_data:
        iin_stats = analyze_steady_state(iin_data)
        vout_stats = analyze_steady_state(vout_data)
        if iin_stats and vout_stats:
            # 计算效率
            p_out = (vout_stats['average'] ** 2) / 10.0  # R_load = 10Ω
            p_in = 12.0 * iin_stats['average']
            if p_in > 0:
                efficiency = (p_out / p_in) * 100
                report.append("\n功率和效率分析:")
                report.append(f"  输出功率: {p_out:.6f} W")
                report.append(f"  输入功率: {p_in:.6f} W")
                report.append(f"  估算效率: {efficiency:.2f} %")

    if il_data:
        il_stats = analyze_steady_state(il_data)
        if il_stats:
            report.append("\n电感电流分析 (稳态):")
            report.append(f"  平均值: {il_stats['average']:.6f} A")
            report.append(f"  最小值: {il_stats['min']:.6f} A")
            report.append(f"  最大值: {il_stats['max']:.6f} A")
            report.append(f"  纹波电流: {il_stats['ripple']:.6f} A")

    report.append("\n" + "=" * 70)
    report.append("参数总结:")
    report.append("  MOSFET: VTO=0.5V, KP=500m, W=1000")
    report.append("  电感: 220uH")
    report.append("  电容: 1000uF")
    report.append("  负载: 10Ω")
    report.append("  占空比: 41.67% (5V/12V)")
    report.append("  开关频率: 100kHz")
    report.append("  仿真时间: 10ms")
    report.append("=" * 70)

    return "\n".join(report)

def main():
    """主函数"""
    try:
        print("正在连接到SIMetrix...")
        automator = SimplisAutomator()
        print("连接成功!")

        # 创建最终优化网表文件
        netlist_path = os.path.join(os.getcwd(), "buck_final.net")
        create_final_buck_netlist(netlist_path)

        # 运行仿真
        run_result = run_simulation(automator, netlist_path)

        # 获取数据
        output_voltage_data, switch_node_data, input_current_data, inductor_current_data = get_simulation_data(automator)

        # 解析数据
        data_vout, data_vsw, data_iin, data_il = None, None, None, None

        results = []
        if output_voltage_data:
            data_vout = parse_show_output(output_voltage_data)
            if data_vout:
                print(f"\n解析到 {len(data_vout)} 个输出电压数据点")
                results.append(("输出电压", data_vout))

        if switch_node_data:
            data_vsw = parse_show_output(switch_node_data)
            if data_vsw:
                print(f"解析到 {len(data_vsw)} 个开关节点电压数据点")
                results.append(("开关节点电压", data_vsw))

        if input_current_data:
            data_iin = parse_show_output(input_current_data)
            if data_iin:
                print(f"解析到 {len(data_iin)} 个输入电流数据点")
                results.append(("输入电流", data_iin))

        if inductor_current_data:
            data_il = parse_show_output(inductor_current_data)
            if data_il:
                print(f"解析到 {len(data_il)} 个电感电流数据点")
                results.append(("电感电流", data_il))

        # 创建最终报告
        final_report = create_final_report(data_vout, data_vsw, data_iin, data_il)
        print(f"\n{final_report}")

        # 保存报告
        with open("buck_final_report.txt", "w") as f:
            f.write(final_report)
        print(f"\n最终报告已保存到: buck_final_report.txt")

        # 保存稳态数据
        if data_vout:
            steady_start = int(len(data_vout) * 0.8)
            steady_data = data_vout[steady_start:]
            with open("buck_steady_state.csv", "w") as f:
                f.write("Time(s),Voltage(V)\n")
                for time, voltage in steady_data:
                    f.write(f"{time:.12e},{voltage:.12f}\n")
            print(f"稳态数据已保存到: buck_steady_state.csv")

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