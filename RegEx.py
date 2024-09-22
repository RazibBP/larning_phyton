import re

text = "Hello!"
ra = re.search(text,"Hello! This is Tahsin spiking")

if ra:
    print("Yes! That is match")

else:
    print("No mAtCh")



t1 = ("Hello.This is Tahsin Spiking")
rea = re.search("^Hello.*Spiking$",t1)

if rea:
    print("This is Thaisn Spiking")
else:
    print("No Match")



t2 = "Hi! I am Tahsin. I am begainar for phyton code. last 12-10-2024 start the phyton basic code and today i am done basic code phyton"
s1 = re.findall("[a-m]",t2)
if s1:
    print("Match A-M code",s1)
else:
    print("No A-M code")



s2 = re.findall("[1-5]",t2)
if s2:
    print("Namber [1-5] code match :",s2)
else:
    print("No Match Namber")


s3 = re.findall("Hi",t2)
print(s3)
s4 = re.sub("Hi","Hello",t2)
if s4:
    print(s4)
else:
    print("No Change")


t3 = "Hello Everyone!. I am Tahsin from Bangladesh in Dhaka. So Today I want to tolk phyton Regular experition."
s5 = re.sub("phyton Regular experition","My Phyton Jerny.So Let's Start",t3)
print(s5)
if s5:
    print("Some text replacse by use sub fantion")
else:
    print("No Text change")



s6 =re.split("phyton",t3)
print(s6)
if s6:
    print("Change some text")
else:
    print("No text change")
