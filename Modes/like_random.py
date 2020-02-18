import time
class LikeRandom:

    def like_hash_photo(self, hashtag, amount):
        amount +=1
        self.driver.get(
            "https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        get_pics = []
        for i in range(1, amount):
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            view_hrefs = self.driver.find_elements_by_tag_name('a')
            view_hrefs = [elem.get_attribute('href') for elem in view_hrefs
                        if '.com/p/' in elem.get_attribute('href')]
            [get_pics.append(href)
                for href in view_hrefs if href not in get_pics]

        unique_photos = len(get_pics)
        print(unique_photos)
        for pictures in get_pics:
            self.driver.get(pictures)
            time.sleep(2)
            self.driver.find_element_by_class_name("wpO6b").click()
            unique_photos -= 1