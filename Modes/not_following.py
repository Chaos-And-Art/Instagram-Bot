import time


class NotFollow:
    def get_notFollowing(self):
        self.driver.find_element_by_xpath(
            "//a[contains(@href,'/{}')]".format(self.username)).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//a[contains(@href,'/following')]").click()
        following = self._get_names()
        self.driver.find_element_by_xpath(
            "//a[contains(@href,'/followers')]") .click()
        followers = self._get_names()
        not_following_back = [
            user for user in following if user not in followers]

        with open("not_following.txt", "w+") as filehandle:
            for listitem in not_following_back:
                filehandle.write('%s\n' % listitem)

        filehandle.close()
        print("\nProcess Complete. Open the 'not_following.txt' file")
        print("to view those you follow but don't follow you back. \n")

    def _get_names(self):
        time.sleep(1)
        scroll_box = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div[2]")
        bottom, top = 0, 1
        while bottom != top:
            bottom = top
            time.sleep(1)
            top = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        getNames = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in getNames if name.text != '']

        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        return names
