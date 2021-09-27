import pytest

##利用pytest進行區間測試，當中可以利用Class進行整體函式定義
##在終端機打上pytest {-v,-s,-m} "filename.py" {內為可改變參數}
##pytest會自動偵測具有test開頭的函式

class TestOrganize:
    def setup_method(self):
        pass

    def test_move_folder(self):
        pass

    def test_organize_folder(self):
        organize_folder(self.testfolder)

