import pytest

##利用pytest進行區間測試，當中可以利用Class進行整體函式定義
##在終端機打上pytest {-v,-s,-m} "filename.py" {內為可改變參數}
##pytest會自動偵測具有test開頭的函式

class TestOrganize:
    def setup_method(self):
        ##setup代表初始訊息，可以移並在這裡輸入需要用到的物件，接下來的測試函式只需打成self.物件名稱，即可使用
        self.x="this"

    def test_move_folder(self):
        pass

    def test_organize_folder(self):
        organize_folder(self.testfolder)

