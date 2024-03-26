import plotly.express as px
import numpy as np
class Spirograph:
    def __init__(self, r_f, r_r, r_d):
        self.r_f = r_f
        self.r_r = r_r
        self.r_d = r_d        
        self.theta = np.arange(0,2 * np.pi * self.r_r/np.gcd(self.r_f, self.r_r),0.01)
        self.x, self.y = self.calculate()
    def calculate(self):
        x = (self.r_f-self.r_r)*np.cos(self.theta) + self.r_d*np.cos((1-self.r_f/self.r_r)*self.theta)
        y = (self.r_f-self.r_r)*np.sin(self.theta) + self.r_d*np.sin((1-self.r_f/self.r_r)*self.theta)
        return x, y    
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

spirograph = Spirograph(7, 2, 1)
fig = px.line(x=spirograph.get_x(), y=spirograph.get_y(), width=400, height=400)
fig.show()