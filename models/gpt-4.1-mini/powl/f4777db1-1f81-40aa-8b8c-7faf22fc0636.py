# Generated from: f4777db1-1f81-40aa-8b8c-7faf22fc0636.json
# Description: This process outlines the establishment of an urban rooftop farming operation on a commercial building. It includes site analysis, environmental impact assessment, structural integrity checks, soil and hydroponic system design, seed selection, installation of irrigation and lighting systems, implementation of pest control measures, and ongoing monitoring for crop health. The process also incorporates community engagement, compliance with local regulations, waste recycling strategies, and market launch preparations, ensuring a sustainable, productive, and community-supported urban agriculture initiative.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey = Transition(label='Site Survey')
impact_study = Transition(label='Impact Study')
structure_check = Transition(label='Structure Check')
soil_testing = Transition(label='Soil Testing')
system_design = Transition(label='System Design')
seed_selection = Transition(label='Seed Selection')
irrigation_setup = Transition(label='Irrigation Setup')
lighting_install = Transition(label='Lighting Install')
pest_control = Transition(label='Pest Control')
community_meet = Transition(label='Community Meet')
regulation_review = Transition(label='Regulation Review')
waste_plan = Transition(label='Waste Plan')
crop_monitor = Transition(label='Crop Monitor')
harvest_prep = Transition(label='Harvest Prep')
market_launch = Transition(label='Market Launch')

# Initial partial order: Site Survey --> Impact Study --> Structure Check (site analysis phase)
site_analysis = StrictPartialOrder(nodes=[site_survey, impact_study, structure_check])
site_analysis.order.add_edge(site_survey, impact_study)
site_analysis.order.add_edge(impact_study, structure_check)

# Design phase: Soil Testing --> System Design
design_phase = StrictPartialOrder(nodes=[soil_testing, system_design])
design_phase.order.add_edge(soil_testing, system_design)

# Seed and installation phase: Seed Selection --> (Irrigation Setup and Lighting Install in parallel)
install_nodes = [irrigation_setup, lighting_install]
seed_and_install = StrictPartialOrder(nodes=[seed_selection] + install_nodes)
seed_and_install.order.add_edge(seed_selection, irrigation_setup)
seed_and_install.order.add_edge(seed_selection, lighting_install)

# Pest Control after installation
pest_phase = StrictPartialOrder(nodes=[pest_control])
# No internal edges as single node

# Community engagement and compliance in parallel with waste plan
community_compliance = StrictPartialOrder(
    nodes=[community_meet, regulation_review, waste_plan]
)
# No edges, all concurrent

# Monitoring loop: Crop Monitor --> Harvest Prep (loop back to Crop Monitor)
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[crop_monitor, harvest_prep]
)

# Market launch after monitoring is finished
launch_phase = StrictPartialOrder(nodes=[market_launch])

# Compose all phases in partial order with dependencies:
# site_analysis --> design_phase --> seed_and_install --> pest_phase
# pest_phase --> community_compliance --> monitor_loop --> launch_phase

nodes_all = [
    site_analysis,
    design_phase,
    seed_and_install,
    pest_phase,
    community_compliance,
    monitor_loop,
    launch_phase
]

root = StrictPartialOrder(nodes=nodes_all)
# Define edges to reflect order:

root.order.add_edge(site_analysis, design_phase)
root.order.add_edge(design_phase, seed_and_install)
root.order.add_edge(seed_and_install, pest_phase)
root.order.add_edge(pest_phase, community_compliance)
root.order.add_edge(community_compliance, monitor_loop)
root.order.add_edge(monitor_loop, launch_phase)