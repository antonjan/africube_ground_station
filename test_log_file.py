#Open new data file
aprs_str = "hello world"
f = open("aprs.txt", "w")
f.write( str(aprs_str)  )      # str() converts to string
f.close()
