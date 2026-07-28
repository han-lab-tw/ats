import sys
from mobly import base_test
from mobly import test_runner
from mobly.asserts import assert_true
from mobly.controllers import android_device

class TabA8BasicTest(base_test.BaseTestClass):

    def setup_class(self):
        # 註冊 AndroidDevice 控制器，Mobly 自動綁定已連線的 Tab A8
        self.ads = self.register_controller(android_device)
        self.dut = self.ads[0]  # DUT (Device Under Test): Samsung Tab A8

    def test_check_tab_a8_status(self):
        """驗證 Tab A8 ADB 響應與設備 Model"""
        serial = self.dut.serial
        self.dut.log.info(f"=== [ATS 2.0] 成功存取裝置 Serial: {serial} ===")

        # 執行 ADB shell 指令取得系統 Model
        model_bytes = self.dut.adb.shell('getprop ro.product.model')
        model = model_bytes.decode('utf-8').strip()
        self.dut.log.info(f"=== [ATS 2.0] 驗證裝置型號 (Model): {model} ===")

        # 斷言檢查：確保設備可檢測且正常響應
        assert_true(self.dut.is_adb_detectable(), "Error: Samsung Tab A8 無法透過 ADB 偵測！")

if __name__ == '__main__':
    test_runner.main()
