from .base import FunctionTest


class LayoutAndStylingTest(FunctionTest):

    def test_layout_and_styling(self):
        # 伊迪丝访问首页
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # 她看到啊输入框完美地居中显示
        inputbox = self.get_item_input_box()
        inputbox.send_keys('testing\\n')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
