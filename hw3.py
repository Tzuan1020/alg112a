# 本習題為參考老師範例後所寫出

p=[] # 給他一個空陣列 
def perm(n,p): #主函式
    i = len(p) #陣列長度
    if(i == n): #判斷是否排完
        print(p) #輸出
        return 
    for x in range(n): 
        if(x not in p): #判斷是否在陣列裡
            p.append(x) #新增到陣列
            perm(n,p) #呼叫主函
            p.pop() #刪除最後一個
perm(5,p) 
