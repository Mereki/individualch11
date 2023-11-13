# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Caleb Mandapat
# Section:      509
# Assignment:   11.13
# Date:         12 November 2023
#
# Order goes Date,Average Daily Wind Speed (mph),Precipitation (in),
# Average Relative Humidity (%),Average Temperature (F),Maximum Temperature (F),Minimum Temperature (F)

monthDict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

fname = "WeatherDataCLL.csv"
maxT = 0
minT = 10000
with open(fname, "r") as f:
    lines = f.read().split("\n")
    # print(lines)
    for i in lines[1:]:  # deals with max and min temps
        i = i.split(",")
        # print(i)
        if i[-2] == '' or i[-1] == '':
            continue
        if int(i[-2]) > maxT:
            maxT = int(i[-2])
        if int(i[-1]) < minT:
            minT = int(i[-1])
    print(f'10-year maximum temperature: {maxT} F')
    print(f'10-year minimum temperature: {minT} F')
    print()
    month = input("Please enter a month: ")
    # month = "July"
    monthTrans = monthDict[month]
    yr = input("Please enter a year: ")
    print()
    # yr = "2022"
    avgTemp = 0.0
    relHumid = 0.0
    windSpd = 0.0
    precip = 0.0
    dayCount = 0
    for j in lines[1:]:
        j = j.split(",")
        # print(j)
        dates = j[0].split("/")
        if dates[0] == str(monthTrans) and dates[2] == str(yr):
            dayCount += 1
            if j[1] == '':
                windSpd += 0
            else:
                windSpd += float(j[1])
            if j[2] == '':
                precip += 0
            elif float(j[2]) == 0.0:
                precip += 0
            else:
                precip += 1
            if j[3] == '':
                relHumid += 0
            else:
                relHumid += float(j[3])
            if j[4] == '':
                avgTemp += 0
            else:
                avgTemp += float(j[4])
    # print(dayCount)
    print(f'For {month} {yr}:')
    print(f'Mean average daily temperature: {avgTemp / dayCount:.1f} F')
    print(f'Mean relative humidity: {relHumid / dayCount:.1f}%')
    print(f'Mean daily wind speed: {windSpd / dayCount:.2f} mph')
    print(f'Percentage of days with precipitation: {(precip / dayCount) * 100:.1f}%')
