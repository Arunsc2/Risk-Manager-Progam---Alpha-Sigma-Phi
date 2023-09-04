import event_sober_assignments

class RM():

    def assignSobers(drivers, stationaries, roamers, bartenders, list, exec, isTwentyOne): 
        event = event_sober_assignments.Event()
        event.resetSobers()
        event.import_sober_data()
        event.import_age_data()
        event.import_exceptions_data()
        event.import_exec_data()
        event.bartenders_twenty_one = isTwentyOne
        event.drivers = drivers
        event.stationaries = stationaries
        event.roamers = roamers
        event.bartenders = bartenders 
        event.list = list
        event.sober_exec = exec

        drivers_assigned = event.assignDrivers()
        roamers_assigned = event.assignRoamers()
        stationaries_assigned = event.assignStationaries()
        list_assigned = event.assignList()
        bartenders_assigned = event.assignBartenders()
        exec_assigened = event.assignExec()

        sobers_assigend = [drivers_assigned, roamers_assigned, stationaries_assigned, list_assigned, bartenders_assigned, exec_assigened]
        return sobers_assigend
        # print(drivers_assigned)
        # print(roamers_assigned)
        # print(event.bartenders_twenty_one)


# rm = RM()
# rm.assignSobers(drivers=2, stationaries=2, roamers=2, bartenders=2, list=2, exec=1, isTwentyOne=True)