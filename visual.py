from process import ProcessedData
import plotly.express as px

class VisualisedData(ProcessedData):

    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    visualised = VisualisedData()
