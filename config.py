# 用户配置，可以配置多个人的，配置多人的可以用来抢多个邻近的位置(采用多线程实现)
# 项目采用区域编号，座位号，以及日期来唯一定位到座位，即通过配置seats和day来确定位置
# seats为列表，第一位数为区域编号，见下面对应表，第二位为座位号，可以有多个座位号，抢不到就往后顺延
# 例如[['13', '016'], ['15', '020']]代表首选三楼c区016座位，其次选四楼b区020座位
# day为字符串，只能填today或tomorrow，意思是抢当天的还是第二天的位置
users = [
    {
        'username': '2019123456',
        'password': '123456',
        'seats': [['13', '018']],
        'day':'today'
    },
    {
        'username': '2020123456',
        'password': '255555',
        'seats': [['13', '009'], ['13', '021']],
        'day':'tomorrow'
    }
]


# 登录\预约失败会推送消息，采取pushplus推送渠道，请自行注册获取token，如不想受到推送请留空
pushplus_token = 'f1d396a853bb4821931cbc6200812345'

# 图书馆各个区域对应的区域编号
# 7 一楼C区
# 8 二楼A区
# 9 二楼B区
# 10 二楼C区
# 11 三楼A区
# 12 三楼B区
# 13 三楼C区
# 14 四楼A区
# 15 四楼B区
# 16 四楼C区
# 17 四楼A电子阅览室K
# 18 四楼自主学习空间
# 19 五楼A区
# 20 五楼B区
# 21 五楼C区
