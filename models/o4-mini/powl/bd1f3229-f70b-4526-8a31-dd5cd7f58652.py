# Generated from: bd1f3229-f70b-4526-8a31-dd5cd7f58652.json
# Description: This process outlines the complex supply chain for urban beekeeping, integrating sustainable sourcing, community engagement, and regulatory compliance. It begins with hive material procurement from eco-certified suppliers, followed by custom hive assembly tailored to city environments. Next, the process manages bee colony acquisition ensuring genetic diversity and disease resistance. Urban apiaries are then strategically located and registered with local authorities. Continuous monitoring includes environmental data collection and adaptive hive maintenance. Honey extraction involves precise timing and contamination prevention. The product undergoes natural filtration, quality testing, and innovative packaging with biodegradable materials. Finally, distribution leverages local markets, subscription services, and educational workshops to promote awareness and sustainability within urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
ms                 = Transition(label="Material Sourcing")
ha                 = Transition(label="Hive Assembly")
cs                 = Transition(label="Colony Selection")
apiary_setup       = Transition(label="Apiary Setup")
rf                 = Transition(label="Regulatory Filing")
env_scan           = Transition(label="Environmental Scan")
hive_monitoring    = Transition(label="Hive Monitoring")
pest_control       = Transition(label="Pest Control")
honey_harvest      = Transition(label="Honey Harvest")
quality_testing    = Transition(label="Quality Testing")
natural_filtration = Transition(label="Natural Filtration")
eco_packaging      = Transition(label="Eco Packaging")
market_dist        = Transition(label="Market Distribution")
subscription_setup = Transition(label="Subscription Setup")
community_outreach = Transition(label="Community Outreach")

# Build the monitoring sequence: Environmental Scan -> Hive Monitoring -> Pest Control
monitor_seq = StrictPartialOrder(
    nodes=[env_scan, hive_monitoring, pest_control]
)
monitor_seq.order.add_edge(env_scan, hive_monitoring)
monitor_seq.order.add_edge(hive_monitoring, pest_control)

# Wrap the monitoring sequence in a loop for "continuous monitoring"
# LOOP(children=[A, B])  executes A, then 0 or more times (B then A)
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_seq, monitor_seq]
)

# Assemble the full process as a strict partial order
root = StrictPartialOrder(
    nodes=[
        ms,
        ha,
        cs,
        apiary_setup,
        rf,
        monitor_loop,
        honey_harvest,
        quality_testing,
        natural_filtration,
        eco_packaging,
        market_dist,
        subscription_setup,
        community_outreach
    ]
)

# Define the main sequential flow
root.order.add_edge(ms, ha)
root.order.add_edge(ha, cs)
root.order.add_edge(cs, apiary_setup)
root.order.add_edge(apiary_setup, rf)
root.order.add_edge(rf, monitor_loop)
root.order.add_edge(monitor_loop, honey_harvest)
root.order.add_edge(honey_harvest, quality_testing)
root.order.add_edge(quality_testing, natural_filtration)
root.order.add_edge(natural_filtration, eco_packaging)

# After packaging, all three distribution/outreach activities proceed concurrently
root.order.add_edge(eco_packaging, market_dist)
root.order.add_edge(eco_packaging, subscription_setup)
root.order.add_edge(eco_packaging, community_outreach)