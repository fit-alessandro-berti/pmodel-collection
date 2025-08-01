# Generated from: c2bf3351-312d-400e-8431-961d9aac3016.json
# Description: This process describes the adaptive urban farming cycle designed to optimize limited space agriculture through dynamic resource allocation, environmental monitoring, and community engagement. It begins with site analysis to assess microclimate and soil conditions, followed by modular bed setup. Sensors gather real-time data on moisture, light, and air quality, which feeds into an AI-driven irrigation and nutrient delivery system. Concurrently, crop selection adapts seasonally based on predictive analytics and community dietary needs. Pest control leverages integrated biological methods, minimizing chemical use. Harvesting is coordinated with local markets and direct consumer feedback to adjust future planting schedules. Continuous education workshops foster urban farmer skills, and waste composting closes the loop, ensuring sustainable nutrient cycling. This cyclical approach promotes resilience, efficiency, and social integration within urban agriculture systems.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transition nodes
Site_Analysis = Transition(label='Site Analysis')
Bed_Setup = Transition(label='Bed Setup')
Sensor_Install = Transition(label='Sensor Install')
Data_Capture = Transition(label='Data Capture')
Irrigation_Adjust = Transition(label='Irrigation Adjust')
Nutrient_Supply = Transition(label='Nutrient Supply')
Crop_Select = Transition(label='Crop Select')
Pest_Monitor = Transition(label='Pest Monitor')
Biocontrol_Deploy = Transition(label='Biocontrol Deploy')
Harvest_Plan = Transition(label='Harvest Plan')
Market_Sync = Transition(label='Market Sync')
Feedback_Gather = Transition(label='Feedback Gather')
Workshop_Host = Transition(label='Workshop Host')
Waste_Compost = Transition(label='Waste Compost')
Cycle_Review = Transition(label='Cycle Review')
Schedule_Update = Transition(label='Schedule Update')

# Data process: Sensor Install --> Data Capture --> LOOP(Irrigation & Nutrient)
irrigation_nutrient = OperatorPOWL(operator=Operator.LOOP,
                                   children=[Irrigation_Adjust, Nutrient_Supply])

data_proc = StrictPartialOrder(nodes=[Sensor_Install, Data_Capture, irrigation_nutrient])
data_proc.order.add_edge(Sensor_Install, Data_Capture)
data_proc.order.add_edge(Data_Capture, irrigation_nutrient)

# Pest control partial order: Pest Monitor --> Biocontrol Deploy
pest_control = StrictPartialOrder(nodes=[Pest_Monitor, Biocontrol_Deploy])
pest_control.order.add_edge(Pest_Monitor, Biocontrol_Deploy)

# Harvest planning partial order: Harvest Plan --> Market Sync --> Feedback Gather
harvest_planning = StrictPartialOrder(nodes=[Harvest_Plan, Market_Sync, Feedback_Gather])
harvest_planning.order.add_edge(Harvest_Plan, Market_Sync)
harvest_planning.order.add_edge(Market_Sync, Feedback_Gather)

# Education and waste compost concurrent activities
education_waste = StrictPartialOrder(nodes=[Workshop_Host, Waste_Compost])
# no order edges between Workshop_Host and Waste_Compost (concurrent)

# Crop Select (seasonal adaptation) runs concurrently with Pest control
crop_pest = StrictPartialOrder(nodes=[Crop_Select, pest_control])

# Crop Select and Pest control are concurrent inside crop_pest

# Combine Harvest and Education/Waste concurrently
harvest_education_waste = StrictPartialOrder(nodes=[harvest_planning, education_waste])
# concurrent, no order edges

# After Bed Setup, parallel branches:
# 1) data_proc
# 2) crop_pest
# 3) harvest_education_waste
parallel_branches = StrictPartialOrder(
    nodes=[data_proc, crop_pest, harvest_education_waste]
)
# no edges between these branches => concurrent

# Construct the main sequence:
# Site Analysis --> Bed Setup --> parallel_branches --> Cycle Review --> Schedule Update
main_seq = StrictPartialOrder(
    nodes=[Site_Analysis, Bed_Setup, parallel_branches, Cycle_Review, Schedule_Update]
)
main_seq.order.add_edge(Site_Analysis, Bed_Setup)
main_seq.order.add_edge(Bed_Setup, parallel_branches)
main_seq.order.add_edge(parallel_branches, Cycle_Review)
main_seq.order.add_edge(Cycle_Review, Schedule_Update)

root = main_seq