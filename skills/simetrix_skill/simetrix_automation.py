import time
import pywinauto
from pywinauto import Application

class SimplisAutomator:
    """
    通过pywinauto调用SIMetrix/SIMPLIS自带的Command Shell，
    实现外部Python代码对该Shell发送指令并读取输出结果的任务。
    """
    def __init__(self):
        try:
            # 使用UIA后端连接到正在运行的SIMPLIS主窗口
            # SIMPLIS 是 Qt5 应用，因此采用 uia 模式识别更为准确
            self.app = Application(backend="uia").connect(title="SIMetrix/SIMPLIS Main Window", class_name="Qt5QWindowIcon")
            self.window = self.app.window(title="SIMetrix/SIMPLIS Main Window", class_name="Qt5QWindowIcon")
            
            # 定位 Command Shell 对话框及其内部控件
            self.shell_dialog = self.window.child_window(title="Command Shell", control_type="Window")
            self.edit_box = self.shell_dialog.child_window(control_type="Edit")
            self.ok_button = self.shell_dialog.child_window(title="Ok", control_type="Button")
            self.output_text = self.shell_dialog.child_window(control_type="Text")
            
        except pywinauto.findwindows.ElementNotFoundError:
            raise Exception("未能找到SIMPLIS Main Window 或 Command Shell，请确保：\n1. SIMPLIS 正在运行。\n2. 并且已打开 Command Shell（可在菜单 View -> Command Shell 打开）。")
        except Exception as e:
            raise Exception(f"连接SIMPLIS Command Shell时出现异常: {e}")

    def get_full_output(self) -> str:
        """
        获取当前Command Shell的全部输出文本。
        """
        try:
            # 通过 UIA 的 ValuePattern 获取文本缓冲区内容
            return self.output_text.iface_value.CurrentValue
        except Exception:
            # 如果出错则尝试后备方式提取
            return self.output_text.legacy_properties().get('Value', '')

    def send_command(self, cmd: str, timeout: float = 2.0, check_interval: float = 0.1) -> str:
        """
        向Command Shell发送指令，并返回该次指令产生的新增输出内容。
        
        :param cmd: 要发送并执行的SIMPLIS/SIMetrix自带命令
        :param timeout: 等待界面输出刷新最长时间（秒）
        :param check_interval: 检查轮询的频率（秒）
        :return: 命令执行产生的新增输出文本（会去除首尾空白）
        """
        # 发送命令前获取当前控制台文本
        old_output = self.get_full_output()
        
        # 在输入框中填入指令
        self.edit_box.set_edit_text(cmd)
        
        # 触发 Ok 按钮来执行指令
        self.ok_button.invoke()
        
        # 轮询检查终端是否有新内容
        start_time = time.time()
        while True:
            new_output = self.get_full_output()
            if len(new_output) > len(old_output):
                # 留出 0.1 秒的缓冲时间确保连续渲染的超长多行文本都写入UI层
                time.sleep(0.1) 
                new_output = self.get_full_output()
                break
            
            if time.time() - start_time > timeout:
                # 超时则跳出
                break
            
            time.sleep(check_interval)
            
        # 截取新增加的那部分输出
        new_text = new_output[len(old_output):]
        return new_text.strip()

if __name__ == "__main__":
    # >>> 使用示例 <<<
    print("正在连接 SIMPLIS Command Shell...")
    try:
        automator = SimplisAutomator()
        
        # 你可以替换这里发送具体针对 SIMPLIS 操作相关的指令
        test_cmd = "Show"
        
        print(f"\n[操作] 发送指令: '{test_cmd}'")
        result = automator.send_command(test_cmd, timeout=3.0)
        
        print("\n[结果] --- 命令执行输出 ---")
        print(result)
        print("---------------------------")
        
    except Exception as e:
        print(f"执行失败: {e}")
