# Generated from: 57a6241f-1bfe-47ed-b147-c38d1d8b58f7.json
# Description: This process outlines the comprehensive steps required to establish a fully operational urban vertical farm within a repurposed industrial building. It involves site assessment, environmental control design, modular system installation, nutrient cycling setup, and integration of AI-driven monitoring. The process ensures sustainable resource use by incorporating rainwater harvesting and waste biomass recycling. Stakeholder coordination includes local authorities, agronomists, and technology providers to optimize crop yield and minimize ecological impact. Continuous testing and adjustment phases guarantee optimal growth conditions and system efficiency before commercial production launch.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
SS = Transition(label='Site Survey')
PA = Transition(label='Permits Acquire')
SM = Transition(label='Stakeholder Meet')
DL = Transition(label='Design Layout')
IF = Transition(label='Install Frame')
SH = Transition(label='Setup Hydroponics')
WH = Transition(label='Water Harvest')
NM = Transition(label='Nutrient Mix')
WP = Transition(label='Waste Process')
LI = Transition(label='Lighting Install')
SC = Transition(label='Sensor Calibrate')
AI = Transition(label='AI Integration')
CP = Transition(label='Crop Planting')
GM = Transition(label='Growth Monitor')
SA = Transition(label='System Audit')
YT = Transition(label='Yield Testing')

# Silent activity for loop continuation
skip = SilentTransition()

# 1) After Site Survey: Permits Acquire and Stakeholder Meet can happen in parallel
permits_stakeholders = StrictPartialOrder(nodes=[PA, SM])
# no order edges => concurrent

# 2) Design Layout follows the coordination phase
# 3) After Design Layout: two branches run concurrently
#    a) Modular installation sequence
mod_install = StrictPartialOrder(nodes=[IF, SH, LI, SC, AI])
mod_install.order.add_edge(IF, SH)
mod_install.order.add_edge(SH, LI)
mod_install.order.add_edge(LI, SC)
mod_install.order.add_edge(SC, AI)

#    b) Nutrient cycling setup sequence
nutrient_cycle = StrictPartialOrder(nodes=[WH, NM, WP])
nutrient_cycle.order.add_edge(WH, NM)
nutrient_cycle.order.add_edge(NM, WP)

# Combine the two branches into a concurrent PO
installation_phase = StrictPartialOrder(nodes=[mod_install, nutrient_cycle])
# no order edges between mod_install and nutrient_cycle => they run in parallel

# 4) After installation, plant the crops
# 5) Continuous testing and adjustment: loop of Growth Monitor + System Audit
test_loop_body = StrictPartialOrder(nodes=[GM, SA])
test_loop_body.order.add_edge(GM, SA)
testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[test_loop_body, skip])

# 6) Final yield testing after the loop
# Build the overall root PO
root = StrictPartialOrder(nodes=[
    SS,
    permits_stakeholders,
    DL,
    installation_phase,
    CP,
    testing_loop,
    YT
])

# Add the control-flow/order dependencies
root.order.add_edge(SS, permits_stakeholders)
root.order.add_edge(permits_stakeholders, DL)
root.order.add_edge(DL, installation_phase)
root.order.add_edge(installation_phase, CP)
root.order.add_edge(CP, testing_loop)
root.order.add_edge(testing_loop, YT)