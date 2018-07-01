from base import init_driver
from page import Page
from base import analyze_file
import pytest


# [("1", "2"), ("3", "4")]
def analyze_file_with_key(key):
    script_data = analyze_file("search_data")[key]
    script_list = list()
    for i in script_data.values():
        script_list.append(i)
    return script_list


    # script_data = analyze_file("search_data")[key]
    # list_data = list()
    # for i in script_data.values():
    #     script_list_data = list()
    #     for j in i.values():
    #         script_list_data.append(j)
    #     list_data.append(script_list_data)
    # return list_data


class TestSearch:

    # def test_login1(self):
    #     assert 1
    #
    # def test_login2(self):
    #     assert 1
    #
    # def test_login3(self):
    #     assert 0

    # def setup(self):
    #     self.driver = init_driver()
    #     self.page = Page(self.driver)
    #
    # @pytest.mark.parametrize("dict", analyze_file_with_key("test_search"))
    # def test_search(self, dict):
    #     # 点击放大镜
    #     self.page.search.click_search()
    #     # 找到输入框 输入文字
    #     self.page.search.input_search(dict["key_word"])
    #     # 点击返回
    #     self.page.search.click_back()


    # [1, 2]
    # @pytest.mark.parametrize(num, [1, 2])
    # [("1", "2"), ("3", "4")]
    # @pytest.mark.parametrize((user, pass), [("xiaoming", "xiaoming"),
    # ("xiaoming", "xiaoming"),("xiaoming", "xiaoming"),
    # ("xiaoming", "xiaoming"),("xiaoming", "xiaoming"),
    # ("xiaoming", "xiaoming"),("xiaoming", "xiaoming"),
    # ("xiaoming", "xiaoming"),("xiaoming", "xiaoming"),
    # ("xiaoming", "xiaoming"),("xiaoming", "xiaoming"),
    # ("xiaoming", "xiaoming"),("xiaoming", "xiaoming"),])
    # [{}, {}]
    # @pytest.mark.parametrize(dict, [{}, {}])

    @pytest.mark.parametrize("dict", analyze_file_with_key("test_login"))
    def test_login(self, dict):
        print(dict)
        username = dict["username"]
        password = dict["password"]
        case_name = dict["case_name"]
        print(username)
        print(password)
        print("-------")

