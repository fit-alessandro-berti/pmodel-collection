# Generated from: 011f8b89-babc-48e1-9fda-ae156710e002.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming facility focused on sustainable food production within a limited city space. It includes site analysis, modular system design, environmental control calibration, nutrient cycling optimization, crop selection based on microclimate data, integration of IoT sensors for real-time monitoring, automation of irrigation and lighting, pest bio-control implementation, data-driven yield forecasting, staff training on hydroponic techniques, community engagement for local sourcing, regulatory compliance checks, energy consumption auditing, waste recycling protocols, and continuous process improvement through AI analytics to maximize output and minimize environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
System_Design = Transition(label='System Design')
Env_Control = Transition(label='Env Control')
Nutrient_Mix = Transition(label='Nutrient Mix')
Crop_Select = Transition(label='Crop Select')
Sensor_Setup = Transition(label='Sensor Setup')
Irrigation_Auto = Transition(label='Irrigation Auto')
Lighting_Adjust = Transition(label='Lighting Adjust')
Pest_Control = Transition(label='Pest Control')
Yield_Forecast = Transition(label='Yield Forecast')
Staff_Training = Transition(label='Staff Training')
Community_Meet = Transition(label='Community Meet')
Compliance_Check = Transition(label='Compliance Check')
Energy_Audit = Transition(label='Energy Audit')
Waste_Recycle = Transition(label='Waste Recycle')
Process_Review = Transition(label='Process Review')

# The process involves some logical partial order and some concurrency.
# Let's outline the process by dependency groups:

# Group 1: Initial design and analysis (Site Survey -> System Design -> Env Control, Nutrient Mix)
po1 = StrictPartialOrder(nodes=[Site_Survey, System_Design, Env_Control, Nutrient_Mix])
po1.order.add_edge(Site_Survey, System_Design)
po1.order.add_edge(System_Design, Env_Control)
po1.order.add_edge(System_Design, Nutrient_Mix)
# Env_Control and Nutrient_Mix concurrent after System Design, no edges between them.

# Group 2: Crop selection and setting up sensors, automation (Crop Select -> Sensor Setup -> (Irrigation Auto and Lighting Adjust concurrent))
po2 = StrictPartialOrder(nodes=[Crop_Select, Sensor_Setup, Irrigation_Auto, Lighting_Adjust])
po2.order.add_edge(Crop_Select, Sensor_Setup)
po2.order.add_edge(Sensor_Setup, Irrigation_Auto)
po2.order.add_edge(Sensor_Setup, Lighting_Adjust)
# Irrigation_Auto and Lighting_Adjust concurrent (no edge between them)

# Group 3: Pest Control and Yield Forecast sequential
po3 = StrictPartialOrder(nodes=[Pest_Control, Yield_Forecast])
po3.order.add_edge(Pest_Control, Yield_Forecast)

# Group 4: Staff Training and Community Meeting concurrent
po4 = StrictPartialOrder(nodes=[Staff_Training, Community_Meet])
# no order edges, fully concurrent

# Group 5: Compliance Check -> Energy Audit -> Waste Recycle sequential
po5 = StrictPartialOrder(nodes=[Compliance_Check, Energy_Audit, Waste_Recycle])
po5.order.add_edge(Compliance_Check, Energy_Audit)
po5.order.add_edge(Energy_Audit, Waste_Recycle)

# Group 6: Process Review loops with Yield Forecast (continuous improvement through AI analytics)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Yield_Forecast, Process_Review])
# Meaning: execute Yield Forecast then choose to exit or execute Process Review then Yield Forecast again

# Now combine the main branches in a partial order reflecting dependencies:
# The general sequencing:
# po1 happens first,
# then po2 and po3 can start after po1 (perhaps after Env Control and Nutrient Mix)
# Join po4, po5 and the loop after those

# To keep reasonable ordering, we connect:

# po2 and po3 after po1
# po4 and po5 after po2 and po3
# loop after po3 and po5 (Yield Forecast is in po3, loop starts from Yield Forecast)

# For cleaner structure, we create a top-level POWL with all nodes: po1, po2, po3, po4, po5, loop

root = StrictPartialOrder(nodes=[po1, po2, po3, po4, po5, loop])

# Add edges reflecting ordering:

# po1 --> po2 and po3
root.order.add_edge(po1, po2)
root.order.add_edge(po1, po3)

# po2 and po3 --> po4 and po5
root.order.add_edge(po2, po4)
root.order.add_edge(po3, po4)
root.order.add_edge(po2, po5)
root.order.add_edge(po3, po5)

# po3 and po5 --> loop
root.order.add_edge(po3, loop)
root.order.add_edge(po5, loop)