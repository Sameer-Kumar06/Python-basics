# f = open("C:\\Users\\samee\\OneDrive\\Desktop\\Data Science\\01_BasicPython\\file.txt", "w")
# f.write("Hello I am Sameer")
# f.close()
#
# f = open("C:\\Users\\samee\\OneDrive\\Desktop\\Data Science\\01_BasicPython\\file.txt", "a")
# f.write("\nMachine Learning")
# f.close()

f = open("/01_BasicPython\\file.txt", "r")
print(f.read())
f.close()