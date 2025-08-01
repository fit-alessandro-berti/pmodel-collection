# Generated from: 0791e5e8-5e4e-4221-ba34-70ceea0a68aa.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a densely populated city environment. It includes site assessment for structural integrity, environmental impact analysis, procurement of modular growing units, integration of IoT sensors for climate control, installation of hydroponic and aeroponic systems, recruitment of specialized agronomists, regulatory compliance checks, development of waste recycling loops, marketing to local retailers, and continuous yield optimization through data analytics. The process ensures sustainable food production with minimal urban footprint, leveraging advanced technology and multi-disciplinary coordination to transform unused vertical spaces into productive agricultural hubs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey   = Transition(label='Site Survey')
load_testing  = Transition(label='Load Testing')
impact_study  = Transition(label='Impact Study')
supply_chain  = Transition(label='Supply Chain')
unit_purchase = Transition(label='Unit Purchase')
energy_audit  = Transition(label='Energy Audit')
system_install = Transition(label='System Install')
sensor_setup  = Transition(label='Sensor Setup')
permits_check = Transition(label='Permits Check')
staff_hiring  = Transition(label='Staff Hiring')
waste_design  = Transition(label='Waste Design')
retail_pitch  = Transition(label='Retail Pitch')
data_review   = Transition(label='Data Review')
yield_adjust  = Transition(label='Yield Adjust')
climate_tune  = Transition(label='Climate Tune')

# Build the loop for continuous yield optimization: 
# do Data Review, then optionally (Yield Adjust -> Climate Tune) and repeat
opt_body = StrictPartialOrder(nodes=[yield_adjust, climate_tune])
opt_body.order.add_edge(yield_adjust, climate_tune)
optimization_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_review, opt_body])

# Main partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_testing, impact_study,
    supply_chain, unit_purchase, energy_audit,
    system_install, sensor_setup,
    permits_check, staff_hiring,
    waste_design, retail_pitch,
    optimization_loop
])

# Define control-flow order
root.order.add_edge(site_survey,   load_testing)
root.order.add_edge(load_testing,  impact_study)

# Procurement path
root.order.add_edge(impact_study,  supply_chain)
root.order.add_edge(supply_chain,  unit_purchase)
root.order.add_edge(impact_study,  unit_purchase)

# Installation path
root.order.add_edge(impact_study,  energy_audit)
root.order.add_edge(energy_audit,  system_install)
root.order.add_edge(unit_purchase, system_install)
root.order.add_edge(system_install, sensor_setup)

# Compliance & staffing
root.order.add_edge(impact_study,  permits_check)
root.order.add_edge(permits_check, staff_hiring)
root.order.add_edge(system_install, staff_hiring)

# Waste design & marketing
root.order.add_edge(staff_hiring,  waste_design)
root.order.add_edge(waste_design,  retail_pitch)
root.order.add_edge(sensor_setup,  retail_pitch)

# Link to the ongoing optimization loop
root.order.add_edge(retail_pitch,  optimization_loop)