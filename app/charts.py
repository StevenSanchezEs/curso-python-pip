import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, valores):
    fig, ax = plt.subplots()
    ax.bar(labels, valores)
    plt.savefig(F'./images/{name}.png')
    plt.close()
    

def generate_pie_chart(labels, valores):
    fig, ax = plt.subplots()
    ax.pie(valores, labels=labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()
    

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    valores = [100, 200, 80]
    #generate_bar_chart(labels, valores)
    generate_pie_chart(labels, valores)