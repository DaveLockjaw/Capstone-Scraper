import swaptopscraper as sts
import os

textData = sts.get_post_data()


def test_one():
    assert textData[0] != ""
    assert textData[1] != ""
    if textData[2] != "":
        assert textData[2] != ""
    if textData[3] != "":
        assert textData[3] != ""


def test_two():
    criteria = ["tshirt", "t-shirt", "TSHIRT", "T-Shirt", "Tshirt", "TShirt", "T-shirt", "T-SHIRT", "tshirts",
                "Tshirts", "TSHIRTS", "t shirt", "T Shirt", "T shirt", "T SHIRT", "t-shirts", "tee", "Tee",
                "TEE", "tank top", "Tank Top", "TANK TOP", "tanktop", "TankTop", "TANKTOP", "tank",
                "Tank", "TANK"]
    if any(i in textData[1] for i in criteria):
        result = True
    else:
        result = False
    assert result is False


def test_three():
    assert len(os.listdir("C:/Users/The Craptop Reborn/PycharmProjects/Capstone/swaptopimages/")) != 0


# Mercari Topsscraper Test
"""def test_one():

    if textData[2] == " | ":
        assert textData[0] != ""
        assert textData[1] != ""
        assert textData[3] != ""
        assert textData[4] != ""
    else:
        assert textData[0] != ""
        assert textData[1] != ""
        assert textData[2] != """""

# Mercari Topsscaper test
"""def test_two():
    print(textData[0])
    criteria = ["tshirt", "t-shirt", "TSHIRT", "T-Shirt", "Tshirt", "TShirt", "T-shirt", "T-SHIRT", "tshirts",
                "Tshirts", "TSHIRTS", "t shirt", "T Shirt", "T shirt", "T SHIRT", "t-shirts", "tee", "Tee",
                "TEE", "tank top", "Tank Top", "TANK TOP", "tanktop", "TankTop", "TANKTOP", "tank",
                "Tank", "TANK"]
    assert any(i not in textData[0] for i in criteria)"""