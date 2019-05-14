# FordGoBike bike share usage: An exploration of usage by user type, weekday, and most frequently traveled routes
### Author: Liz Herdter
### Completion Date: March 2019
### Udacity DAND


## Dataset


For this investigation I explored ride rates by day of the week, hour within the day, and the user type. I also explored average duration of a ride by day of the week, hour wihtin the day, and the user type. Finally, I visualized the path most traveled (start and end station id).

Ford GoBike is a bike share system in the San Francisco Bay Area. This program was piloted in 2013 and as of 2018 there were 7000 bikes in the Ford GoBike fleet spread across the Bay Area, East Bay, and San Jose. The bikes are locked into a network of docking stations around the city. They can be unlocked from one station and returned to any other station making them ideal for one way trips. The bike are accessible 24/7/365. More about this program is can be accessed here.

This dataset has 16 features and nearly 2 million records. Each record corresponds to a single trip made. Features incluce duration of the ride, start time, end time, start station, start station name, start station lat and long, end station, end station name, end station lat and long, bike id, user type, member birth year, and member gender.

This dataset can be used to explore the total number of rides at an hourly, daily, weekly, and monthly temporal resolution. It can also be used to learn about peak rides from each station. Other interesting features included the interaction between number of rides made in each hour based on the day as well as average duration across hours in each day. Additionally, this dataset will provide information about what stations are most traveled too and from and identify areas where more bikes might be used or target spatial areas for new bikeshare stations. 


## Summary of Findings

Total rides are variable over months with greater total rides occuring during the summer months (June - October). In September total rides decline a bit (likely because of the hot weather) and then peak back in October when fall comes and the weather is much nicer. Total rides by duration clearly follow a log-normal distribution as evident by the very right skewed distribution.

Usage rate peaks during the week during commuting hours. Weekend usage is lower overall. Weekend usage rate is highest during lunch time. Subscribers use the bikeshare much more than do one time customers. Average ride duration is generally greater for customers as opposed to subscribers who use the bike share frequently and know where they are going and are being efficient with their time. 

Not all stations are used equally. There are some stations that are used much more than others. For all stations subcribers are more frequent users than are customers. The top five paths taken in terms of start station to end station are: 

15,6   (San Francisco Ferry Building -> The Embarcadero at Sansome St)  
6,16   (The Embarcadero at Sansome St -> Steuart St at Market St)    
81,15  (Berry St at 4th St -> San Francisco Ferry Building)    
182,196  (19th Street BART -> Grand Ave at Perkins St)    
6,15   (The Embarcadero at Sansome St -> San Fran Ferry Building) 


## Key Insights for Presentation

The presentation depicts usage by hour and user type for each weekday, average ride duration of these rides by user type, and the total trips made between the top 25 start stations. Average duration is depicted on non-transformed scale in the presentation so that I could depict average duration. I have chosen not to present the distributions as I do not believe the distributions are as easy to conceptualize as are point plots. 

Stations most traveled have been trimmed so that the travel rate is at least 1500. I removed start and end station combinations for where there were fewer that 1500 trips for ease of visualization. 