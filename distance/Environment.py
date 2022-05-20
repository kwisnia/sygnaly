class Environment:
    def __init__(
        self,
        time_step,
        signal_velocity,
        item_velocity,
        distance_sensor,
        start_item_distance,
    ):
        self.time_step = time_step
        self.signal_velocity = signal_velocity
        self.item_velocity = item_velocity
        self.distance_sensor = distance_sensor
        self.item_distance = start_item_distance
        self.timestamp = 0.0

    def step(self):
        self.timestamp += self.time_step

        self.item_distance += self.item_velocity * self.time_step

        delay = self.item_distance / self.signal_velocity * 2.0
        self.distance_sensor.update(delay, self.timestamp, self.signal_velocity)
