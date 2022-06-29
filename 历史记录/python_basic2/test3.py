# 作者: 张浩然
# 2022年06月07日15时31分33秒
# 将列表 [3,‘a’,5.2,4,{},9,[]] 中 大于3的整数或浮点数置为1，其余置为0
class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "家具名称：%s,占地：%f"%(self.name,self.area)
class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.free_area = area
        self.area = area
        self.item_list = []
    def __str__(self):
        return "户型：%s,占地:%f,剩余占地%f,[家具:%s]"%(self.house_type,self.area,self.free_area,self.item_list)
    def add_item(self,item:HouseItem):
        if self.free_area < item.area:
            print("对不起房间位置不够！")
            return
        else:
            self.free_area = self.free_area - item.area
            print("添置家具%s,占地%f,房间剩余占地：%f"%(item.name,item.area,self.free_area))
            self.item_list.append(item.name)
house = House("三室一厅",60)
item1 = HouseItem("席梦思",4)
item2 = HouseItem("居然",6)

house.add_item(item1)
house.add_item(item2)
print(house)










