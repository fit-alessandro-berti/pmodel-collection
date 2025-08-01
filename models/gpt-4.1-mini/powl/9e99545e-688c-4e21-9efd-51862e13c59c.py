# Generated from: 9e99545e-688c-4e21-9efd-51862e13c59c.json
# Description: This process outlines the complex establishment of an urban vertical farm within a repurposed industrial building. It involves site assessment, modular system design, climate control integration, hydroponic setup, nutrient cycling optimization, and automated monitoring. The process also includes workforce training on advanced agricultural technology, securing sustainability certifications, and establishing direct-to-consumer supply chains. Coordination with local authorities for zoning compliance and environmental impact assessments is critical. Post-installation, ongoing data analysis and iterative system tuning ensure optimal crop yields and minimal resource consumption, fostering a resilient urban food production ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
site_assess = Transition(label='Site Assess')
design_modules = Transition(label='Design Modules')
install_hydroponics = Transition(label='Install Hydroponics')
set_climate = Transition(label='Set Climate')
integrate_sensors = Transition(label='Integrate Sensors')
calibrate_lighting = Transition(label='Calibrate Lighting')
configure_nutrients = Transition(label='Configure Nutrients')
train_staff = Transition(label='Train Staff')
certify_green = Transition(label='Certify Green')
test_irrigation = Transition(label='Test Irrigation')
connect_power = Transition(label='Connect Power')
analyze_data = Transition(label='Analyze Data')
adjust_parameters = Transition(label='Adjust Parameters')
launch_marketing = Transition(label='Launch Marketing')
review_compliance = Transition(label='Review Compliance')
schedule_maintenance = Transition(label='Schedule Maintenance')
manage_waste = Transition(label='Manage Waste')

# Setup nutrient cycling optimization loop:
# Loop: execute Configure Nutrients,
#       then either exit or execute Test Irrigation then Configure Nutrients again.
nutrient_loop = OperatorPOWL(operator=Operator.LOOP, children=[configure_nutrients, test_irrigation])

# Climate control integration partial order:
# Set Climate --> Integrate Sensors --> Calibrate Lighting
climate_po = StrictPartialOrder(nodes=[set_climate, integrate_sensors, calibrate_lighting])
climate_po.order.add_edge(set_climate, integrate_sensors)
climate_po.order.add_edge(integrate_sensors, calibrate_lighting)

# Hydroponic system setup partial order with power connection:
# Install Hydroponics --> Connect Power
hydro_po = StrictPartialOrder(nodes=[install_hydroponics, connect_power])
hydro_po.order.add_edge(install_hydroponics, connect_power)

# Workforce training and certification partial order:
# Train Staff --> Certify Green
training_cert_po = StrictPartialOrder(nodes=[train_staff, certify_green])
training_cert_po.order.add_edge(train_staff, certify_green)

# Coordination and compliance partial order:
# Review Compliance --> Schedule Maintenance
compliance_po = StrictPartialOrder(nodes=[review_compliance, schedule_maintenance])
compliance_po.order.add_edge(review_compliance, schedule_maintenance)

# Post-installation analysis partial order:
# Analyze Data --> Adjust Parameters (assumed sequential)
analysis_po = StrictPartialOrder(nodes=[analyze_data, adjust_parameters])
analysis_po.order.add_edge(analyze_data, adjust_parameters)

# Marketing launch and waste management concurrent
marketing_waste_po = StrictPartialOrder(nodes=[launch_marketing, manage_waste])

# Assemble all installation activities partial order with dependencies:

# Site Assess must happen before Design Modules
# Design Modules happens before parallel setup of hydroponics, climate, nutrient_loop
install_po = StrictPartialOrder(nodes=[
    site_assess, design_modules, hydro_po, climate_po, nutrient_loop,
    training_cert_po, compliance_po, analysis_po, marketing_waste_po
])

# Define dependencies (edges):
# site_assess --> design_modules
install_po.order.add_edge(site_assess, design_modules)

# design_modules --> hydro_po (Install Hydroponics)
install_po.order.add_edge(design_modules, hydro_po)

# design_modules --> climate_po (Set Climate)
install_po.order.add_edge(design_modules, climate_po)

# design_modules --> nutrient_loop (Configure Nutrients loop)
install_po.order.add_edge(design_modules, nutrient_loop)

# hydro_po --> training_cert_po (after installation, train staff etc.)
install_po.order.add_edge(hydro_po, training_cert_po)

# climate_po --> training_cert_po (same as above)
install_po.order.add_edge(climate_po, training_cert_po)

# nutrient_loop --> training_cert_po (same as above)
install_po.order.add_edge(nutrient_loop, training_cert_po)

# training_cert_po --> compliance_po
install_po.order.add_edge(training_cert_po, compliance_po)

# compliance_po --> analysis_po
install_po.order.add_edge(compliance_po, analysis_po)

# analysis_po --> marketing_waste_po
install_po.order.add_edge(analysis_po, marketing_waste_po)

# This structure respects the dependencies described:
# Site Assess -> Design Modules
# Design Modules -> Install Hydroponics / Set Climate / Configure Nutrients (nutrient loop)
# After these three are done, train staff and certify green
# Then review compliance and schedule maintenance
# Then analyze data and adjust parameters
# Last, launch marketing and manage waste concurrently.

root = install_po