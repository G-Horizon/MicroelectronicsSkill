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
                                       
                                                
            self.app = Application(backend="uia").connect(title="SIMetrix/SIMPLIS Main Window", class_name="Qt5QWindowIcon")
            self.window = self.app.window(title="SIMetrix/SIMPLIS Main Window", class_name="Qt5QWindowIcon")
            
                                        
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
                                             
            return self.output_text.iface_value.CurrentValue
        except Exception:
                           
            return self.output_text.legacy_properties().get('Value', '')

    def send_command(self, cmd: str, timeout: float = 2.0, check_interval: float = 0.1) -> str:
        """
        向Command Shell发送指令，并返回该次指令产生的新增输出内容。
        
        :param cmd: 要发送并执行的SIMPLIS/SIMetrix自带命令
        :param timeout: 等待界面输出刷新最长时间（秒）
        :param check_interval: 检查轮询的频率（秒）
        :return: 命令执行产生的新增输出文本（会去除首尾空白）
        """
                        
        old_output = self.get_full_output()
        
                   
        self.edit_box.set_edit_text(cmd)
        
                       
        self.ok_button.invoke()
        
                      
        start_time = time.time()
        while True:
            new_output = self.get_full_output()
            if len(new_output) > len(old_output):
                                                  
                time.sleep(0.1) 
                new_output = self.get_full_output()
                break
            
            if time.time() - start_time > timeout:
                       
                break
            
            time.sleep(check_interval)
            
                     
        new_text = new_output[len(old_output):]
        return new_text.strip()

if __name__ == "__main__":
                  
    print("正在连接 SIMPLIS Command Shell...")
    try:
        automator = SimplisAutomator()
        
                                       
        test_cmd = "Show"
        
        print(f"\n[操作] 发送指令: '{test_cmd}'")
        result = automator.send_command(test_cmd, timeout=3.0)
        
        print("\n[结果] --- 命令执行输出 ---")
        print(result)
        print("---------------------------")
        
    except Exception as e:
        print(f"执行失败: {e}")
