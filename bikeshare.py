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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city, month, day = '', '', ''
    while city not in CITY_DATA.keys():
        city = input("Please enter a city (chicago, new york city, washington): ").lower()
        if city not in CITY_DATA.keys():
            print("Invalid input. Please try again.")

    # get user input for month (all, january, february, ... , june)
    while month not in list(('january', 'february', 'march', 'april', 'may', 'june', 'all')):
        month = input("Please enter a month (January, February, March, April, May, June or All): ").lower()
        if month not in list(('january', 'february', 'march', 'april', 'may', 'june', 'all')):
            print("Invalid input. Please try again.")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in list(('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')):
        day = input("Please enter a day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All): ").lower()
        if day not in list(('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')):
            print("Invalid input. Please try again.")
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
    df = pd.read_csv(f'{CITY_DATA[city]}')
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of Week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        df = df[df['Month'] == month.title()]
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of Week'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour
    most_common_month = df['Month'].mode()[0]
    print("Most Common Month:", most_common_month)
    # display the most common day of week
    most_common_day = df['Day of Week'].mode()[0]
    print("Most Common Day of Week:", most_common_day)
    # display the most common start hour
    most_common_hour = df['Hour'].mode()[0]
    print("Most Common Start Hour:", most_common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station:", most_common_start_station)
    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most Common End Station:", most_common_end_station)
    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    most_common_trip = df['Trip'].mode()[0]
    print("Most Common Trip:", most_common_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_duration = df['Trip Duration'].sum()
    print("Total Trip Duration:", total_duration)
    # display mean travel time
    average_duration = df['Trip Duration'].mean()
    print("Average Trip Duration:", average_duration)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types:\n", user_types)
    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nGender Counts:\n", gender_counts)
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print("\nBirth Year Stats:")
        print("Earliest Year:", earliest_year)
        print("Most Recent Year:", most_recent_year)
        print("Most Common Year:", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    row_index = 0
    while True:
        show_data = input("Would you like to see 5 lines of raw data? Enter 'yes' or 'no': ").lower()
        if show_data == 'yes':
            print(df.iloc[row_index:row_index + 5])
            row_index += 5
            if row_index >= len(df):
                print("No more data to display!")
                break
        elif show_data == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()