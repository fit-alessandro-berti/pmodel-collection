# Generated from: 3879bc4a-bfa5-40df-a9e7-89f5da7af3d9.json
# Description: This process outlines the complex supply chain involved in urban beekeeping, integrating environmental monitoring, community engagement, and sustainable product distribution. It begins with hive site selection based on microclimate data and urban flora analysis, followed by custom hive fabrication using recycled materials. Next, queen bee sourcing is managed through selective breeding programs to ensure disease resistance. Routine hive inspections incorporate sensor data for hive health assessment, triggering adaptive feeding and pest control strategies. Honey extraction is performed in modular mobile units to minimize contamination, then quality tested for urban pollutants. Packaging combines eco-friendly materials with local branding initiatives. Distribution leverages a hybrid model of direct sales at farmers markets and subscription-based delivery services. Throughout the process, educational workshops and citizen-science data collection are integrated to foster community involvement and promote urban biodiversity awareness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_select    = Transition(label='Site Select')
flora_survey   = Transition(label='Flora Survey')
micro_map      = Transition(label='Microclimate Map')
hive_design    = Transition(label='Hive Design')
material_src   = Transition(label='Material Source')
hive_build     = Transition(label='Hive Build')
queen_breed    = Transition(label='Queen Breed')
hive_inspect   = Transition(label='Hive Inspect')
sensor_check   = Transition(label='Sensor Check')
feed_adjust    = Transition(label='Feed Adjust')
pest_control   = Transition(label='Pest Control')
honey_extract  = Transition(label='Honey Extract')
quality_test   = Transition(label='Quality Test')
eco_package    = Transition(label='Eco Package')
market_setup   = Transition(label='Market Setup')
subscribe_setup= Transition(label='Subscribe Setup')
workshop_plan  = Transition(label='Workshop Plan')
data_collect   = Transition(label='Data Collect')

# Build the partial order
root = StrictPartialOrder(nodes=[
    flora_survey, micro_map, site_select,
    hive_design, material_src, hive_build,
    queen_breed, hive_inspect, sensor_check,
    feed_adjust, pest_control, honey_extract,
    quality_test, eco_package, market_setup,
    subscribe_setup, workshop_plan, data_collect
])

# Site selection depends on surveys
root.order.add_edge(flora_survey, site_select)
root.order.add_edge(micro_map,   site_select)

# Hive fabrication
root.order.add_edge(site_select, hive_design)
root.order.add_edge(site_select, material_src)
root.order.add_edge(hive_design, hive_build)
root.order.add_edge(material_src, hive_build)

# Queen sourcing
root.order.add_edge(hive_build,  queen_breed)

# Routine inspection loop (linearized partial order)
root.order.add_edge(queen_breed,  hive_inspect)
root.order.add_edge(hive_inspect, sensor_check)
root.order.add_edge(sensor_check, feed_adjust)
root.order.add_edge(sensor_check, pest_control)

# Extraction and testing
root.order.add_edge(feed_adjust,   honey_extract)
root.order.add_edge(pest_control,  honey_extract)
root.order.add_edge(honey_extract, quality_test)

# Packaging and distribution
root.order.add_edge(quality_test,   eco_package)
root.order.add_edge(eco_package,    market_setup)
root.order.add_edge(eco_package,    subscribe_setup)

# Workshops and data collection run concurrently throughout (no edges)

# 'root' now holds the complete POWL model.