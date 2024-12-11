def builder():
    cat = open("./Questions/categories.txt", "r")
    categories = []
    for x in cat:
        categories.append(x[:-1])
    
    cat.close()
    c = ["_E", "_M", "_H"]
    qa = ["_Q", "_A"]
    dr = "./Questions/"
    end = ".txt"

    body = """"""

    for x in categories:
        for y in c:
            for z in qa:
                f = open(dr + x + y + z + end, "w")

                f.write(body)

                f.close()
        

builder()