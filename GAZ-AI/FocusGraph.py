import matplotlib.pyplot as plt

def focus_graph():
    file = open("focus.txt", "r")
    content = file.read()
    file.close()
    
    content = content.split(",")
    x1 = []
    for i in range(0, len(content)):
        content[i] = float(content[i])
        x1.append(i)
        
    print(content)
    y1 = content
    
    plt.plot(x1,y1,color = "red",marker = "o")
    plt.title("YOUR FOCUSED TIME",fontsize = 16)
    plt.xlabel("Times",fontsize = 14)
    plt.ylabel("Focus Time", fontsize = 14)
    plt.grid()
    plt.show()