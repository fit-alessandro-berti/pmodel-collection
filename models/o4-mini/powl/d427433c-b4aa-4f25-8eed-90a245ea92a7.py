# Generated from: d427433c-b4aa-4f25-8eed-90a245ea92a7.json
# Description: This process outlines the complex supply chain for artisanal cheese production, starting from raw milk collection from multiple small farms, followed by quality testing, milk blending, and fermentation monitoring. The process involves aging control, packaging customization based on regional demand, cold-chain logistics coordination, regulatory compliance checks, and finally, distribution to niche gourmet retailers. Throughout, traceability is maintained via blockchain recording, while dynamic pricing models are applied based on market trends and seasonal variations. Customer feedback loops are integrated to adjust future batches and optimize flavor profiles, ensuring a premium product that balances tradition and innovation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
mc    = Transition(label="Milk Collection")
qt    = Transition(label="Quality Testing")
mb    = Transition(label="Milk Blending")
sc    = Transition(label="Starter Culture")
fc    = Transition(label="Fermentation Check")
ccu   = Transition(label="Curd Cutting")
ws    = Transition(label="Whey Separation")
mp    = Transition(label="Molding Press")
ss    = Transition(label="Salting Stage")
ac    = Transition(label="Aging Control")
pd    = Transition(label="Packaging Design")
cs    = Transition(label="Cold Shipping")
ca    = Transition(label="Compliance Audit")
bl    = Transition(label="Blockchain Log")
mpri  = Transition(label="Market Pricing")
of    = Transition(label="Order Fulfillment")
fr    = Transition(label="Feedback Review")

# Loop for repeated quality testing & compliance until pass:
#   Quality Testing; ( Compliance Audit; Quality Testing )* ; exit
qa_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[qt, ca]
)

# Main supply‐chain flow, with blockchain logging concurrent to all steps
main_flow = StrictPartialOrder(
    nodes=[mc, qa_loop, mb, sc, fc, ccu, ws, mp, ss, ac, pd, cs, mpri, of, bl]
)
# Define the sequential control‐flow edges (bl is left unconnected → concurrent)
main_flow.order.add_edge(mc,   qa_loop)
main_flow.order.add_edge(qa_loop, mb)
main_flow.order.add_edge(mb,   sc)
main_flow.order.add_edge(sc,   fc)
main_flow.order.add_edge(fc,   ccu)
main_flow.order.add_edge(ccu,  ws)
main_flow.order.add_edge(ws,   mp)
main_flow.order.add_edge(mp,   ss)
main_flow.order.add_edge(ss,   ac)
main_flow.order.add_edge(ac,   pd)
main_flow.order.add_edge(pd,   cs)
main_flow.order.add_edge(cs,   mpri)
main_flow.order.add_edge(mpri, of)

# Top‐level loop for customer feedback driving batch adjustments:
#   main_flow; ( Feedback Review; main_flow )* ; exit
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_flow, fr]
)