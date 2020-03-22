import pyshorteners										#Import the pyshorteners module
url=input("Please enter the URL: ")						#store the input URL in url variable
s=pyshorteners.Shortener()								#call the pyshortener's shortener function and store it as an object in s
print("Your shortened URL is: ",s.tinyurl.short(url))	#while printing, use the object to call the tinyurl function with short() action
