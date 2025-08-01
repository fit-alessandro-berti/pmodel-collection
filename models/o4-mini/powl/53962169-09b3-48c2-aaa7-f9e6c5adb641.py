# Generated from: 53962169-09b3-48c2-aaa7-f9e6c5adb641.json
# Description: Urban Beekeeping Management is a specialized process that involves maintaining and optimizing bee colonies within city environments. This process includes site evaluation for apiary placement, hive installation, monitoring bee health amid urban stressors, managing forage diversity, controlling pests and diseases without harmful chemicals, harvesting honey and beeswax sustainably, engaging with community stakeholders, and ensuring compliance with local regulations. Additionally, it integrates data-driven decisions using environmental sensors and IoT devices to track hive conditions, weather patterns, and pollution levels, thereby enabling proactive intervention to support colony resilience and productivity in a challenging urban ecosystem. The process also emphasizes educational outreach to raise awareness about pollinator importance and urban biodiversity conservation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey       = Transition(label='Site Survey')
hive_setup        = Transition(label='Hive Setup')
colony_inspection = Transition(label='Colony Inspection')
health_monitoring = Transition(label='Health Monitoring')
pest_control      = Transition(label='Pest Control')
forage_analysis   = Transition(label='Forage Analysis')
data_collection   = Transition(label='Data Collection')
pollution_check   = Transition(label='Pollution Check')
honey_harvest     = Transition(label='Honey Harvest')
wax_processing    = Transition(label='Wax Processing')
community_liaison = Transition(label='Community Liaison')
regulation_review = Transition(label='Regulation Review')
equipment_clean   = Transition(label='Equipment Clean')
sensor_calib      = Transition(label='Sensor Calibration')
education_outreach= Transition(label='Education Outreach')
weather_tracking  = Transition(label='Weather Tracking')
waste_disposal    = Transition(label='Waste Disposal')

# Monitoring partial order (concurrent monitoring tasks)
monitoring = StrictPartialOrder(nodes=[
    colony_inspection,
    health_monitoring,
    data_collection,
    sensor_calib,
    weather_tracking,
    pollution_check
])
# No edges => all these can happen in any order / concurrently

# Management partial order (concurrent management tasks)
management = StrictPartialOrder(nodes=[
    pest_control,
    forage_analysis
])
# No edges => pest control and forage analysis can proceed in parallel

# Loop: do monitoring, then either exit or do management and repeat monitoring
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitoring, management]
)

# Harvest sequence: honey then wax
harvest_seq = StrictPartialOrder(nodes=[honey_harvest, wax_processing])
harvest_seq.order.add_edge(honey_harvest, wax_processing)

# Cleanup sequence: equipment clean then waste disposal
cleanup_seq = StrictPartialOrder(nodes=[equipment_clean, waste_disposal])
cleanup_seq.order.add_edge(equipment_clean, waste_disposal)

# Community & compliance concurrently
community_outreach = StrictPartialOrder(nodes=[
    community_liaison,
    education_outreach,
    regulation_review
])
# No edges => these three can be done in any order / concurrently

# Assemble the root process
root = StrictPartialOrder(nodes=[
    site_survey,
    hive_setup,
    monitoring_loop,
    harvest_seq,
    cleanup_seq,
    community_outreach
])
# Define the high‐level ordering
root.order.add_edge(site_survey,     hive_setup)
root.order.add_edge(hive_setup,      monitoring_loop)
root.order.add_edge(monitoring_loop, harvest_seq)
root.order.add_edge(harvest_seq,     cleanup_seq)
root.order.add_edge(cleanup_seq,     community_outreach)