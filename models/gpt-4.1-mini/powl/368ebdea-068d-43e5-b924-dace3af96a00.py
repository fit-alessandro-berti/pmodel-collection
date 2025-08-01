# Generated from: 368ebdea-068d-43e5-b924-dace3af96a00.json
# Description: This process outlines the complex coordination required to establish a sustainable urban rooftop farm in a dense city environment. It involves initial site assessment, securing permits, designing modular planting systems, sourcing eco-friendly materials, installing irrigation and solar power, recruiting local volunteers, conducting soil and air quality tests, and establishing supply chains for seeds and organic fertilizers. After installation, the farm undergoes regular maintenance, pest monitoring, and community engagement activities to ensure productivity and environmental compliance. The process concludes with periodic harvest cycles and distribution logistics to local markets and restaurants, emphasizing sustainability and social impact throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Survey = Transition('Site Survey')
Permit_Filing = Transition('Permit Filing')
Design_Layout = Transition('Design Layout')
Material_Sourcing = Transition('Material Sourcing')
Irrigation_Setup = Transition('Irrigation Setup')
Solar_Install = Transition('Solar Install')
Volunteer_Recruit = Transition('Volunteer Recruit')
Soil_Testing = Transition('Soil Testing')
Air_Sampling = Transition('Air Sampling')
Seed_Selection = Transition('Seed Selection')
Fertilizer_Order = Transition('Fertilizer Order')
Modular_Assembly = Transition('Modular Assembly')
Pest_Monitoring = Transition('Pest Monitoring')
Community_Outreach = Transition('Community Outreach')
Harvest_Cycle = Transition('Harvest Cycle')
Distribution_Plan = Transition('Distribution Plan')
Maintenance_Check = Transition('Maintenance Check')

# The process description's major stages:
# 1) Initial site assessment and permits
# 2) Design & sourcing materials
# 3) Installation & assembly
# 4) Testing (soil, air), seed and fertilizer supply chains
# 5) Recruitment of volunteers in parallel with installation & testing
# 6) After installation, maintenance, pest monitoring, community outreach looped
# 7) Periodic harvest cycles + distribution
#
# We'll model the loop for maintenance, pest monitoring, community outreach,
# then a partial order for harvest and distribution as final steps.

# Initial site assessment and permits (Site Survey -> Permit Filing)
init_assessment = StrictPartialOrder(nodes=[Site_Survey, Permit_Filing])
init_assessment.order.add_edge(Site_Survey, Permit_Filing)

# Design Layout follows Permit Filing
design_and_sourcing = StrictPartialOrder(nodes=[Design_Layout, Material_Sourcing])
# Material sourcing can happen in parallel or after design; to simplify: Design_Layout --> Material_Sourcing
design_and_sourcing.order.add_edge(Design_Layout, Material_Sourcing)

# Installation: Irrigation Setup, Solar Install, Modular Assembly
installation = StrictPartialOrder(nodes=[Irrigation_Setup, Solar_Install, Modular_Assembly])
# They are concurrent activities, but Modular Assembly depends on Material Sourcing,
# we will connect outside.

# Testing & supply chains: Soil Testing, Air Sampling, Seed Selection, Fertilizer Order
testing_and_supply = StrictPartialOrder(nodes=[Soil_Testing, Air_Sampling, Seed_Selection, Fertilizer_Order])
# No strict order among testing and supply activities: concurrent

# Volunteer Recruiting (can be done parallel to installation and testing)
volunteer = Volunteer_Recruit

# Build partial order for design phase to installation and volunteer recruiting
# Overall: Permit Filing --> Design Layout --> Material Sourcing --> Installation (all three concurrently)
# Volunteer Recruit concurrent with Installation and Testing
# Testing depends on Material Sourcing (sourcing materials needed for seed/fertilizer testing)

# Combine design -> material sourcing -> (installation || testing || volunteer)

post_permit = StrictPartialOrder(nodes=[design_and_sourcing, installation, testing_and_supply, volunteer])
post_permit.order.add_edge(design_and_sourcing, installation)
post_permit.order.add_edge(design_and_sourcing, testing_and_supply)
post_permit.order.add_edge(design_and_sourcing, volunteer)

# Testing and Volunteer are concurrent with installation (no order edges needed between installation and volunteer/testing)
# (volunteer and testing_and_supply and installation all start after design_and_sourcing)

# Installation requires Material Sourcing, which is included in design_and_sourcing.

# Complete structure up to installation and volunteers/testing:
phase1 = StrictPartialOrder(nodes=[init_assessment, post_permit])
phase1.order.add_edge(init_assessment, post_permit)

# The installation phase must precede the maintenance loop and harvest/distribution phases

# Define the maintenance loop:
# loop node * (A, B): run A, then either exit or run B then A again
# Here:
# A = StrictPartialOrder([Maintenance Check, Pest Monitoring, Community Outreach]) all concurrent
maint_activities = StrictPartialOrder(nodes=[Maintenance_Check, Pest_Monitoring, Community_Outreach])
# no order edges inside for concurrency

# B = silent transition (skip) because after each iteration can exit directly, no intermediate step
skip = SilentTransition()

maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maint_activities, skip])

# After maintenance loop, Harvest Cycle and Distribution Plan sequential (Harvest --> Distribution)
harvest_dist = StrictPartialOrder(nodes=[Harvest_Cycle, Distribution_Plan])
harvest_dist.order.add_edge(Harvest_Cycle, Distribution_Plan)

# Compose post installation: maintenance loop then harvest and distribution
post_installation = StrictPartialOrder(nodes=[maintenance_loop, harvest_dist])
post_installation.order.add_edge(maintenance_loop, harvest_dist)

# Compose full process:
# phase1 --> post_installation
root = StrictPartialOrder(nodes=[phase1, post_installation])
root.order.add_edge(phase1, post_installation)