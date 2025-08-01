# Generated from: bafb7c0a-eae3-49a7-a210-235d7d22f2f1.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farm within a densely populated city environment. It starts with site analysis and zoning compliance, followed by microclimate assessment and modular system design. Procurement of specialized hydroponic equipment and nutrient solutions is critical, alongside integration of IoT sensors for real-time monitoring. Installation requires coordination with utility providers for optimized energy and water usage. Post-installation, seed selection and planting are carefully managed to match urban growth cycles. Continuous environmental adjustments, pest management using biological controls, and automated harvesting complete the cycle. Finally, produce packaging and distribution focus on minimizing carbon footprint while ensuring freshness, targeting local markets and restaurants. This process demands interdisciplinary collaboration between agronomists, engineers, urban planners, and supply chain experts to balance sustainability, efficiency, and profitability in a confined urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_analysis = Transition(label='Site Analysis')
zoning_check = Transition(label='Zoning Check')
microclimate_study = Transition(label='Microclimate Study')
system_design = Transition(label='System Design')
equipment_order = Transition(label='Equipment Order')
nutrient_prep = Transition(label='Nutrient Prep')
sensor_setup = Transition(label='Sensor Setup')
utility_coordination = Transition(label='Utility Coordination')
installation_phase = Transition(label='Installation Phase')
seed_selection = Transition(label='Seed Selection')
planting_stage = Transition(label='Planting Stage')
environmental_tune = Transition(label='Environmental Tune')
pest_control = Transition(label='Pest Control')
automated_harvest = Transition(label='Automated Harvest')
packaging_ops = Transition(label='Packaging Ops')
distribution_plan = Transition(label='Distribution Plan')

# Phase 1: Site analysis and zoning
phase1 = StrictPartialOrder(nodes=[site_analysis, zoning_check])
phase1.order.add_edge(site_analysis, zoning_check)

# Phase 2: Microclimate study and system design (concurrent after zoning)
phase2 = StrictPartialOrder(nodes=[microclimate_study, system_design])
# no order between microclimate_study and system_design, concurrent

# Phase 3: Procurement phase - equipment order, nutrient prep, sensor setup - concurrent
procurement = StrictPartialOrder(nodes=[equipment_order, nutrient_prep, sensor_setup])

# Phase 4: Utility coordination before installation
utility_install = StrictPartialOrder(nodes=[utility_coordination, installation_phase])
utility_install.order.add_edge(utility_coordination, installation_phase)

# Phase 5: Planting preparation - seed selection and planting stage sequential
planting_prep = StrictPartialOrder(nodes=[seed_selection, planting_stage])
planting_prep.order.add_edge(seed_selection, planting_stage)

# Phase 6: Continuous cycle of environmental tuning, pest control, automated harvest
# Modeled as a loop: do environmental tune, then choose to exit or do (pest control then automated harvest then environmental tune)
# For LOOP, children=[do_activity, do_loop_body]:
# do_activity: environmental_tune
# do_loop_body: pest_control -> automated_harvest (partial order sequential)
loop_body = StrictPartialOrder(nodes=[pest_control, automated_harvest])
loop_body.order.add_edge(pest_control, automated_harvest)
loop = OperatorPOWL(operator=Operator.LOOP, children=[environmental_tune, loop_body])

# Phase 7: Packaging and distribution sequential
pack_distrib = StrictPartialOrder(nodes=[packaging_ops, distribution_plan])
pack_distrib.order.add_edge(packaging_ops, distribution_plan)

# Combine phases:
# Full partial order nodes:
nodes = [
    phase1,   # site_analysis -> zoning_check
    phase2,   # microclimate_study, system_design concurrent
    procurement, # equipment_order, nutrient_prep, sensor_setup concurrent
    utility_install, # utility_coordination -> installation_phase
    planting_prep, # seed_selection -> planting_stage
    loop, # environmental tuning loop
    pack_distrib # packaging -> distribution
]

root = StrictPartialOrder(nodes=nodes)

# Define order between phases
# phase1 -> phase2 concurrent nodes
root.order.add_edge(phase1, phase2)

# phase2 -> procurement
root.order.add_edge(phase2, procurement)

# procurement -> utility_install
root.order.add_edge(procurement, utility_install)

# utility_install -> installation_phase is internal to utility_install (already done)
# utility_install -> planting_prep
root.order.add_edge(utility_install, planting_prep)

# planting_prep -> loop (environmental tuning cycle)
root.order.add_edge(planting_prep, loop)

# loop -> packaging and distribution
root.order.add_edge(loop, pack_distrib)