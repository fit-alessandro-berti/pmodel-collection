# Generated from: 7b4bc1bc-c193-4508-b9bc-447481d9c69f.json
# Description: This process outlines the complex operational cycle of an urban vertical farm that integrates hydroponics, automated environmental controls, and real-time data analytics to maximize crop yield and sustainability. It begins with seed selection and preparation, followed by nutrient solution formulation and automated planting in multi-layered growth trays. Continuous monitoring of microclimate conditions such as humidity, temperature, and light intensity is conducted using IoT sensors. Data is analyzed to adjust parameters dynamically via AI-driven controls. Pollination is simulated mechanically or via controlled introduction of pollinator insects. Harvesting robots selectively pick mature produce, which is then quality-checked and sorted by automated vision systems. Post-harvest processing includes washing, packaging in biodegradable materials, and cold storage. The process concludes with logistics coordination for local distribution, waste recycling, and system maintenance to ensure sustainability and minimize downtime.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SeedPrep = Transition(label='Seed Prep')
NutrientMix = Transition(label='Nutrient Mix')
AutomatedPlant = Transition(label='Automated Plant')
MicroclimateCheck = Transition(label='Microclimate Check')
DataCapture = Transition(label='Data Capture')
AIAdjustments = Transition(label='AI Adjustments')
PollinationStep = Transition(label='Pollination Step')
HarvestRobots = Transition(label='Harvest Robots')
QualityScan = Transition(label='Quality Scan')
ProduceSort = Transition(label='Produce Sort')
WashCycle = Transition(label='Wash Cycle')
EcoPackaging = Transition(label='Eco Packaging')
ColdStorage = Transition(label='Cold Storage')
LocalDispatch = Transition(label='Local Dispatch')
SystemCleanup = Transition(label='System Cleanup')
WasteRecycle = Transition(label='Waste Recycle')

# Build Microclimate monitoring and adjustment loop:
# Loop: 
#   A = MicroclimateCheck followed by DataCapture and AIAdjustments
#   B = silent transition (exit)
microclimate_check = StrictPartialOrder(nodes=[MicroclimateCheck, DataCapture, AIAdjustments])
microclimate_check.order.add_edge(MicroclimateCheck, DataCapture)
microclimate_check.order.add_edge(DataCapture, AIAdjustments)

skip = SilentTransition()

microclimate_loop = OperatorPOWL(operator=Operator.LOOP, children=[microclimate_check, skip])

# Pollination choice mechanical or pollinator insects
# PollinationStep as described, is one activity; 
# but description says "simulated mechanically or via insects"
# model that choice with two silent branches under XOR:
# For simplicity, two silent transitions represent each method, label-less
mechanical = SilentTransition()
insects = SilentTransition()
pollination_choice = OperatorPOWL(operator=Operator.XOR, children=[mechanical, insects])

# Connect pollination_choice to PollinationStep by ordering pollination_choice --> PollinationStep

pollination_PO = StrictPartialOrder(nodes=[pollination_choice, PollinationStep])
pollination_PO.order.add_edge(pollination_choice, PollinationStep)

# Harvesting sequence:
# Harvest Robots --> Quality Scan --> Produce Sort
harvest_PO = StrictPartialOrder(nodes=[HarvestRobots, QualityScan, ProduceSort])
harvest_PO.order.add_edge(HarvestRobots, QualityScan)
harvest_PO.order.add_edge(QualityScan, ProduceSort)

# Post-harvest processing sequence:
# Wash Cycle --> Eco Packaging --> Cold Storage
postharvest_PO = StrictPartialOrder(nodes=[WashCycle, EcoPackaging, ColdStorage])
postharvest_PO.order.add_edge(WashCycle, EcoPackaging)
postharvest_PO.order.add_edge(EcoPackaging, ColdStorage)

# Final logistics and cleanup partial order:
# Local Dispatch --> Waste Recycle and System Cleanup concurrency (no order)
logistics_cleanup_PO = StrictPartialOrder(nodes=[LocalDispatch, WasteRecycle, SystemCleanup])
logistics_cleanup_PO.order.add_edge(LocalDispatch, WasteRecycle)
logistics_cleanup_PO.order.add_edge(LocalDispatch, SystemCleanup)

# Initial partial order: Seed Prep --> Nutrient Mix --> Automated Plant
initial_PO = StrictPartialOrder(nodes=[SeedPrep, NutrientMix, AutomatedPlant])
initial_PO.order.add_edge(SeedPrep, NutrientMix)
initial_PO.order.add_edge(NutrientMix, AutomatedPlant)

# Connect the pieces in order:
# initial_PO --> microclimate_loop --> pollination_PO --> harvest_PO --> postharvest_PO --> logistics_cleanup_PO
root = StrictPartialOrder(
    nodes=[
        initial_PO,
        microclimate_loop,
        pollination_PO,
        harvest_PO,
        postharvest_PO,
        logistics_cleanup_PO
    ]
)
root.order.add_edge(initial_PO, microclimate_loop)
root.order.add_edge(microclimate_loop, pollination_PO)
root.order.add_edge(pollination_PO, harvest_PO)
root.order.add_edge(harvest_PO, postharvest_PO)
root.order.add_edge(postharvest_PO, logistics_cleanup_PO)