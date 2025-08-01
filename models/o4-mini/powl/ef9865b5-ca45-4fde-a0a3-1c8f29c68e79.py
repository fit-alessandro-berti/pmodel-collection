# Generated from: ef9865b5-ca45-4fde-a0a3-1c8f29c68e79.json
# Description: This process outlines the comprehensive steps involved in establishing an urban rooftop farm on a commercial building. It includes site assessment for structural integrity and sunlight exposure, obtaining necessary permits, designing modular planting systems, sourcing sustainable materials, installing irrigation and sensor networks, recruiting skilled urban farmers, conducting soil-less planting trials, implementing pest management strategies, and setting up a digital monitoring platform. The process concludes with initial harvest planning and community engagement activities aimed at promoting urban agriculture benefits and local food sourcing awareness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
permit_review = Transition(label='Permit Review')
structural_test = Transition(label='Structural Test')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
system_calibrate = Transition(label='System Calibrate')
soilless_prep = Transition(label='Soilless Prep')
recruit_farmers = Transition(label='Recruit Farmers')
trial_planting = Transition(label='Trial Planting')
pest_control = Transition(label='Pest Control')
data_monitor = Transition(label='Data Monitor')
harvest_plan = Transition(label='Harvest Plan')
community_outreach = Transition(label='Community Outreach')

# loop: perform trial planting, then optionally run pest control and repeat trial planting
loop_trials = OperatorPOWL(operator=Operator.LOOP, children=[trial_planting, pest_control])

root = StrictPartialOrder(nodes=[
    site_survey,
    permit_review,
    structural_test,
    design_layout,
    material_sourcing,
    irrigation_setup,
    sensor_install,
    system_calibrate,
    soilless_prep,
    recruit_farmers,
    loop_trials,
    data_monitor,
    harvest_plan,
    community_outreach
])

# define partial order relations
root.order.add_edge(site_survey, permit_review)
root.order.add_edge(permit_review, structural_test)
root.order.add_edge(permit_review, design_layout)
root.order.add_edge(structural_test, material_sourcing)
root.order.add_edge(design_layout, material_sourcing)
root.order.add_edge(material_sourcing, irrigation_setup)
root.order.add_edge(material_sourcing, sensor_install)
root.order.add_edge(irrigation_setup, system_calibrate)
root.order.add_edge(sensor_install, system_calibrate)
root.order.add_edge(system_calibrate, soilless_prep)
root.order.add_edge(system_calibrate, recruit_farmers)
root.order.add_edge(soilless_prep, loop_trials)
root.order.add_edge(recruit_farmers, loop_trials)
root.order.add_edge(loop_trials, data_monitor)
root.order.add_edge(data_monitor, harvest_plan)
root.order.add_edge(data_monitor, community_outreach)