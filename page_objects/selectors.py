from enum import Enum


class Main_Selectors(Enum):
    MAIN_TABLE = '//*[@id="divResultSQL"]//tbody/tr[1]/th[1]'
    RUN_BUTTON = "ws-btn"
    ADRESS_TABLE = '//*[@id="divResultSQL"]//tbody/tr[2]/td[4]'
    TABLE = '//*[@id="divResultSQL"]//tbody/tr'
    TABLE_COUNT = '//*[@id="divResultSQL"]//tbody/tr[2]/td'
