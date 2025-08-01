# Generated from: 11707635-a7a9-4da6-87a1-91228671398b.json
# Description: This process outlines the establishment of an urban vertical farm designed to optimize space utilization in dense city environments. It involves initial site assessment, modular structure assembly, hydroponic system installation, environmental control calibration, crop selection tailored to microclimates, nutrient solution formulation, automated monitoring setup, staff training on specialized equipment, pest management planning using integrated pest management techniques, scheduling of planting and harvesting cycles, data analytics for yield optimization, waste recycling integration, community engagement for local sourcing, compliance verification with urban agricultural regulations, and final operational handover ensuring sustainability and scalability of the farm infrastructure.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Structure_Build = Transition(label='Structure Build')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Climate_Control = Transition(label='Climate Control')
Crop_Selection = Transition(label='Crop Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Install = Transition(label='Sensor Install')
Staff_Training = Transition(label='Staff Training')
Pest_Planning = Transition(label='Pest Planning')
Plant_Scheduling = Transition(label='Plant Scheduling')
Yield_Analysis = Transition(label='Yield Analysis')
Waste_Recycle = Transition(label='Waste Recycle')
Community_Meet = Transition(label='Community Meet')
Regulation_Check = Transition(label='Regulation Check')
Operation_Handover = Transition(label='Operation Handover')

# Construct partial order according to described logical sequence:
# Site Survey --> Structure Build --> Hydroponic Setup --> Climate Control
# --> Crop Selection --> Nutrient Mix --> Sensor Install --> Staff Training
# --> Pest Planning --> Plant Scheduling --> Yield Analysis --> Waste Recycle
# --> Community Meet --> Regulation Check --> Operation Handover

root = StrictPartialOrder(
    nodes=[
        Site_Survey, Structure_Build, Hydroponic_Setup, Climate_Control, Crop_Selection,
        Nutrient_Mix, Sensor_Install, Staff_Training, Pest_Planning, Plant_Scheduling,
        Yield_Analysis, Waste_Recycle, Community_Meet, Regulation_Check, Operation_Handover
    ]
)

root.order.add_edge(Site_Survey, Structure_Build)
root.order.add_edge(Structure_Build, Hydroponic_Setup)
root.order.add_edge(Hydroponic_Setup, Climate_Control)
root.order.add_edge(Climate_Control, Crop_Selection)
root.order.add_edge(Crop_Selection, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Sensor_Install)
root.order.add_edge(Sensor_Install, Staff_Training)
root.order.add_edge(Staff_Training, Pest_Planning)
root.order.add_edge(Pest_Planning, Plant_Scheduling)
root.order.add_edge(Plant_Scheduling, Yield_Analysis)
root.order.add_edge(Yield_Analysis, Waste_Recycle)
root.order.add_edge(Waste_Recycle, Community_Meet)
root.order.add_edge(Community_Meet, Regulation_Check)
root.order.add_edge(Regulation_Check, Operation_Handover)