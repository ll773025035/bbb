import allure
import requests

@allure.feature("get请求")
@allure.story("下载文件1")
@allure.title("用例名1")
def test_no_params():
    # r = requests.get("https://www.baidu.com")
    # r = requests.request(method="GET",url="https://www.baidu.com")
    sess = requests.session()
    r = sess.request(method="GET", url="https://www.baidu.com")

    print(r.text)

@allure.feature("get请求")
@allure.story("下载文件2")
@allure.title("用例名2")
def test_get_query():
    pa = {"accountName":"xuepl123"}
    r = requests.request("GET","http://qa.yansl.com:8084/acc/getAccInfo",params=pa)
    print(r.text)

@allure.feature("get请求")
@allure.story("下载文件3")
@allure.title("用例名3")
def test_get_path():
    r = requests.request("GET", "http://qa.yansl.com:8084/acc/getAllAccs/{pageNum}/{pageSize}".format(pageNum=1,pageSize=10))
    print(r.text)

@allure.feature("get请求")
@allure.story("下载文件4")
@allure.title("用例名4")
def test_get_file(pub_data):
    with allure.step("第一步、准备测试数据"):pass
    p = {"pridCode":"63803y"}
    h = {"token":pub_data["token"]}
    with allure.step("第二步、发送请求"):pass
    r = requests.request("GET","http://qa.yansl.com:8084/product/downProdRepertory",params=p,headers=h)
    with allure.step("第三步、请求数据"):
        allure.attach("请求行，请求头，请求正文","请求信息",allure.attachment_type.TEXT)
    with open("aa.xls","wb") as f:
        f.write(r.content)


def test_post_json():
    data = {
  "pwd": "abc123",
  "userName": "tuu653"
}
    r = requests.post("http://qa.yansl.com:8084/login",json=data)
    print(r.text)


def test_post_upload_file(pub_data):
    data = {
        "file":open("aa.xls","rb")
    }
    h = {"token":pub_data["token"]}
    r = requests.post("http://qa.yansl.com:8084/product/uploaProdRepertory",files=data,headers=h)
    print(r.text)