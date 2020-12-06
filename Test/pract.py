import os
from datetime import datetime

curr_time = datetime.now()
    # 2020_10_09_23_48_57.3294873849
curr = str(curr_time).replace("-", "_").replace(" ", "_").replace(":", "_")
#html_file = os.getcwd() + "/../Reports/" +get_current_date_time()  + "ReportFile.html"
html_file = os.getcwd() + "/Main/Reports/" + curr.split(".")[0] + "ReportFile.html"
print("Path : "+ html_file)
