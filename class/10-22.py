todos = []

while(1):
    user = input("請輸入代辦事項，若要結束請寫exit：")
    if(user == "exit"):
        break
    todos.append(user)


print(todos)
