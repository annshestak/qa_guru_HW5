from selene import browser, be, by, have, command
import os
def test_form_submit(open_browser):
    browser.open('/')

    browser.element('#firstName').type('Hanna')
    browser.element('#lastName').type('Shestak')
    browser.element('#userEmail').type('annshestak@yopmail.com')
    browser.element('[for = "gender-radio-2').click()
    browser.element('#userNumber').type('2345523454')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('[value = "11"]').click()
    browser.element('.react-datepicker__year-select').element('[value = "1998"]').click()
    browser.element('.react-datepicker__day--030').click()
    browser.element('#subjectsInput').type('Com')
    browser.element(".subjects-auto-complete__menu-list--is-multi").element('#react-select-2-option-1').click()
    browser.element('[for = "hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/sunset.jpg'))
    browser.element('#currentAddress').type('Any street apt. 5')
    browser.element('#state').click().element(by.text('NCR')).click()

