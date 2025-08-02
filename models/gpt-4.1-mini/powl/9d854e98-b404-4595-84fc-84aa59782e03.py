# Generated from: 9d854e98-b404-4595-84fc-84aa59782e03.json
# Description: This process outlines the establishment of an urban rooftop farming system on a commercial building. It involves initial site assessment considering structural load and sunlight exposure, followed by designing modular planting units and integrating smart irrigation technology. The process includes sourcing sustainable materials, obtaining necessary permits, and conducting soil testing to ensure optimal conditions. Installation requires coordinating logistics for equipment delivery, assembling hydroponic systems, and setting up environmental sensors. Post-installation activities focus on training staff for maintenance, implementing pest control strategies, and establishing a harvesting and distribution schedule to local markets. Continuous monitoring and reporting ensure system efficiency and crop yield optimization while maintaining compliance with city regulations and sustainability standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
site_assessment = Transition(label="Site Assessment")
load_testing = Transition(label="Load Testing")
sunlight_survey = Transition(label="Sunlight Survey")
design_modules = Transition(label="Design Modules")
source_materials = Transition(label="Source Materials")
permit_application = Transition(label="Permit Application")
soil_testing = Transition(label="Soil Testing")
equipment_delivery = Transition(label="Equipment Delivery")
system_assembly = Transition(label="System Assembly")
sensor_setup = Transition(label="Sensor Setup")
staff_training = Transition(label="Staff Training")
pest_control = Transition(label="Pest Control")
harvest_planning = Transition(label="Harvest Planning")
market_distribution = Transition(label="Market Distribution")
performance_review = Transition(label="Performance Review")

# Site assessment partial order: "Site Assessment" --> "Load Testing", "Sunlight Survey"
site_assessment_po = StrictPartialOrder(
    nodes=[site_assessment, load_testing, sunlight_survey]
)
site_assessment_po.order.add_edge(site_assessment, load_testing)
site_assessment_po.order.add_edge(site_assessment, sunlight_survey)

# Design modules depends on site assessment phase
design_po = StrictPartialOrder(
    nodes=[site_assessment_po, design_modules]
)
design_po.order.add_edge(site_assessment_po, design_modules)

# Material, permit, and soil testing can happen in parallel after design
materials_permit_soil_po = StrictPartialOrder(
    nodes=[source_materials, permit_application, soil_testing]
)
# no order edges: concurrently done

# Installation phase partial order: equipment delivery --> system assembly --> sensor setup
installation_po = StrictPartialOrder(
    nodes=[equipment_delivery, system_assembly, sensor_setup]
)
installation_po.order.add_edge(equipment_delivery, system_assembly)
installation_po.order.add_edge(system_assembly, sensor_setup)

# Post installation: staff training --> pest control --> harvest planning --> market distribution
post_install_po = StrictPartialOrder(
    nodes=[staff_training, pest_control, harvest_planning, market_distribution]
)
post_install_po.order.add_edge(staff_training, pest_control)
post_install_po.order.add_edge(pest_control, harvest_planning)
post_install_po.order.add_edge(harvest_planning, market_distribution)

# Continuous monitoring and reporting as performance review, runs after post installation
# We model it as occurring after market_distribution
final_po = StrictPartialOrder(
    nodes=[post_install_po, performance_review]
)
final_po.order.add_edge(post_install_po, performance_review)

# Build overall process partial order connecting phases:
# design_po --> materials_permit_soil_po --> installation_po --> final_po
root = StrictPartialOrder(
    nodes=[design_po, materials_permit_soil_po, installation_po, final_po]
)
root.order.add_edge(design_po, materials_permit_soil_po)
root.order.add_edge(materials_permit_soil_po, installation_po)
root.order.add_edge(installation_po, final_po)