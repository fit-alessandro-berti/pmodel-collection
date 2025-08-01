# Generated from: 34a3dd64-e162-4b1e-ab40-ceeb79266bfc.json
# Description: This process involves the design, installation, and optimization of a vertical farming system within an urban environment. It begins with site analysis and ends with continuous yield monitoring. The workflow includes integrating IoT sensors for environment control, sourcing sustainable materials, coordinating with local authorities for permits, and establishing supply chain logistics for fresh produce delivery. The process also addresses energy-efficient lighting installation, water recycling systems, automated nutrient delivery, and staff training on high-tech farming equipment. It ensures compliance with urban agriculture regulations and incorporates community engagement programs to promote awareness and adoption of vertical farming solutions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
permit_check     = Transition(label='Permit Check')
design_layout    = Transition(label='Design Layout')
material_sourcing= Transition(label='Material Sourcing')
install_sensors  = Transition(label='Install Sensors')
setup_lighting   = Transition(label='Setup Lighting')
water_system     = Transition(label='Water System')
nutrient_mix     = Transition(label='Nutrient Mix')
iot_integration  = Transition(label='IoT Integration')
energy_audit     = Transition(label='Energy Audit')
staff_training   = Transition(label='Staff Training')
test_run         = Transition(label='Test Run')
compliance_review= Transition(label='Compliance Review')
community_meet   = Transition(label='Community Meet')
supply_setup     = Transition(label='Supply Setup')
yield_monitor    = Transition(label='Yield Monitor')

# Silent transition for loop continuation decision
skip = SilentTransition()

# Loop for continuous yield monitoring: do yield_monitor, then either exit or do skip->yield_monitor again
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_monitor, skip])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_check,
    design_layout,
    material_sourcing,
    install_sensors,
    setup_lighting,
    water_system,
    nutrient_mix,
    iot_integration,
    energy_audit,
    staff_training,
    test_run,
    compliance_review,
    community_meet,
    supply_setup,
    monitor_loop
])

# Add ordering dependencies
edges = [
    (site_survey,    permit_check),
    (site_survey,    design_layout),
    (permit_check,   material_sourcing),
    (design_layout,  material_sourcing),
    (material_sourcing, install_sensors),
    (material_sourcing, setup_lighting),
    (material_sourcing, water_system),
    (material_sourcing, nutrient_mix),
    (install_sensors,  iot_integration),
    (setup_lighting,   iot_integration),
    (water_system,     iot_integration),
    (nutrient_mix,     iot_integration),
    (iot_integration,  energy_audit),
    (iot_integration,  staff_training),
    (energy_audit,     test_run),
    (staff_training,   test_run),
    (test_run,         compliance_review),
    (test_run,         community_meet),
    (compliance_review, supply_setup),
    (community_meet,    supply_setup),
    (supply_setup,      monitor_loop)
]

for src, tgt in edges:
    root.order.add_edge(src, tgt)