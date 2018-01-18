'''Abreviated version of https://github.com/truggles/Z_to_TauTau_13TeV/blob/master/util/pileUpVertexCorrections.py'''
# taken from Tyler Ruggles

import ROOT
from collections import OrderedDict

def PUreweight( dataFile ) :
    # https://twiki.cern.ch/twiki/bin/view/CMS/HiggsToTauTauWorking2015#PU_reweighting
    #data/Data_Pileup_2016_271036-284044_80bins.root - Moriond2017, full 2016 dataset
    datafile = ROOT.TFile('data/PileUpTemplate/'+dataFile, 'READ') 
    dHist = datafile.Get('pileup')
    dHist.Scale( 1 / dHist.Integral() )

    # For 2017 94X samples
    samplefile = ROOT.TFile('data/PileUpTemplate/MCTemplate2017.root', 'READ') 
    sHist = samplefile.Get('pileup')
    sHist.Scale( 1 / sHist.Integral() )

    reweightDict = OrderedDict()
    for i in range( 1, dHist.GetXaxis().GetNbins()+1 ) :
        # dHist has exactly 600 bins, not 601 w/ over/underflow
        if sHist.GetBinContent( i ) > 0 :
            ratio = dHist.GetBinContent( i ) / sHist.GetBinContent( i )
        else : ratio = 0
        reweightDict[ (i-1)/10. ] = ratio
    return reweightDict


