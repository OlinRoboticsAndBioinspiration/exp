for x in [50, 70, 90]:
    for y in [50, 70, 90]:
        f = open("config_template.csv").read()
        f = f.replace("CONFIG1", "."+str(x))
        f = f.replace("CONFIG2", "."+str(y))
        w = open("config/" + str(x) + "x" + str(y) + ".csv", "wb+")
        w.write(f)
        w.close()