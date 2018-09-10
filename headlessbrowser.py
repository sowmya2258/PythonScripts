from selenium import webdriver
driver= webdriver.PhantomJS(executable_path= r 'E:\Software\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get("http://python.org")
html= driver.page_source
print html

