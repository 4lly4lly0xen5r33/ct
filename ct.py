listOfEvents = []
listOfTime = []


def alter(changling):
    finished = (input("Done to Quit or Ready to start"))
    while finished != "done":
        finished = (input("Done to Quit or Ready to start"))


        act = (input("Change? Remove?"))
        if act == "change":
            newEvent = (input("New event name:"))
            newTime = (input("New time:"))
            listOfEvents.append(newEvent)
            listOfTime.append(newTime)
            listOfEvents.remove(listOfEvents[-2])
            listOfTime.remove(listOfTime[-2])
            return
        if act == "remove":
            listOfEvents.remove(listOfEvents[-1])
            listOfTime.remove(changling)
        if act == "done":
            return






print("Day2Day Scheduler")


listchoices = (input("Type ""NEW"" to create a new list. Type ""VIEW"" to view most recent list. Type ""DELETE"" to get rid of your most recent list."))
while listchoices != "quit":
    if listchoices == "new" or listchoices == "NEW":
        a = int(input("How many events will be in your schedule this time?"))
        while a != 0:
            events = (input("Name the event: "))
            listOfEvents.append(events)
            time = int(input("Enter time for event as 4 digits, for example, if the time was 12:30, you would just enter 1230, if time was 2: 40 PM, you would just answer 1440."))
            if time > 2459:
                print("ERROR")
            else:
                listOfTime.append(time)
                changeItem = (input("type alter to remove item from list or edit"))
            if changeItem == "alter":
                alter(listOfTime[-1])
                a = a + 1
            else:
                a = a-1
        print("Done with list!")
    listchoices = (input("Type ""NEW"" to create a new list. Type ""VIEW"" to view most recent list. Type ""DELETE"" to get rid of your most recent list."))


    if listchoices == "view" or listchoices == "VIEW":
        show = list(zip(listOfEvents, listOfTime))
        show.sort(reverse=True)
        print(*show,sep='\n')
        listchoices = (input("Type ""NEW"" to create a new list. Type ""VIEW"" to view most recent list. Type ""DELETE"" to get rid of your most recent list."))


