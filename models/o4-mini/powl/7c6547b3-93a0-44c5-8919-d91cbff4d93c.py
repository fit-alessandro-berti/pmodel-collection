# Generated from: 7c6547b3-93a0-44c5-8919-d91cbff4d93c.json
# Description: This process outlines the complex steps involved in establishing a vertical farming operation within an urban environment. It includes site selection based on environmental and logistical factors, integration of advanced hydroponic systems, and deployment of automated climate control technologies. Regulatory compliance and community engagement ensure sustainable and socially responsible development. Continuous monitoring and data analytics optimize crop yield and resource efficiency, while supply chain coordination facilitates timely distribution to local markets. The process concludes with staff training and iterative system improvements to adapt to changing urban conditions and consumer demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey       = Transition(label='Site Survey')
regulation_check  = Transition(label='Regulation Check')
design_layout     = Transition(label='Design Layout')
tech_integration  = Transition(label='Tech Integration')
hydroponic_setup  = Transition(label='Hydroponic Setup')
climate_control   = Transition(label='Climate Control')
sensor_install    = Transition(label='Sensor Install')
water_testing     = Transition(label='Water Testing')
energy_audit      = Transition(label='Energy Audit')
supplier_vetting  = Transition(label='Supplier Vetting')
community_meet    = Transition(label='Community Meet')
market_prep       = Transition(label='Market Prep')
logistics_plan    = Transition(label='Logistics Plan')
staff_hiring      = Transition(label='Staff Hiring')
training_session  = Transition(label='Training Session')
crop_planning     = Transition(label='Crop Planning')
yield_monitoring  = Transition(label='Yield Monitoring')
data_analysis     = Transition(label='Data Analysis')
feedback_review   = Transition(label='Feedback Review')
system_upgrade    = Transition(label='System Upgrade')

# Define the continuous improvement loop: monitor -> (upgrade -> monitor)* 
monitoring = StrictPartialOrder(nodes=[yield_monitoring, data_analysis, feedback_review])
monitoring.order.add_edge(yield_monitoring, data_analysis)
monitoring.order.add_edge(data_analysis, feedback_review)

loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring, system_upgrade])

# Assemble the main partial order
root = StrictPartialOrder(nodes=[
    site_survey, regulation_check, design_layout, tech_integration, hydroponic_setup,
    climate_control, sensor_install, water_testing, energy_audit, supplier_vetting,
    community_meet, market_prep, logistics_plan, staff_hiring, training_session,
    crop_planning, loop
])

# Core sequential flow
root.order.add_edge(site_survey, regulation_check)
root.order.add_edge(regulation_check, design_layout)
root.order.add_edge(design_layout, tech_integration)
root.order.add_edge(tech_integration, hydroponic_setup)
root.order.add_edge(hydroponic_setup, climate_control)
root.order.add_edge(climate_control, sensor_install)

# Parallel testing & audit after sensor install
root.order.add_edge(sensor_install, water_testing)
root.order.add_edge(sensor_install, energy_audit)

# Supplier vetting & community engagement in parallel after design
root.order.add_edge(design_layout, supplier_vetting)
root.order.add_edge(design_layout, community_meet)

# Market prep & logistics after supplier & community tasks
root.order.add_edge(supplier_vetting, market_prep)
root.order.add_edge(community_meet, market_prep)
root.order.add_edge(supplier_vetting, logistics_plan)
root.order.add_edge(community_meet, logistics_plan)

# Staffing and training before crop planning
root.order.add_edge(hydroponic_setup, staff_hiring)
root.order.add_edge(staff_hiring, training_session)
root.order.add_edge(training_session, crop_planning)

# Testing, audit, market & logistics inform crop planning
root.order.add_edge(water_testing, crop_planning)
root.order.add_edge(energy_audit, crop_planning)
root.order.add_edge(market_prep, crop_planning)
root.order.add_edge(logistics_plan, crop_planning)

# Enter the continuous improvement loop
root.order.add_edge(crop_planning, loop)