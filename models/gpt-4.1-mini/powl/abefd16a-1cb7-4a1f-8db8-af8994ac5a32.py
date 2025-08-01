# Generated from: abefd16a-1cb7-4a1f-8db8-af8994ac5a32.json
# Description: This process outlines the end-to-end establishment of an urban vertical farm within a repurposed warehouse. It involves site analysis, environmental control system installation, hydroponic setup, crop selection tailored for vertical growth, nutrient solution formulation, automated lighting programming, integrated pest management deployment, staff training on unique farming techniques, continuous monitoring via IoT sensors, data analysis for yield optimization, packaging design for urban consumers, logistics planning for fresh delivery, compliance checks with agricultural regulations, marketing strategy targeting local markets, and ongoing sustainability assessments to minimize energy and water consumption while maximizing crop output in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Floor_Mapping = Transition(label='Floor Mapping')
System_Install = Transition(label='System Install')
Hydro_Setup = Transition(label='Hydro Setup')
Crop_Select = Transition(label='Crop Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Light_Program = Transition(label='Light Program')
Pest_Control = Transition(label='Pest Control')
Staff_Training = Transition(label='Staff Training')
Sensor_Setup = Transition(label='Sensor Setup')
Data_Review = Transition(label='Data Review')
Package_Design = Transition(label='Package Design')
Delivery_Plan = Transition(label='Delivery Plan')
Compliance_Check = Transition(label='Compliance Check')
Market_Launch = Transition(label='Market Launch')
Sustainability = Transition(label='Sustainability')

# Create PO with all nodes
root = StrictPartialOrder(nodes=[
    Site_Analysis, Floor_Mapping, System_Install, Hydro_Setup, Crop_Select,
    Nutrient_Mix, Light_Program, Pest_Control, Staff_Training, Sensor_Setup,
    Data_Review, Package_Design, Delivery_Plan, Compliance_Check, Market_Launch,
    Sustainability
])

# Add edges for the natural sequential dependencies inferred from the description:
#
# Site Analysis --> Floor Mapping --> System Install --> Hydro Setup
root.order.add_edge(Site_Analysis, Floor_Mapping)
root.order.add_edge(Floor_Mapping, System_Install)
root.order.add_edge(System_Install, Hydro_Setup)

# Hydro Setup --> Crop Select --> Nutrient Mix --> Light Program --> Pest Control
root.order.add_edge(Hydro_Setup, Crop_Select)
root.order.add_edge(Crop_Select, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Light_Program)
root.order.add_edge(Light_Program, Pest_Control)

# Pest Control --> Staff Training
root.order.add_edge(Pest_Control, Staff_Training)

# Staff Training --> Sensor Setup --> Data Review
root.order.add_edge(Staff_Training, Sensor_Setup)
root.order.add_edge(Sensor_Setup, Data_Review)

# Data Review --> Package Design --> Delivery Plan
root.order.add_edge(Data_Review, Package_Design)
root.order.add_edge(Package_Design, Delivery_Plan)

# Delivery Plan --> Compliance Check --> Market Launch --> Sustainability
root.order.add_edge(Delivery_Plan, Compliance_Check)
root.order.add_edge(Compliance_Check, Market_Launch)
root.order.add_edge(Market_Launch, Sustainability)