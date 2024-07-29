import unittest  # 匯入了 Python 的內建單元測試模組 unittest
import cap


class MyTest(unittest.TestCase):
    # 繼承自 unittest.TestCase。這意味著這個類別中的方法將會被 unittest 模組當作測試來執行。
    def test_one(self):
        text = "sample"
        result = cap.cap_text(text)
        # assertEqual 語句檢查每個特定的輸入組合是否產生預期的輸出。
        self.assertEqual(result, "Sample")

    def test_two(self):
        text = "just testing"
        result = cap.cap_text(text)
        self.assertEqual(result, "Just Testing")


# 這部分代碼保證了當這個測試腳本被直接運行時，會調用 unittest.main() 來執行所有的測試方法。
# unittest.main() 會自動搜集並運行繼承自 unittest.TestCase 的類中的所有方法，這些方法名稱以 test 開頭。
if __name__ == '__main__':
    unittest.main()
