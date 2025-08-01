# Generated from: 53962169-09b3-48c2-aaa7-f9e6c5adb641.json
# Description: Urban Beekeeping Management is a specialized process that involves maintaining and optimizing bee colonies within city environments. This process includes site evaluation for apiary placement, hive installation, monitoring bee health amid urban stressors, managing forage diversity, controlling pests and diseases without harmful chemicals, harvesting honey and beeswax sustainably, engaging with community stakeholders, and ensuring compliance with local regulations. Additionally, it integrates data-driven decisions using environmental sensors and IoT devices to track hive conditions, weather patterns, and pollution levels, thereby enabling proactive intervention to support colony resilience and productivity in a challenging urban ecosystem. The process also emphasizes educational outreach to raise awareness about pollinator importance and urban biodiversity conservation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
site_survey = Transition(label='Site Survey')
hive_setup = Transition(label='Hive Setup')
colony_inspection = Transition(label='Colony Inspection')
health_monitoring = Transition(label='Health Monitoring')
pest_control = Transition(label='Pest Control')
forage_analysis = Transition(label='Forage Analysis')
data_collection = Transition(label='Data Collection')
pollution_check = Transition(label='Pollution Check')
honey_harvest = Transition(label='Honey Harvest')
wax_processing = Transition(label='Wax Processing')
community_liaison = Transition(label='Community Liaison')
regulation_review = Transition(label='Regulation Review')
equipment_clean = Transition(label='Equipment Clean')
sensor_calibration = Transition(label='Sensor Calibration')
education_outreach = Transition(label='Education Outreach')
weather_tracking = Transition(label='Weather Tracking')
waste_disposal = Transition(label='Waste Disposal')

# The process structure interpretation:

# Initial partial order: Site Survey --> Hive Setup
init_po = StrictPartialOrder(nodes=[site_survey, hive_setup])
init_po.order.add_edge(site_survey, hive_setup)

# Inspection loop: Colony Inspection then Health Monitoring and Pest Control
# Loop with A = Colony Inspection
# B = choice between Health Monitoring and Pest Control

# Choice between Health Monitoring and Pest Control
health_or_pest = OperatorPOWL(operator=Operator.XOR, children=[health_monitoring, pest_control])

# Loop: execute Colony Inspection (A), then choice (B), then back to A or exit
inspection_loop = OperatorPOWL(operator=Operator.LOOP, children=[colony_inspection, health_or_pest])

# Forage Analysis concurrent with Data Collection (which itself contains Pollution Check and Weather Tracking)
# Data Collection nodes:
# Sensor calibration before Data Collection
sensor_data_po = StrictPartialOrder(nodes=[sensor_calibration,
                                           data_collection,
                                           pollution_check,
                                           weather_tracking])
# Order: sensor_calibration --> data_collection --> {pollution_check, weather_tracking} concurrently
sensor_data_po.order.add_edge(sensor_calibration, data_collection)
sensor_data_po.order.add_edge(data_collection, pollution_check)
sensor_data_po.order.add_edge(data_collection, weather_tracking)

# Forage Analysis runs concurrently with sensor_data_po
forage_and_data_po = StrictPartialOrder(nodes=[forage_analysis, sensor_data_po])
# No order edges between forage_analysis and sensor_data_po (concurrent)

# Honey Harvest then Wax Processing in sequence
harvest_po = StrictPartialOrder(nodes=[honey_harvest, wax_processing])
harvest_po.order.add_edge(honey_harvest, wax_processing)

# Community Liaison and Regulation Review concurrent (stakeholder engagement)
community_po = StrictPartialOrder(nodes=[community_liaison, regulation_review])

# Equipment Clean and Waste Disposal sequential cleanup
cleanup_po = StrictPartialOrder(nodes=[equipment_clean, waste_disposal])
cleanup_po.order.add_edge(equipment_clean, waste_disposal)

# Education Outreach can occur concurrently with cleanup or after community_po?
# Let’s model Education Outreach concurrent with community_po and cleanup_po (both represent different aftercare activities)
aftercare_po = StrictPartialOrder(nodes=[community_po, cleanup_po, education_outreach])
# No order among community_po, cleanup_po, education_outreach

# Define full process as a partial order combining all parts:

# Nodes list:
# start sequence: init_po
# inspection_loop after hive_setup
# forage_and_data_po concurrent with inspection_loop (interpret monitoring and data-driven decisions concurrent)
# harvest_po after inspection_loop and forage_and_data_po
# aftercare_po after harvest_po

root = StrictPartialOrder(nodes=[init_po, inspection_loop, forage_and_data_po, harvest_po, aftercare_po])

# Define order edges accordingly:

# hive_setup --> inspection_loop
root.order.add_edge(init_po, inspection_loop)
# inspection_loop --> harvest_po (harvest after inspection)
root.order.add_edge(inspection_loop, harvest_po)
# forage_and_data_po runs concurrently but should complete before harvest_po
root.order.add_edge(forage_and_data_po, harvest_po)

# harvest_po --> aftercare_po
root.order.add_edge(harvest_po, aftercare_po)