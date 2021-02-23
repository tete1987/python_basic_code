#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/2/23 16:05 
# @Author : TETE
# @File : 27_ddtTest.py 

import requests
import ddt
import unittest

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'


@ddt.ddt()
class TestLaGou(unittest.TestCase):
    def get_headers(self):
        headers = {
            'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'Cookie': 'user_trace_token=20210223104241-923a154d-3fa1-4bb9-ab75-da925dc59fb1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1614048160; _ga=GA1.2.2052834203.1614048160; LGUID=20210223104241-ca01d4b0-687e-41e8-abf1-109ee07e3410; sajssdk_2015_cross_new_user=1; _gid=GA1.2.136225885.1614048189; gate_login_token=b8ea475680bc12efc9a1a5eaaab49410f3a3b8874f086660; LG_LOGIN_USER_ID=8b5a6de87e2b1047a5e59ecd395142324a20d5ac0a1e8db0; LG_HAS_LOGIN=1; _putrc=B741C13D6977086C; JSESSIONID=ABAAAECABFAACEA439763EAC569E8B4B1C1E1136F2D3199; login=true; unick=%E7%89%B9%E6%97%A5%E6%A0%BC%E4%B9%90; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=113; privacyPolicyPopup=false; index_location_city=%E5%8C%97%E4%BA%AC; WEBTJ-ID=20210223104356-177ccc594a9ccb-09f58920e7165c-3e385b04-2073600-177ccc594aa445; RECOMMEND_TIP=true; sensorsdata2015session=%7B%7D; __lg_stoken__=b532d321aedfc32d3bebd6aaecb3acb8ac4eba1fb370d4bb77fd106649af4c917be365aff0b17438b18c0f70dadc721750a4b94151ee893914d451b608d3ed4517d1366f1aab; TG-TRACK-CODE=search_code; LGSID=20210223152426-efd36fda-7119-4ed2-b29f-d3064abd57cf; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5F%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; _gat=1; SEARCH_ID=f10276e6d1574338adb4e0f46de68d9f; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1614065067; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%229071199%22%2C%22%24device_id%22%3A%22177ccc4d833203-06dae534e8e48-3e385b04-2073600-177ccc4d8341c4%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2274.0.3729.169%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22first_id%22%3A%22177ccc4d833203-06dae534e8e48-3e385b04-2073600-177ccc4d8341c4%22%7D; X_HTTP_TOKEN=e1b10b78c965bef6070560416173065d1fd6f8a775; LGRID=20210223152433-ee10b6aa-8a2f-4aa7-b3b8-57df2a66dff6',
            'Referer': 'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput='
        }
        return headers

    @ddt.data((1,),(2,))
    @ddt.unpack
    def test_lagou(self,page):
        r = requests.post(
            url=url,
            headers=self.get_headers(),
            data={'first': False, 'pn': page, 'kd': '自动化测试', 'sid': '5a84135cfc404da29e1c8487db1ffde7'},
            # verify=False
        )
        print(r.json())
        assert r.json()['success']

if __name__ == '__main__':
    unittest.main(verbosity=2)