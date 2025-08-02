# Generated from: f5832b03-40af-4433-9245-7972f57881aa.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farming system within a repurposed warehouse. It integrates architectural planning, environmental control calibration, crop selection based on microclimate data, automated nutrient delivery setup, waste recycling mechanisms, and real-time growth monitoring. The process demands coordination across construction, agronomy, IoT integration, and sustainability compliance teams to optimize yield while minimizing energy and water consumption in an urban environment. Stakeholder engagement includes local authorities, technology vendors, and community groups to ensure regulatory adherence and social acceptance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Legal_Review = Transition(label='Legal Review')
Tech_Sourcing = Transition(label='Tech Sourcing')
Structural_Build = Transition(label='Structural Build')
Climate_Setup = Transition(label='Climate Setup')
Irrigation_Install = Transition(label='Irrigation Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
Crop_Select = Transition(label='Crop Select')
Nutrient_Prep = Transition(label='Nutrient Prep')
Waste_System = Transition(label='Waste System')
Automation_Config = Transition(label='Automation Config')
Trial_Growth = Transition(label='Trial Growth')
Data_Analysis = Transition(label='Data Analysis')
Quality_Audit = Transition(label='Quality Audit')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Compliance_Check = Transition(label='Compliance Check')

# Construction phase partial order
construction = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, Structural_Build])
construction.order.add_edge(Site_Survey, Design_Layout)
construction.order.add_edge(Design_Layout, Structural_Build)

# Environmental & IoT setup: two partial orders concurrent - climate setup and sensor/install
env_setup1 = StrictPartialOrder(nodes=[Climate_Setup, Irrigation_Install])
env_setup1.order.add_edge(Climate_Setup, Irrigation_Install)

env_setup2 = StrictPartialOrder(nodes=[Sensor_Deploy, Tech_Sourcing])
env_setup2.order.add_edge(Sensor_Deploy, Tech_Sourcing)

env_iot_setup = StrictPartialOrder(nodes=[env_setup1, env_setup2])
# No order edges between env_setup1 and env_setup2 to run concurrently

# Crop & nutrient prep partial order
crop_nutrient = StrictPartialOrder(nodes=[Crop_Select, Nutrient_Prep])
crop_nutrient.order.add_edge(Crop_Select, Nutrient_Prep)

# Waste & automation partial order
waste_and_auto = StrictPartialOrder(nodes=[Waste_System, Automation_Config])
waste_and_auto.order.add_edge(Waste_System, Automation_Config)

# Monitoring & analysis partial order
monitoring = StrictPartialOrder(nodes=[Trial_Growth, Data_Analysis, Quality_Audit])
monitoring.order.add_edge(Trial_Growth, Data_Analysis)
monitoring.order.add_edge(Data_Analysis, Quality_Audit)

# Stakeholder & compliance partial order
stakeholder = StrictPartialOrder(nodes=[Stakeholder_Meet, Legal_Review, Compliance_Check])
stakeholder.order.add_edge(Stakeholder_Meet, Legal_Review)
stakeholder.order.add_edge(Legal_Review, Compliance_Check)

# Integrate agronomy-related activities (crop, waste, monitoring)
agronomy = StrictPartialOrder(nodes=[crop_nutrient, waste_and_auto, monitoring])
agronomy.order.add_edge(crop_nutrient, waste_and_auto)
agronomy.order.add_edge(waste_and_auto, monitoring)

# Integrate construction, environmental/IoT setup, agronomy and stakeholder
root = StrictPartialOrder(
    nodes=[construction, env_iot_setup, agronomy, stakeholder]
)

root.order.add_edge(construction, env_iot_setup)
root.order.add_edge(env_iot_setup, agronomy)
root.order.add_edge(agronomy, stakeholder)