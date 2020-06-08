''' Set '''
basket = {'apple', 'orange', 'apple'}
'orange' in basket
'orange'[::-1]          # Reverse
{w for w in basket if w==w[::-1] and len(w) >= 4}

a = set('absdfasdfasd')
b = set('osajfldsaj')
a - b   # 差集在A中，不在B中
z = a.difference(b) 
a | b   # 并集
result = a.union(b, z) 
a & b   # 交集
result = a.intersection(b, z)
a ^ b   # 不同时包含于a，b

# 添加
a.add()
a.update()
# 移除
a.remove(a)     # 要求a存在，否则报错
a.discard(a)    # 不要求a存在，不报错
a.pop()         # 随机删除一个元素
# 清空
a.clear()
len(a)
# 拷贝
b = a.copy()