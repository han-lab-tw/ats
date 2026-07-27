#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device


class TabA8SanityTest(base_test.BaseTestClass):

    def setup_class(self):
        # 註冊並取得受測裝置 (DUT - Device Under Test)
        self.dut = self.register_controller(android_device)[0]
        self.dut.log.info("成功建立與 Samsung Galaxy Tab A8 的連線！")

    def test_01_verify_device_online(self):
        """驗證設備系統屬性 (Brand / Model) 是否能正常讀取"""
        brand = self.dut.adb.shell('getprop ro.product.brand').decode('utf-8').strip()
        model = self.dut.adb.shell('getprop ro.product.model').decode('utf-8').strip()

        self.dut.log.info(f"檢測到受測裝置品牌: {brand}, 型號: {model}")

        # 基本斷言：確保有正常取回型號字串
        assert len(model) > 0, "無法取得裝置型號，請檢查 ADB 連線狀態！"

    def test_02_check_battery_status(self):
        """讀取系統 dumpsys 電池狀態資訊"""
        battery_info = self.dut.adb.shell('dumpsys battery').decode('utf-8')
        self.dut.log.info("成功取得電池 dumpsys 資訊")

        assert "level" in battery_info, "dumpsys battery 回傳異常，無法檢測電量"

    def teardown_class(self):
        self.dut.log.info("Samsung Galaxy Tab A8 輕量驗證測試完畢。")


if __name__ == '__main__':
    test_runner.main()
