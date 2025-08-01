# Generated from: 0f4dbd3f-265d-4e3d-b98d-09f1239bd8e5.json
# Description: This process outlines the intricate steps involved in establishing an urban beekeeping operation within a densely populated city environment. It involves securing legal permits, site assessment for optimal hive placement considering microclimate and pollution levels, sourcing sustainable and disease-resistant bee colonies, designing modular hive systems adaptable to rooftop and balcony spaces, implementing integrated pest management tailored for urban pests, monitoring hive health through IoT sensors, coordinating community awareness programs to educate residents on bee safety, harvesting honey while ensuring minimal disruption to the colony, processing and packaging honey with urban branding, and maintaining continuous compliance with environmental and health regulations to promote urban biodiversity and sustainable practices.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
permit       = Transition(label='Permit Check')
survey       = Transition(label='Site Survey')
design       = Transition(label='Hive Design')
colony       = Transition(label='Colony Source')
install      = Transition(label='Hive Install')
sensor_setup = Transition(label='Sensor Setup')
health_mon   = Transition(label='Health Monitor')
data_an      = Transition(label='Data Analyze')
pest_ctrl    = Transition(label='Pest Control')
community    = Transition(label='Community Meet')
safety_tr    = Transition(label='Safety Training')
harvest      = Transition(label='Honey Harvest')
process_h    = Transition(label='Honey Process')
brand        = Transition(label='Brand Design')
waste        = Transition(label='Waste Manage')
audit        = Transition(label='Regulation Audit')

# Build the monitoring loop: after Health Monitor, repeat Data Analyze -> Pest Control
loop_body = StrictPartialOrder(nodes=[data_an, pest_ctrl])
loop_body.order.add_edge(data_an, pest_ctrl)
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[health_mon, loop_body])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    permit, survey, design, colony, install,
    sensor_setup,
    monitoring_loop,
    community, safety_tr,
    harvest, process_h, brand, waste, audit
])

# Sequential startup: Permit -> Survey -> Design -> Colony sourcing -> Install -> Sensor setup
root.order.add_edge(permit, survey)
root.order.add_edge(survey, design)
root.order.add_edge(design, colony)
root.order.add_edge(colony, install)
root.order.add_edge(install, sensor_setup)

# After sensor setup two threads in parallel:
#   1) enter the monitoring loop
#   2) host community awareness + safety training
root.order.add_edge(sensor_setup, monitoring_loop)
root.order.add_edge(sensor_setup, community)

# Community awareness followed by safety training
root.order.add_edge(community, safety_tr)

# Both the loop (on exit) and the completion of training must precede the honey harvest
root.order.add_edge(monitoring_loop, harvest)
root.order.add_edge(safety_tr, harvest)

# Final steps: Harvest -> Process -> Brand -> Waste management -> Audit
root.order.add_edge(harvest, process_h)
root.order.add_edge(process_h, brand)
root.order.add_edge(brand, waste)
root.order.add_edge(waste, audit)