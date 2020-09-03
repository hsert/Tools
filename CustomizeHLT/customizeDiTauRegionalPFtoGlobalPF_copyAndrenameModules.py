# Customisation function to convert the regional PF reconstruction to global one for the recommended ditau HLT
#, which is medium isolation with pt = 35 GeV..

# If you spot anything, please get in contact with
# hale.sert@cern.ch

# NOTE: This customisation function assumes that one of the lepton+tau HLT (e.g. mutau) has been already included in the dumped menu,
#       together with ditau HLT which uses regional PF reconstuction.
#       The purpose of including mutau HLT is that the function uses modules used in the global PF reconstuction of the tau leg of mutau HLT
#       to perform the conversion to global PF reconstuction from regional PF reconstruction.

import FWCore.ParameterSet.Config as cms

def customizeDiTauRegionalPFtoGlobalPF_menuwithMuTau(process):

    copy_existing_and_rename_current_module(process, "hltHpsPFTauProducerReg", "hltHpsPFTauProducer")
    copy_existing_and_rename_current_module(process, "hltParticleFlowReg", "hltParticleFlowForTaus")
    copy_existing_and_rename_current_module(process, "hltMergedTracksTauReg", "hltMergedTracks")
    copy_existing_and_rename_current_module(process, "hltMuonsReg", "hltMuons")
    copy_existing_and_rename_current_module(process, "hltMuonLinksReg", "hltMuonLinks")
    copy_existing_and_rename_current_module(process, "hltPFMuonMergingTauReg", "hltPFMuonMerging")
    copy_existing_and_rename_current_module(process, "hltPFTauPiZerosReg", "hltPFTauPiZeros")
    copy_existing_and_rename_current_module(process, "hltParticleFlowBlockReg", "hltParticleFlowBlockForTaus")
    copy_existing_and_rename_current_module(process, "hltTauPFJets08RegionReg", "hltTauPFJets08Region")
    copy_existing_and_rename_current_module(process, "hltHpsPFTauTrackReg", "hltHpsPFTauTrack")
    copy_existing_and_rename_current_module(process, "hltHpsSelectedPFTausTrackFindingReg", "hltHpsSelectedPFTausTrackFinding")
    copy_existing_and_rename_current_module(process, "hltLightPFTracksReg", "hltLightPFTracks")

    # the ones existing only in Regional version, so they need to be renamed directly..

    listPt35Modules =['hltHpsDoublePFTau35Reg',
                    'hltHpsDoublePFTau35TrackPt1Reg']

    listPt40Modules =['hltHpsDoublePFTau40Reg',
                    'hltHpsDoublePFTau40TrackPt1Reg']

    for att in (listPt35Modules + listPt40Modules):
        if hasattr(process, att):
            rename_module(process, att, att[:-3])

    listMediumIsolation =['hltHpsPFTauMediumAbsoluteChargedIsolationDiscriminatorReg',
                        'hltHpsPFTauMediumRelativeChargedIsolationDiscriminatorReg',
                        'hltHpsPFTauMediumAbsOrRelChargedIsolationDiscriminatorReg',
                        'hltHpsSelectedPFTausTrackPt1MediumChargedIsolationReg',
                        'hltHpsL1JetsHLTDoublePFTauTrackPt1MediumChargedIsolationMatchReg']

    listMediumIsoPt35 =['hltPreDoubleMediumChargedIsoPFTauHPS35Trk1eta2p1Reg',
                        'hltHpsDoublePFTau35TrackPt1MediumChargedIsolationReg',
                        'hltHpsDoublePFTau35TrackPt1MediumChargedIsolationL1HLTMatchedReg',
                        'hltHpsDoublePFTau35TrackPt1MediumChargedIsolationDz02Reg']

    listMediumIsoPt40 =['hltPreDoubleMediumChargedIsoPFTauHPS40Trk1eta2p1Reg',
                        'hltHpsDoublePFTau40TrackPt1MediumChargedIsolationReg',
                        'hltHpsDoublePFTau40TrackPt1MediumChargedIsolationL1HLTMatchedReg',
                        'hltHpsDoublePFTau40TrackPt1MediumChargedIsolationDz02Reg']

    listTightIsolation =['hltHpsPFTauTightAbsoluteChargedIsolationDiscriminatorReg',
                        'hltHpsPFTauTightRelativeChargedIsolationDiscriminatorReg',
                        'hltHpsPFTauTightAbsOrRelChargedIsolationDiscriminatorReg',
                        'hltHpsSelectedPFTausTrackPt1TightChargedIsolationReg',
                        'hltHpsL1JetsHLTDoublePFTauTrackPt1TightChargedIsolationMatchReg']

    listTightIsoPt35 =[ 'hltPreDoubleTightChargedIsoPFTauHPS35Trk1eta2p1Reg',
                        'hltHpsDoublePFTau35TrackPt1TightChargedIsolationReg',
                        'hltHpsDoublePFTau35TrackPt1TightChargedIsolationL1HLTMatchedReg',
                        'hltHpsDoublePFTau35TrackPt1TightChargedIsolationDz02Reg']

    listTightIsoPt40 =[ 'hltPreDoubleTightChargedIsoPFTauHPS40Trk1eta2p1Reg',
                        'hltHpsDoublePFTau40TrackPt1TightChargedIsolationReg',
                        'hltHpsDoublePFTau40TrackPt1TightChargedIsolationL1HLTMatchedReg',
                        'hltHpsDoublePFTau40TrackPt1TightChargedIsolationDz02Reg']


    for att in (listMediumIsolation + listMediumIsoPt35 +  listMediumIsoPt40 + listTightIsolation + listTightIsoPt35 + listTightIsoPt40):
        if hasattr(process, att):
            rename_module(process, att, att[:-3])


    rename_module(process, "hltHpsSelectedPFTausTrackPt1Reg", "hltHpsSelectedPFTausTrackPt1")
    rename_module(process, "hltHpsPFTauTrackPt1DiscriminatorReg", "hltHpsPFTauTrackPt1Discriminator")

    # the ones that does not exist in global one, so one can delete them..
    delattr(process, "hltTrackIter0RefsForJets4Iter1TauReg")
    delattr(process, "hltAK4Iter0TrackJets4Iter1TauReg")
    delattr(process, "hltIter0TrackAndTauJets4Iter1TauReg")

    copy_existing_and_rename_current_module(process, "hltAK4Iter1TrackJets4Iter2TauReg", "hltAK4Iter1TrackJets4Iter2")
    copy_existing_and_rename_current_module(process, "hltDoubletRecoveryClustersRefRemovalTauReg", "hltDoubletRecoveryClustersRefRemoval")
    copy_existing_and_rename_current_module(process, "hltDoubletRecoveryMaskedMeasurementTrackerEventTauReg", "hltDoubletRecoveryMaskedMeasurementTrackerEvent")
    copy_existing_and_rename_current_module(process, "hltAK4PFJetsReg", "hltAK4PFJetsForTaus")

    copy_existing_and_rename_current_module(process, "hltDoubletRecoveryPFlowCkfTrackCandidatesTauReg", "hltDoubletRecoveryPFlowCkfTrackCandidates")
    copy_existing_and_rename_current_module(process, "hltDoubletRecoveryPFlowCtfWithMaterialTracksTauReg", "hltDoubletRecoveryPFlowCtfWithMaterialTracks")
    copy_existing_and_rename_current_module(process, "hltDoubletRecoveryPFlowPixelClusterCheckTauReg", "hltDoubletRecoveryPFlowPixelClusterCheck")
    copy_existing_and_rename_current_module(process, "hltDoubletRecoveryPFlowPixelHitDoubletsTauReg", "hltDoubletRecoveryPFlowPixelHitDoublets")
    copy_existing_and_rename_current_module(process, "hltDoubletRecoveryPFlowPixelSeedsTauReg", "hltDoubletRecoveryPFlowPixelSeeds")
    copy_existing_and_rename_current_module(process, "hltDoubletRecoveryPFlowTrackCutClassifierTauReg", "hltDoubletRecoveryPFlowTrackCutClassifier")
    copy_existing_and_rename_current_module(process, "hltDoubletRecoveryPFlowTrackSelectionHighPurityTauReg", "hltDoubletRecoveryPFlowTrackSelectionHighPurity")
    copy_existing_and_rename_current_module(process, "hltDoubletRecoveryPixelLayersAndRegionsTauReg", "hltDoubletRecoveryPixelLayersAndRegions")

    copy_existing_and_rename_current_module(process, "hltHpsCombinatoricRecoTausReg", "hltHpsCombinatoricRecoTaus")
    copy_existing_and_rename_current_module(process, "hltHpsPFTauDiscriminationByDecayModeFindingNewDMsReg", "hltHpsPFTauDiscriminationByDecayModeFindingNewDMs")
    copy_existing_and_rename_current_module(process, "hltHpsPFTauProducerSansRefsReg", "hltHpsPFTauProducerSansRefs")
    copy_existing_and_rename_current_module(process, "hltHpsPFTauTrackFindingDiscriminatorReg", "hltHpsPFTauTrackFindingDiscriminator")
    copy_existing_and_rename_current_module(process, "hltHpsSelectionDiscriminatorReg", "hltHpsSelectionDiscriminator")
    copy_existing_and_rename_current_module(process, "hltHpsTauPFJetsRecoTauChargedHadronsWithNeutralsReg", "hltHpsTauPFJetsRecoTauChargedHadronsWithNeutrals")

    copy_existing_and_rename_current_module(process, "hltIter0PFLowPixelSeedsFromPixelTracksTauReg", "hltIter0PFLowPixelSeedsFromPixelTracks")
    copy_existing_and_rename_current_module(process, "hltIter0PFlowCkfTrackCandidatesTauReg", "hltIter0PFlowCkfTrackCandidates")
    copy_existing_and_rename_current_module(process, "hltIter0PFlowCtfWithMaterialTracksTauReg", "hltIter0PFlowCtfWithMaterialTracks")
    copy_existing_and_rename_current_module(process, "hltIter0PFlowTrackCutClassifierTauReg", "hltIter0PFlowTrackCutClassifier")
    copy_existing_and_rename_current_module(process, "hltIter0PFlowTrackSelectionHighPurityTauReg", "hltIter0PFlowTrackSelectionHighPurity")

    copy_existing_and_rename_current_module(process, "hltIter1ClustersRefRemovalTauReg", "hltIter1ClustersRefRemoval")
    copy_existing_and_rename_current_module(process, "hltIter1MergedTauReg", "hltIter1Merged")
    copy_existing_and_rename_current_module(process, "hltIter1PFlowCkfTrackCandidatesTauReg", "hltIter1PFlowCkfTrackCandidates")
    copy_existing_and_rename_current_module(process, "hltIter1MaskedMeasurementTrackerEventTauReg", "hltIter1MaskedMeasurementTrackerEvent")
    copy_existing_and_rename_current_module(process, "hltIter1PFlowCtfWithMaterialTracksTauReg", "hltIter1PFlowCtfWithMaterialTracks")
    copy_existing_and_rename_current_module(process, "hltIter1PFlowPixelClusterCheckTauReg", "hltIter1PFlowPixelClusterCheck")
    copy_existing_and_rename_current_module(process, "hltIter1PFlowPixelHitDoubletsTauReg", "hltIter1PFlowPixelHitDoublets")
    copy_existing_and_rename_current_module(process, "hltIter1PFlowPixelHitQuadrupletsTauReg", "hltIter1PFlowPixelHitQuadruplets")
    copy_existing_and_rename_current_module(process, "hltIter1PFlowPixelSeedsTauReg", "hltIter1PFLowPixelSeedsFromPixelTracks") # double check this
    copy_existing_and_rename_current_module(process, "hltIter1PFlowPixelTrackingRegionsTauReg", "hltIter1PFlowPixelTrackingRegions")
    copy_existing_and_rename_current_module(process, "hltIter1PFlowTrackCutClassifierDetachedTauReg", "hltIter1PFlowTrackCutClassifierDetached")
    copy_existing_and_rename_current_module(process, "hltIter1PFlowTrackCutClassifierMergedTauReg", "hltIter1PFlowTrackCutClassifierMerged")
    copy_existing_and_rename_current_module(process, "hltIter1PFlowTrackCutClassifierPromptTauReg", "hltIter1PFlowTrackCutClassifierPrompt")
    copy_existing_and_rename_current_module(process, "hltIter1PFlowTrackSelectionHighPurityTauReg", "hltIter1PFlowTrackSelectionHighPurity")
    copy_existing_and_rename_current_module(process, "hltIter1PixelLayerQuadrupletsTauReg", "hltIter1PixelLayerQuadruplets")
    copy_existing_and_rename_current_module(process, "hltIter1TrackAndTauJets4Iter2TauReg", "hltIter1TrackAndTauJets4Iter2")
    copy_existing_and_rename_current_module(process, "hltIter1TrackRefsForJets4Iter2TauReg", "hltIter1TrackRefsForJets4Iter2")

    copy_existing_and_rename_current_module(process, "hltIter2ClustersRefRemovalTauReg", "hltIter2ClustersRefRemoval")
    copy_existing_and_rename_current_module(process, "hltIter2MaskedMeasurementTrackerEventTauReg", "hltIter2MaskedMeasurementTrackerEvent")
    copy_existing_and_rename_current_module(process, "hltIter2MergedTauReg", "hltIter2Merged")
    copy_existing_and_rename_current_module(process, "hltIter2PFlowCkfTrackCandidatesTauReg", "hltIter2PFlowCkfTrackCandidates")
    copy_existing_and_rename_current_module(process, "hltIter2PFlowCtfWithMaterialTracksTauReg", "hltIter2PFlowCtfWithMaterialTracks")
    copy_existing_and_rename_current_module(process, "hltIter2PFlowPixelClusterCheckTauReg", "hltIter2PFlowPixelClusterCheck")
    copy_existing_and_rename_current_module(process, "hltIter2PFlowPixelHitTripletsTauReg", "hltIter2PFlowPixelHitTriplets")
    copy_existing_and_rename_current_module(process, "hltIter2PFlowPixelHitDoubletsTauReg", "hltIter2PFlowPixelHitDoublets")
    copy_existing_and_rename_current_module(process, "hltIter2PFlowPixelSeedsTauReg", "hltIter2PFlowPixelSeeds")
    copy_existing_and_rename_current_module(process, "hltIter2PFlowPixelTrackingRegionsTauReg", "hltIter2PFlowPixelTrackingRegions")
    copy_existing_and_rename_current_module(process, "hltIter2PFlowTrackCutClassifierTauReg", "hltIter2PFlowTrackCutClassifier")
    copy_existing_and_rename_current_module(process, "hltIter2PFlowTrackSelectionHighPurityTauReg", "hltIter2PFlowTrackSelectionHighPurity")
    copy_existing_and_rename_current_module(process, "hltIter2PixelLayerTripletsTauReg", "hltIter2PixelLayerTriplets")


    # delete & modify sequences
    delattr(process, "HLTIterativeTrackingIteration3ForIterL3FromL1Muon")
    delattr(process, "HLTIterativeTrackingIteration1TauReg")
    delattr(process, "HLTIter1TrackAndTauJets4Iter2SequenceTauReg")
    delattr(process, "HLTIterativeTrackingIteration2TauReg")
    delattr(process, "HLTIter0TrackAndTauJet4Iter1SequenceTauReg")
    delattr(process, "HLTIterativeTrackingIteration0TauReg")
    delattr(process, "HLTIterativeTrackingDoubletRecoveryTauReg")
    delattr(process, "HLTIterativeTrackingIter02TauReg")

    delattr(process, "HLTPFTauHPSReg")
    delattr(process, "HLTTrackReconstructionForPFReg")
    delattr(process, "HLTPFJetTriggerSequenceReg")
    delattr(process, "HLTPFJetTriggerSequenceRegNoMu")
    delattr(process, "HLTParticleFlowSequenceReg")
    delattr(process, "HLTRegionalPFTauHPSSequence")
    delattr(process, "HLTPFJetsSequenceReg")


    if hasattr(process, "HLTHPSMediumChargedIsoPFTauSequenceReg"):
        delattr(process, "HLTHPSMediumChargedIsoPFTauSequenceReg")
        process.HLTHPSMediumChargedIsoPFTauSequence = cms.Sequence(process.hltHpsPFTauMediumAbsoluteChargedIsolationDiscriminator+process.hltHpsPFTauMediumRelativeChargedIsolationDiscriminator+process.hltHpsPFTauMediumAbsOrRelChargedIsolationDiscriminator)

    if hasattr(process, "HLTHPSTightChargedIsoPFTauSequenceReg"):
        delattr(process, "HLTHPSTightChargedIsoPFTauSequenceReg")
        process.HLTHPSMediumChargedIsoPFTauSequence = cms.Sequence(process.hltHpsPFTauMediumAbsoluteChargedIsolationDiscriminator+process.hltHpsPFTauMediumRelativeChargedIsolationDiscriminator+process.hltHpsPFTauMediumAbsOrRelChargedIsolationDiscriminator)

    if hasattr(process, "HLTHPSDoublePFTauPt35Eta2p1Trk1Reg"):
        delattr(process, "HLTHPSDoublePFTauPt35Eta2p1Trk1Reg")
        process.HLTHPSDoublePFTauPt35Eta2p1Trk1 = cms.Sequence(process.hltHpsDoublePFTau35+process.hltHpsPFTauTrackPt1Discriminator+process.hltHpsSelectedPFTausTrackPt1+process.hltHpsDoublePFTau35TrackPt1)

    if hasattr(process, "HLTHPSDoublePFTauPt40Eta2p1Trk1Reg"):
        delattr(process, "HLTHPSDoublePFTauPt40Eta2p1Trk1Reg")
        process.HLTHPSDoublePFTauPt40Eta2p1Trk1 = cms.Sequence(process.hltHpsDoublePFTau40+process.hltHpsPFTauTrackPt1Discriminator+process.hltHpsSelectedPFTausTrackPt1+process.hltHpsDoublePFTau40TrackPt1)

    if hasattr(process, "HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v4"):
        #delattr(process, "HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v4")
        process.HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v4 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleTauBigOR + process.hltPreDoubleMediumChargedIsoPFTauHPS35Trk1eta2p1 + process.HLTL2TauJetsL1TauSeededSequence + process.hltDoubleL2Tau26eta2p2 + process.HLTL2p5IsoTauL1TauSeededSequence + process.hltDoubleL2IsoTau26eta2p2 + process.HLTGlobalPFTauHPSSequence + process.HLTHPSDoublePFTauPt35Eta2p1Trk1 + process.HLTHPSMediumChargedIsoPFTauSequence + process.hltHpsSelectedPFTausTrackPt1MediumChargedIsolation + process.hltHpsDoublePFTau35TrackPt1MediumChargedIsolation + process.hltHpsL1JetsHLTDoublePFTauTrackPt1MediumChargedIsolationMatch + process.hltHpsDoublePFTau35TrackPt1MediumChargedIsolationL1HLTMatched + process.hltHpsDoublePFTau35TrackPt1MediumChargedIsolationDz02 + process.HLTEndSequence )

    if hasattr(process, "HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v1"):
        delattr(process, "HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v1")
        process.HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1_Global_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleTauBigOR + process.hltPreDoubleTightChargedIsoPFTauHPS35Trk1eta2p1 + process.HLTL2TauJetsL1TauSeededSequence + process.hltDoubleL2Tau26eta2p2 + process.HLTL2p5IsoTauL1TauSeededSequence + process.hltDoubleL2IsoTau26eta2p2 + process.HLTGlobalPFTauHPSSequence + process.HLTHPSDoublePFTauPt35Eta2p1Trk1 + process.HLTHPSMediumChargedIsoPFTauSequence + process.hltHpsSelectedPFTausTrackPt1TightChargedIsolation + process.hltHpsDoublePFTau35TrackPt1TightChargedIsolation + process.hltHpsL1JetsHLTDoublePFTauTrackPt1TightChargedIsolationMatch + process.hltHpsDoublePFTau35TrackPt1MediumChargedIsolationL1HLTMatched + process.hltHpsDoublePFTau35TrackPt1MediumChargedIsolationDz02 + process.HLTEndSequence )

    if hasattr(process, "HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1_Reg_v1"):
        delattr(process, "HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1_Reg_v1")
        process.HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1_Global_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleTauBigOR + process.hltPreDoubleMediumChargedIsoPFTauHPS40Trk1eta2p1 + process.HLTL2TauJetsL1TauSeededSequence + process.hltDoubleL2Tau26eta2p2 + process.HLTL2p5IsoTauL1TauSeededSequence + process.hltDoubleL2IsoTau26eta2p2 + process.HLTGlobalPFTauHPSSequence + process.HLTHPSDoublePFTauPt40Eta2p1Trk1 + process.HLTHPSMediumChargedIsoPFTauSequence + process.hltHpsSelectedPFTausTrackPt1MediumChargedIsolation + process.hltHpsDoublePFTau40TrackPt1MediumChargedIsolation + process.hltHpsL1JetsHLTDoublePFTauTrackPt1MediumChargedIsolationMatch + process.hltHpsDoublePFTau40TrackPt1MediumChargedIsolationL1HLTMatched + process.hltHpsDoublePFTau40TrackPt1MediumChargedIsolationDz02 + process.HLTEndSequence )

    if hasattr(process, "HLT_DoubleTightChargedIsoPFTauHPS40_Trk1_eta2p1_Reg_v1"):
        delattr(process, "HLT_DoubleTightChargedIsoPFTauHPS40_Trk1_eta2p1_Reg_v1")
        process.HLT_DoubleTightChargedIsoPFTauHPS40_Trk1_eta2p1_Global_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleTauBigOR + process.hltPreDoubleTightChargedIsoPFTauHPS40Trk1eta2p1 + process.HLTL2TauJetsL1TauSeededSequence + process.hltDoubleL2Tau26eta2p2 + process.HLTL2p5IsoTauL1TauSeededSequence + process.hltDoubleL2IsoTau26eta2p2 + process.HLTGlobalPFTauHPSSequence + process.HLTHPSDoublePFTauPt40Eta2p1Trk1 + process.HLTHPSMediumChargedIsoPFTauSequence + process.hltHpsSelectedPFTausTrackPt1TightChargedIsolation + process.hltHpsDoublePFTau40TrackPt1TightChargedIsolation + process.hltHpsL1JetsHLTDoublePFTauTrackPt1TightChargedIsolationMatch + process.hltHpsDoublePFTau40TrackPt1MediumChargedIsolationL1HLTMatched + process.hltHpsDoublePFTau40TrackPt1MediumChargedIsolationDz02 + process.HLTEndSequence )

    return process


