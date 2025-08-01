# Generated from: 368ebdea-068d-43e5-b924-dace3af96a00.json
# Description: This process outlines the complex coordination required to establish a sustainable urban rooftop farm in a dense city environment. It involves initial site assessment, securing permits, designing modular planting systems, sourcing eco-friendly materials, installing irrigation and solar power, recruiting local volunteers, conducting soil and air quality tests, and establishing supply chains for seeds and organic fertilizers. After installation, the farm undergoes regular maintenance, pest monitoring, and community engagement activities to ensure productivity and environmental compliance. The process concludes with periodic harvest cycles and distribution logistics to local markets and restaurants, emphasizing sustainability and social impact throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey       = Transition(label='Site Survey')
permit_filing     = Transition(label='Permit Filing')
design_layout     = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
modular_assembly  = Transition(label='Modular Assembly')
irrigation_setup  = Transition(label='Irrigation Setup')
solar_install     = Transition(label='Solar Install')
volunteer_recruit = Transition(label='Volunteer Recruit')
soil_testing      = Transition(label='Soil Testing')
air_sampling      = Transition(label='Air Sampling')
seed_selection    = Transition(label='Seed Selection')
fertilizer_order  = Transition(label='Fertilizer Order')
maintenance_check     = Transition(label='Maintenance Check')
pest_monitoring       = Transition(label='Pest Monitoring')
community_outreach    = Transition(label='Community Outreach')
harvest_cycle         = Transition(label='Harvest Cycle')
distribution_plan     = Transition(label='Distribution Plan')

# Silent transition for loop exits
skip = SilentTransition()

# Build the maintenance loop: Maintenance Check → Pest Monitoring → Community Outreach
maintenance_body = StrictPartialOrder(nodes=[maintenance_check, pest_monitoring, community_outreach])
maintenance_body.order.add_edge(maintenance_check, pest_monitoring)
maintenance_body.order.add_edge(pest_monitoring, community_outreach)
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_body, skip])

# Build the harvest/distribution loop: Harvest Cycle → Distribution Plan
harvest_body = StrictPartialOrder(nodes=[harvest_cycle, distribution_plan])
harvest_body.order.add_edge(harvest_cycle, distribution_plan)
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_body, skip])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_filing,
    design_layout,
    material_sourcing,
    modular_assembly,
    irrigation_setup,
    solar_install,
    volunteer_recruit,
    soil_testing,
    air_sampling,
    seed_selection,
    fertilizer_order,
    maintenance_loop,
    harvest_loop
])

# Initial sequence: Site Survey → Permit Filing
root.order.add_edge(site_survey, permit_filing)

# After permit: Design and Material Sourcing in parallel
root.order.add_edge(permit_filing, design_layout)
root.order.add_edge(permit_filing, material_sourcing)

# After design & materials: Modular Assembly
root.order.add_edge(design_layout, modular_assembly)
root.order.add_edge(material_sourcing, modular_assembly)

# After assembly: Installation & recruiting & testing & supply tasks in parallel
post_assembly = [
    irrigation_setup,
    solar_install,
    volunteer_recruit,
    soil_testing,
    air_sampling,
    seed_selection,
    fertilizer_order
]
for t in post_assembly:
    root.order.add_edge(modular_assembly, t)

# After all setup tasks, enter the maintenance loop
for t in post_assembly:
    root.order.add_edge(t, maintenance_loop)

# After maintenance completes, enter the harvest/distribution loop
root.order.add_edge(maintenance_loop, harvest_loop)