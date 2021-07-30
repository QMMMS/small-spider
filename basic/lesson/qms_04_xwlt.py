import xlwt

workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook
worksheet = workbook.add_sheet("sheet1")
# worksheet.write(0, 0, "hello")  # 行,列,内容
# workbook.save("example.xls")

n = 1
while n < 10:
    i = 1
    while i <= n:
        print("%d*%d=%d" % (i, n, i * n), end="\t")
        worksheet.write(n-1, i-1, "%d*%d=%d" % (i, n, i * n))
        i += 1
    print()
    n += 1
workbook.save("example.xls")
