import FWCore.ParameterSet.Config as cms

L1HPSPFTauSeedAnalyzer = cms.EDAnalyzer("L1HPSPFTauSeedAnalyzer",
  srcL1PFCands              = cms.InputTag("l1pfCandidates:PF"),
  srcL1PFJets               = cms.InputTag("ak4PFL1PFCorrected"),                      
  srcL1Vertices             = cms.InputTag("VertexProducer:l1vertextdr"),
  genTauToken               = cms.InputTag("tauGenJetsSelectorAllHadrons"),
  min_seedChargedPFCand_pt  = cms.double(5.),
  max_seedChargedPFCand_eta = cms.double(2.4),
  max_seedChargedPFCand_dz  = cms.double(1.e+3),
  min_seedPFJet_pt          = cms.double(30.),
  max_seedPFJet_eta         = cms.double(2.4),
  min_genTau_pt             = cms.double(30.),
  max_genTau_eta            = cms.double(2.4),
  signalQualityCuts = cms.PSet(
    chargedHadron = cms.PSet(
      min_pt = cms.double(0.),
      max_dz = cms.double(0.4),
    ),
    neutralHadron = cms.PSet(
      min_pt = cms.double(0.)
    ),
    muon = cms.PSet(
      min_pt = cms.double(0.),
      max_dz = cms.double(0.4),
    ),
    electron = cms.PSet(
      min_pt = cms.double(0.),
      max_dz = cms.double(0.4),
    ),
    photon = cms.PSet(
      min_pt = cms.double(0.)
    )
  ),
  dqmDirectory = cms.string("L1HPSPFTauSeedAnalyzer"),
)


AnalyzerSeq = cms.Sequence(
    L1HPSPFTauSeedAnalyzer
)
