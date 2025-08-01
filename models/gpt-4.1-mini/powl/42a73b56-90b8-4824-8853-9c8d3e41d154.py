# Generated from: 42a73b56-90b8-4824-8853-9c8d3e41d154.json
# Description: This process outlines the complex steps required to establish a fully operational urban vertical farming facility in a metropolitan area. It involves site analysis, modular system design, climate control integration, crop selection based on microclimate data, automated nutrient delivery calibration, pest management without pesticides, staff training on hydroponics, real-time growth monitoring using IoT sensors, supply chain coordination for local distribution, sustainability assessment, community engagement programs, regulatory compliance checks, continuous yield optimization, and post-launch performance review to ensure scalability and profitability within the urban agriculture sector.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
climate_setup = Transition(label='Climate Setup')
crop_select = Transition(label='Crop Select')
nutrient_calibrate = Transition(label='Nutrient Calibrate')
pest_control = Transition(label='Pest Control')
staff_training = Transition(label='Staff Training')
sensor_deploy = Transition(label='Sensor Deploy')
growth_monitor = Transition(label='Growth Monitor')
supply_align = Transition(label='Supply Align')
sustainability_check = Transition(label='Sustainability Check')
community_outreach = Transition(label='Community Outreach')
compliance_audit = Transition(label='Compliance Audit')
yield_optimize = Transition(label='Yield Optimize')
performance_review = Transition(label='Performance Review')

# Build partial orders to reflect ordering and concurrency

# Initial phase: site survey then design modules
po1 = StrictPartialOrder(nodes=[site_survey, design_modules])
po1.order.add_edge(site_survey, design_modules)

# Climate setup and crop select depend on design modules, but can run concurrently
po2 = StrictPartialOrder(nodes=[climate_setup, crop_select])
# Both depend on design_modules, so we connect design_modules --> climate_setup and design_modules --> crop_select

# Nutrient calibrate depends on climate setup, pest control and staff training depend on crop select (can run concurrently)
nutrient_calibrate_po = Transition(label='Nutrient Calibrate')
nutrient_calibrate = nutrient_calibrate  # already defined

# Will use 'nutrient_calibrate' as defined
po3 = StrictPartialOrder(nodes=[nutrient_calibrate, pest_control, staff_training])
# Order:
# climate_setup --> nutrient_calibrate
# crop_select --> pest_control
# crop_select --> staff_training

# sensor_deploy depends on staff_training (trained staff deploy sensors), growth_monitor depends on sensor_deploy
po4 = StrictPartialOrder(nodes=[sensor_deploy, growth_monitor])
po4.order.add_edge(sensor_deploy, growth_monitor)
# staff_training --> sensor_deploy
# so connect staff_training --> sensor_deploy

# supply_align, sustainability_check, community_outreach, compliance_audit can run after growth_monitor,
# can be concurrent
po5 = StrictPartialOrder(nodes=[supply_align, sustainability_check, community_outreach, compliance_audit])
#  growth_monitor --> each of these four

# yield_optimize depends on compliance_audit and sustainability_check (both must be done)
# we merge those as a PO, then yield_optimize after
po6 = StrictPartialOrder(nodes=[yield_optimize])
# dependencies: compliance_audit --> yield_optimize
#               sustainability_check --> yield_optimize

# performance_review depends on yield_optimize and supply_align (both must be done)
po7 = StrictPartialOrder(nodes=[performance_review])
# yield_optimize --> performance_review
# supply_align --> performance_review
# community_outreach does not block performance_review, but logically likely ends before

# Now connect the partial orders with their dependencies:

root_nodes = [
    po1,
    climate_setup,
    crop_select,
    po3,
    po4,
    po5,
    po6,
    po7
]

# Create overall root POWL and add edges according to dependencies between sub-models

root = StrictPartialOrder(nodes=root_nodes)

# Add edges according to dependencies inside sub components first (already done inside po1, po3, po4, po5, po6, po7).

# Now add edges between these nodes at top level:

# po1 = [site_survey, design_modules]
# climate_setup, crop_select depend on design_modules

root.order.add_edge(po1, climate_setup)  # design_modules (in po1) --> climate_setup
root.order.add_edge(po1, crop_select)    # design_modules --> crop_select

# po3 depends on climate_setup and crop_select:

# po3 nodes: nutrient_calibrate, pest_control, staff_training
root.order.add_edge(climate_setup, po3)  # climate_setup --> nutrient_calibrate in po3
root.order.add_edge(crop_select, po3)    # crop_select --> pest_control & staff_training in po3

# po4 depends on staff_training (which is in po3), so po3 --> po4
root.order.add_edge(po3, po4)

# po5 depends on growth_monitor (in po4)
root.order.add_edge(po4, po5)

# po6 depends on compliance_audit and sustainability_check both in po5, so po5 --> po6
root.order.add_edge(po5, po6)

# po7 depends on supply_align (in po5) and yield_optimize (in po6)
root.order.add_edge(po5, po7)
root.order.add_edge(po6, po7)