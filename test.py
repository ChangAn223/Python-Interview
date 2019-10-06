"""
m = input().split(' ')
n = int(input())

m = map(int, m)
count = 0
min = []
for i in m:
    if i >= n:
        res = i // n
        count += res
        if i % n:
            min.append(i % n)
    else:
        min.append(i % n)
min = sorted(min)
left = 0
right = len(min) - 1
while left < right:
    t = min[left] + min[right]
    if t > n:
        count += 1
        right -= 1
    elif t == n:
        left += 1
        right -= 1
        count += 1
    else:
        min[right] = t
        left += 1
if left == right:
    count += 1
print(count)
"""

"""
import heapq


class MaxHeap():
    def __init__(self, n):
        self.n = n
        self.t = 0
        self.q = []

    def push(self, x):
        if self.t < self.n:
            heapq.heappush(self.q, x)
            self.t += 1
        else:
            res = self.q[0]
            if x > res:
                heapq.heapreplace(self.q, x)


str = input().split(' ')
n = int(input())
set = set()
heap = MaxHeap(n)
for s in str:
    set.add(len(s))
for i in set:
    heap.push(i)
print(heap.q[0] if heap.t >= heap.n else heap.q[-1])
"""

# import threading
#
# lock = threading.Lock()
# l = []
#
#
# def test1(n):
#     lock.acquire()
#     l.append(n)
#     print(l)
#     lock.release()
#
#
# def test(n):
#     l.append(n)
#     print(l)
#
#
# def main():
#     for i in range(0, 10):
#         th = threading.Thread(target=test, args=(i,))
#         th.start()
#
#
# main()

# def consumer():
#     r = 'i am coming'
#     while True:
#         message = yield r
#         if message:
#             print('consumer is :', message)
#             r = '200 ok'
#         else:
#             return
#
#
# def producer(c):
#     r = c.send(None)
#     print(r)
#     for i in range(1, 4):
#         print('producer ', i)
#         r = c.send(i)
#         print(r)
#     c.close()
#
# c = consumer()
# producer(c)

# def sort(list):
#     left = 0
#     right = len(list) - 1
#     while left < right:
#         while list[left] % 2 != 0 and left < right:
#             left += 1
#         while list[right] % 2 == 0 and left < right:
#             right -= 1
#         list[left], list[right] = list[right], list[left]
#         left += 1
#         right -= 1
#     return list
#
# print(sort([2,2,2,2,8]))

# def delete_n(root, n):
#     left = right = root
#     for i in range(n-1):
#         if right:
#             right = right.next
#         else:
#             return root
#     while right:
#         right = right.next
#         left = left.next
#     t = left.next
#     left.value = t.value
#     left.next = t.next
#     del t
#     return left

#
# def is_huiwen(s):
#     if s == s[::-1]:
#         return True
#     return False
#
# def all_str(length,s,n):
#     str_list=[]
#     for i in range(length-n):
#         str_list.append(s[i:i+n])
#     return str_list
#
# def solution(s):
#     length = len(s)
#     res = ''
#     for i in range(1,length+1):
#         str_list = all_str(length,s,i)
#         for str in str_list:
#             if is_huiwen(str):
#                 res = str
#     return res
#
# print(solution('abacdea'))


# class Node(object):
#     def __init__(self, name=None, value=None):
#         self.name = name
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# # 哈夫曼树类
# class HuffmanTree(object):
#
#     # 根据Huffman树的思想：以叶子节点为基础，反向建立Huffman树
#     def __init__(self, char_weights):
#         self.a = [Node(part[0], part[1]) for part in char_weights]  # 根据输入的字符及其频数生成叶子节点
#         while len(self.a) != 1:
#             self.a.sort(key=lambda node: node.value, reverse=True)
#             c = Node(value=(self.a[-1].value + self.a[-2].value))
#             c.left = self.a.pop(-1)
#             c.right = self.a.pop(-1)
#             self.a.append(c)
#         self.root = self.a[0]
#         self.b = range(10)  # self.b用于保存每个叶子节点的Haffuman编码,range的值只需要不小于树的深度就行
#
#     # 用递归的思想生成编码
#     def pre(self, dict, tree, length):
#         node = tree
#         if not node:
#             return
#         elif node.name:
#             t = [self.b[i] for i in range(length)]
#             dict[node.name] = ''.join(map(str, t))
#             return
#         self.b = list(self.b)
#         self.b[length] = 0
#         self.pre(dict, node.left, length + 1)
#         self.b[length] = 1
#         self.pre(dict, node.right, length + 1)
#
#     # 生成哈夫曼编码
#     def get_code(self):
#         dict = {}
#         self.pre(dict, self.root, 0)
#         return dict
#
#
# if __name__ == '__main__':
#     # 输入的是字符及其频数
#     char_weights = [('a', 5), ('b', 4), ('c', 10), ('d', 8), ('f', 15), ('g', 2)]
#     tree = HuffmanTree(char_weights)
#     dict = tree.get_code()


# def solution(s):
#     s = s.replace(' ', '')  # 去空格
#     count = int(s, 16)  # 一起转十进制
#     res_list = []
#     while count:
#         t = count & 7 # 与二进制 111 与运算得到每三位的值
#         res_list.append(t)
#         count = count >> 3  # 右移3位继续
#     t = len(res_list) % 3   # 是否需要高位补0
#     if t:
#         res_list.extend([0] * (3 - t))  # 高位补0
#     res = []
#     for i in range(len(res_list)//3):   # 每3位十进制组成一个配置
#         if res_list[3*i] == res_list[3*i+1] and res_list[3*i+1]==res_list[3*i+2]:   # 3位相等
#             if res_list[3*i] == 0:  # 3位全0 不输出
#                 continue
#             res.append(str(res_list[3*i]))  # 3位相等切不为0，则过滤只保留一个
#         else:
#             res.append(str(res_list[3*i]) + str(res_list[3*i+1]) + str(res_list[3*i+2]))
#     return ' '.join(res)[::-1]
#
#
# if __name__ == "__main__":
#     s = input()
#     print(solution(s))

# def reOrderArray(array):
#     # write code here
#     left = -1
#     right = 0
#     while right < len(array):
#         if array[right] % 2 == 0:
#             if left == -1:
#                 left = right
#             else:
#                 array[left], array[right] = array[right], array[left]
#         elif array[right] % 2 == 1 and left != -1:
#             array[left], array[right] = array[right], array[left]
#             if right == len(array)-1:
#                 return array
#             left += 1
#             right = left
#         right += 1
#     print(array)
#
# array = [1,2,3,4,5,6,7]
# reOrderArray(array)

arr = [6, -1, 8, -4, -6, 3, 2, -2, 5]

def dp_opt(arr):
    res = [0 for i in range(len(arr))]
    # 初始化
    res[0] = arr[0]
    # 开始循环
    max_sum = res[0]
    for i in range(1, len(arr)):
        a = res[i - 1] + arr[i]
        b = arr[i]
        res[i] = max(a, b)
        max_sum = max_sum if max_sum >res[i] else res[i]
    return max_sum

print(dp_opt(arr))
