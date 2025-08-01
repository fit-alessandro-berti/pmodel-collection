# Generated from: 95850c46-42b9-474f-b989-4ca730949347.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farm integrating IoT sensors, AI-driven climate control, and hydroponic systems. It involves seed selection based on market trends, nutrient solution calibration, automated seeding, and environmental monitoring. Continuous data analysis optimizes growth conditions while predictive maintenance ensures equipment uptime. Post-harvest, produce undergoes quality sorting, packaging with sustainable materials, and direct-to-consumer distribution via an app platform. The process also includes waste recycling into bio-fertilizers and real-time feedback integration from customers to adjust crop varieties and schedules, maximizing yield in limited urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automated_Seeding = Transition(label='Automated Seeding')
Sensor_Calibration = Transition(label='Sensor Calibration')
Climate_Control = Transition(label='Climate Control')
Growth_Monitoring = Transition(label='Growth Monitoring')
Data_Analysis = Transition(label='Data Analysis')
Predictive_Repair = Transition(label='Predictive Repair')
Harvest_Sorting = Transition(label='Harvest Sorting')
Eco_Packaging = Transition(label='Eco Packaging')
Order_Dispatch = Transition(label='Order Dispatch')
Customer_Feedback = Transition(label='Customer Feedback')
Waste_Recycling = Transition(label='Waste Recycling')
Crop_Adjustment = Transition(label='Crop Adjustment')
Yield_Reporting = Transition(label='Yield Reporting')

# Model continuous data analysis + predictive repair as a loop: 
# perform (Data Analysis) 
# then choose to exit or do (Predictive Repair) before looping back
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[Data_Analysis, Predictive_Repair])

# Model the post-harvest sequence: Harvest Sorting -> Eco Packaging -> Order Dispatch
post_harvest_PO = StrictPartialOrder(nodes=[Harvest_Sorting, Eco_Packaging, Order_Dispatch])
post_harvest_PO.order.add_edge(Harvest_Sorting, Eco_Packaging)
post_harvest_PO.order.add_edge(Eco_Packaging, Order_Dispatch)

# Model waste recycling and customer feedback leading to crop adjustment, followed by yield reporting
# Waste Recycling and Customer Feedback can be concurrent
feedback_PO = StrictPartialOrder(nodes=[Waste_Recycling, Customer_Feedback, Crop_Adjustment, Yield_Reporting])
# Crop Adjustment depends on both Waste Recycling and Customer Feedback
feedback_PO.order.add_edge(Waste_Recycling, Crop_Adjustment)
feedback_PO.order.add_edge(Customer_Feedback, Crop_Adjustment)
# Yield Reporting follows Crop Adjustment
feedback_PO.order.add_edge(Crop_Adjustment, Yield_Reporting)

# Model initial seed & nutrient + seeding preparation partial order
preparation_PO = StrictPartialOrder(nodes=[Seed_Selection, Nutrient_Mix, Automated_Seeding])
# Seed Selection precedes Automated Seeding
preparation_PO.order.add_edge(Seed_Selection, Automated_Seeding)
# Nutrient Mix precedes Automated Seeding
preparation_PO.order.add_edge(Nutrient_Mix, Automated_Seeding)

# Sensor Calibration and Climate Control are concurrent but must be done before Growth Monitoring
calib_climate_PO = StrictPartialOrder(nodes=[Sensor_Calibration, Climate_Control, Growth_Monitoring])
calib_climate_PO.order.add_edge(Sensor_Calibration, Growth_Monitoring)
calib_climate_PO.order.add_edge(Climate_Control, Growth_Monitoring)

# Combine preparation, calibration/climate control, and growth monitoring/data loop sequentially:
# preparation_PO -> calib_climate_PO -> data_loop
phase1_PO = StrictPartialOrder(nodes=[preparation_PO, calib_climate_PO])
# Dep edges: preparation_PO --> calib_climate_PO
phase1_PO.order.add_edge(preparation_PO, calib_climate_PO)

phase2_PO = StrictPartialOrder(nodes=[phase1_PO, data_loop])
phase2_PO.order.add_edge(phase1_PO, data_loop)

# After data loop ends, continue with harvest etc., then feedback
final_PO = StrictPartialOrder(nodes=[phase2_PO, post_harvest_PO, feedback_PO])
final_PO.order.add_edge(phase2_PO, post_harvest_PO)
final_PO.order.add_edge(post_harvest_PO, feedback_PO)

root = final_PO