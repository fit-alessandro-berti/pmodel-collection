# Generated from: 90958393-a27c-40b8-bce6-dd508c8b1f8a.json
# Description: This process outlines the complex setup of an urban vertical farm designed to optimize space and resource efficiency in densely populated city environments. It involves site analysis, modular design, climate control integration, nutrient cycling, automated seeding, growth monitoring, pest management, and harvest logistics. The process requires coordination between architects, agronomists, engineers, and supply chain experts to ensure sustainable crop production year-round while minimizing water use and energy consumption. Advanced IoT sensors and AI-driven analytics are employed to continuously adapt environmental parameters, maximize yield, and reduce waste, creating a resilient food production system within urban infrastructure.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Design_Layout = Transition(label='Design Layout')
Modular_Build = Transition(label='Modular Build')
Climate_Setup = Transition(label='Climate Setup')
Water_System = Transition(label='Water System')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Automation = Transition(label='Seed Automation')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Lighting_Adjust = Transition(label='Lighting Adjust')
Data_Collection = Transition(label='Data Collection')
Yield_Forecast = Transition(label='Yield Forecast')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Manage = Transition(label='Waste Manage')
Supply_Sync = Transition(label='Supply Sync')
Quality_Check = Transition(label='Quality Check')
Energy_Audit = Transition(label='Energy Audit')

# Overall structure:
# Site Analysis -> Design Layout -> Modular Build
# Modular Build followed by a choice/parallel for Climate Setup and Water System + Nutrient Mix
# Climate Setup and Water System + Nutrient Mix are parallel and need to finish before Seed Automation
# After Seed Automation: Growth Monitor continuously loops with Pest Control and Lighting Adjust (control and adjust growth environment)
# Growth monitoring loop includes Data Collection and Yield Forecast as choices/concurrent inside the monitoring loop
# After exit loop, Harvest Plan -> Waste Manage + Supply Sync (concurrent) -> Quality Check -> Energy Audit

# Build substructures:

# Climate branch partial order: Climate Setup alone
climate_po = StrictPartialOrder(nodes=[Climate_Setup])

# Water & Nutrient setup partial order with Water System preceding Nutrient Mix
water_nutrient_po = StrictPartialOrder(nodes=[Water_System, Nutrient_Mix])
water_nutrient_po.order.add_edge(Water_System, Nutrient_Mix)

# Combine climate_po and water_nutrient_po in parallel (no order edges between them)
setup_parallel = StrictPartialOrder(nodes=[climate_po, water_nutrient_po])

# Seed Automation follows both setup branches
seed_branch = StrictPartialOrder(nodes=[setup_parallel, Seed_Automation])
seed_branch.order.add_edge(setup_parallel, Seed_Automation)

# Growth Monitor loop body: Pest Control and Lighting Adjust can run concurrently after Growth Monitor
# Model Growth Monitor first, then concurrently Pest Control and Lighting Adjust after Growth Monitor
growth_monitor_po = StrictPartialOrder(nodes=[Growth_Monitor, Pest_Control, Lighting_Adjust])

growth_monitor_po.order.add_edge(Growth_Monitor, Pest_Control)
growth_monitor_po.order.add_edge(Growth_Monitor, Lighting_Adjust)

# Inside the loop, after executing the growth_monitor_po, we have a choice:
# either exit loop or continue with Data Collection and Yield Forecast (concurrent)
# Data Collection and Yield Forecast run in parallel (no order edges)
data_yield_po = StrictPartialOrder(nodes=[Data_Collection, Yield_Forecast])

# Loop is: execute growth_monitor_po, then either exit or execute data_yield_po then again growth_monitor_po
# We use OperatorPOWL(Operator.LOOP, [growth_monitor_po, data_yield_po])

growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor_po, data_yield_po])

# After exiting growth monitoring loop:
# Harvest Plan -> Waste Manage and Supply Sync concurrently -> Quality Check -> Energy Audit

# Waste Manage and Supply Sync concurrent
post_harvest_parallel = StrictPartialOrder(nodes=[Waste_Manage, Supply_Sync])

# Harvest Plan precedes the parallel waste and supply sync
post_harvest = StrictPartialOrder(nodes=[Harvest_Plan, post_harvest_parallel])
post_harvest.order.add_edge(Harvest_Plan, post_harvest_parallel)

# Quality Check after parallel nodes
quality_sequence = StrictPartialOrder(nodes=[post_harvest, Quality_Check])
quality_sequence.order.add_edge(post_harvest, Quality_Check)

# Energy Audit after Quality Check
final_sequence = StrictPartialOrder(nodes=[quality_sequence, Energy_Audit])
final_sequence.order.add_edge(quality_sequence, Energy_Audit)

# Now combine all into the main process:
# Site Analysis -> Design Layout -> Modular Build -> seed_branch -> growth_loop -> final_sequence

main_po = StrictPartialOrder(
    nodes=[Site_Analysis, Design_Layout, Modular_Build, seed_branch, growth_loop, final_sequence]
)
main_po.order.add_edge(Site_Analysis, Design_Layout)
main_po.order.add_edge(Design_Layout, Modular_Build)
main_po.order.add_edge(Modular_Build, seed_branch)
main_po.order.add_edge(seed_branch, growth_loop)
main_po.order.add_edge(growth_loop, final_sequence)

root = main_po