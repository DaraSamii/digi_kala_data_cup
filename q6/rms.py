try:
    n = input()
    n_list = input().split(' ')

    exit_indexes = [n_list.index('2')+ 1]

    e = int(input())
    e_list = []
    for i in range(e):
        e_list.append([int(x) for x in input().split(' ')])

    #print(n_list)

    #print(exit_indexes)

    d = []
    states = []

    for es in e_list:
        for exit in exit_indexes:
            if es[1] == exit:
                states.append(es)
                break


    exit_indexes = [i[0] for i in states]
    #print(exit_indexes)
    counter = 0
    while states != []:
        counter += 1
        if counter == 3:
            break
        d.append(states)
        e_list = [i for i in e_list if i not in states]
        states = []

        exit_indexes1 = []
        for es in e_list:
            for exit in exit_indexes:
                if es[1] == exit:
                    states.append(es)
                    exit_indexes1.append(es[0])
                    break

        #print(states)
        exit_indexes= exit_indexes1
        #print(exit_indexes)


    #print(d)

    qualified = []
    #print(len(d))
    for i in range(len(d)-1,0,-1):
        #print(i)
        qualified_state = []
        for l in d[i-1]:
            #print(l)
            In = l[0]
            out = l[1]
            Max = l[2]
            #print(Max)
            s = 0
            for j in d[i]:
                if j[1] == In:
                    s += j[2]
            #print(s,'s')

            if s > Max:
                #print('True')
                qualified_state.append((In,out,Max))
            else:
                #print('ss')
                qualified_state.append((In, out, s))

            #print('helo')
            #print(qualified_state)
            qualified.append(qualified_state)


    print(sum([i[2] for i in qualified[-1]]))
except:
    print(0)