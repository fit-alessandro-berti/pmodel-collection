# Generated from: 9d854e98-b404-4595-84fc-84aa59782e03.json
# Description: This process outlines the establishment of an urban rooftop farming system on a commercial building. It involves initial site assessment considering structural load and sunlight exposure, followed by designing modular planting units and integrating smart irrigation technology. The process includes sourcing sustainable materials, obtaining necessary permits, and conducting soil testing to ensure optimal conditions. Installation requires coordinating logistics for equipment delivery, assembling hydroponic systems, and setting up environmental sensors. Post-installation activities focus on training staff for maintenance, implementing pest control strategies, and establishing a harvesting and distribution schedule to local markets. Continuous monitoring and reporting ensure system efficiency and crop yield optimization while maintaining compliance with city regulations and sustainability standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# define activities
site_assessment    = Transition(label='Site Assessment')
load_testing       = Transition(label='Load Testing')
sunlight_survey    = Transition(label='Sunlight Survey')
design_modules     = Transition(label='Design Modules')
source_materials   = Transition(label='Source Materials')
permit_application = Transition(label='Permit Application')
soil_testing       = Transition(label='Soil Testing')
equipment_delivery = Transition(label='Equipment Delivery')
system_assembly    = Transition(label='System Assembly')
sensor_setup       = Transition(label='Sensor Setup')
staff_training     = Transition(label='Staff Training')
pest_control       = Transition(label='Pest Control')
harvest_planning   = Transition(label='Harvest Planning')
market_distribution= Transition(label='Market Distribution')
performance_review = Transition(label='Performance Review')

# build the partial order
root = StrictPartialOrder(nodes=[
    site_assessment, load_testing, sunlight_survey, design_modules,
    source_materials, permit_application, soil_testing,
    equipment_delivery, system_assembly, sensor_setup,
    staff_training, pest_control, harvest_planning,
    market_distribution, performance_review
])

# initial assessment flows
root.order.add_edge(site_assessment, load_testing)
root.order.add_edge(site_assessment, sunlight_survey)
# after assessments, design
root.order.add_edge(load_testing, design_modules)
root.order.add_edge(sunlight_survey, design_modules)
# design leads to sourcing, permitting, testing
root.order.add_edge(design_modules, source_materials)
root.order.add_edge(design_modules, permit_application)
root.order.add_edge(design_modules, soil_testing)
# prepare for installation
root.order.add_edge(source_materials, equipment_delivery)
root.order.add_edge(permit_application, system_assembly)
root.order.add_edge(equipment_delivery, system_assembly)
# installation sequence
root.order.add_edge(system_assembly, sensor_setup)
# post-installation activities
root.order.add_edge(sensor_setup, staff_training)
root.order.add_edge(sensor_setup, pest_control)
root.order.add_edge(sensor_setup, harvest_planning)
# harvesting to distribution
root.order.add_edge(harvest_planning, market_distribution)
# final review
root.order.add_edge(staff_training, performance_review)
root.order.add_edge(pest_control, performance_review)
root.order.add_edge(market_distribution, performance_review)