import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    def city_check():
        flag = 0
        city = input('Please provide a City from Chicago, New York City or Washington\n')
        city = city.lower()
        while(flag == 0):
            if(city == 'chicago' or city == 'new york city' or city == 'washington'):
                flag = 1
                return city
            else:
                city = input('Please provide correct City!!\n')

    city = city_check()

    # TO DO: get user input for month (all, january, february, ... , june)
    def month_check():
        flag = 0
        month = input('Please provide a month from January to June or type all.\n')
        month = month.lower()
        while(flag == 0):
            if(month == 'january' or month == 'febuary' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all'):
                flag = 1
                return month
            else:
                month = input('Please provide correct Month!!\n')

    month = month_check()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    def day_check():
        flag = 0
        day = input('Please provide a Day of week from Monday to Sunday or type all\n')
        day = day.lower()
        while(flag == 0):
            if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all'):
                flag = 1
                return day
            else:
                day = input('Please provide correct Day!!\n')

    day = day_check()

    print('-'*40)
    return city, month, day


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
    
    #df = pd.read_csv(CITY_DATA[city])
    
    if(city.lower() == 'chicago'):
        df = pd.read_csv('chicago.csv')
    elif(city.lower() == 'new york city'):
        df = pd.read_csv('new_york_city.csv')
    else:
        df = pd.read_csv('washington.csv')

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('The most frequent month: ',popular_month)
          
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print('The most frequent day: ',popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most frequent hour: ',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most frequent Start Station: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most frequent End Station: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    #popular_combination = df['Start Station', 'End Station'].mode()[0]
    #print('Most frequent combination of Start Station and End Station : ', popular_combination)
    #row_list = []
    
    #for rows in df.intertuples():
    #    my_list = [rows['Start Station'], rows['End Station']]
     #   row_list.append(my_list)
        
    df['popular combination'] = df['Start Station'] + df['End Station']
    popular_combination = df['popular combination'].mode()[0]
    print('Most frequent combination of Start Station and End Station : ', popular_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time : ', total_travel_time)
          
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time : ', mean_travel_time)
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        genders = df['Gender'].value_counts()      
        print(genders)
          
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('Earliest Year of Birth : ', earliest_year)
          
        recent_year = df['Birth Year'].max()
        print('Most recent Year of Birth : ', recent_year)
          
        common_year = df['Birth Year'].mode()[0]
        print('Most common Year of Birth', common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        s = 0
        e = 5
        while True:
            display = input('\nWould you like to see some data?\n')
            if display.lower() == 'yes':
                print(df[s:e])
                s += 5
                e += 5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
