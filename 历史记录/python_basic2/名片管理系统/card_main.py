# 作者: 张浩然
# 2022年06月08日21时39分22秒
'''
程序的入口
每一次启动名片管理系统都通过main启动
在 cards_main 中添加一个 无限循环
'''
import card_tool
while True:
    # Todo (小明)显示菜单栏
    card_tool.show_menu()
    action = input("请选择操作功能")
    print("您的操作是：%s"%action)
    # 根具用户输入决定后续的操作
    if action in["1","2","3"]:
        if action == "1":
            card_tool.new_card()
        elif action == "2":
            card_tool.show_all()
        elif action == "3":
            m = card_tool.search_card()
            card_tool.deal_card(m)
    elif action == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("输入错误，请重新输入")
'''
card_main的所有代码开发完毕'''