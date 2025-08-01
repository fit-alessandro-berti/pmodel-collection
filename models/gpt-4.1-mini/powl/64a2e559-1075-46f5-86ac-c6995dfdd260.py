# Generated from: 64a2e559-1075-46f5-86ac-c6995dfdd260.json
# Description: This process outlines the complex operational cycle of an urban vertical farm specializing in multi-crop production within a controlled environment. It involves initial seed sourcing and genetic selection, followed by nutrient solution optimization and automated planting. Continuous monitoring of microclimate variables and pest detection uses IoT sensors and AI-driven analytics. Crop growth is managed through adaptive lighting and irrigation schedules, integrating real-time data feedback. Harvesting is precisely timed using maturity indicators, and post-harvest handling includes automated sorting, quality inspection, and packaging. Waste biomass is recycled onsite through bio-digestion, generating energy and fertilizers. The process concludes with distribution logistics optimized for urban delivery routes, incorporating demand forecasting and sustainability metrics to minimize carbon footprint and maximize yield efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
Seed_Selection = Transition(label='Seed Selection')
Genetic_Testing = Transition(label='Genetic Testing')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automated_Plant = Transition(label='Automated Plant')
Microclimate_Scan = Transition(label='Microclimate Scan')
Pest_Detect = Transition(label='Pest Detect')
Light_Control = Transition(label='Light Control')
Irrigation_Set = Transition(label='Irrigation Set')
Growth_Monitor = Transition(label='Growth Monitor')
Maturity_Check = Transition(label='Maturity Check')
Automated_Harvest = Transition(label='Automated Harvest')
Quality_Inspect = Transition(label='Quality Inspect')
Sort_Packaging = Transition(label='Sort Packaging')
Waste_Recycling = Transition(label='Waste Recycling')
Energy_Recovery = Transition(label='Energy Recovery')
Delivery_Plan = Transition(label='Delivery Plan')
Demand_Forecast = Transition(label='Demand Forecast')

# Initial seed sourcing and genetic selection (strict sequence)
seed_processing = StrictPartialOrder(nodes=[Seed_Selection, Genetic_Testing])
seed_processing.order.add_edge(Seed_Selection, Genetic_Testing)

# Nutrient solution optimization and automated planting (strict sequence)
planting = StrictPartialOrder(nodes=[Nutrient_Mix, Automated_Plant])
planting.order.add_edge(Nutrient_Mix, Automated_Plant)

# Monitoring: microclimate scan and pest detection (concurrent)
monitoring = StrictPartialOrder(nodes=[Microclimate_Scan, Pest_Detect])
# no edges means concurrent

# Crop growth management: adaptive lighting and irrigation set run concurrently before growth monitor
lighting_irrigation = StrictPartialOrder(nodes=[Light_Control, Irrigation_Set])
# concurrent: no order edges

growth_management = StrictPartialOrder(nodes=[lighting_irrigation, Growth_Monitor])
growth_management.order.add_edge(lighting_irrigation, Growth_Monitor)  # effectively ordering combined nodes

# However, `lighting_irrigation` is itself a StrictPartialOrder; to integrate properly,
# we will flatten: nodes = Light_Control, Irrigation_Set, Growth_Monitor, with Light_Control and Irrigation_Set concurrent and both before Growth_Monitor

growth_management = StrictPartialOrder(nodes=[Light_Control, Irrigation_Set, Growth_Monitor])
growth_management.order.add_edge(Light_Control, Growth_Monitor)
growth_management.order.add_edge(Irrigation_Set, Growth_Monitor)

# Post-harvest handling: automated harvest then choice of quality inspect and sort packaging in parallel, both before next steps
# The description says sorting, quality inspection and packaging. We'll model Quality Inspect and Sort Packaging as concurrent, both after automated harvest.

post_harvest = StrictPartialOrder(nodes=[Automated_Harvest, Quality_Inspect, Sort_Packaging])
post_harvest.order.add_edge(Automated_Harvest, Quality_Inspect)
post_harvest.order.add_edge(Automated_Harvest, Sort_Packaging)
# Quality Inspect and Sort Packaging concurrent

# Waste biomass recycling with bio-digestion energy and fertilizer generation modeled as sequence
waste_energy = StrictPartialOrder(nodes=[Waste_Recycling, Energy_Recovery])
waste_energy.order.add_edge(Waste_Recycling, Energy_Recovery)

# Distribution planning with demand forecasting (demand forecasting before delivery plan)
distribution = StrictPartialOrder(nodes=[Demand_Forecast, Delivery_Plan])
distribution.order.add_edge(Demand_Forecast, Delivery_Plan)

# Build the main process partial order connecting above parts strictly in sequence mimicking the process description:

# Step 1: seed_processing --> planting
# Step 2: planting --> monitoring
# Step 3: monitoring --> growth_management
# Step 4: growth_management --> Maturity_Check (single node)
# Step 5: Maturity_Check --> post_harvest
# Step 6: post_harvest --> waste_energy
# Step 7: waste_energy --> distribution

main_nodes = [
    seed_processing,
    planting,
    monitoring,
    growth_management,
    Maturity_Check,
    post_harvest,
    waste_energy,
    distribution
]

root = StrictPartialOrder(nodes=main_nodes)

root.order.add_edge(seed_processing, planting)
root.order.add_edge(planting, monitoring)
root.order.add_edge(monitoring, growth_management)
root.order.add_edge(growth_management, Maturity_Check)
root.order.add_edge(Maturity_Check, post_harvest)
root.order.add_edge(post_harvest, waste_energy)
root.order.add_edge(waste_energy, distribution)