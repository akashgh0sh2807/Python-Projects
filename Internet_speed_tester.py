# Importing the speedtest module.
import speedtest

# Assigning the speedtest.Speedtest() segment to ookla variable and making a result dictionary.
ookla = speedtest.Speedtest()
result = {1: ookla.download(), 2: ookla.upload(), 3: ookla.results.ping}

# Giving the options to the user for selecting and taking back input in x variable.
print(" Press 1 for checking download speed\n Press 2 for checking upload speed\n Press 3 for checking"
      " network latency")
x = int(input("Enter your selection: "))

# Giving back the result according to the selection made.

# Download speed.
if x == 1:
    print("Download speed of your network is:", result[1])
# Upload speed.
elif x == 2:
    print("Upload speed of your network is:", result[2])
# Latency(Ping) speed.
elif x == 3:
    print("Response time of your network is:", result[3])
# No selection made.
else:
    print("We are assuming that you're facing some issue, please try again later.")
