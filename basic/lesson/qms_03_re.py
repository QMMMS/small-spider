import re


def test1():
    rule1 = re.compile("a")
    target1 = rule1.search("abc").string
    print(target1)


def test2():
    target2 = re.search(".*", "china")
    print(target2)


def test3():
    target3 = re.findall("[a-z]", "1m2")
    print(target3)


def test4():
    target4 = re.sub("a", "b", "abc")
    # 查1， 用2换
    print(target4)
    print(r"\abb\c\'")
    # r 无视转义功能


test4()
