
array = []
n = int(input("Enter how many numbers do you want to enter : "))

print ("inter your number than press ENTER : ")
for i in range(0, n):
	ele = int(input())

	array.append(ele)
	
print("here is your list : ", array)
var = [*set(array)]
print ("here is your var without duplication: ", var)