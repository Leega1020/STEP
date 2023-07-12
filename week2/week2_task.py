import json
print("------------------- Task 1 -----------------------")
def find_and_print(messages):
    
    data=messages.items()
    for names,words in data:
        if "18 years old" in words or "college student"in words or "legal age in Taiwan" in words or "vote" in words:
             print(names)

    
     #判斷準則
     #{"18 years old":18歲>17歲,
     #"college student":大學生通常大於17歲,
     #"legal age":台灣法定年齡為18,
     #"vote":美國投票年齡為18歲
     # }
     

find_and_print({
"Bob":"My name is Bob. I'm 18 years old.", 
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week", 
"Jenny":"Good morning."
})

print("------------------- Task 2 -----------------------")



def calculate_sum_of_bonus(data):
    aa=json.dumps(data)
    list=data["employees"] 
    sum=0
    all=[]
    for content in list:
        names=(content["name"])
        performances=(content["performance"])
        roles=(content["role"])
        salarys=(content["salary"])
        salarys=(str(salarys).replace(",",""))
        if salarys.endswith("USD"):
           salarys=int((str(salarys).replace("USD","")))*30
        salarys=int(salarys)
        
        if performances== "above average": 
           per_bonus=salarys*0.08
           
        elif performances=="average":
           per_bonus=salarys*0.05
          
        elif performances=="below average":
           per_bonus=0
           
           
       
        if roles== "Engineer": 
           role_bonus=salarys*0.02
           
        elif roles=="CEO":
           role_bonus=salarys*0.03
          
        elif roles=="Sales":
           role_bonus=salarys*0.01
           
        
        
        total_bonus=int(per_bonus+role_bonus)
       # print(total_bonus)
        all.append(total_bonus)
    for i in all:
        sum+=i
    print(sum)
    
  

    
calculate_sum_of_bonus({ 
"employees":[
{
   "name":"John",
   "salary":"1000USD",
   "performance":"above average", 
   "role":"Engineer"
}, 
{   "name":"Bob", 
    "salary":60000,
    "performance":"average",
    "role":"CEO"
}, 
{   "name":"Jenny",
    "salary":"50,000", 
    "performance":"below average", 
    "role":"Sales"
} ]
}) 

print("------------------- Task 3 -----------------------")

def func(*data):
    middle=[]
    for i in data:
        middle.append(i[1])
   
    for b in middle:
        if middle.count(b)==1:
            theindex=middle.index(b)
            print (data[theindex])
            break
         
    if middle.count(b)!=1:
        print("沒有")



func("彭⼤牆", "王明雅", "吳明")
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")


print("------------------- Task 4 -----------------------")

def get_number(index):
    arr=[0]
    sum=0
    i=0
    while i <=(index+1):
        sum+=4
        arr.append(sum)
        sum=sum-1
        arr.append(sum)
        i+=1

    print(arr[index])

get_number(1)
get_number(5)
get_number(10)

print("------------------- Task 5 -----------------------")


def find_index_of_car(seats, status, number):
    okseat=[]   
    for i in range(len(status)):
       if status[i]==1:
           okseat.append(seats[i])
    
    
    cloest=min(okseat, key=lambda x: abs(x - number))
   
    
    for i in range(len(seats)): 
        if seats[i]==cloest and seats[i]>=number:
        
          print(i)
        elif seats[i]==cloest and seats[i]<number:print("-1")
  

find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) 
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) 
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4)  