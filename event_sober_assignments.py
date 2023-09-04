from datetime import date

class Event(): 

    name = ''
    date_of_event = ''
    drivers = 0 
    stationaries = 0
    sober_exec = 0
    roamers = 0
    bartenders = 0
    bartenders_twenty_one = True
    list = 0
    max_soberShifts = 0

    sober_data_dict = {}
    sobers = []
    over_twenty_one = []
    exceptions = []
    exec = []



    def import_sober_data(self): 

        file = open('sober_data/sober_data.txt', 'r')
        for line in file: 
            if line != '\n':
                last_name =  line.split(',')[0]
                second_line = line.split(',')[1].strip()
                first_name = ''
                sober_shifts = 0
                is_alphabet = True

                for char in second_line: 
                    if char != ' ' and char != '\t': 
                        if is_alphabet == True: 
                            first_name = first_name + char
                        else:
                            sober_shifts = int(char)
                    else:
                        is_alphabet = False

                full_name = first_name + ' ' + last_name
                dict_line = {full_name.lower() : sober_shifts}
                if self.max_soberShifts < sober_shifts:
                    self.max_soberShifts = sober_shifts 
                self.sober_data_dict.update(dict_line)
                    


    def import_age_data(self): 
        file = open('sober_data/birthdays.txt', 'r')
        for line in file: 
            if line != '\n':
                last_name =  line.split(',')[0]
                second_line = line.split(',')[1].strip()
                first_name = ''
                birthday = ''
                is_alphabet = True
                for char in second_line: 
                    if char != ' ' and char != '\t': 
                        if is_alphabet == True: 
                            first_name = first_name + char
                        else:
                            birthday = birthday + char
                    else:
                        is_alphabet = False
                full_name = first_name + ' ' + last_name
                birthday_split = birthday.split('/')


            if self.is_over_twenty_one(birthday=birthday_split): 
                self.over_twenty_one.append(full_name.lower())
        
    def import_exceptions_data(self): 
        file = open('sober_data/excuses.txt', 'r')
        for line in file: 
            if line != '\n':
                name = line.lower()
                self.exceptions.append(name.rstrip('\n'))

    def import_exec_data(self):
        file = open('sober_data/exec.txt', 'r')
        for line in file:
            if line != '\n': 
                name = line.lower()
                self.exec.append(name.rstrip('\n'))



    def is_over_twenty_one(self, birthday): 
        year = int(birthday[2])
        day = int(birthday[1])
        month = int(birthday[0])
        today = date.today()

        if (today.year - year) >  21: 
            return True
        elif (today.year - year) == 21: 
            if month < today.month: 
                return True
            elif month == today.month: 
                if day <= today.day: 
                    return True
        
        return False
    
    def assignDrivers(self):
        driver_count = 0 
        drivers_assigned = []
        for i in range(self.max_soberShifts + 1):
            for name in self.sober_data_dict: 
                if self.sober_data_dict[name] == i:
                    if name not in self.sobers and name not in drivers_assigned and name not in self.exceptions and name not in self.exec:
                        if self.bartenders_twenty_one and name not in self.over_twenty_one: 
                            drivers_assigned.append(name)
                            self.sobers.append(name)
                            driver_count = driver_count + 1
                        elif self.bartenders_twenty_one == False:
                            drivers_assigned.append(name)
                            self.sobers.append(name)
                            driver_count = driver_count + 1
                    if driver_count >= self.drivers: 
                        break
            else: 
                continue
            break

        return drivers_assigned
    
    def assignRoamers(self): 
        roamer_count = 0
        roamers_assigned = []

        for i in range(self.max_soberShifts + 1):
            for name in self.sober_data_dict: 
                if self.sober_data_dict[name] == i:
                    if name not in self.sobers and name not in roamers_assigned and name not in self.exceptions and name not in self.exec:
                        if self.bartenders_twenty_one and name not in self.over_twenty_one: 
                            roamers_assigned.append(name)
                            self.sobers.append(name)
                            roamer_count = roamer_count + 1
                        elif self.bartenders_twenty_one == False:
                            roamers_assigned.append(name)
                            self.sobers.append(name)
                            roamer_count = roamer_count + 1
                    if roamer_count >= self.roamers: 
                        break
            else: 
                continue
            break

        return roamers_assigned
    
    def assignStationaries(self): 
        stationary_count = 0
        stationaries_assigned = []

        for i in range(self.max_soberShifts + 1):
            for name in self.sober_data_dict: 
                if self.sober_data_dict[name] == i:
                    if name not in self.sobers and name not in stationaries_assigned and name not in self.exceptions and name not in self.exec:
                        if self.bartenders_twenty_one and name not in self.over_twenty_one: 
                            stationaries_assigned.append(name)
                            self.sobers.append(name)
                            stationary_count = stationary_count + 1
                        elif self.bartenders_twenty_one == False:
                            stationaries_assigned.append(name)
                            self.sobers.append(name)
                            stationary_count = stationary_count + 1
                    if stationary_count >= self.stationaries: 
                        break
            else: 
                continue
            break

        return stationaries_assigned
    
    def assignList(self): 
        list_count = 0
        list_assigned = []

        for i in range(self.max_soberShifts + 1):
            for name in self.sober_data_dict: 
                if self.sober_data_dict[name] == i:
                    if name not in self.sobers and name not in list_assigned and name not in self.exceptions and name not in self.exec:
                        if self.bartenders_twenty_one and name not in self.over_twenty_one: 
                            list_assigned.append(name)
                            self.sobers.append(name)
                            list_count = list_count + 1
                        elif self.bartenders_twenty_one == False:
                            list_assigned.append(name)
                            self.sobers.append(name)
                            list_count = list_count + 1
                    if list_count >= self.list: 
                        break
            else: 
                continue
            break

        return list_assigned
    
    def assignBartenders(self): 
        bartender_count = 0
        bartenders_assigned = []

        for i in range(self.max_soberShifts + 1):
            for name in self.sober_data_dict: 
                if self.sober_data_dict[name] == i:
                    if name not in self.sobers and name not in bartenders_assigned and name not in self.exceptions and name not in self.exec:
                        if self.bartenders_twenty_one and name in self.over_twenty_one: 
                            bartenders_assigned.append(name)
                            self.sobers.append(name)
                            bartender_count = bartender_count + 1
                        else:
                            bartenders_assigned.append(name)
                            self.sobers.append(name)
                            bartender_count = bartender_count + 1
                    if bartender_count >= self.bartenders: 
                        break
            else: 
                continue
            break

        return bartenders_assigned
    
    def assignExec(self): 
        exec_count = 0
        exec_assigned = []

        for i in range(self.max_soberShifts + 1):
            for name in self.sober_data_dict: 
                if self.sober_data_dict[name] == i:
                    if name not in self.sobers and name not in exec_assigned and name not in self.exceptions and name in self.exec:
                        exec_assigned.append(name)
                        self.sobers.append(name)
                        exec_count = exec_count + 1
                        # print(name)
                    if exec_count >= self.sober_exec: 
                        break
            else: 
                continue
            break
        
        return exec_assigned
    

        
    




    def resetSobers(self): 
        self.sobers = []

    
    





            