def rename_mod_inputs(pset,oldmod,newmod):
    names = pset.parameterNames_()
    for para_name in names:
        if hasattr(pset,para_name):
            para = getattr(pset,para_name)
            para_type = para.pythonTypeName()
            if para_type == "cms.InputTag":
                if para.getModuleLabel() == oldmod:
                    para.setModuleLabel(newmod)
            if para_type == "cms.VInputTag":
                for tag in para:
                    if type(tag)==cms.InputTag:
                        if tag.getModuleLabel() == oldmod:
                            tag.setModuleLabel(newmod)
                    else:
                        modlabel = tag.split(":")[0]
                        if modlabel == oldmod:
                            tag.replace(modlabel+":",newmod+":")
            if para_type == "cms.PSet":
                rename_mod_inputs(para,oldmod,newmod)
            if para_type == "cms.VPSet":
                #oddly iterating over it normally
                #wipes out parameters after untracked paras
                for index in range(0,len(para)):
                    rename_mod_inputs(para[index],oldmod,newmod)

def rename_mod_inputs_allprod(process,oldmod,newmod):
    for prodname in (process.producerNames().split() + process.filterNames().split()) :
        prod = getattr(process,prodname)
        #print "begin ",prodname
        rename_mod_inputs(prod,oldmod,newmod)
        #print "end",prodname


def rename_module(process,name,new_name):
    mod = getattr(process,name)
    setattr(process,new_name,mod.clone())
    new_mod = getattr(process,new_name)
    for taskname,task in process.tasks.iteritems():
        task.replace(mod,new_mod)
    for seqname,seq in process.sequences.iteritems():
        seq.replace(mod,new_mod)
    for pathname,path in process.paths.iteritems():
        path.replace(mod,new_mod)
    for pathname,path in process.endpaths.iteritems():
        path.replace(mod,new_mod)
    rename_mod_inputs_allprod(process,name,new_name)
    delattr(process,name)


def copy_existing_and_rename_current_module(process, name, new_name):
    mod = getattr(process,new_name)
    setattr(process,new_name + "_tmp",mod.clone())
    rename_module(process, name, new_name)
    mod_tmp = getattr(process, new_name + "_tmp")
    setattr(process,new_name, mod_tmp.clone())
    delattr(process, new_name + "_tmp")
