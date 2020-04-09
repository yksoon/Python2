apart = [101, 102, 103, 104]
for i in apart:
    print("Newspaper delivery: ", i)


apart2 = apart = [[101, 102, 103, 104],[201, 202, 203, 204],
                  [301, 302, 303, 304], [401, 402, 403, 404]]
type(apart2[0])

apart2[0][0]

for i in apart2:
    for n in apart2[i]:
        
        print("Newspaper delivery: ", apart2[i][n])
        
        if apart2[i][n] == apart2[1][2]:
            pass

