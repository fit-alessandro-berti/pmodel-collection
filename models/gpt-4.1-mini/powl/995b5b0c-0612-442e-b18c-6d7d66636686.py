# Generated from: 995b5b0c-0612-442e-b18c-6d7d66636686.json
# Description: This process outlines the launch of a vertical farming operation within an urban environment, integrating agricultural technology, sustainable energy use, and community engagement. It involves site assessment, modular setup, hydroponic nutrient calibration, AI-driven growth monitoring, waste recycling, and local market integration. The approach balances technological innovation with ecological impact, ensuring efficient resource use and social acceptance. Key steps include sensor installation for microclimate control, automated seeding, pest management without pesticides, data analytics for yield prediction, and partnership formation with local businesses and residents to promote fresh produce accessibility and educational outreach.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Assess = Transition(label='Site Assess')
Tech_Design = Transition(label='Tech Design')
Modular_Build = Transition(label='Modular Build')
Install_Sensors = Transition(label='Install Sensors')
Calibrate_Nutrients = Transition(label='Calibrate Nutrients')
Seed_Automation = Transition(label='Seed Automation')
Climate_Control = Transition(label='Climate Control')
Pest_Monitor = Transition(label='Pest Monitor')
Waste_Cycle = Transition(label='Waste Cycle')
Data_Analyze = Transition(label='Data Analyze')
Yield_Predict = Transition(label='Yield Predict')
Market_Link = Transition(label='Market Link')
Community_Meet = Transition(label='Community Meet')
Energy_Optimize = Transition(label='Energy Optimize')
Report_Results = Transition(label='Report Results')

# Structure reasoning:
# The process flows roughly as:
# 1. Site Assess
# 2. Tech Design
# 3. Modular Build
# 4. Install Sensors
# 5. Calibrate Nutrients
# 6. Seed Automation
# Then parallel activities reflecting continuous monitoring and management:
#   - Climate Control
#   - Pest Monitor
# These two run concurrently (partial order with no edges between them).
# After that:
# 7. Waste Cycle
# 8. Data Analyze --> Yield Predict
# Finally, community engagement and closing steps:
# Market Link and Community Meet run concurrently after Data Analyze/Yield Predict
# Energy Optimize and Report Results run sequentially at the end after Market/Community are done.

# Build partial order for steps 1 to 6 sequentially
step1to6_nodes = [Site_Assess, Tech_Design, Modular_Build, Install_Sensors, Calibrate_Nutrients, Seed_Automation]
step1to6 = StrictPartialOrder(nodes=step1to6_nodes)
for i in range(len(step1to6_nodes)-1):
    step1to6.order.add_edge(step1to6_nodes[i], step1to6_nodes[i+1])

# Concurrent activities: Climate Control and Pest Monitor after Seed Automation
# These are concurrent, so no ordering edges between them, but both depend on Seed Automation
concurrent_monitor = StrictPartialOrder(nodes=[Climate_Control, Pest_Monitor])
# We will embed this partial order and link Seed_Automation to both concurrently running activities.

# Waste Cycle after both Climate Control and Pest Monitor
waste_and_data = StrictPartialOrder(nodes=[Waste_Cycle, Data_Analyze, Yield_Predict])
# Waste Cycle -> Data Analyze -> Yield Predict
waste_and_data.order.add_edge(Waste_Cycle, Data_Analyze)
waste_and_data.order.add_edge(Data_Analyze, Yield_Predict)

# Market Link and Community Meet run concurrently after Yield Predict
community_market = StrictPartialOrder(nodes=[Market_Link, Community_Meet])

# Energy Optimize -> Report Results sequentially after community engagement
final_steps = StrictPartialOrder(nodes=[Energy_Optimize, Report_Results])
final_steps.order.add_edge(Energy_Optimize, Report_Results)

# Build overall partial order and combine partial orders according to dependencies:

# Start from step1to6
nodes_overall = [step1to6, concurrent_monitor, waste_and_data, community_market, final_steps]
root = StrictPartialOrder(nodes=nodes_overall)

# Add edges to define dependencies among these partial orders:
# Seed Automation -> Climate Control and Pest Monitor 
root.order.add_edge(step1to6, concurrent_monitor)

# Climate Control and Pest Monitor -> Waste Cycle
# Because concurrent_monitor has no edges between its two nodes, both must precede Waste Cycle
# We add edges from concurrent_monitor to waste_and_data
root.order.add_edge(concurrent_monitor, waste_and_data)

# Yield Predict is inside waste_and_data; community_market depends on Yield Predict
# So we add edge from waste_and_data to community_market
root.order.add_edge(waste_and_data, community_market)

# community_market -> final_steps
root.order.add_edge(community_market, final_steps)