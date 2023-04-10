import qrcode
import pandas as pd
import PIL
from PIL import Image
from MyQR import myqr
import os
import pymysql

from db.model.ExpoTicket import ExpoTicket

data_list = []
#----------------------数据源------------------------

# 读取excel文件
df = pd.read_excel('res/example.xlsx', sheet_name='Sheet1')
# index = 12345678t
# for i in range(0,100000):
#     df.loc[i,'A'] = index+i
# # 保存文件
# df.to_excel('res/example.xlsx', sheet_name='Sheet1', index=False)

# 获取列名
# print(df.columns)
# # 获取单元格内容
# cell = df.loc[0, 'A']
# print(cell)

# 遍历单元格
# for index, row in df.iterrows():
#     for column in df.columns:
#         print(row[column])
#         data_list.append(row[column])
# iconI = Image.open("res/hg.gif")
# iconI.convert("RGBA")


# conn = pymysql.connect(host='192.168.1.155', port=3306, user='pms', password='wmqe123', db='pms_health_expo', charset='utf8')
# sql = "SELECT ticket_id FROM tb_expo_ticket WHERE is_used = 0"
# try:
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for i in result:
#         data_list.append(i[0])
# except:
#     print("Error: unable to fetch data")

#---------------------图片生成------------------------
# menuName = ""
# for i, data in enumerate(data_list):
    # qr = qrcode.QRCode(
    #     version = None,
    #     error_correction = qrcode.constants.ERROR_CORRECT_H,
    #     box_size = 10,
    #     border = 1
    # )
    # qr.add_data(data)
    # qr.make()

    # fill_color和back_color分别控制前景颜色和背景颜色，支持输入RGB色，注意颜色更改可能会导致二维码扫描识别失败
    # img = Image.new("RGB", (qr.size, qr.size), (255, 255, 255));
    # img = qr.make_image()
    # img = qrcode.make(data)  # 生成二维码图片
    # img.save(f'res/img/{data}.png')  # 保存为图片，文件名为example_1.png, example_2.png, ...
    # icon = Image.open(f'res/img/{data}.png')
    # # icon.convert("RGBA")
    # icon.paste(iconI, (50, 50))
    # icon.save(f'res/img/{data}.gif')
    # 动态二维码
    # picture='res/hg.gif'
    # menu = i % 10000
    # if menu == 0:
    #     menuName = f"{i}-{i+10000}"
    #     os.mkdir(f'res/img/{menuName}')
    # myqr.run(words=str(data),colorized=True,save_name=f'res/img/{menuName}/{data}.png')


def filterLinePropertyName(line):
    if '__' in line:
        return False
    elif 'class_manager' in line:
        return False
    else:
        return True

if __name__ == "__main__":
    a = ExpoTicket.query([ExpoTicket.ticket_id])


    #----------------获取两万条数据库中不存在的ticketId
    ticketIdList = []
    notExistTicketList = []
    for i in a:
        ticketIdList.append(i.ticket_id)
    index = 10000000
    while len(notExistTicketList) < 20000:
        if index not in ticketIdList:
            print(index)
            notExistTicketList.append(index)
        index += 1
    pd.DataFrame(dict({"二维码":notExistTicketList})).to_excel('res/二维码.xlsx', sheet_name='Sheet1', index=False)


    # dataDict = {}
    # for name in filter(filterLinePropertyName,ExpoTicket.__dict__.keys()):
    #     dataDict[name] = []
    # for i in a:
    #     dataDict['id'].append(i.id)
    #     dataDict['join_id'].append(i.join_id)
    #     dataDict['ticket_id'].append(i.ticket_id)
    #     dataDict['is_sync'].append(i.is_sync)
    #     dataDict['is_used'].append(i.is_used)
    #     dataDict['is_entrance'].append(i.is_entrance)
    #     dataDict['sort'].append(i.sort)
    #     dataDict['create_date'].append(i.create_date)
    #     dataDict['sync_date'].append(i.sync_date)
    #     dataDict['use_date'].append(i.use_date)
    # df = pd.DataFrame(dataDict)
    # fileName = ExpoTicket.__name__ + '.xlsx'
    # df.to_excel(fileName, sheet_name='Sheet1', index=False)
