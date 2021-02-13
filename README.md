# avg-temperature
Get the average temperature for the last 7 days
 
This program will use the Netatmo's API to retrieve the temperature data from a chosen device.
In this implementation the device is fixed.
You need to get access to the API using the credentials given on your corresponding application.

The program will output the average temperature for the period. The program also draws a plot of the temperature for this period of time.

To run this from command prompt
- Use a file contains the credentials. This file should contain *client_id*, *client_secret*, *username* and *password*, each on a separate line.
> Locate to the folder contains auth.py, temperature.py and the file containing the credentials

> ```>python temperature.py <filename>```
- Use the input from keyboard
> ```>python temperature.py```

> The program will then ask you to enter the necessary information.
 
The output for the program should look like this:
```
Getting data from <time> to <time>
Your client id:
Your client secret:
Your username:
Your password:
Authentication Successful!
Average temperature last 7 days: 2 degree C
```
