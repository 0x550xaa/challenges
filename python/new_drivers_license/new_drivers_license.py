class TimeSpentGettingALicense:
    def __init__(self, name, available_agents, other_people):
        self.name = name
        self.available_agents = available_agents
        self.clients = sorted(f'{name} {other_people}'.split(' '))
    
    def calculate(self):
        time_spent = self.my_group() * 20
        print(time_spent)
    
    def my_group(self):
        position = self.clients.index(self.name)
        group = (position + 1) / self.available_agents
        print(group, round(group, 0))
        if group > round(group, 0):
            group = round(group, 0) + 1
        else:
            group = round(group, 0)
        return group
        


# One word names and no duplicates allowed

TimeSpentGettingALicense(input(), int(input()), input()).calculate()
