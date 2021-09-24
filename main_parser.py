from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='Drivers/chromedriver.exe')


try:
    driver.get(url='https://vitalur.by/actions/')
    time.sleep(1.5)
    close_button = driver.find_element_by_class_name('backdrop-close').click()

    while True:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight-423);")
            more_actions = driver.find_element_by_class_name('reviews-list__table-more').click()

        except:
            break
        with open('index.html', 'w') as f:
            f.writelines(driver.page_source)


except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()