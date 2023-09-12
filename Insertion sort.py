#Insertion sort
import random
x = random.sample(range(1,15),10)
#print(x)

def insertion_sort(x):
    step_count=0
    for j in range(1, len(x)):
        key=x[j]
        i=j-1
        while i>=0 and x[i]>key:
            x[i+1]=x[i]
            i=i-1
            step_count+=1
            #print(f'Insertion sort Iteration result is {x}')
        x[i+1]=key    
    #print(f'The final answer is {x} with number of iterations to achieve the answer as {step_count}')
    # List sorted in ascending order
    return step_count

x1 = random.sample(range(1,15),10)
#print(x1)
insertion_sort(x1)


#Bubble sort
y = random.sample(range(1,15),10)
#print(y)
def bubble_sort(y):
    it_count=0
    for i in range(0,len(y)-1):# start from first
        for j in range(len(y)-1,i,-1):# start from last
            if y[j] < y[j-1]:
                '''
                swap y[j] and y[j-1] to achieve ascending order
                '''
                temp=y[j]
                y[j]=y[j-1]
                y[j-1]=temp
                it_count+=1
                #print(f'Bubble sort Iteration result is {y}')
    #print(f'The final answer is {y} with number of iterations to achieve the answer as {it_count}')
    return it_count

y1 = random.sample(range(1,15),10)
#print(y1)
bubble_sort(y1)
insertion_ct_list=[]
bubble_ct_list=[]
obs_count=[]
for i in range(15):
    a = 15
    b = 10
    obs_count.append(b*(i+1))
    x2 = random.sample(range(1,a*(i+1)), b*(i+1))
    y2 = random.sample(range(1,a*(i+1)), b*(i+1))
    #print(f'original list before insertion sort{x2}')
    op1 = insertion_sort(x2)
    #print(op1)
    insertion_ct_list.append(op1)
    #print(f'original list before bubble sort{y2}')
    op2 = bubble_sort(y2)
    bubble_ct_list.append(op2)
print(f'Observations, iterations count for insertion sort is {list(zip(obs_count, insertion_ct_list))}')
print(f'Observations, iterations count for bubble sort is {list(zip(obs_count, bubble_ct_list))}')



