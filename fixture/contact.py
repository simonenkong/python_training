__author__ = 'Nataly'

from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[25]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[25]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()

        self.change_field_value("byear", contact.byear)

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[17]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[17]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[10]").click()

        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def add_new(self, contact):
        wd = self.app.wd
        self.go_to_contact_page()
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def go_to_contact_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0:
            wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.go_to_contact_page()
        self.select_first_contact()
        # submit group deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close popup
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_index(self, i):
        wd = self.app.wd
        self.go_to_contact_page()
        # find i-th contact
        wd.find_element_by_xpath("//tr[" + str(i+1) + "]/td[1]/input").click()
        # submit contact deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close popup
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.go_to_contact_page()
        # submit first contact edit
        wd.find_element_by_css_selector('img[alt="Edit"]').click()
        self.fill_contact_form(contact)
        # submit contact edit
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_index(self, contact, i):
        wd = self.app.wd
        self.go_to_contact_page()
        # submit i-th contact edit
        wd.find_element_by_xpath("//tr[" + str(i+1) + "]/td[8]/a/img").click()
        self.fill_contact_form(contact)
        # submit contact edit
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.go_to_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                lastname = element.find_elements_by_css_selector('td')[1].text
                firstname = element.find_elements_by_css_selector('td')[2].text
                address = element.find_elements_by_css_selector('td')[3].text
                all_emails = element.find_elements_by_css_selector('td')[4].text
                all_phones = element.find_elements_by_css_selector('td')[5].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_emails_from_home_page=all_emails,
                                                  address=address, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.go_to_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.go_to_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname,
                       id=id, home=home, work=work, mobile=mobile, phone2=phone2, address=address,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2)