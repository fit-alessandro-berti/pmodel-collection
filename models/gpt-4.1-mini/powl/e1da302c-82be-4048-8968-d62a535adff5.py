# Generated from: e1da302c-82be-4048-8968-d62a535adff5.json
# Description: This process outlines the complex supply chain and operational workflow for an urban beekeeping business that produces honey, beeswax products, and educational services. It involves sourcing specialized urban-friendly bee colonies, adapting hive designs for rooftop and balcony installations, monitoring hive health with IoT sensors, harvesting honey safely without disrupting urban environments, processing raw materials in small-scale urban facilities, packaging with eco-friendly materials, managing direct-to-consumer deliveries via bicycle couriers, coordinating educational workshops for city residents, and ensuring compliance with municipal regulations. The process also integrates community engagement activities and data-driven hive maintenance schedules to optimize yield while minimizing environmental impact in dense city areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities:
Colony_Sourcing = Transition(label='Colony Sourcing')
Hive_Design = Transition(label='Hive Design')
Site_Survey = Transition(label='Site Survey')
Installation_Prep = Transition(label='Installation Prep')
Hive_Setup = Transition(label='Hive Setup')
Sensor_Install = Transition(label='Sensor Install')
Health_Monitor = Transition(label='Health Monitor')
Pest_Control = Transition(label='Pest Control')
Honey_Harvest = Transition(label='Honey Harvest')
Wax_Processing = Transition(label='Wax Processing')
Product_Packaging = Transition(label='Product Packaging')
Order_Dispatch = Transition(label='Order Dispatch')
Workshop_Setup = Transition(label='Workshop Setup')
Community_Outreach = Transition(label='Community Outreach')
Regulation_Check = Transition(label='Regulation Check')
Data_Analysis = Transition(label='Data Analysis')
Maintenance_Plan = Transition(label='Maintenance Plan')

# Model the supply chain and setup flow: Colony Sourcing -> Hive Design -> Site Survey -> Installation Prep -> Hive Setup -> Sensor Install
setup_po = StrictPartialOrder(nodes=[
    Colony_Sourcing, Hive_Design, Site_Survey, Installation_Prep, Hive_Setup, Sensor_Install
])
setup_po.order.add_edge(Colony_Sourcing, Hive_Design)
setup_po.order.add_edge(Hive_Design, Site_Survey)
setup_po.order.add_edge(Site_Survey, Installation_Prep)
setup_po.order.add_edge(Installation_Prep, Hive_Setup)
setup_po.order.add_edge(Hive_Setup, Sensor_Install)

# Monitoring and maintenance loop:
# Loop( Health Monitor, Pest Control )
# Then Data Analysis -> Maintenance Plan after loop ends
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[Health_Monitor, Pest_Control])
monitoring_and_plan = StrictPartialOrder(nodes=[monitoring_loop, Data_Analysis, Maintenance_Plan])
monitoring_and_plan.order.add_edge(monitoring_loop, Data_Analysis)
monitoring_and_plan.order.add_edge(Data_Analysis, Maintenance_Plan)

# Harvest and processing branch:
# Honey Harvest -> Wax Processing -> Product Packaging -> Order Dispatch
processing_po = StrictPartialOrder(nodes=[
    Honey_Harvest, Wax_Processing, Product_Packaging, Order_Dispatch
])
processing_po.order.add_edge(Honey_Harvest, Wax_Processing)
processing_po.order.add_edge(Wax_Processing, Product_Packaging)
processing_po.order.add_edge(Product_Packaging, Order_Dispatch)

# Educational and community outreach branch:
# Workshop Setup and Community Outreach can be concurrent
edu_comm_po = StrictPartialOrder(nodes=[Workshop_Setup, Community_Outreach])

# Regulation Check must happen before Installation Prep (safety & compliance)
# So Regulation_Check is prior to Installation_Prep in main flow
# We'll incorporate Regulation_Check just before Installation_Prep
reg_check_po = StrictPartialOrder(nodes=[Regulation_Check, Installation_Prep])
reg_check_po.order.add_edge(Regulation_Check, Installation_Prep)

# Incorporate Regulation Check into main setup flow replacing Installation_Prep node with reg_check_po as partial order
# So the main setup sequence up to Site Survey, then Regulation Check -> Installation Prep, then Hive Setup and Sensor Install

# Redefine setup with Regulation Check:
setup_nodes = [
    Colony_Sourcing, Hive_Design, Site_Survey,
    # Insert reg_check_po structure before Hive Setup and Sensor Install
    reg_check_po,
    Hive_Setup, Sensor_Install
]

root = StrictPartialOrder(nodes=setup_nodes + [monitoring_loop, Data_Analysis, Maintenance_Plan,
                                             Honey_Harvest, Wax_Processing, Product_Packaging, Order_Dispatch,
                                             Workshop_Setup, Community_Outreach])

# Edges for main supply chain with reg_check_po as composite:
root.order.add_edge(Colony_Sourcing, Hive_Design)
root.order.add_edge(Hive_Design, Site_Survey)
root.order.add_edge(Site_Survey, reg_check_po)
root.order.add_edge(reg_check_po, Hive_Setup)
root.order.add_edge(Hive_Setup, Sensor_Install)

# Monitoring loop and plan after Sensor Install (continuous production)
root.order.add_edge(Sensor_Install, monitoring_loop)
root.order.add_edge(monitoring_loop, Data_Analysis)
root.order.add_edge(Data_Analysis, Maintenance_Plan)

# Processing flow can start after Sensor Install concurrently with monitoring
root.order.add_edge(Sensor_Install, Honey_Harvest)
root.order.add_edge(Honey_Harvest, Wax_Processing)
root.order.add_edge(Wax_Processing, Product_Packaging)
root.order.add_edge(Product_Packaging, Order_Dispatch)

# Educational and community outreach run concurrently with everything after Sensor Install
root.order.add_edge(Sensor_Install, Workshop_Setup)
root.order.add_edge(Sensor_Install, Community_Outreach)