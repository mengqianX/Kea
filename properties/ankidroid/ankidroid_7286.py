import sys
sys.path.append("..")
from kea.core import *

class Test(Kea):
      

    @initializer()
    def set_up(self):
        pass

    @mainPath()
    def preview_card_should_not_preview_wrong_card_mainpath(self):
        d(description="Navigate up").click()
        d(text="Card browser").click()
        d(resourceId="com.ichi2.anki:id/dropdown_deck_name").click()
        d(text="All decks").click()

    @precondition(
        lambda self: d(resourceId="com.ichi2.anki:id/dropdown_deck_name").exists() and
        d(resourceId="com.ichi2.anki:id/action_search").exists() and 
        d(resourceId="com.ichi2.anki:id/card_sfld").exists()

    )
    @rule()
    def preview_card_should_not_preview_wrong_card(self):
        random_selected_card = random.choice(d(resourceId="com.ichi2.anki:id/card_sfld"))
        content = random_selected_card.get_text()
        print("content: " + str(content))
        random_selected_card.long_click()
        
        d(description="More options").click()
        
        d(text="Preview").click()
        
        new_content = d(resourceId="qa").get_text()
        print("new_content: " + str(new_content))
        assert content == new_content, "previewed card should be the same as the selected card"



if __name__ == "__main__":
    t = Test()
    
    setting = Setting(
        apk_path="./apk/ankidroid/2.13.0.apk",
        device_serial="emulator-5554",
        output_dir="../output/ankidroid/7286/guided",
        policy_name="guided"
    )
    start_kea(t,setting)
    
