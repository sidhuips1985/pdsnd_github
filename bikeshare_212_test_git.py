import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    citys = ['chicago','new york','washington']
    while True:
          try :
              city = input('please select you want to see data\n select city from  Chicago, New York, or Washington?')
          except ValueError:
               print('please enter correct value')
               
          if city.lower() in  citys:
              #return city
              break
          else:
               print("please select correct city")


    # get user input for month (all, january, february, ... , june)
    months =['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("\n please select month from  January, February, March, April, May, June \n or type 'all'  if you do not have any preference?\n")
        if month.lower()  in months:
             #return month
             break
        else:
            print('please select correct month')
     
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    while True:
        day = input("\n please select day \n please select Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday \n or type 'all' if you do not have any preference.\n ")
        if day.lower() not in days:
             print('please select correct day')
        else:
            #return day
            break                   
    


    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # 
    
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['day']= df['day'].str.lower()  
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        
    if day != 'all':
        
        df =df[df['day'] == day]

    return df


    print(df)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    Mod_month = df['month'].mode()[0]
    print("print most commmon month using mod fuction: month is  {}".format (Mod_month))
    month_list = df['month'].tolist()
    
    month_dict = {}
    
    for month in month_list:
        if month not in month_dict:
            month_dict[month] = 0
        month_dict [month] += 1
    for key, value in month_dict.items(): 
        print("Count by  month  : month {}: count {}" .format (key, value))
        
    month_dict = max(month_dict,key=month_dict.get)  
    
    print("print most commmon month using dictionary fuction {}".format (month_dict))
        
     # display the most common day of week       
    Common_day = df['day'].mode()[0] 
    print('Most Common day in week:', Common_day) 
        
               
            
    # display the most common start hour
            
    common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most Common start hour:', common_start_hour)
   
    
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_Station = df['Start Station'].mode()[0]
    print("most commonly used start station: {}".format(Start_Station))

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("most commonly used end station:{}".format(end_station))


    # display most frequent combination of start station and end station trip
    df['Combination_Station'] = ' from '+df["Start Station"] + ' to ' + df["End Station"]
    Comm_station = df['Combination_Station'].mode()[0]
    print("Most frequent used  station combination  is {}".format(Comm_station))
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time , i am using Sum function 
    total_travel  = df['Trip Duration'].tolist()
    total_travel = sum(total_travel)
    print("total travel time : {}".format(total_travel))
    
    


    # display mean travel time , i am using Mean fuction 
    mean_travel = df['Trip Duration'].mean()
    
    print("mean Travel time is :{}".format( mean_travel))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df.groupby(['User Type'])['Start Time'].count()
    print("count of user by  user type \n {}".format(count_user_type))

    # Display counts of gender using group by and count and if statement to check if Gender column in data frame 
    
    if 'Gender' not in df.columns:
        print ("there is no gender information")
        
    else :    
       gender =  df.groupby(['Gender'])['Gender'].count()
       print("\count of user by  user type \n {}".format(gender))  
        
        


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print ("there is no gender information")
    else:
        # Min will calculate min value 
        earliest_birth = df['Birth Year'].min()
        print("earliest birth year : {}".format(earliest_birth))
        
        # Max will calculate max value 
        recent_birth = df['Birth Year'].max()
        print("recent birth year  : {}".format(recent_birth))
        
        # Mode will calculate common year
        common_year_birth = df['Birth Year'].mode()[0]
        print("common birth year  : {}".format(common_year_birth))   
        
        
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    
    while True:
         raw_data = input('please  type yes or no if you want to see raw data ')
         raw_data = raw_data.lower()
         n = 5
    
         if raw_data == 'yes' :
                     
              print(df.head(n))
              
              while True :
                  seedata = input('do you want see more data say yes or no ')
                  seedata =  seedata.lower()
                  if seedata == 'yes':
                      n = n+5
                      print(df[n:n+5])
                 
                  else :
                     break 
    
         else:
             print('thank you')
             break
        
        
    
    
     
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
