import plotly.express as px
import plotly.graph_objects as go
from IPython.display import HTML

import plotly.graph_objs as go
import plotly.offline as pof

## 設定為離線
pof.plot([{'x': [1, 7, 8], 'y': [3, 8, 14]}], filename = 'My First Plotly', show_link = True, link_text = "Plotly Links", image = 'png', image_width = 800, image_height= 900)