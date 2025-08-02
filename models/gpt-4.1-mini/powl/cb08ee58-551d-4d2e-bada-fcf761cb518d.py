# Generated from: cb08ee58-551d-4d2e-bada-fcf761cb518d.json
# Description: This process outlines the complex establishment of an urban vertical farming facility within a dense metropolitan area. It involves site selection based on sunlight and water access, modular system design tailored to building constraints, integration of IoT sensors for real-time crop monitoring, specialized nutrient delivery setup, automated climate control calibration, and compliance with local agricultural and safety regulations. The process also includes community engagement for sustainable practices, energy source assessment emphasizing renewable options, staff training on hydroponic and aeroponic techniques, and post-installation performance optimization to maximize yield while minimizing resource consumption. Throughout, synchronization with urban infrastructure and environmental impact assessments are critical to ensure feasibility and sustainability in an atypical urban agricultural setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Light_Mapping = Transition(label='Light Mapping')
Water_Testing = Transition(label='Water Testing')
Design_Modules = Transition(label='Design Modules')
IoT_Setup = Transition(label='IoT Setup')
Sensor_Calibration = Transition(label='Sensor Calibration')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Control = Transition(label='Climate Control')
Regulatory_Check = Transition(label='Regulatory Check')
Community_Meet = Transition(label='Community Meet')
Energy_Audit = Transition(label='Energy Audit')
Staff_Training = Transition(label='Staff Training')
Installation = Transition(label='Installation')
System_Testing = Transition(label='System Testing')
Yield_Analysis = Transition(label='Yield Analysis')
Resource_Audit = Transition(label='Resource Audit')
Impact_Review = Transition(label='Impact Review')

# Site survey branch: Site Survey -> (Light Mapping || Water Testing)
site_survey_po = StrictPartialOrder(
    nodes=[Site_Survey, Light_Mapping, Water_Testing]
)
site_survey_po.order.add_edge(Site_Survey, Light_Mapping)
site_survey_po.order.add_edge(Site_Survey, Water_Testing)

# Design Modules after site survey data
design = StrictPartialOrder(
    nodes=[Design_Modules]
)

# IoT Setup branch (IoT Setup -> Sensor Calibration)
iot_branch = StrictPartialOrder(
    nodes=[IoT_Setup, Sensor_Calibration]
)
iot_branch.order.add_edge(IoT_Setup, Sensor_Calibration)

# Nutrient Mix, Climate Control, Regulatory Check sequence
nutrients_branch = StrictPartialOrder(
    nodes=[Nutrient_Mix, Climate_Control, Regulatory_Check]
)
nutrients_branch.order.add_edge(Nutrient_Mix, Climate_Control)
nutrients_branch.order.add_edge(Climate_Control, Regulatory_Check)

# Community Meet and Energy Audit can run concurrently after Regulatory Check
community_energy = StrictPartialOrder(
    nodes=[Community_Meet, Energy_Audit]
)

# Staff Training comes after both Community Meet and Energy Audit
staff_training_po = StrictPartialOrder(
    nodes=[Staff_Training]
)

# Installation after Staff Training
installation_po = StrictPartialOrder(
    nodes=[Installation]
)

# System Testing after Installation
system_testing_po = StrictPartialOrder(
    nodes=[System_Testing]
)

# Yield Analysis, Resource Audit, and Impact Review run concurrently after System Testing
final_checks_po = StrictPartialOrder(
    nodes=[Yield_Analysis, Resource_Audit, Impact_Review]
)

# Define the top-level partial order connecting the subparts in their proper order:
# site_survey_po --> design --> iot_branch --> nutrients_branch --> community_energy --> staff_training_po -->
# installation_po --> system_testing_po --> final_checks_po

# Compose top level nodes list
top_nodes = [
    site_survey_po,
    design,
    iot_branch,
    nutrients_branch,
    community_energy,
    staff_training_po,
    installation_po,
    system_testing_po,
    final_checks_po
]

root = StrictPartialOrder(nodes=top_nodes)

# Add ordering edges between these nodes according to described sequential flow
root.order.add_edge(site_survey_po, design)
root.order.add_edge(design, iot_branch)
root.order.add_edge(iot_branch, nutrients_branch)
root.order.add_edge(nutrients_branch, community_energy)
root.order.add_edge(community_energy, staff_training_po)
root.order.add_edge(staff_training_po, installation_po)
root.order.add_edge(installation_po, system_testing_po)
root.order.add_edge(system_testing_po, final_checks_po)

# Within community_energy, Community_Meet and Energy_Audit run concurrently (no order edges)
# Within site_survey_po, Site Survey precedes Light Mapping and Water Testing, which run concurrently.
# Within nutrients_branch, linear order Nutrient Mix -> Climate Control -> Regulatory Check.

# This model captures the described partial orders, concurrency, and sequential dependencies.
