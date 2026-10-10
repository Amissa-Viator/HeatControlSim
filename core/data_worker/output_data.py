class OutputData:
    def __init__(self, x_value: float, u_value: float, v_value: float):
        self.x_value = x_value
        self.u_value = u_value
        self.v_value = v_value

    @property
    def get_x_value(self) -> float:
        return self.x_value

    @property
    def get_u_value(self) -> float:
        return self.u_value

    @property
    def get_v_value(self) -> float:
        return self.v_value

    def as_dict(self):
        return {"x": self.x_value, "u": self.u_value, "v": self.v_value}
