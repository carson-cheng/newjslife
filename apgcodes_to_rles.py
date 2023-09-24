# converts apgcodes to rles via lifelib
import lifelib, glob
sess = lifelib.load_rules('b3s23')
lt = sess.lifetree(n_layers=1)
files = glob.glob("apgcodes/*.txt")
limits = [0, 1048576]
includes = [486, 972]
for file in files:
    rles = ""
    prefix = ""
    with open(file) as f:
        prefix = file.split("/")[-1].split(".")[0]
        period = int(prefix.split("xp")[1])
        # if-statement can be removed if you need to update all periods
        if period < limits[1] and period > limits[0]:
            #if period in includes:
            apgcodes = f.read().split("\n")
            for apgcode in apgcodes:
                if "x" in apgcode:
                    rle_string = lt.pattern(apgcode).rle_string()
                    rles += (rle_string.split("golly")[1])
    # if-statement can be removed if you need to update all periods
    if period < limits[1] and period > limits[0]:
        with open("rles/" + prefix + ".txt", "w") as wf:
            wf.write(rles)
                
        
