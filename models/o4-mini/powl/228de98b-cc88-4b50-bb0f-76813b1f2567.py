# Generated from: 228de98b-cc88-4b50-bb0f-76813b1f2567.json
# Description: This process outlines the comprehensive steps involved in launching an urban vertical farm that integrates sustainable agriculture technology with community engagement and real-time data analytics. It begins with site evaluation using environmental sensors and urban zoning regulations, followed by modular infrastructure setup including hydroponic and aeroponic systems. Concurrently, partnerships with local suppliers and distribution networks are established to ensure fresh produce delivery. The process also involves continuous monitoring through IoT devices, adaptive nutrient management based on crop feedback, and workforce training emphasizing both agricultural expertise and technology operation. Additionally, a community outreach program is deployed to promote education, local involvement, and market awareness. Finally, a feedback loop incorporates customer insights and operational data to optimize yield and sustainability, ensuring the farm remains economically viable and environmentally responsible in a dense urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ss  = Transition('Site Survey')
rr  = Transition('Regulation Review')
ts  = Transition('Tech Selection')
mb  = Transition('Modular Build')
ssu = Transition('System Setup')
sv  = Transition('Supplier Vetting')
dp  = Transition('Distribution Plan')
ii  = Transition('IoT Install')
cm  = Transition('Crop Monitoring')
na  = Transition('Nutrient Adjust')
st  = Transition('Staff Training')
co  = Transition('Community Outreach')
ml  = Transition('Market Launch')
fa  = Transition('Feedback Analyze')
yo  = Transition('Yield Optimize')
sa  = Transition('Sustainability Audit')

# Build the redo-phase of the feedback loop: Yield Optimize -> Sustainability Audit
redo = StrictPartialOrder(nodes=[yo, sa])
redo.order.add_edge(yo, sa)

# Build the loop: each iteration starts with Feedback Analyze, then either exit
# or go through the redo-phase and loop again
loop = OperatorPOWL(operator=Operator.LOOP, children=[fa, redo])

# Assemble the top‐level partial order
root = StrictPartialOrder(
    nodes=[ss, rr, ts, mb, ssu, sv, dp, ii, cm, na, st, co, ml, loop]
)

# Site evaluation
root.order.add_edge(ss, rr)

# After evaluation: tech selection and supplier vetting in parallel
root.order.add_edge(rr, ts)
root.order.add_edge(rr, sv)

# Modular infrastructure after tech is chosen
root.order.add_edge(ts, mb)
root.order.add_edge(ts, ssu)

# Distribution plan after supplier vetting
root.order.add_edge(sv, dp)

# Once infrastructure modules and system are ready, install IoT
root.order.add_edge(mb, ii)
root.order.add_edge(ssu, ii)

# Crop monitoring and adaptive nutrient management
root.order.add_edge(ii, cm)
root.order.add_edge(cm, na)

# Workforce training and community outreach once system is set up
root.order.add_edge(ssu, st)
root.order.add_edge(ssu, co)

# Market launch requires distribution plan, trained staff, and outreach done
root.order.add_edge(dp, ml)
root.order.add_edge(st, ml)
root.order.add_edge(co, ml)

# After market launch we enter the feedback loop
root.order.add_edge(ml, loop)