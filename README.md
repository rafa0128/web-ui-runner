## 简介
基于selenium的web-ui自动化测试框架

<img src="https://cdn.nlark.com/yuque/0/2023/png/153412/1679393906942-27fc45ff-65fa-4b4a-9435-ee3780c0109f.png"  width="100%">

## 环境
```
python 3.10+
安装依赖： pip install -r requirement
```

## 执行
```
python run.py
```

## 项目结构
```
web-ui-runner
├─run.py # 执行入口
├─requirement.txt # 模块依赖 pip install -r requirement.txt
├─public
|  ├─Common.py # 公共类
|  ├─Decorator.py # 装饰器类
|  ├─Config.py # 配置读取类
|  ├─config.ini # 配置信息  
|  ├─Log.py # 日志类
|  ├─HTMLTestReport.py # 测试报告类
├─case
|   ├─case*.py # 各个场景的测试用例
|   ├─mask_case.py # 测试用例集合执行
├─report # 存放测试报告和截图文件
```

## Python API
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# 浏览器
driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver = webdriver.Edge()
driver = webdriver.Safari()

driver.get("http://www.google.com") #打开网址

# 定位查询
elements = driver.find_element(By.ID, "tomatoes")
class By:
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"

for e in elements: #获取满足条件的元素
    print(e.text)    

# 交互
driver.back() #后退
driver.forward() #前进
driver.refresh() #刷新
driver.find_element(By.CLASS_NAME, "tomatoes").click() #点击
driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER) #发送键位

# 信息
is_email_visible = driver.find_element(By.NAME, "email_input").is_displayed() #是否显示
value = driver.find_element(By.NAME, 'btnK').is_enabled() #是否启用 
value = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']:first-of-type").is_selected() #是否被选定 
attr = driver.find_element(By.CSS_SELECTOR, "h1").tag_name #获取元素标签名 
res = driver.find_element(By.CSS_SELECTOR, "h1").rect #位置和大小 （坐标、宽高）
cssValue = driver.find_element(By.LINK_TEXT, "More information...").value_of_css_property('color') #获取元素CSS值 
text = driver.find_element(By.CSS_SELECTOR, "h1").text #文本内容 
email_txt = driver.find_element(By.NAME, "email_input").get_attribute("value") #获取特性或属性 

# 清除
SearchInput = driver.find_element(By.NAME, "q")
SearchInput.send_keys("selenium")
SearchInput.clear()

# 选择
select_element = driver.find_element(By.NAME, 'selectomatic')
select = Select(select_element)
option_list = select.options #获取全部选项
select.select_by_visible_text('Four')  #根据文本选中
select.select_by_value('two') #根据值选中
select.select_by_index(3) #根据序号选中
select.deselect_by_value('eggs') #取消选中选项
with pytest.raises(NotImplementedError): #禁用选项
    select.select_by_value('disabled')

# 窗口
width = driver.get_window_size().get("width") #获取窗口的宽
height = driver.get_window_size().get("height") #获取窗口的高
driver.minimize_window() #最小化
driver.fullscreen_window() #全屏化
driver.maximize_window() #最大化
driver.set_window_size(1024, 768) #设置窗口大小
driver.set_window_position(0, 0) #将窗口移动到主显示器的左上角
x = driver.get_window_position().get('x') #得到窗口的位置
y = driver.get_window_position().get('y')

# 截图
driver.save_screenshot('./image.png') #屏幕截图
ele = driver.find_element(By.CSS_SELECTOR, 'h1') #元素屏幕截图
ele.screenshot('./image.png')

# 文件上传
driver.get("https://the-internet.herokuapp.com/upload");
driver.find_element(By.ID,"file-upload").send_keys(r"./selenium-snapshot.jpg")
driver.find_element(By.ID,"file-submit").submit()
if(driver.page_source.find("File Uploaded!")):
    print("file upload success")
else:
    print("file upload not successful")
    
# 等待
el = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.TAG_NAME,"p")) # 显式等待（不一定等3秒，满足条件后提前结束）
driver.implicitly_wait(10) # 隐式等待
wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException]) #流畅等待（等待条件的最大时间量，以及检查条件的频率，配置等待来忽略等待时出现的特定类型的异常）
```