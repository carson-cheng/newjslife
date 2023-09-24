import glob
files = glob.glob("apgcodes/*.txt")
for item in files:
    with open(item) as rf:
        contents = rf.read()
        lines = contents.split("\n")
        final_output = ""
        for item in lines:
            if len(item) > 0:
                final_output += (item+"\n")
        print(final_output)
