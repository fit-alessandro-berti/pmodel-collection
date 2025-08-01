# Generated from: d460587c-54a1-4a67-bbc5-b48e55b72949.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm on a commercial building. It includes initial structural assessments, securing permits, soil and water testing, installation of hydroponic systems, integration of renewable energy sources, crop selection based on microclimate data, stakeholder coordination, ongoing environmental monitoring, and market launch strategies. The process ensures compliance with city regulations, maximizes yield efficiency, and incorporates community engagement initiatives to promote urban agriculture awareness and education. It requires interdisciplinary collaboration among engineers, agronomists, architects, and local authorities to successfully transform unused rooftop spaces into productive green environments that contribute to local food security and urban ecosystem enhancement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey = Transition(label='Site Survey')
load_testing = Transition(label='Load Testing')
permit_filing = Transition(label='Permit Filing')
soil_sampling = Transition(label='Soil Sampling')
water_testing = Transition(label='Water Testing')
system_design = Transition(label='System Design')
material_order = Transition(label='Material Order')
system_install = Transition(label='System Install')
solar_setup = Transition(label='Solar Setup')
crop_planning = Transition(label='Crop Planning')
stakeholder_meet = Transition(label='Stakeholder Meet')
env_audit = Transition(label='Environmental Audit')
growth_monitoring = Transition(label='Growth Monitoring')
pest_control = Transition(label='Pest Control')
market_launch = Transition(label='Market Launch')

# Ongoing environmental monitoring loop: do an audit, then optionally do growth & pest checks, then audit again...
monitoring_repeat = StrictPartialOrder(nodes=[growth_monitoring, pest_control])
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[env_audit, monitoring_repeat])

# Parallel installation of hydroponic system and solar setup
branch_install = StrictPartialOrder(nodes=[material_order, system_install])
branch_install.order.add_edge(material_order, system_install)
parallel_install = StrictPartialOrder(nodes=[branch_install, solar_setup])

# Parallel soil and water testing after permit
testing = StrictPartialOrder(nodes=[soil_sampling, water_testing])

# Assemble the whole process as a partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_testing, permit_filing,
    testing,
    system_design, parallel_install,
    crop_planning, stakeholder_meet,
    monitor_loop,
    market_launch
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, load_testing)
root.order.add_edge(load_testing, permit_filing)

# After permits, do soil/water testing and start system design
root.order.add_edge(permit_filing, testing)
root.order.add_edge(permit_filing, system_design)

# After design, install and solar setup in parallel
root.order.add_edge(system_design, parallel_install)

# Crop planning once testing & installations are done
root.order.add_edge(testing, crop_planning)
root.order.add_edge(parallel_install, crop_planning)

# Stakeholder coordination → monitoring loop → market launch
root.order.add_edge(crop_planning, stakeholder_meet)
root.order.add_edge(stakeholder_meet, monitor_loop)
root.order.add_edge(monitor_loop, market_launch)