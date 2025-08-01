# Generated from: 4c778126-70d5-435a-8de3-49c6c14040c7.json
# Description: This process outlines the complex and multidisciplinary steps required to establish a sustainable urban rooftop farming system. It involves site assessment for structural integrity, microclimate analysis, soil and water testing, design of modular planting beds, installation of automated irrigation and nutrient delivery systems, integration of renewable energy sources, implementation of pest management strategies, staff training on urban agriculture techniques, and ongoing monitoring of crop health and yield. The process also includes community engagement to promote urban farming awareness, securing permits and compliance with local regulations, and establishing supply chains for distribution. This atypical but realistic process ensures efficient utilization of rooftop spaces to produce fresh, local food in densely populated urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_assess    = Transition(label='Site Assess')
load_test      = Transition(label='Load Test')
climate_scan   = Transition(label='Climate Scan')
soil_sample    = Transition(label='Soil Sample')
water_check    = Transition(label='Water Check')
permit_acquire = Transition(label='Permit Acquire')
community_meet = Transition(label='Community Meet')
bed_design     = Transition(label='Bed Design')
irrigation     = Transition(label='Irrigation Setup')
energy_install = Transition(label='Energy Install')
pest_control   = Transition(label='Pest Control')
staff_train    = Transition(label='Staff Train')
supply_chain   = Transition(label='Supply Chain')
crop_monitor   = Transition(label='Crop Monitor')
yield_report   = Transition(label='Yield Report')
waste_recycle  = Transition(label='Waste Recycle')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    site_assess, load_test, climate_scan, soil_sample, water_check,
    permit_acquire, community_meet, bed_design, irrigation, energy_install,
    pest_control, staff_train, supply_chain, crop_monitor, yield_report,
    waste_recycle
])

# Add sequencing and concurrency relations
root.order.add_edge(site_assess, load_test)
root.order.add_edge(load_test, climate_scan)

# Parallel soil & water testing
root.order.add_edge(climate_scan, soil_sample)
root.order.add_edge(climate_scan, water_check)

# Permit and community engagement after testing
root.order.add_edge(soil_sample, permit_acquire)
root.order.add_edge(water_check, permit_acquire)
root.order.add_edge(soil_sample, community_meet)
root.order.add_edge(water_check, community_meet)

# Bed design starts once permits and community meet are done
root.order.add_edge(permit_acquire, bed_design)
root.order.add_edge(community_meet, bed_design)

# Installation phases in parallel
root.order.add_edge(bed_design, irrigation)
root.order.add_edge(bed_design, energy_install)

# Pest control after installations
root.order.add_edge(irrigation, pest_control)
root.order.add_edge(energy_install, pest_control)

# Staff training then supply chain setup
root.order.add_edge(pest_control, staff_train)
root.order.add_edge(staff_train, supply_chain)

# Ongoing monitoring and reporting
root.order.add_edge(supply_chain, crop_monitor)
root.order.add_edge(crop_monitor, yield_report)

# Waste recycling after yield report
root.order.add_edge(yield_report, waste_recycle)