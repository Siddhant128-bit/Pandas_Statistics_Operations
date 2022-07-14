import pandas as pd

def get_data_and_process():
    number_of_items=int(input('Enter number of items: '))
    data=[]
    frequency=[]
    for i in range(0,number_of_items):
        temp=float(input('Enter data for '+str(i+1)+' term: '))
        data.append(temp)
        temp=int(input('Enter Frequency for '+str(i+1)+' term: '))
        frequency.append(temp)
    df=pd.DataFrame()
    df['X']=data
    df['f']=frequency
    df['fX']=df['f']*df['X']
    df['X**2']=df['X']**2
    df['fX**2']=df['f']*df['X']**2
    print(df)
    N=df['f'].sum()
    mean=(df['fX'].sum())/N
    SD=((df['fX**2'].sum()/N)-(df['fX'].sum()/N)**2)**(1/2)
    mode=df['X'].loc[df['f'].idxmax()]
    print("Mean: "+str(mean)+'\nStandard Deviation: '+str(SD)+'\nMode: '+str(mode))
    df.to_excel('freq_data.xlsx')

def load_data_and_process():
    df=pd.read_excel('freq_data.xlsx')
    new_data_list=[]
    for i in range(df.shape[0]):
        for f in range(0,df['f'].iloc[i]):
            new_data_list.append(df['X'].iloc[i])
    final_df=pd.DataFrame()
    final_df['X']=new_data_list
    mean=final_df['X'].mean()
    mode=float(final_df['X'].mode())
    SD=final_df['X'].std(ddof=0)
    median=final_df['X'].median()
    print("Mean: "+str(mean)+'\nStandard Deviation: '+str(SD)+'\nMedian: '+str(median)+'\nMode: '+str(mode))


def main_function():
    choice=int(input('Enter choice 1 to enter yourself and 2 to load from File: '))
    if choice==1:
        get_data_and_process()
    else:
        load_data_and_process()

main_function()