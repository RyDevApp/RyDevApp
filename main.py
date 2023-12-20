import RyPy
from RyPy import Bio

class Wealth:
    def __init__(self):
    self.physical_health = PhysicalHealth()
    self.mental_health = MentalHealth() 
    self.spiritual_health = SpiritualHealth() 
    self.net_worth = NetWorth() 
    self.reputation = Reputation()

    def update_health(self):
        while True:
            # Check for critical physical health condition
            if self.physical_health.status < 50:
                self.handle_critical_physical_health()
                break  # Break out of the loop if physical health is critical

            # Check the balance between mental and spiritual health
            if not self.mental_and_spiritual_health_balanced():
                self.balance_mental_and_spiritual_health()
            
            break  # Exit the loop when all conditions are checked

    def handle_critical_physical_health(self):
        # Handle the repercussions of critical physical health
        self.mental_health.decrease()
        self.spiritual_health.decrease()
        self.net_worth.decrease_due_to_health()
        self.reputation.decrease_due_to_health()

    def mental_and_spiritual_health_balanced(self):
        # Returns True if mental and spiritual health are balanced
        return abs(self.mental_health.status - self.spiritual_health.status) <= 10

    def balance_mental_and_spiritual_health(self):
        # Balances mental and spiritual health
        if self.mental_health.status > self.spiritual_health.status:
            self.spiritual_health.increase()
        else:
            self.mental_health.increase()

    def manage_wealth_and_reputation(self):
        if self.net_worth.amount > 100000:
            self.reputation.increase_due_to_wealth()
        else:
            if self.reputation.level > 80:
                self.net_worth.increase_due_to_reputation()
    
    def __init__(self):
            self.status = 100

        def update(self, change):
            self.status = max(0, min(100, self.status + change))
            return "Mental health status: " + str(self.status)

    class PhysicalHealth:
        def __init__(self):
            self.status = 100

        def update(self, change):
            self.status = max(0, min(100, self.status + change))
            return "Physical health status: " + str(self.status)

    class SpiritualHealth:
        def __init__(self):
            self.status = 100

        def update(self, change):
            self.status = max(0, min(100, self.status + change))
            return "Spiritual health status: " + str(self.status)

    def __init__(self):
        self.money = 0
        self.connections = []
        self.knowledge = []
        self.mental_health = self.MentalHealth()
        self.physical_health = self.PhysicalHealth()
        self.spiritual_health = self.SpiritualHealth()

    def overall_health_status(self):
        return (self.mental_health.status + self.physical_health.status + self.spiritual_health.status) / 3

    def accumulate(self):
        self.money += 1
        self.knowledge.append('new skill')
        self.connections.append('new contact')

    def life_journey(self):
        for _ in range(5):  # Simulating 5 cycles of life activities
            self.accumulate()

            # Adjust health based on activities
            if self.overall_health_status() > 80:
                print("Time to take a break and focus on health.")
                self.mental_health.update(-10)
                self.physical_health.update(-10)
                self.spiritual_health.update(-5)
            else:
                print("Pushing through with passion and hard work.")
                self.mental_health.update(-20)
                self.physical_health.update(-15)
                self.spiritual_health.update(-10)

            print(f"Overall health status: {self.overall_health_status()}")

# Create a Wealth instance to simulate life journey
my_wealth = Wealth()

# Simulate the journey
my_wealth.life_journey()
