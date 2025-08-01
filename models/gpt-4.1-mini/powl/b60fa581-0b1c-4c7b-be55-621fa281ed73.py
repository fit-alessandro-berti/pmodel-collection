# Generated from: b60fa581-0b1c-4c7b-be55-621fa281ed73.json
# Description: This process outlines the setup of an urban vertical farming system within a repurposed industrial building. It involves site assessment, structural modifications, installation of hydroponic systems, integration of IoT sensors, and optimization of environmental controls. The process also includes staff training on automated nutrient delivery, pest management without chemicals, and continuous data monitoring to maximize crop yield and sustainability in an urban environment. Coordination with local authorities for zoning compliance and energy sourcing from renewable providers is essential to ensure regulatory adherence and minimize carbon footprint. The final phases focus on pilot crop cultivation, harvesting workflows, and market distribution planning tailored for urban consumers seeking fresh, locally grown produce.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define individual activities as Transitions
site_assess = Transition(label='Site Assess')
structural_mod = Transition(label='Structural Mod')
hydroponic_fit = Transition(label='Hydroponic Fit')
iot_setup = Transition(label='IoT Setup')
env_control = Transition(label='Env Control')
nutrient_plan = Transition(label='Nutrient Plan')
pest_monitor = Transition(label='Pest Monitor')
staff_train = Transition(label='Staff Train')
energy_audit = Transition(label='Energy Audit')
compliance_check = Transition(label='Compliance Check')
crop_pilot = Transition(label='Crop Pilot')
harvest_prep = Transition(label='Harvest Prep')
data_review = Transition(label='Data Review')
market_plan = Transition(label='Market Plan')
waste_manage = Transition(label='Waste Manage')
distribution = Transition(label='Distribution')

# Step 1: Preparation and structural setup
prep_po = StrictPartialOrder(nodes=[site_assess, structural_mod])
prep_po.order.add_edge(site_assess, structural_mod)

# Step 2: Installation of hydroponic and IoT systems (concurrent)
install_po = StrictPartialOrder(nodes=[hydroponic_fit, iot_setup])
# concurrent, no order edges

# Step 3: Environmental control preparation after installations
env_po = StrictPartialOrder(nodes=[env_control])
# will be ordered after install_po, so no internal edges

# Step 4: Staff training branch (three related activities concurrent)
staff_train_po = StrictPartialOrder(nodes=[nutrient_plan, pest_monitor, staff_train])
# concurrent among these three

# Step 5: Energy and compliance audits (can be concurrent)
audit_po = StrictPartialOrder(nodes=[energy_audit, compliance_check])
# concurrent

# Step 6: Pilot cultivation and harvest preparation
pilot_harvest_po = StrictPartialOrder(nodes=[crop_pilot, harvest_prep])
pilot_harvest_po.order.add_edge(crop_pilot, harvest_prep)

# Step 7: Data review and market planning, waste management and distribution
final_po = StrictPartialOrder(nodes=[data_review, market_plan, waste_manage, distribution])
# Define order: data_review and market_plan concurrent,
# waste_manage and distribution concurrent,
# but market_plan must precede distribution (planning then distribution)
final_po.order.add_edge(market_plan, distribution)

# Construct overall PO with partial order among these phases reflecting dependencies:
# prep_po --> install_po --> env_po --> staff_train_po and audit_po (concurrent)
# then pilot_harvest_po --> final_po

# So root nodes:
# root_nodes = [prep_po, install_po, env_control, staff_train_po, audit_po, pilot_harvest_po, final_po]

root = StrictPartialOrder(nodes=[prep_po, install_po, env_control, staff_train_po, audit_po, pilot_harvest_po, final_po])

# Add the inter-phase edges representing the process flow:
root.order.add_edge(prep_po, install_po)            # preparation before installation
root.order.add_edge(install_po, env_control)        # installation before env control
root.order.add_edge(env_control, staff_train_po)    # env control before staff training
root.order.add_edge(env_control, audit_po)          # env control before audits (concurrent branches)
root.order.add_edge(staff_train_po, pilot_harvest_po) # staff training before pilot & harvest
root.order.add_edge(audit_po, pilot_harvest_po)     # audits also before pilot & harvest
root.order.add_edge(pilot_harvest_po, final_po)     # pilot & harvest before final steps