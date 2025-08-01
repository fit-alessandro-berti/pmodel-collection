# Generated from: 7eff00f2-528d-4ec0-b807-0489f510f9b1.json
# Description: This process involves establishing an urban vertical farm within a repurposed warehouse. It includes site inspection, structural reinforcement, hydroponic system installation, environmental control configuration, crop selection, nutrient solution formulation, seedling propagation, automated lighting setup, pest monitoring, data analytics integration, staff training, harvest scheduling, packaging design, market testing, and waste recycling. The goal is to optimize space, reduce resource consumption, and deliver fresh produce efficiently to urban consumers while maintaining sustainability and scalability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteInspect = Transition(label='Site Inspect')
StructureCheck = Transition(label='Structure Check')
HydroponicsInstall = Transition(label='Hydroponics Install')
EnvControl = Transition(label='Env Control')
CropSelect = Transition(label='Crop Select')
NutrientMix = Transition(label='Nutrient Mix')
SeedlingGrow = Transition(label='Seedling Grow')
LightSetup = Transition(label='Light Setup')
PestMonitor = Transition(label='Pest Monitor')
DataIntegrate = Transition(label='Data Integrate')
StaffTrain = Transition(label='Staff Train')
HarvestPlan = Transition(label='Harvest Plan')
PackDesign = Transition(label='Pack Design')
MarketTest = Transition(label='Market Test')
WasteRecycle = Transition(label='Waste Recycle')

# Construct partial orders reflecting logical dependencies:

# Initial site preparation and checks
prep = StrictPartialOrder(nodes=[SiteInspect, StructureCheck])
prep.order.add_edge(SiteInspect, StructureCheck)

# Hydroponics install depends on structural check
install = StrictPartialOrder(nodes=[HydroponicsInstall, EnvControl])
install.order.add_edge(HydroponicsInstall, EnvControl)

# Crop related preparation in partial order:
crop_prep = StrictPartialOrder(nodes=[CropSelect, NutrientMix, SeedlingGrow])
crop_prep.order.add_edge(CropSelect, NutrientMix)
crop_prep.order.add_edge(NutrientMix, SeedlingGrow)

# Setup activities: lighting and pest monitoring concurrent (no order)
setup = StrictPartialOrder(nodes=[LightSetup, PestMonitor])

# Data integrate and staff training concurrent after setup
post_setup = StrictPartialOrder(nodes=[DataIntegrate, StaffTrain])

# Harvest planning depends on crop prep and setup finished
harvest = HarvestPlan

# Packaging and market testing can be done concurrently after harvest plan
pack_market = StrictPartialOrder(nodes=[PackDesign, MarketTest])

# Waste recycling can run concurrently with pack/market
waste = WasteRecycle

# Compose main partial order
nodes_main = [prep, install, crop_prep, setup, post_setup, harvest, pack_market, waste]
root = StrictPartialOrder(nodes=nodes_main)

# Order edges between these groups representing overall flow
root.order.add_edge(prep, install)          # After structure check, install
root.order.add_edge(install, crop_prep)     # After hydroponics/env control, crop prep
root.order.add_edge(crop_prep, setup)       # After crop prep, setup lighting and pest monitor
root.order.add_edge(setup, post_setup)      # After setup, data and staff training
root.order.add_edge(post_setup, harvest)    # After data/staff, harvest planning
root.order.add_edge(harvest, pack_market)   # After harvest plan, packaging and marketing
# Waste recycling can start after install (or run concurrently after prep/install)
root.order.add_edge(install, waste)