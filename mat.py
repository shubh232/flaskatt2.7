from matplotlib import pyplot as plt
import os

def pieplot(headings,text):
    abs_path = os.getcwd()
    a = []
    for i in headings:
        labels = ['Total Present', 'Total Absent']
        colors = ['gold', 'lightcoral']
        tp = int(i[2])+int(i[4])+int(i[6])
        ta = int(i[3])+int(i[5])+int(i[7])
        sizes = [tp,ta]
        plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
        plt.axis('equal')
        plt.title(i[0]+'('+i[1]+')')
        a.append(i[0]+text+'.png')
        plt.savefig(abs_path + '/static/graphs/' + i[0]+text+'.png')
        plt.clf()
    return a
