# src/simulation/agent_model.py

from mesa import Agent, Model
from mesa.time import SimultaneousActivation

class WorkerAgent(Agent):
    def __init__(self, unique_id, model, origin, destination):
        super().__init__(unique_id, model)
        self.origin = origin
        self.destination = destination
        self.position = origin
        self.path = [origin]
        self.arrived = False

    def step(self):
        if self.arrived:
            return

        lat, lon = self.position
        dlat = (self.destination[0] - lat) * 0.1
        dlon = (self.destination[1] - lon) * 0.1

        new_lat = lat + dlat
        new_lon = lon + dlon
        self.position = (new_lat, new_lon)
        self.path.append(self.position)

        if abs(new_lat - self.destination[0]) < 0.001 and abs(new_lon - self.destination[1]) < 0.001:
            self.arrived = True

class CommuteSimulation(Model):
    def __init__(self, dataframe):
        self.schedule = SimultaneousActivation(self)
        self.agents = []

        for i, row in dataframe.iterrows():
            origin = (row['Lat_Residencia'], row['Lon_Residencia'])
            destination = (row['Lat_Trabajo'], row['Lon_Trabajo'])
            agent = WorkerAgent(i, self, origin, destination)
            self.schedule.add(agent)
            self.agents.append(agent)

    def step(self):
        self.schedule.step()

    def run(self, steps=20):
        for _ in range(steps):
            self.step()

    def get_trajectories(self):
        return [agent.path for agent in self.agents]


# USO DESDE NOTEBOOKS:
#from src.simulation.agent_model import CommuteSimulation

#modelo = CommuteSimulation(df)
#modelo.run(steps=20)
#trayectorias = modelo.get_trajectories()

