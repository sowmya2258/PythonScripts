from selenium import webdriver

#driver = webdriver.PhantomJS (executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver = webdriver.Chrome(executable_path = r'C:\Users\exe files\chromedriver.exe')

driver.get('http://python.org')

#html_doc = driver.page_source

#print (html_doc)

