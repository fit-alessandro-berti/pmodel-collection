# Generated from: c884c0ad-4b6c-478e-8553-2c8264c78c4d.json
# Description: This process manages the end-to-end supply chain for an urban vertical farming enterprise specializing in locally grown produce using hydroponic systems. It begins with seed sourcing from specialized suppliers and continues through germination monitoring, nutrient solution preparation, automated planting, and environmental condition adjustment. The process includes continuous crop health scanning with IoT sensors, integrated pest management without pesticides, and dynamic growth rate analysis to optimize yield. Harvesting is automated with robotic arms, followed by sorting and quality verification based on size and freshness. Packaging uses biodegradable materials and is tracked via blockchain for transparency. The distribution phase coordinates with last-mile delivery partners using AI route optimization to ensure freshness upon arrival. Customer feedback is collected digitally to improve future crop cycles, and waste is minimized through composting and recycling programs integrated into the system. Data analytics drive predictive maintenance of equipment and forecast demand to adjust planting schedules dynamically, ensuring sustainability and profitability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Seed_Sourcing = Transition(label='Seed Sourcing')
Germination_Check = Transition(label='Germination Check')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automated_Planting = Transition(label='Automated Planting')
Climate_Control = Transition(label='Climate Control')
Crop_Scanning = Transition(label='Crop Scanning')
Pest_Monitoring = Transition(label='Pest Monitoring')
Growth_Analysis = Transition(label='Growth Analysis')
Robotic_Harvest = Transition(label='Robotic Harvest')
Quality_Sort = Transition(label='Quality Sort')
Eco_Packaging = Transition(label='Eco Packaging')
Blockchain_Track = Transition(label='Blockchain Track')
Route_Planning = Transition(label='Route Planning')
Feedback_Collect = Transition(label='Feedback Collect')
Waste_Recycling = Transition(label='Waste Recycling')
Data_Analytics = Transition(label='Data Analytics')
Demand_Forecast = Transition(label='Demand Forecast')
Maintenance_Alert = Transition(label='Maintenance Alert')

# Loop for continual crop health scanning and integrated pest management:
# Loop (Crop Scanning, Pest Monitoring)

crop_pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[Crop_Scanning, Pest_Monitoring])

# Loop for data-driven adjustment: dynamic growth analysis driving adjustments 
# Loop (Growth Analysis, Data Analytics)
growth_data_loop = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Analysis, Data_Analytics])

# Loop for forecasting and maintenance loop: forecast demand then maintenance alert        
forecast_maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[Demand_Forecast, Maintenance_Alert])

# Partial order for initial farming setup sequence:
init_setup = StrictPartialOrder(nodes=[
    Seed_Sourcing, Germination_Check, Nutrient_Mix, Automated_Planting, Climate_Control])

init_setup.order.add_edge(Seed_Sourcing, Germination_Check)
init_setup.order.add_edge(Germination_Check, Nutrient_Mix)
init_setup.order.add_edge(Nutrient_Mix, Automated_Planting)
init_setup.order.add_edge(Automated_Planting, Climate_Control)

# Partial order for harvesting and packaging sequence:
harvest_packaging = StrictPartialOrder(nodes=[
    Robotic_Harvest, Quality_Sort, Eco_Packaging, Blockchain_Track])

harvest_packaging.order.add_edge(Robotic_Harvest, Quality_Sort)
harvest_packaging.order.add_edge(Quality_Sort, Eco_Packaging)
harvest_packaging.order.add_edge(Eco_Packaging, Blockchain_Track)

# Partial order for distribution and feedback:
distribution_feedback = StrictPartialOrder(nodes=[
    Route_Planning, Feedback_Collect, Waste_Recycling])

distribution_feedback.order.add_edge(Route_Planning, Feedback_Collect)
distribution_feedback.order.add_edge(Feedback_Collect, Waste_Recycling)

# Composite partial order with all main parts:
root = StrictPartialOrder(nodes=[
    init_setup, 
    crop_pest_loop, 
    growth_data_loop, 
    harvest_packaging, 
    distribution_feedback,
    forecast_maintenance_loop
])

# Define relations (edges/dependencies) between main parts:
root.order.add_edge(init_setup, crop_pest_loop)       # After initial setup, start crop scanning/pest monitoring loop
root.order.add_edge(crop_pest_loop, growth_data_loop) # Growth analysis depends on crop scanning/pest monitoring
root.order.add_edge(growth_data_loop, harvest_packaging) # Harvesting after growth analysis
root.order.add_edge(harvest_packaging, distribution_feedback) # Distribution and feedback after packaging
root.order.add_edge(distribution_feedback, forecast_maintenance_loop) # Maintenance and forecasting after distribution cycle