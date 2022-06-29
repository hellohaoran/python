# 作者: 张浩然
# 2022年06月08日21时39分09秒
'''
使用 字典 记录 每一张名片 的详细信息 •
 使用 列表 统一记录所有的 名片字典
'''
card_list = []
def show_menu():
    '''
    显示菜单
    :return:
    '''
    print("*"*50)
    print("欢迎使用【菜单管理系统】")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*"*50)

def new_card():
    '''
    新建名片
    :return:
    '''
    print("-"*50)
    print("功能：新建名片")
    #1.提示用户输入名片信息
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ号码：")
    email = input("请输入邮箱：")
    card_dict = {"name":name,
                 'phone':phone,
                 'qq':qq,
                 'email':email}
    card_list.append(card_dict)
    print(card_dict)
    print("成功添加%s的名片"%card_dict["name"])
def show_all():
    '''显示全部
    :return:
    循环遍历名片列表，顺序显示每一个字典的信息
    '''
    print("-"*50)
    print("功能：显示全部")
    if len(card_list) == 0:
        print("提示：没有任何名片记录")
        return
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end = "\t\t\t    ")
    print("")
    print("="*50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s"%(card_dict["name"],card_dict["phone"],card_dict["qq"],card_dict["email"]))

def search_card():
    '''搜索名片
    1. 提示用户要搜索的姓名
    2. 根据用户输入的姓名遍历列表
    3. 搜索到指定的名片后，再执行后续的操作
    '''
    print("-"*50)
    print("功能：搜索名片")
    #1.提示要搜索的姓名
    find_name = input("请输入要搜索的姓名：")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
            print("-"*40)
            print("%s\t\t%s\t\t%s\t\t%s"%(card_dict["name"],card_dict["phone"],card_dict["qq"],card_dict["email"]))
            print("-"*40)
            break
    else:
        print("没有找到%s"%find_name)
    return card_dict
def deal_card(find_dict):
    '''
    操作找到的名片
    :param find_dict:找到的名片
    :return:
    '''
    print(find_dict)
    action_str = input("请选择要执行的操作"
                       "[1] 修改[2] 删除[0] 返回上一级菜单")
    if action_str == "1":
        find_dict["name"] = input("请输入姓名：")
        find_dict["phone"] = input("请输入电话：")
        find_dict["qq"] = input("请输入QQ：")
        find_dict["emial"] = input("请输入邮箱：")
        print("%s的名片修改成功！" % find_dict["name"])
    elif action_str == "2":
      card_list.remove(find_dict)
    else:
        show_menu()



if __name__ == "__main__":
    new_card()
    show_all()