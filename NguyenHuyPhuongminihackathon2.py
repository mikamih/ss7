# colorlist=["blue", "red", "teal", "green"]
# print (colorlist)
# newcolorlist=input("input a new color: ")
# colorlist.append(newcolorlist)
# print ("new color list: ", colorlist)

# numlist=[5, 1, 8, 92, -1, 30]
# numbercheck=int(input("Input a number: "))
# for i in numlist:
#     if numbercheck-i==0:
#         print ("number found at position: ", numlist[8])
#     else:
#         print ("number not found")


# list3=[5, 1, 8, 92, 7, 30]
# for i in list3:
#     if i %2 ==0:
#         print ("Even numbers: ",i)

distancelist= [9.274, 43.35, 12.04, 9.96, 10.09]
populationlist= [247100, 333300, 266800, 420900, 318000]

print("poppulation density of: ")
print ("BD: ", populationlist[0] / distancelist[0])
print ("BTL: ", populationlist[1] / distancelist[1])
print ("CG: ", populationlist[2] / distancelist[2])
print ("DD: ", populationlist[3] / distancelist[3])
print ("HBT: ", populationlist[4] / distancelist[4])

scorelist= [78, 56, 67]
print ("high score: ")
print ("1.", scorelist[0])
print ("2.", scorelist[1])
print ("3.", scorelist[2])
newscorelist=input("input a new score: ")
scorelist.append(newscorelist)
print (scorelist)

highscore= sorted(scorelist, reverse= True )
print (highscore)