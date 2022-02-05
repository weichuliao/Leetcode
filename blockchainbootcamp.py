# Problem Link: https://gist.github.com/hitripod/54dece738afea7d7cf88d576579cb625

# 題目描述
# 幣圈裡面，有一種暱稱叫做 韭菜 的生物，如果你想要低價買入他們手上的比特幣，放出一些恐慌訊息，他們馬上就會賣掉；相反的，如果你想要高價賣出你手上的囤貨，你只要放出利好消息，他們就會蜂蛹買入。

# 輸入說明
# 第一行有一個整數 N (N <= 999,999,999,999)，代表有 n 個韭菜由左至右排成一排，這些韭菜手上都持有比特幣，由最左邊的韭菜開始編號： 1, 2, 3, ..., N。
# 第二行有一整數 M (M <= 999999)，接下來會有 M 次割韭菜的行為。
# 接下來 M 行每行有兩個整數 [i, j]。表示對從 i 到 j 的這堆韭菜進行收割。
# 輸出說明
# 請輸出最後有多少韭菜還沒有賣掉比特幣？

# 範例輸入：
# 5 // N
# 3 // M
# 1 3 // [i, j] 
# 3 5 // [i, j]
# 1 5 // [i, j]

# 範例輸出：
# 4


def rugPull() -> int:
    with open("myinput.txt") as fp:
        n = fp.readline()   # N個韭菜
        m = fp.readline()   # 收割M次
        n = int(n)
        people = [0] * n    # 韭菜編號
        ans = n             # 最後手上有比特幣的韭菜總數量

        lines = fp.readlines()
        for line in lines:
            # 字串處理
            ran = line.split(' ')
            start = int(ran[0])
            end = int(ran[1]) + 1

            # 收割韭菜
            for i in range(start, end):
                if people[i-1] > -1:        # 如果韭菜尚未被收割完畢
                    people[i-1] += 1        # 便依照韭菜編號紀錄已經被收割次數
                    if people[i-1] >= 3:    # 被收割超過3次等同手上沒有比特幣
                        people[i-1] = -1    # -1標記該韭菜出局
                        ans -= 1            # 擁有比特幣的韭菜總數量-1
    return print(ans)

rugPull()



# class Solution:
#     def rugPull(self) -> int:
#         with open("myinput.txt") as fp:
#             n = fp.readline()   # N個韭菜
#             m = fp.readline()   # 收割M次
#             n = int(n)
#             people = [0] * n    # 韭菜編號
#             ans = n             # 最後手上有比特幣的韭菜總數量

#             lines = fp.readlines()
#             for line in lines:
#                 # 字串處理
#                 ran = line.split(' ')
#                 start = int(ran[0])
#                 end = int(ran[1]) + 1

#                 # 收割韭菜
#                 for i in range(start, end):
#                     if people[i-1] > -1:        # 如果韭菜尚未被收割完畢
#                         people[i-1] += 1        # 便依照韭菜編號紀錄已經被收割次數
#                         if people[i-1] >= 3:    # 被收割超過3次等同手上沒有比特幣
#                             people[i-1] = -1    # -1標記該韭菜出局
#                             ans -= 1            # 擁有比特幣的韭菜總數量-1
#         return ans

#     def __init__(self) -> None:
#         if __name__ == '__main__':
#             print(self.rugPull())
#             pass

# run = Solution()