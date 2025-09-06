import winreg
import sys

# 定義要操作的登錄機碼路徑和數值名稱
# HKEY_CURRENT_USER 在 winreg 模組中對應 winreg.HKEY_CURRENT_USER
REG_PATH = r"SOFTWARE\Microsoft\IME\15.0\IMETC"
VALUE_NAME = "Enable Simplified Chinese Output"

def main():
    """
    主函式，用於查詢和切換輸入法的簡繁體輸出模式。
    """
    try:
        # 使用 'with' 陳述式來開啟登錄機碼，可以確保操作結束後自動關閉
        # 需要同時有讀取(KEY_READ)和寫入(KEY_WRITE)的權限
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_READ | winreg.KEY_WRITE) as key:
            
            # 查詢目前的數值資料和類型
            current_value, reg_type = winreg.QueryValueEx(key, VALUE_NAME)

            # 顯示查詢結果
            print("查詢結果")
            print("===================")
            print(f"數值名稱: {VALUE_NAME}")
            print(f"數值資料: {current_value}")
            print("===================\n")

            # 根據目前的數值決定要切換的目標
            if current_value == "0x00000001":
                new_value = "0x00000000"
                print("偵測到目前為「簡體中文」輸出模式。")
                print("正在切換成 -> 【繁體中文】輸出模式...")
            elif current_value == "0x00000000":
                new_value = "0x00000001"
                print("偵測到目前為「繁體中文」輸出模式。")
                print("正在切換成 -> 【簡體中文】輸出模式...")
            else:
                print(f"錯誤：目前的數值資料 '{current_value}' 非預期值，無法進行切換。")
                return # 結束函式

            # 使用 winreg.SetValueEx 更新數值資料
            # 參數分別是：機碼控制代碼, 數值名稱, 保留(必須為0), 數值類型, 新的數值資料
            winreg.SetValueEx(key, VALUE_NAME, 0, winreg.REG_SZ, new_value)
            print(f"成功將數值更新為: {new_value}")

    except FileNotFoundError:
        # 如果機碼或數值名稱不存在，會觸發此錯誤
        print("查詢結果")
        print("===================")
        print(f"錯誤：找不到指定的登錄機碼或數值。")
        print(f"請確認 HKEY_CURRENT_USER\\{REG_PATH} 是否存在。")
    except PermissionError:
        # 如果沒有足夠的權限修改，會觸發此錯誤
        print("錯誤：權限不足。")
        print("請嘗試「以系統管理員身分執行」此程式。")
    except Exception as e:
        # 捕獲其他所有未預期的錯誤
        print(f"發生未預期的錯誤: {e}")
    finally:
        # 無論成功或失敗，都執行這段程式碼
        # 倒數3秒後結束
        print("\n3 秒後自動結束...")
        for i in range(3, 0, -1):
            print(f"{i}...", end='', flush=True)
            import time
            time.sleep(1)

if __name__ == "__main__":
    main()
