import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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

<<<<<<< HEAD
    city = input('Which city would you like to analyze? Chicago, New York or Washington: ').lower()

    while city not in CITY_DATA:

        print('That is not a valid city name. Please try again.')
=======
    city = input('Which city would you like to analyze? Chicago, New York or Washington: ').lower()

    while city not in CITY_DATA:

        print('Sorry that is not a valid city name. Please input a valid name.')
>>>>>>> 46b4a929b7cfb013ed730962556de96ac29ff35c
        city = input('Which city would you like to analyze? Chicago, New York or Washington?\n').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please input month name: ')

    while month not in ['january', 'february', 'mars', 'april', 'may', 'june', 'all']:
        print('Please enter a valid month name')
        month = input('Choose month (all, january, february, ... , june): ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please input day of week: ')
    while day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
        print('Please choose correct day')
        day = input('Choose day of week (all, monday, tuesday, ... sunday): ')


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
      # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_name'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'mars', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_name'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common travel Month: {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('the most common travel day of week : {}'.format(df['day_name'].mode()[0]))

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print('the most common travel start hour: {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most common used start station: {}'.format(
        df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('the most common used end station: {}'.format(
        df['End Station'].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    same_trip = df.groupby(['Start Station', 'End Station'])
    print(" common trip:\n {}".format(same_trip.size().sort_values().tail(1)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time :", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of various user types:")
    print(df['User Type'].value_counts())

    if city != 'washington':

    # TO DO: Display counts of gender
        print("The counts of gender:")
        print(df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest birth year is: {}".format(
            str(int(df['Birth Year'].min())))
        )
        print("The latest birth year is: {}".format(
            str(int(df['Birth Year'].max())))
        )
        print("The most common birth year is: {}".format(
            str(int(df['Birth Year'].mode().values[0])))
        )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    show_rows = 5
    rows_start = 0
    rows_end = show_rows - 1    # use index values for rows

    print_line = lambda char: print(char[0] * 90)

    print('\n    Would you like to see some raw data from the current dataset?')
    while True:
        raw_data = input('      (y or n):  ')
        if raw_data.lower() == 'y':
            # display show_rows number of lines, but display to user as starting from row as 1
            # e.g. if rows_start = 0 and rows_end = 4, display to user as "rows 1 to 5"
            print('\n    Displaying rows {} to {}:'.format(rows_start + 1, rows_end + 1))
            print('\n', df.iloc[rows_start : rows_end + 1])
            rows_start += show_rows
            rows_end += show_rows
            print_line('.')
            print('\n    Would you like to see the next {} rows?'.format(show_rows))
            continue
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print('►Bike share systems Statistic Data for {} ◄ '.format(city.capitalize()))
        print('=' * 50)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
