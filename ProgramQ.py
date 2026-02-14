def search(l,t):
    result = False
    for i in l:
        if i == t:
            result = True
    return result
queuelist = []
queuename = []
instruction = 0
currentqueue = -1
instruction_no = 0
while True:
    instruction_no += 1
    if currentqueue == -1:
        currentindex = -1
    else:
        currentindex = queuename.index(currentqueue)
    instruction_no += 1
    ilist = list(map(str, input('<Instruction> ').split()))
    if len(ilist) == 0:
        continue
    instruction = ilist[0]
    if instruction == 'halt':
        print('ProgramQ is halted.')
        break
        
    elif instruction == 'help':
        print('ProgramQ is a simple flash program where you can control "Queues" using instructions.')
        print('Every queues in this program uses First-in&First-out method')
        print('This means elements added first will be removed first.')
        print('---------------------------------------------------------------------------------------------')
        print('halt : Halt ProgramQ, all the data are deleted upon halting')
        print('mkq <queuename> : Generate a new Queue <queuename>')
        print('cq <queuename> : Move to the Queue <queuename>')
        print('cqi <index> : Move to the Queue with index <index>')
        print('rm <queuename> : Delete Queue <queuename>')
        print('current : Print the queue that you are currently in')
        print('check : Examine the queue that you are currently in')
        print('check qs : Examine the queuelist')
        print('enq <element> : Add element <element> from the back of the queue.')
        print('deq : Remove an element from the front of the queue.')
        print('size : Output the size of the queue that you are currently in')
        print('size qs : Output the size of the queuelist')
        print('empty : Output if the current queue is empty.')
        print('empty qs : Output if the queuelist is empty.')
        print('untarget : Deselect the queue.')
        print()
        
    elif instruction == 'mkq':
        if len(ilist) == 1:
            print('Necessary Input Undetected. (queueName)')
            print()
            continue
        if search(queuename, ilist[1]) == True:
            print('Queue already existing')
            print()
            continue
        if len(ilist) == 2:
            queuename.append(ilist[1])
            queuelist.append([])
            print('Added queue named', ilist[1])
            print()
            
    elif instruction == 'cq':
        if len(ilist) == 1:
            print('Necessary Input Undetected. (queueName)')
            print()
            continue
        canmove = False
        for i in queuename:
            if i == ilist[1]:
                canmove = True
        if canmove == True:
            currentqueue = ilist[1]
            print('Moved to queue', ilist[1])
            print()
        if canmove == False:
            print('Invalid Queue Name.')
            print()
            continue
         
    elif instruction == 'cqi':
        if len(ilist) == 1:
            print('Necessary Input Undetected. (queueIndex)')
            print()
            continue
        if int(len(queuelist)) <= int(ilist[1]):
            print("Queue Index out of range.")
            print()
            continue
        currentqueue = queuename[int(ilist[1])]
        print('Moved to queue index', ilist[1], "(", currentqueue, ')' )
        print()
        
    elif instruction == 'rm':
        if len(ilist) == 1:
            print('Necessary Input Undetected. (queueName)')
            print()
            continue
        canmove = False
        for i in queuename:
            if i == ilist[1]:
                canmove = True
        if canmove == True:
            print('Removed Queue', ilist[1])
            rmindex = queuename.index(ilist[1])
            queuename.pop(rmindex)
            queuelist.pop(rmindex)
            if ilist[1] == currentqueue:
                currentqueue = -1
            print()
        if canmove == False:
            print('Invalid Queue Name.')
            print()
            continue
            
    elif instruction == 'current':
        if currentqueue == -1:
            print('You are not in a queue.')
            print()
            continue
        print("Current Queue:", currentqueue, '(Index ', queuename.index(currentqueue), ')')
        print()    
    elif instruction == 'check':
        if len(ilist) == 1:
            if currentqueue == -1:
                print('Queue unselected')
                print()
                continue
            print(queuelist[currentindex])
            print()
            continue
        if ilist[1] == 'qs':
            print(queuename)
            print()
    
    elif instruction == 'enq':
        if currentqueue == -1:
            print('Queue unselected')
            print()
            continue
        if len(ilist) == 1:
            print('Necessary Input Undetected (elementName)')
            print()
            continue
        queuelist[currentindex].append(ilist[1])
        print('Enqueued element', ilist[1])
        print()
    
    elif instruction == 'deq':
        if currentqueue == -1:
            print('Queue unselected')
            print()
            continue
        if len(queuelist[currentindex]) == 0:
            print('No elements in queue')
            print()
            continue
        print('Dequeued element', queuelist[currentindex][0])
        queuelist[currentindex].pop(0)
        print()
    
    elif instruction == 'size':
        if len(ilist) == 1:
            if currentqueue == -1:
                print('Queue unselected')
                print()
                continue
            print('Size of selected queue:', len(queuelist[currentindex]))
            print()
            continue
        if ilist[1] == 'qs':
            print('Amount of queues:', len(queuelist))
            print()
            
    elif instruction == 'empty':
        if len(ilist) == 1:
            if currentqueue == -1:
                print('Queue unselected')
                print()
                continue
            if len(queuelist[currentindex]) == 0:
                print(True)
                print()
                continue
            if len(queuelist[currentindex]) != 0:
                print(False)
                print()
                continue
        if ilist[1] == 'qs':
            if len(queuelist) == 0:
                print(True)
                print()
                continue
            else:
                print(False)
                print()
                continue
                
    elif instruction == 'untarget':
        currentqueue = -1
        print('Deselected Queue.')
        print()
        continue
    
    else:
        print('Invalid instruction')
        print()