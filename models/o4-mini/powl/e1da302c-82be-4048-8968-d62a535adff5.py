# Generated from: e1da302c-82be-4048-8968-d62a535adff5.json
# Description: This process outlines the complex supply chain and operational workflow for an urban beekeeping business that produces honey, beeswax products, and educational services. It involves sourcing specialized urban-friendly bee colonies, adapting hive designs for rooftop and balcony installations, monitoring hive health with IoT sensors, harvesting honey safely without disrupting urban environments, processing raw materials in small-scale urban facilities, packaging with eco-friendly materials, managing direct-to-consumer deliveries via bicycle couriers, coordinating educational workshops for city residents, and ensuring compliance with municipal regulations. The process also integrates community engagement activities and data-driven hive maintenance schedules to optimize yield while minimizing environmental impact in dense city areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
colony       = Transition(label="Colony Sourcing")
design       = Transition(label="Hive Design")
survey       = Transition(label="Site Survey")
install_prep = Transition(label="Installation Prep")
setup        = Transition(label="Hive Setup")
sensor       = Transition(label="Sensor Install")
reg_check    = Transition(label="Regulation Check")
workshop     = Transition(label="Workshop Setup")
community    = Transition(label="Community Outreach")
honey        = Transition(label="Honey Harvest")
wax          = Transition(label="Wax Processing")
pack         = Transition(label="Product Packaging")
dispatch     = Transition(label="Order Dispatch")

# Two separate instances of Health Monitor for loop entry and body
hm_entry     = Transition(label="Health Monitor")
hm_body      = Transition(label="Health Monitor")
da           = Transition(label="Data Analysis")
mp           = Transition(label="Maintenance Plan")
pc           = Transition(label="Pest Control")

# Define the body of the maintenance loop: Data Analysis -> Maintenance Plan -> Pest Control -> Health Monitor
loop_body = StrictPartialOrder(
    nodes=[da, mp, pc, hm_body]
)
loop_body.order.add_edge(da, mp)
loop_body.order.add_edge(mp, pc)
loop_body.order.add_edge(pc, hm_body)

# Define the LOOP: first execute hm_entry, then either exit or do loop_body then hm_entry again
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[hm_entry, loop_body]
)

# Define the educational/community branch: Workshop Setup -> Community Outreach
edu_branch = StrictPartialOrder(
    nodes=[workshop, community]
)
edu_branch.order.add_edge(workshop, community)

# Build the root partial order with all nodes
root = StrictPartialOrder(
    nodes=[
        colony,
        design,
        survey,
        install_prep,
        setup,
        sensor,
        reg_check,
        maintenance_loop,
        honey,
        wax,
        pack,
        dispatch,
        edu_branch
    ]
)

# Initial setup sequence
root.order.add_edge(colony, design)
root.order.add_edge(design, survey)
root.order.add_edge(survey, install_prep)
root.order.add_edge(install_prep, setup)
root.order.add_edge(setup, sensor)
root.order.add_edge(sensor, reg_check)

# After regulation check, spawn both the maintenance loop and the educational branch
root.order.add_edge(reg_check, maintenance_loop)
root.order.add_edge(reg_check, edu_branch)

# After finishing maintenance, proceed to harvesting & dispatch
root.order.add_edge(maintenance_loop, honey)
root.order.add_edge(honey, wax)
root.order.add_edge(wax, pack)
root.order.add_edge(pack, dispatch)