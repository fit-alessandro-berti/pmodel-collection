# Generated from: 910ba68f-7da5-4eb1-b460-cb418d7ba47d.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a repurposed building. It requires coordination across multiple disciplines including structural assessment, environmental control integration, hydroponic system design, and supply chain logistics. The process begins with site selection and feasibility studies, followed by modular infrastructure installation, nutrient solution calibration, and automated monitoring setup. Concurrently, a multi-tier crop scheduling system is developed to optimize yield cycles. The process also incorporates community engagement initiatives and regulatory compliance checks to ensure sustainability and social acceptance. Continuous data analysis and system refinement are conducted post-launch to maximize efficiency and profitability in a confined urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition, OperatorPOWL
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey        = Transition(label='Site Survey')
feasibility_check  = Transition(label='Feasibility Check')
structural_audit   = Transition(label='Structural Audit')
design_layout      = Transition(label='Design Layout')
regulatory_review  = Transition(label='Regulatory Review')
community_meet     = Transition(label='Community Meet')
supply_chain       = Transition(label='Supply Chain')
system_install     = Transition(label='System Install')
hydroponics_setup  = Transition(label='Hydroponics Setup')
nutrient_mix       = Transition(label='Nutrient Mix')
climate_control    = Transition(label='Climate Control')
lighting_config    = Transition(label='Lighting Config')
sensor_deploy      = Transition(label='Sensor Deploy')
automation_link    = Transition(label='Automation Link')
crop_planning      = Transition(label='Crop Planning')
data_analysis      = Transition(label='Data Analysis')
system_adjust      = Transition(label='System Adjust')

# Loop for continuous data analysis and system refinement
post_launch_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_analysis, system_adjust]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, feasibility_check, structural_audit, design_layout,
    regulatory_review, community_meet, supply_chain,
    system_install, hydroponics_setup, nutrient_mix,
    climate_control, lighting_config, sensor_deploy,
    automation_link, crop_planning, post_launch_loop
])

# Sequence: Site Survey -> Feasibility Check -> Structural Audit -> Design Layout
root.order.add_edge(site_survey, feasibility_check)
root.order.add_edge(feasibility_check, structural_audit)
root.order.add_edge(structural_audit, design_layout)

# Regulatory and community checks after feasibility
root.order.add_edge(feasibility_check, regulatory_review)
root.order.add_edge(feasibility_check, community_meet)

# Supply chain kicks in after both regulatory and community
root.order.add_edge(regulatory_review, supply_chain)
root.order.add_edge(community_meet, supply_chain)

# System installation depends on design and supply chain
root.order.add_edge(design_layout, system_install)
root.order.add_edge(supply_chain, system_install)

# Hydroponics setup as part of installation
root.order.add_edge(system_install, hydroponics_setup)
root.order.add_edge(hydroponics_setup, nutrient_mix)
root.order.add_edge(hydroponics_setup, climate_control)
root.order.add_edge(hydroponics_setup, lighting_config)

# Automated monitoring setup
root.order.add_edge(system_install, sensor_deploy)
root.order.add_edge(sensor_deploy, automation_link)

# Crop planning can run in parallel after design
root.order.add_edge(design_layout, crop_planning)

# Post-launch loop depends on all setup and planning
root.order.add_edge(automation_link, post_launch_loop)
root.order.add_edge(crop_planning, post_launch_loop)
root.order.add_edge(nutrient_mix, post_launch_loop)
root.order.add_edge(climate_control, post_launch_loop)
root.order.add_edge(lighting_config, post_launch_loop)