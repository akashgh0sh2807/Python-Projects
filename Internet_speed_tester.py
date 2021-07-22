import speedtest

ookla = speedtest.Speedtest()
result = {1: ookla.download(), 2: ookla.upload(), 3: ookla.results.ping}
print(" Press 1 for checking download speed\n Press 2 for checking upload speed\n Press 3 for checking"
      " network latency")
x = int(input("Enter your selection: "))

if x == 1:
    print("Download speed of your network is:", result[1])
elif x == 2:
    print("Upload speed of your network is:", result[2])
elif x == 3:
    print("Response time of your network is:", result[3])
else:
    print("We are assuming that you're facing some issue, please try again later.")
