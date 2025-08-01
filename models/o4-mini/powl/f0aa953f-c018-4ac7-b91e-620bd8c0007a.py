# Generated from: f0aa953f-c018-4ac7-b91e-620bd8c0007a.json
# Description: This process involves establishing an urban vertical farm within a repurposed high-rise building. It includes site analysis, modular system design, environmental control calibration, nutrient solution formulation, seedling preparation, and automated monitoring integration. The setup ensures sustainable crop production through resource recycling, energy optimization, and waste management while complying with urban agricultural regulations. The process culminates in operational validation and community engagement to promote local food sourcing.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
system_assembly = Transition(label='System Assembly')
climate_setup = Transition(label='Climate Setup')
light_calibration = Transition(label='Light Calibration')
seed_selection = Transition(label='Seed Selection')
seedling_prep = Transition(label='Seedling Prep')
nutrient_mix = Transition(label='Nutrient Mix')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
data_integration = Transition(label='Data Integration')
waste_routing = Transition(label='Waste Routing')
energy_audit = Transition(label='Energy Audit')
regulation_check = Transition(label='Regulation Check')
operational_test = Transition(label='Operational Test')
community_outreach = Transition(label='Community Outreach')

root = StrictPartialOrder(nodes=[
    site_survey, design_layout, system_assembly, climate_setup, light_calibration,
    seed_selection, seedling_prep, nutrient_mix, irrigation_setup, sensor_install,
    data_integration, waste_routing, energy_audit, regulation_check,
    operational_test, community_outreach
])

root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, system_assembly)
root.order.add_edge(system_assembly, climate_setup)
root.order.add_edge(climate_setup, light_calibration)
root.order.add_edge(light_calibration, seed_selection)
root.order.add_edge(seed_selection, seedling_prep)
root.order.add_edge(seedling_prep, nutrient_mix)
root.order.add_edge(nutrient_mix, irrigation_setup)
root.order.add_edge(irrigation_setup, sensor_install)
root.order.add_edge(sensor_install, data_integration)

root.order.add_edge(data_integration, waste_routing)
root.order.add_edge(data_integration, energy_audit)

root.order.add_edge(waste_routing, regulation_check)
root.order.add_edge(energy_audit, regulation_check)

root.order.add_edge(regulation_check, operational_test)
root.order.add_edge(operational_test, community_outreach)