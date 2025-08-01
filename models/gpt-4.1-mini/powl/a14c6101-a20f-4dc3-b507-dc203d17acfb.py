# Generated from: a14c6101-a20f-4dc3-b507-dc203d17acfb.json
# Description: This process involves the meticulous restoration of vintage mechanical watches, combining expertise in horology, materials science, and historical research. The workflow begins with an initial inspection to assess the watch’s condition and authenticity, followed by disassembly where each component is carefully cataloged. Cleaning involves ultrasonic baths and gentle chemical treatments tailored to delicate parts. Repair focuses on fabricating or sourcing rare replacement components, including gears and springs, often requiring custom machining or handcrafting. Reassembly demands precision alignment and lubrication using specialized oils. The process includes timing calibration to ensure accuracy, aesthetic restoration of dials and hands, and final quality control under various conditions. Documentation of provenance and restoration steps is maintained for collectors. This atypical process blends technical skill with conservation ethics, ensuring the watch's functional revival while preserving its historical integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
InitialInspect = Transition(label='Initial Inspect')
ComponentCatalog = Transition(label='Component Catalog')
DisassembleParts = Transition(label='Disassemble Parts')
UltrasonicClean = Transition(label='Ultrasonic Clean')
ChemicalTreat = Transition(label='Chemical Treat')
FabricateGears = Transition(label='Fabricate Gears')
SourceSprings = Transition(label='Source Springs')
HandcraftParts = Transition(label='Handcraft Parts')
AlignMechanism = Transition(label='Align Mechanism')
ApplyLubricate = Transition(label='Apply Lubricate')
CalibrateTiming = Transition(label='Calibrate Timing')
RestoreDial = Transition(label='Restore Dial')
RefinishHands = Transition(label='Refinish Hands')
QualityControl = Transition(label='Quality Control')
DocumentHistory = Transition(label='Document History')
FinalAssembly = Transition(label='Final Assembly')
TestFunction = Transition(label='Test Function')

# Choice among repair sub-activities: FabricateGears, SourceSprings, HandcraftParts
RepairChoice = OperatorPOWL(operator=Operator.XOR, children=[FabricateGears, SourceSprings, HandcraftParts])

# Cleaning is two concurrent activities
CleaningPO = StrictPartialOrder(nodes=[UltrasonicClean, ChemicalTreat])
# No order between them (concurrent)

# Repair loop: After executing RepairChoice, choose to exit or do RepairChoice again
RepairLoop = OperatorPOWL(operator=Operator.LOOP, children=[RepairChoice, RepairChoice])

# Assembly includes final alignment and lubrication
AssemblyPO = StrictPartialOrder(nodes=[AlignMechanism, ApplyLubricate, FinalAssembly])
AssemblyPO.order.add_edge(AlignMechanism, ApplyLubricate)
AssemblyPO.order.add_edge(ApplyLubricate, FinalAssembly)

# Restoration order: RestoreDial --> RefinishHands
RestorationPO = StrictPartialOrder(nodes=[RestoreDial, RefinishHands])
RestorationPO.order.add_edge(RestoreDial, RefinishHands)

# Define main partial order nodes and control flow
# Process flow:
# InitialInspect --> ComponentCatalog --> DisassembleParts --> CleaningPO --> RepairLoop --> AssemblyPO 
# --> CalibrateTiming --> RestorationPO --> QualityControl --> DocumentHistory --> TestFunction

root = StrictPartialOrder(
    nodes=[
        InitialInspect,
        ComponentCatalog,
        DisassembleParts,
        CleaningPO,
        RepairLoop,
        AssemblyPO,
        CalibrateTiming,
        RestorationPO,
        QualityControl,
        DocumentHistory,
        TestFunction
    ]
)

# Define order edges between activities / submodels
root.order.add_edge(InitialInspect, ComponentCatalog)
root.order.add_edge(ComponentCatalog, DisassembleParts)
root.order.add_edge(DisassembleParts, CleaningPO)
root.order.add_edge(CleaningPO, RepairLoop)
root.order.add_edge(RepairLoop, AssemblyPO)
root.order.add_edge(AssemblyPO, CalibrateTiming)
root.order.add_edge(CalibrateTiming, RestorationPO)
root.order.add_edge(RestorationPO, QualityControl)
root.order.add_edge(QualityControl, DocumentHistory)
root.order.add_edge(DocumentHistory, TestFunction)