import sys
sys.path.append("..")
from kea.core import *

class Test(Kea):

    @initializer()
    def set_up(self):
        d(text="Cinema").click()
        
        d(resourceId="de.rampro.activitydiary.debug:id/fab_attach_picture").click()
        
        if d(text="Allow").exists():
            d(text="AllOW").click()
            
            d(resourceId="de.rampro.activitydiary.debug:id/fab_attach_picture").click()
            
        if d(text="Allow all the time").exists():
            d(text="Allow all the time").click()
            
        d.press("back")

    @mainPath()
    def delete_pics_should_work_mainpath(self):
        d(resourceId="de.rampro.activitydiary.debug:id/select_card_view").click()
        d(resourceId="de.rampro.activitydiary.debug:id/fab_attach_picture").click()
        d(resourceId="com.android.camera:id/shutter_button").click()
        d(resourceId="com.android.camera:id/btn_done").click()
        d(description = "Open Navigation").click()
        d(text="Diary").click()

    @precondition(
        lambda self: d(text="Diary").exists() and 
        d(resourceId="de.rampro.activitydiary.debug:id/picture").exists() and not 
        d(text="Settings").exists() 
    )
    @rule()
    def delete_pics_should_work(self):
        pic_count = d(resourceId="de.rampro.activitydiary.debug:id/picture").count
        print("pic count: " + str(pic_count))
        # random select a pic
        random_index = random.randint(0, pic_count - 1)
        selected_pic = d(resourceId="de.rampro.activitydiary.debug:id/picture")[random_index]
        selected_pic_name = selected_pic.up(resourceId="de.rampro.activitydiary.debug:id/activity_name").get_text()
        print("selected pic name: " + selected_pic_name)
        
        selected_pic.long_click()
        time.sleep(2)
        d(text="OK").click()
        
        after_pic_count = d(resourceId="de.rampro.activitydiary.debug:id/picture").count 
        print("after pic count: " + str(after_pic_count))
        assert after_pic_count == pic_count - 1, "pic not deleted"
        for i in range(after_pic_count):
            pic_name = d(resourceId="de.rampro.activitydiary.debug:id/picture")[i].up(resourceId="de.rampro.activitydiary.debug:id/activity_name").get_text()
            assert pic_name != selected_pic_name, "pic not deleted "+pic_name+" "+selected_pic_name



if __name__ == "__main__":
    t = Test()
    
    setting = Setting(
        apk_path="./apk/activitydiary/1.1.8.apk",
        device_serial="emulator-5554",
        output_dir="output/activitydiary/118/guided/1",
        policy_name="random"
    )
    start_kea(t,setting)
    
