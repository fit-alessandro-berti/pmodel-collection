# Generated from: d726c9d5-daef-4950-8a6b-5f75d4a9c904.json
# Description: This process outlines the establishment of an urban rooftop farming system in a dense metropolitan area. It involves site assessment, structural evaluation, soil and water testing, and selecting suitable crops based on microclimate data. The procedure also includes procuring eco-friendly materials, installing modular planters, integrating automated irrigation and nutrient delivery systems, and setting up solar-powered sensors for real-time environmental monitoring. Additionally, community engagement and training sessions are conducted to ensure sustainable maintenance and maximize local participation. The process concludes with periodic yield analysis and adaptive adjustments to optimize productivity while minimizing environmental impact in a constrained urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Site_Survey = Transition(label='Site Survey')
Structure_Check = Transition(label='Structure Check')
Soil_Sample = Transition(label='Soil Sample')
Water_Test = Transition(label='Water Test')
Crop_Selection = Transition(label='Crop Selection')
Material_Order = Transition(label='Material Order')
Planter_Setup = Transition(label='Planter Setup')
Irrigation_Install = Transition(label='Irrigation Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
Solar_Setup = Transition(label='Solar Setup')
Data_Integration = Transition(label='Data Integration')
Community_Meet = Transition(label='Community Meet')
Training_Session = Transition(label='Training Session')
Yield_Monitor = Transition(label='Yield Monitor')
Adjust_Plan = Transition(label='Adjust Plan')

# Partial order for site assessment branch (concurrent Soil Sample and Water Test after Site Survey and Structure Check)
site_assessment = StrictPartialOrder(
    nodes=[Site_Survey, Structure_Check, Soil_Sample, Water_Test, Crop_Selection]
)
site_assessment.order.add_edge(Site_Survey, Structure_Check)
site_assessment.order.add_edge(Structure_Check, Soil_Sample)
site_assessment.order.add_edge(Structure_Check, Water_Test)
site_assessment.order.add_edge(Soil_Sample, Crop_Selection)
site_assessment.order.add_edge(Water_Test, Crop_Selection)

# Partial order for installation branch (Material Order -> Planter Setup -> multiple installs in partial order)
installation = StrictPartialOrder(
    nodes=[Material_Order, Planter_Setup, Irrigation_Install, Sensor_Deploy, Solar_Setup, Data_Integration]
)
installation.order.add_edge(Material_Order, Planter_Setup)
installation.order.add_edge(Planter_Setup, Irrigation_Install)
installation.order.add_edge(Planter_Setup, Sensor_Deploy)
installation.order.add_edge(Planter_Setup, Solar_Setup)
# Data integration happens after all installations
installation.order.add_edge(Irrigation_Install, Data_Integration)
installation.order.add_edge(Sensor_Deploy, Data_Integration)
installation.order.add_edge(Solar_Setup, Data_Integration)

# Partial order for community engagement and training (Community Meet -> Training Session)
community = StrictPartialOrder(
    nodes=[Community_Meet, Training_Session]
)
community.order.add_edge(Community_Meet, Training_Session)

# Loop for monitoring and adjustment: loop(Yield_Monitor, Adjust_Plan)
loop_monitor_adjust = OperatorPOWL(operator=Operator.LOOP, children=[Yield_Monitor, Adjust_Plan])

# Combine the main parts in partial order:
# site_assessment -> installation -> community -> loop_monitor_adjust
root = StrictPartialOrder(
    nodes=[site_assessment, installation, community, loop_monitor_adjust]
)
root.order.add_edge(site_assessment, installation)
root.order.add_edge(installation, community)
root.order.add_edge(community, loop_monitor_adjust)