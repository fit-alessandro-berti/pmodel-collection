# Generated from: 718a0fba-873e-4b96-93a2-9180385c7ce7.json
# Description: This process outlines the atypical yet realistic supply chain management for urban beekeeping. It involves sourcing sustainable hive materials from local artisans, coordinating micro-scale nectar collection schedules with city flora bloom cycles, ensuring compliance with municipal regulations on apiary placement, monitoring hive health remotely using IoT sensors, orchestrating community workshops for beekeeper training, managing seasonal honey extraction and packaging, facilitating direct-to-consumer urban farmers markets sales, and implementing a feedback loop for continuous product and process improvement. The complexity arises from intertwining ecological factors, regulatory constraints, and hyper-localized logistics within a dense urban environment, demanding agile coordination across diverse stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Material_Sourcing = Transition(label='Material Sourcing')
Design_Approval = Transition(label='Design Approval')
Regulation_Check = Transition(label='Regulation Check')
Artisan_Liaison = Transition(label='Artisan Liaison')
Bloom_Mapping = Transition(label='Bloom Mapping')
Nectar_Timing = Transition(label='Nectar Timing')
Hive_Setup = Transition(label='Hive Setup')
Sensor_Install = Transition(label='Sensor Install')
Health_Monitor = Transition(label='Health Monitor')
Workshop_Plan = Transition(label='Workshop Plan')
Training_Deliver = Transition(label='Training Deliver')
Honey_Extract = Transition(label='Honey Extract')
Packaging_Prep = Transition(label='Packaging Prep')
Market_Setup = Transition(label='Market Setup')
Customer_Feedback = Transition(label='Customer Feedback')
Process_Review = Transition(label='Process Review')

# Build:
# 1) Sourcing chain: Material Sourcing -> Design Approval -> Regulation Check -> Artisan Liaison
sourcing_po = StrictPartialOrder(nodes=[Material_Sourcing, Design_Approval, Regulation_Check, Artisan_Liaison])
sourcing_po.order.add_edge(Material_Sourcing, Design_Approval)
sourcing_po.order.add_edge(Design_Approval, Regulation_Check)
sourcing_po.order.add_edge(Regulation_Check, Artisan_Liaison)

# 2) Nectar collection coordination: Bloom Mapping -> Nectar Timing
nectar_po = StrictPartialOrder(nodes=[Bloom_Mapping, Nectar_Timing])
nectar_po.order.add_edge(Bloom_Mapping, Nectar_Timing)

# 3) Hive setup: Hive Setup and Sensor Install concurrent before Health Monitor
hive_setup_po = StrictPartialOrder(nodes=[Hive_Setup, Sensor_Install, Health_Monitor])
hive_setup_po.order.add_edge(Hive_Setup, Health_Monitor)
hive_setup_po.order.add_edge(Sensor_Install, Health_Monitor)

# 4) Workshops: Workshop Plan -> Training Deliver
workshops_po = StrictPartialOrder(nodes=[Workshop_Plan, Training_Deliver])
workshops_po.order.add_edge(Workshop_Plan, Training_Deliver)

# 5) Honey processing: Honey Extract -> Packaging Prep
honey_proc_po = StrictPartialOrder(nodes=[Honey_Extract, Packaging_Prep])
honey_proc_po.order.add_edge(Honey_Extract, Packaging_Prep)

# 6) Market sales: Market Setup
# It's a single activity

# 7) Feedback loop: Customer Feedback and Process Review loop
# Model loop with * (Customer Feedback, Process Review)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Customer_Feedback, Process_Review])

# Now combine major phases in partial order, considering ecological & logistical dependencies
# First: sourcing_po and nectar_po run concurrently
# After completion of sourcing_po and nectar_po, proceed to hive_setup_po
# Workshops (workshops_po) can start after hive setup started (let's assume after Hive_Setup)
# Honey processing (honey_proc_po) starts after Training Deliver and Health Monitor (both needed)
# Market setup starts after Packaging Prep done
# Feedback loop runs concurrently with Market Setup (continuous improvement)
root_nodes = [
    sourcing_po,
    nectar_po,
    hive_setup_po,
    workshops_po,
    honey_proc_po,
    Market_Setup,
    feedback_loop
]

root = StrictPartialOrder(nodes=root_nodes)

# Order edges:

# sourcing_po and nectar_po run concurrently: no edges between them

# sourcing_po and nectar_po both precede hive_setup_po
root.order.add_edge(sourcing_po, hive_setup_po)
root.order.add_edge(nectar_po, hive_setup_po)

# workshops_po can start after Hive_Setup done, which is a node in hive_setup_po
root.order.add_edge(hive_setup_po, workshops_po)

# honey_proc_po starts after Training Deliver (in workshops_po) and Health Monitor (in hive_setup_po)

# To enforce this, we add edges:
root.order.add_edge(workshops_po, honey_proc_po)
root.order.add_edge(hive_setup_po, honey_proc_po)

# Market_Setup after Packaging Prep (in honey_proc_po)
root.order.add_edge(honey_proc_po, Market_Setup)

# Feedback loop runs concurrently with Market_Setup: no edge needed

# The final model 'root' is the combination above.
