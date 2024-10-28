import requests
oscthread = requests.get("https://catagolue.hatsya.com/textcensus/b3s23/oscthread_stdin").text
b3s23osc = requests.get("https://catagolue.hatsya.com/textcensus/b3s23/b3s23osc_stdin").text
jslife = requests.get("https://catagolue.hatsya.com/textcensus/b3s23/jslife_stdin").text
objects = (oscthread + b3s23osc + jslife).split("\n")
apgcodes = [x.split('"')[1] for x in objects if len(x) > 0]
apgcodes = list(set(apgcodes))
'''for item in objects:
    if len(item) > 0:
        apgcode = item.split('"')[1]
        if apgcode[0:2] == "xp":
            prefix = apgcode.split("_")[0]
            with open(f"apgcodes/{prefix}.txt", "a") as af:
                af.write(apgcode + "\n")
'''
for apgcode in apgcodes:
    if apgcode[0:2] == "xp":
        prefix = apgcode.split("_")[0]
        with open(f"apgcodes/{prefix}.txt", "a") as af:
            af.write(apgcode + "\n")