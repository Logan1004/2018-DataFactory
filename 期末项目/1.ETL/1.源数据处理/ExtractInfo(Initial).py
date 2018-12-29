data=[]
# 提取movie相关信息 product/productId,review/score,review/time
f = open("movie.txt","r")
data = f.readlines()
f.close()

data2 = []
f = open("movieout.txt","r")
data2 = f.readlines()
f.close()

i=-4
tempString = ""
flag = 0
with open("movieoutput","w") as f:
    while i<len(data2):
        i = i + 4
        print(i)
        temp = data2[i].split(" ")[1]
        if (tempString == temp):
            if (flag==0): continue
            else:
                for j in range(0,3):
                    f.write(data2[i+j])
        else:
            tempString = temp
            if (temp in data):
                flag=1
                print(temp)
                for j in range(0,3):
                    f.write(data2[i+j])
            else: flag=0




