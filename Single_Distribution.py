import pandas as pd 

def get_data():
    number_of_items=int(input('Enter number of Data: '))
    data=[]
    for item in range(0,number_of_items):
        temp=float(input('Enter value for '+str(item+1)+' term: '))
        data.append(temp)
        print(data)
    df=pd.DataFrame()
    df['X']=data
    df['X**2']=df['X']**2
    sum_of_x=df['X'].sum()
    sum_of_x_squared=df['X**2'].sum()
    mean=sum_of_x/number_of_items
    S_D=((sum_of_x_squared/number_of_items)-(sum_of_x/number_of_items)**2)**(1/2)
    df=df.sort_values(by='X',ascending=True)
    if number_of_items%2==0:
        mean_term=number_of_items/2
        median=df['X'].iloc[int(mean_term)-1]
    else: 
        mean_term=(number_of_items+1)/2
        median=df['X'].iloc[int(mean_term)-1]
    print(df)
    print(median)
    print(mean,S_D)
    df.to_excel('data.xlsx')
def load_data():
    df=pd.read_excel('data.xlsx')
    df=df[['X','X**2']]
    mean=df['X'].mean()
    median=df['X'].median()
    S_D=df['X'].std(ddof=0)
    print(df)
    print('Mean: '+str(mean))
    print(mean,median,S_D)

def main_function():
    choice=int(input('Enter 1 to enter data, 2 to load data: '))
    if choice==1:
        table=get_data()
    elif choice==2:
        table=load_data()

main_function()