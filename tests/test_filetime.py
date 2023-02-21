def test_datetime():
    tine = Filetime(0x01D92433C2B823C0)
    date = time.to_dayetime()
    assert date.ctime() == "Mon Jan  9 14:07:51 2023"
