# Generated from: f1df3585-3cd1-4306-8f32-4ae2ed3e100d.json
# Description: This process involves establishing an urban vertical farm by integrating advanced hydroponic systems with IoT-based environmental controls. It begins with site assessment and infrastructure planning, followed by modular rack installation, nutrient solution formulation, and sensor calibration. Concurrently, automated lighting and climate systems are configured to optimize plant growth cycles. Seed selection and germination are closely monitored through data analytics to ensure maximum yield. The process also includes pest management using bio-controls, periodic system maintenance, and real-time crop health monitoring. Finally, harvested produce undergoes quality checks before packaging and distribution, ensuring freshness and sustainability in urban food supply chains.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
SiteAssess = Transition(label='Site Assess')
PlanLayout = Transition(label='Plan Layout')

InstallRacks = Transition(label='Install Racks')
MixNutrients = Transition(label='Mix Nutrients')
CalibrateSensors = Transition(label='Calibrate Sensors')

SetupLighting = Transition(label='Setup Lighting')
ConfigureClimate = Transition(label='Configure Climate')

SelectSeeds = Transition(label='Select Seeds')
MonitorGerminate = Transition(label='Monitor Germinate')

ApplyBioControls = Transition(label='Apply Bio-controls')
MaintainSystems = Transition(label='Maintain Systems')
AnalyzeData = Transition(label='Analyze Data')

HarvestCrops = Transition(label='Harvest Crops')
QualityCheck = Transition(label='Quality Check')
PackageProduce = Transition(label='Package Produce')
DistributeGoods = Transition(label='Distribute Goods')

# Partial order for site assessment and planning
site_plan_po = StrictPartialOrder(nodes=[SiteAssess, PlanLayout])
site_plan_po.order.add_edge(SiteAssess, PlanLayout)

# Partial order for installation and preparation (3 activities in sequence)
install_prep_po = StrictPartialOrder(nodes=[InstallRacks, MixNutrients, CalibrateSensors])
install_prep_po.order.add_edge(InstallRacks, MixNutrients)
install_prep_po.order.add_edge(MixNutrients, CalibrateSensors)

# Partial order for lighting and climate setup - concurrent (no edges)
lighting_climate_po = StrictPartialOrder(nodes=[SetupLighting, ConfigureClimate])

# Partial order for seed selection and germination monitoring
seed_monitor_po = StrictPartialOrder(nodes=[SelectSeeds, MonitorGerminate])
seed_monitor_po.order.add_edge(SelectSeeds, MonitorGerminate)

# Partial order for pest management, maintenance and data analysis - all concurrent
pest_maintain_analyze_po = StrictPartialOrder(nodes=[ApplyBioControls, MaintainSystems, AnalyzeData])

# Partial order for final harvesting and distribution sequence
harvest_dist_po = StrictPartialOrder(
    nodes=[HarvestCrops, QualityCheck, PackageProduce, DistributeGoods])
harvest_dist_po.order.add_edge(HarvestCrops, QualityCheck)
harvest_dist_po.order.add_edge(QualityCheck, PackageProduce)
harvest_dist_po.order.add_edge(PackageProduce, DistributeGoods)

# Now combine modular installation/preparation with lighting/climate concurrent
install_lighting_po = StrictPartialOrder(
    nodes=[install_prep_po, lighting_climate_po])
# installation/prep must precede lighting/climate setup to optimize growth? 
# No explicit order given, but sentence says "Concurrently, automated lighting and climate systems..."
# Since Setup Lighting and Configure Climate are concurrent, they run concurrently with modular installation and preparation
# The text says: "modular rack installation, nutrient solution formulation, and sensor calibration" first
# Then concurrently "lighting and climate" configured
# So: install_prep_po --> lighting_climate_po
install_lighting_po.order.add_edge(install_prep_po, lighting_climate_po)

# Combine seed selection and monitoring with data analytics concurrent
# The description states seed selection and germination are closely monitored through data analytics
# So Analyze Data is semantically connected closely to Decide Seeds and Monitor Germinate
# We already put Analyze Data in the pest_maintain_analyze_po group
# To reflect that Analyze Data relates to seed/monitor, better to merge Analyze Data with seed_monitor_po as concurrency
# Let's split Analyze Data out of pest_maintain_analyze_po and join it here instead:

# Extract Analyze Data from pest_maintain_analyze_po
pest_maintain_po = StrictPartialOrder(nodes=[ApplyBioControls, MaintainSystems])
# no order edges (concurrent)
# Add Analyze Data to seed_monitor_po concurrency
seed_monitor_analyze_po = StrictPartialOrder(
    nodes=[seed_monitor_po, AnalyzeData]
)

# Concurrent means no edges at this level

# Now the process is:
# 1) site_plan_po
# 2) install_prep_po --> lighting_climate_po (install_lighting_po)
# 3) seed_monitor_analyze_po
# 4) pest_maintain_po
# 5) harvest_dist_po

# Synchronize overall order:
# From description:
# Site assess and infrastructure planning (site_plan_po),
# followed by modular rack installation, nutrient solution formulation, and sensor calibration (install_prep_po),
# concurrently lighting and climate (lighting_climate_po)
# Then seed selection and germination monitoring close with data analytics (seed_monitor_analyze_po)
# Also pest management, periodic maintenance (pest_maintain_po) runs during or after? Description says "process also includes"
# We place pest_maintain_po concurrent with seed_monitor_analyze_po since it says "periodic system maintenance" and "pest management" - concurrent and ongoing
# Finally harvested produce etc. (harvest_dist_po)

# So assemble the root StrictPartialOrder with nodes as the above major blocks:

root = StrictPartialOrder(
    nodes=[site_plan_po, install_lighting_po, seed_monitor_analyze_po, pest_maintain_po, harvest_dist_po]
)

# Add order edges based on the sequence:
root.order.add_edge(site_plan_po, install_lighting_po)
root.order.add_edge(install_lighting_po, seed_monitor_analyze_po)
root.order.add_edge(seed_monitor_analyze_po, harvest_dist_po)

# pest_maintain_po is concurrent with seed_monitor_analyze_po and harvest_dist_po, thus no edges to/from it

# Final: root models the entire process
