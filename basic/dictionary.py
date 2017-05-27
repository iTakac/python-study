# coding:utf-8

# 辞書
grades = { "Joel" : 80, "Tim" : 95 }
joels_grade = grades["Joel"]
print(joels_grade)

try:
    kates_grades = grades["Kate"]
except KeyError:
    print ("no grade for Kate!")

print ("Joel" in grades)
print ("Kate" in grades)
print (grades.get("Joel",0))
print (grades.get("Kate",0))
print (grades.get("No One"))

print (grades)
grades["Kate"] = 100
print (grades)
print (len(grades))

tweet = {
    "user" : "joelgrus" ,
    "text" : "Data Science is Awesome" ,
    "retweet_count" : 100 ,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome","#yolo"] ,
    }

print (tweet)
print (tweet.keys())
print (tweet.values())
print (tweet.items())

