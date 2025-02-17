import sys
sys.path.append("..")
from kea.core import *

class Test(Kea):
    

    @initializer()
    def set_up(self):
        d.press("back")

    @mainPath()
    def share_menu_should_display_mainpath(self):
        d(description="Open menu").click()
        d(text="Add Podcast", resourceId="de.danoeh.antennapod.debug:id/txtvTitle").click()
        d(resourceId="de.danoeh.antennapod.debug:id/discovery_cover").click()
        d(text="Subscribe").click()

    @precondition(
        lambda self: d(resourceId="de.danoeh.antennapod.debug:id/butShowInfo").exists()
    )
    @rule()
    def share_menu_should_display(self):
        d(resourceId="de.danoeh.antennapod.debug:id/butShowInfo").click()
        
        d(description="More options").click()
        
        assert d(text="Share").exists(), "share not found"


if __name__ == "__main__":
    t = Test()
    
    setting = Setting(
        apk_path="./apk/antennapod/2.1.0.apk",
        device_serial="emulator-5554",
        output_dir="../output/antennapod/4734/guided",
        policy_name="guided"
    )
    start_kea(t,setting)
    
