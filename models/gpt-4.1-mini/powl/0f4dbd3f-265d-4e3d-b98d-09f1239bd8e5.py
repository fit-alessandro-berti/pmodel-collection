# Generated from: 0f4dbd3f-265d-4e3d-b98d-09f1239bd8e5.json
# Description: This process outlines the intricate steps involved in establishing an urban beekeeping operation within a densely populated city environment. It involves securing legal permits, site assessment for optimal hive placement considering microclimate and pollution levels, sourcing sustainable and disease-resistant bee colonies, designing modular hive systems adaptable to rooftop and balcony spaces, implementing integrated pest management tailored for urban pests, monitoring hive health through IoT sensors, coordinating community awareness programs to educate residents on bee safety, harvesting honey while ensuring minimal disruption to the colony, processing and packaging honey with urban branding, and maintaining continuous compliance with environmental and health regulations to promote urban biodiversity and sustainable practices.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Permit_Check = Transition(label='Permit Check')
Site_Survey = Transition(label='Site Survey')
Hive_Design = Transition(label='Hive Design')
Colony_Source = Transition(label='Colony Source')
Pest_Control = Transition(label='Pest Control')
Sensor_Setup = Transition(label='Sensor Setup')
Health_Monitor = Transition(label='Health Monitor')
Community_Meet = Transition(label='Community Meet')
Safety_Training = Transition(label='Safety Training')
Hive_Install = Transition(label='Hive Install')
Honey_Harvest = Transition(label='Honey Harvest')
Honey_Process = Transition(label='Honey Process')
Brand_Design = Transition(label='Brand Design')
Regulation_Audit = Transition(label='Regulation Audit')
Waste_Manage = Transition(label='Waste Manage')
Data_Analyze = Transition(label='Data Analyze')

# Construct the process partial order reflecting described dependencies

# Initial: securing legal permits must be done first
# After permit, site survey and design can happen in parallel, but design likely after site survey
# Colony source and pest control can proceed after site survey
# Sensor setup, community meet, safety training can happen after design and colony source, or in parallel
# Hive install after design, colony source, pest control, and safety training
# Honey harvest after hive install and health monitoring
# Honey process and brand design after honey harvest
# Regulation audit and waste manage and data analyze last - continuous compliance and analysis

# Create partial order with appropriate edges

nodes = [
    Permit_Check,
    Site_Survey,
    Hive_Design,
    Colony_Source,
    Pest_Control,
    Sensor_Setup,
    Health_Monitor,
    Community_Meet,
    Safety_Training,
    Hive_Install,
    Honey_Harvest,
    Honey_Process,
    Brand_Design,
    Regulation_Audit,
    Waste_Manage,
    Data_Analyze
]

root = StrictPartialOrder(nodes=nodes)

# Permit Check --> Site Survey
root.order.add_edge(Permit_Check, Site_Survey)

# Site Survey --> Hive Design
root.order.add_edge(Site_Survey, Hive_Design)

# Site Survey --> Colony Source
root.order.add_edge(Site_Survey, Colony_Source)

# Site Survey --> Pest Control
root.order.add_edge(Site_Survey, Pest_Control)

# Hive Design --> Sensor Setup
root.order.add_edge(Hive_Design, Sensor_Setup)

# Colony Source --> Safety Training
root.order.add_edge(Colony_Source, Safety_Training)

# Pest Control --> Safety Training
root.order.add_edge(Pest_Control, Safety_Training)

# Hive Design --> Community Meet
root.order.add_edge(Hive_Design, Community_Meet)

# Safety Training --> Hive Install
root.order.add_edge(Safety_Training, Hive_Install)

# Colony Source --> Hive Install
root.order.add_edge(Colony_Source, Hive_Install)

# Pest Control --> Hive Install
root.order.add_edge(Pest_Control, Hive_Install)

# Sensor Setup --> Health Monitor
root.order.add_edge(Sensor_Setup, Health_Monitor)

# Hive Install --> Honey Harvest
root.order.add_edge(Hive_Install, Honey_Harvest)

# Health Monitor --> Honey Harvest
root.order.add_edge(Health_Monitor, Honey_Harvest)

# Honey Harvest --> Honey Process
root.order.add_edge(Honey_Harvest, Honey_Process)

# Honey Harvest --> Brand Design
root.order.add_edge(Honey_Harvest, Brand_Design)

# Honey Process --> Regulation Audit
root.order.add_edge(Honey_Process, Regulation_Audit)

# Brand Design --> Regulation Audit
root.order.add_edge(Brand_Design, Regulation_Audit)

# Regulation Audit --> Waste Manage
root.order.add_edge(Regulation_Audit, Waste_Manage)

# Regulation Audit --> Data Analyze
root.order.add_edge(Regulation_Audit, Data_Analyze)