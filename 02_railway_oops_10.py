# import pandas as pd

# pd.DataFrame()
class RailwayForm:
    formType = 'RailwayForm'
    def printData(self):
        print(f'name is {self.name} and train is {self.train}')


utsavApplication = RailwayForm()
utsavApplication.name = 'utsav'
utsavApplication.train = 'rajdhani Express'
utsavApplication.printData()
