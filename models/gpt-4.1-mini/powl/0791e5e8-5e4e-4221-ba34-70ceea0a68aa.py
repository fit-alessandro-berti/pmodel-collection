# Generated from: 0791e5e8-5e4e-4221-ba34-70ceea0a68aa.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a densely populated city environment. It includes site assessment for structural integrity, environmental impact analysis, procurement of modular growing units, integration of IoT sensors for climate control, installation of hydroponic and aeroponic systems, recruitment of specialized agronomists, regulatory compliance checks, development of waste recycling loops, marketing to local retailers, and continuous yield optimization through data analytics. The process ensures sustainable food production with minimal urban footprint, leveraging advanced technology and multi-disciplinary coordination to transform unused vertical spaces into productive agricultural hubs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Load_Testing = Transition(label='Load Testing')
Impact_Study = Transition(label='Impact Study')
Unit_Purchase = Transition(label='Unit Purchase')
Sensor_Setup = Transition(label='Sensor Setup')
System_Install = Transition(label='System Install')
Staff_Hiring = Transition(label='Staff Hiring')
Permits_Check = Transition(label='Permits Check')
Waste_Design = Transition(label='Waste Design')
Retail_Pitch = Transition(label='Retail Pitch')
Climate_Tune = Transition(label='Climate Tune')
Data_Review = Transition(label='Data Review')
Yield_Adjust = Transition(label='Yield Adjust')
Supply_Chain = Transition(label='Supply Chain')
Energy_Audit = Transition(label='Energy Audit')

# Construct partial order for site assessment branch: Site Survey --> Load Testing & Impact Study in parallel
site_assessment = StrictPartialOrder(
    nodes=[Site_Survey, Load_Testing, Impact_Study],
)
site_assessment.order.add_edge(Site_Survey, Load_Testing)
site_assessment.order.add_edge(Site_Survey, Impact_Study)
# Load Testing and Impact Study concurrent (no edge between them)

# Procurement and installation flow:
# Unit Purchase --> Sensor Setup --> System Install
procurement_install = StrictPartialOrder(
    nodes=[Unit_Purchase, Sensor_Setup, System_Install],
)
procurement_install.order.add_edge(Unit_Purchase, Sensor_Setup)
procurement_install.order.add_edge(Sensor_Setup, System_Install)

# Staff hiring and permits check in parallel:
staff_permits = StrictPartialOrder(
    nodes=[Staff_Hiring, Permits_Check]
)  # no order = concurrent

# Waste Design is a loop with continuous yield optimization including Climate Tune, Data Review, Yield Adjust
# Loop node: Waste Design is A, body B is sequence: Climate Tune --> Data Review --> Yield Adjust
waste_loop_body = StrictPartialOrder(
    nodes=[Climate_Tune, Data_Review, Yield_Adjust]
)
waste_loop_body.order.add_edge(Climate_Tune, Data_Review)
waste_loop_body.order.add_edge(Data_Review, Yield_Adjust)

waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[Waste_Design, waste_loop_body])

# Marketing flow: Retail Pitch
marketing = Retail_Pitch

# Supply Chain and Energy Audit concurrent (both wrap around support functions)
support_funcs = StrictPartialOrder(
    nodes=[Supply_Chain, Energy_Audit]
)  # no order = concurrent

# Assemble main workflow partial order:
# site_assessment --> procurement_install --> (staff_permits parallel with waste_loop and marketing and support)
main_partial = StrictPartialOrder(
    nodes=[site_assessment, procurement_install, staff_permits, waste_loop, marketing, support_funcs]
)
main_partial.order.add_edge(site_assessment, procurement_install)
main_partial.order.add_edge(procurement_install, staff_permits)
# staff_permits, waste_loop, marketing, support_funcs start after procurement_install concurrently
main_partial.order.add_edge(procurement_install, waste_loop)
main_partial.order.add_edge(procurement_install, marketing)
main_partial.order.add_edge(procurement_install, support_funcs)

# Done: save to root
root = main_partial