# Customisation function to convert the regional PF reconstruction to global one for the signal ditau HLTs
# which is medium isolation with pt = 35 GeV case..

# If you spot anything, please get in contact with
# hale.sert@cern.ch

# NOTE: This customisation function assumes that one of the lepton+tau HLT (e.g. mutau) has been already included in the dumped menu,
#       together with ditau HLT which uses regional PF reconstuction.
#       The purpose of including mutau HLT is that the function uses modules used in the global PF reconstuction of the tau leg of mutau HLT
#       to perform the conversion to global PF reconstuction from regional PF reconstruction.

import FWCore.ParameterSet.Config as cms

def customizeDiTauRegionalPFtoGlobalPF(process):

    # the ones existing only in Regional version, so they need to be renamed..
    listHpsDoublePFModules =['hltHpsDoublePFTau35Reg']

    listHpsDoubleTauTrkModules =['hltHpsDoublePFTau35TrackPt1Reg']

    for att in (listHpsDoublePFModules):
        if hasattr(process, att):
            mod = getattr(process, att)
            setattr(process, att[:-3], mod.clone(
                inputTag = cms.InputTag("hltHpsPFTauProducer"),
            )
            )
    for att in (listHpsDoubleTauTrkModules):
        if hasattr(process, att):
            mod = getattr(process, att)
            setattr(process, att[:-3], mod.clone(
                inputTag = cms.InputTag("hltHpsSelectedPFTausTrackPt1"),
            ))

    listMediumIsolation =['hltHpsPFTauMediumAbsoluteChargedIsolationDiscriminatorReg',
                        'hltHpsPFTauMediumRelativeChargedIsolationDiscriminatorReg',
                        'hltHpsPFTauMediumAbsOrRelChargedIsolationDiscriminatorReg']

    for att in (listMediumIsolation):
        if hasattr(process, att):
            mod = getattr(process, att)
            if att.find("AbsOrRelChargedIsolationDiscriminatorReg") < 0:
                setattr(process, att[:-3], mod.clone(
                    PFTauProducer = cms.InputTag("hltHpsPFTauProducer"),
                    particleFlowSrc = cms.InputTag("hltParticleFlowForTaus"),
                    ))
            else:
                setattr(process, att[:-3], mod.clone(
                    PFTauProducer = cms.InputTag("hltHpsPFTauProducer"),
                    Prediscriminants = cms.PSet(
                        BooleanOperator = cms.string('or'),
                        discr1 = cms.PSet(
                            Producer = cms.InputTag("hltHpsPFTauMediumAbsoluteChargedIsolationDiscriminator"),
                        ),
                        discr2 = cms.PSet(
                            Producer = cms.InputTag("hltHpsPFTauMediumRelativeChargedIsolationDiscriminator"),
                        )
                    )
                    ))

    listSelectedMedium =['hltHpsSelectedPFTausTrackPt1MediumChargedIsolationReg']

    for att in (listSelectedMedium):
        if hasattr(process, att):
            mod = getattr(process, att)
            setattr(process, att[:-3], mod.clone(
                discriminators = cms.VPSet(
                    cms.PSet(
                        discriminator = cms.InputTag("hltHpsPFTauTrackPt1Discriminator"),
                        selectionCut = cms.double(0.5)
                    ),
                    cms.PSet(
                        discriminator = cms.InputTag("hltHpsPFTauMediumAbsOrRelChargedIsolationDiscriminator"),
                        selectionCut = cms.double(0.5)
                    )
                ),
                src = cms.InputTag("hltHpsPFTauProducer")
            ))

    listMediumIsoPt35 =['hltPreDoubleMediumChargedIsoPFTauHPS35Trk1eta2p1Reg',
                    'hltHpsDoublePFTau35TrackPt1MediumChargedIsolationReg',
                    'hltHpsDoublePFTau35TrackPt1MediumChargedIsolationL1HLTMatchedReg',
                    'hltHpsDoublePFTau35TrackPt1MediumChargedIsolationDz02Reg']

    listL1JetsMedium =['hltHpsL1JetsHLTDoublePFTauTrackPt1MediumChargedIsolationMatchReg']

    for index, att in enumerate(listMediumIsoPt35 + listL1JetsMedium):
        if hasattr(process, att):
            mod = getattr(process, att)
            if index ==0:
                setattr(process, att[:-3], mod.clone())
            if index == 1:
                setattr(process, att[:-3], mod.clone(
                    inputTag = cms.InputTag("hltHpsSelectedPFTausTrackPt1MediumChargedIsolation"),
                ))
            if index == 2:
                setattr(process, att[:-3], mod.clone(
                    inputTag = cms.InputTag("hltHpsL1JetsHLTDoublePFTauTrackPt1MediumChargedIsolationMatch"),
                ))
            if index == 3:
                setattr(process, att[:-3], mod.clone(
                    JetSrc = cms.InputTag("hltHpsL1JetsHLTDoublePFTauTrackPt1MediumChargedIsolationMatch"),
                ))
            if index ==4:
                setattr(process, att[:-3], mod.clone(
                    JetSrc = cms.InputTag("hltHpsSelectedPFTausTrackPt1MediumChargedIsolation"),
                ))

    process.hltHpsSelectedPFTausTrackPt1 = process.hltHpsSelectedPFTausTrackPt1Reg.clone(
        discriminators = cms.VPSet(cms.PSet(
            discriminator = cms.InputTag("hltHpsPFTauTrackPt1Discriminator"),
            selectionCut = cms.double(0.5)
            )),
            src = cms.InputTag("hltHpsPFTauProducer"),
    )
    process.hltHpsPFTauTrackPt1Discriminator = process.hltHpsPFTauTrackPt1DiscriminatorReg.clone(
        PFTauProducer = cms.InputTag("hltHpsPFTauProducer"),
    )


    # add sequences
    process.HLTHPSMediumChargedIsoPFTauSequence = cms.Sequence(process.hltHpsPFTauMediumAbsoluteChargedIsolationDiscriminator+process.hltHpsPFTauMediumRelativeChargedIsolationDiscriminator+process.hltHpsPFTauMediumAbsOrRelChargedIsolationDiscriminator)

    process.HLTHPSDoublePFTauPt35Eta2p1Trk1 = cms.Sequence(process.hltHpsDoublePFTau35+process.hltHpsPFTauTrackPt1Discriminator+process.hltHpsSelectedPFTausTrackPt1+process.hltHpsDoublePFTau35TrackPt1)

    process.HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Global_v4 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleTauBigOR + process.hltPreDoubleMediumChargedIsoPFTauHPS35Trk1eta2p1 + process.HLTL2TauJetsL1TauSeededSequence + process.hltDoubleL2Tau26eta2p2 + process.HLTL2p5IsoTauL1TauSeededSequence + process.hltDoubleL2IsoTau26eta2p2 + process.HLTGlobalPFTauHPSSequence + process.HLTHPSDoublePFTauPt35Eta2p1Trk1 + process.HLTHPSMediumChargedIsoPFTauSequence + process.hltHpsSelectedPFTausTrackPt1MediumChargedIsolation + process.hltHpsDoublePFTau35TrackPt1MediumChargedIsolation + process.hltHpsL1JetsHLTDoublePFTauTrackPt1MediumChargedIsolationMatch + process.hltHpsDoublePFTau35TrackPt1MediumChargedIsolationL1HLTMatched + process.hltHpsDoublePFTau35TrackPt1MediumChargedIsolationDz02 + process.HLTEndSequence )


    # if one would like to replace Reg one to Global one, please comment out the folowing path to remove it
   # mod = getattr(process, "HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Global_v4")
    #sdelattr(process, "HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v4")


    return process
