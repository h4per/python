

class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self, new_cpu):
        self.__cpu = new_cpu

    @property
    def memory(self):
        return self.__memory
    
    @memory.setter
    def memory(self, new_memory):
        self.__memory = new_memory

    def make_computations(self):
        result = self.__cpu + self.__memory
        print("Computations result:", result)
    
    def __str__(self) -> str:
        return f"Комп: CPU = {self.__cpu}, Память = {self.__memory}"

    def __lt__(self, other):
        return self.memory < other.memory
    
    def __gt__(self, other):
        return self.memory > other.memory
    
    def __eq__(self, other):
        return self.memory == other.memory
    
    def __ne__(self, other):
        return self.memory != other.memory
    
    def __ge__(self, other):
        return self.memory >= other.memory

    def __le__(self, other):
        return self.memory <= other.memory
    


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list
    
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list
    
    @sim_cards_list.setter
    def sim_cards_list(self, new_sim_cards_list):
        self.__sim_cards_list = new_sim_cards_list


    def call(self, sim_card_number, call_to_number):
        if sim_card_number == 1:
            return f"Идет звонок на номер {call_to_number} с сим-карты-1 - Beeline"
        elif sim_card_number == 2:
            return f"Идет звонок на номер {call_to_number} с сим-карты-2 - O!"
        elif sim_card_number == 3:
            return f"Идет звонок на номер {call_to_number} с сим-карты-3 - Megacom"
        else:
            print("Ошибка")

    def __str__(self) -> str:
        return f"Симки: {self.__sim_cards_list}"




class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def __str__(self):
        return f"Смартфон: Процессор = {self.cpu}, Память = {self.memory}, Симки = {self.sim_cards_list}"
    
    def use_gps(self, location):
        print(f"Осталось 10км до {location}")



# для Computer
pc = Computer("Intel", "18GB")
pc2 = Computer("Snapdragon", "8GB")
# print("Процессор:", pc.cpu)
# print("Память:", pc.memory)
# print(pc)

# print(pc == pc2)
# print(pc != pc2)
# print(pc < pc2)
# print(pc > pc2)
# print(pc <= pc2)
# print(pc >= pc2)

# pc.cpu = "AMD"
# pc.memory = "32GB"
# print(pc.cpu, pc.memory)

# pc.make_computations()



# для Phone
phon = Phone(["Билайн", "Мегаком", "О!", "НТС"])
# print(phon)

# print(phon.sim_cards_list)
phon.sim_cards_list = ["МТС", "Chicken"]
# print(phon.sim_cards_list)

# print(phon.call(1, "+996 775 15 15 06"))
# print(phon.call(2, "+996 775 15 15 06"))
# print(phon.call(3, "+996 775 15 15 06"))



# для SmartPhone
smartphone1 = SmartPhone("MediaTek", "12GB",["Kyrgyztelecom", "sim324"])
smartphone2 = SmartPhone("Exynos", "6GB", ["Kyrgyztelecom", "sim324"])
# print(smartphone1)
# print(smartphone2)

# smartphone1.use_gps("Ош")
