# taken from Tyler Ruggles

import ROOT
import os
import subprocess
import math

# New minBias xsec: https://hypernews.cern.ch/HyperNews/CMS/get/luminosity/613/2/1/1/1.html
def makeDataPUTemplate( cert, puJson, year='17' ) :
    executeArray = [
        'pileupCalc.py',
        '-i',
        '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions%s/13TeV/%s' % (year, cert),
        '--inputLumiJSON',
        '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions%s/13TeV/PileUp/%s' % (year, puJson),
        '--calcMode',
        'true',
        '--minBiasXsec',
        '69200',
        '--maxPileupBin',
        '100',
        '--numPileupBins',
        '1000',
        'data/PileUpTemplate/DataTemplate_RunBF2017_69p2MinBiasXS_100bins.root']
    subprocess.call( executeArray )

def makeMCPUTemplateUsingNTruePU( ) :
	use1000bins = True
	MCdist = []
	sHist = TH1F ("sHist", "", 1000, 0, 100)
	dHist = TH1F ("pileup", "pileup", 1000, 0, 100)
	samplefile = ROOT.TFile('/eos/user/h/hsert/TriggerStudies/ForkedRepo/Samples/12062018/NTuple_0WJets_12Apr2018_12062018_PU_1000binMC.root', 'READ')
	c1 = TCanvas ("c1", "c1", 600, 600)
	c1.SetGridx()
	c1.SetGridy()
	sTree = samplefile.Get('Ntuplizer/TagAndProbe')
    for iEv in range (0, sTree.GetEntries()):
		sTree.GetEntry(iEv)
			if(use1000bins):
				dHist.Fill(sTree.nTruePU)
	        else:
				sHist.Fill(sTree.nTruePU)

        if not use1000bins:
            nBins = sHist.GetXaxis().GetNbins()
            for i in range(1, nBins + 1):
                MCdist.append(sHist.GetBinContent(i))
                print "bin content", sHist.GetBinContent(i)
            for i in range(1, nBins*10 + 1):
                dHist.SetBinContent( i, MCdist[ (i-1)/10 ] )

        dHist.SaveAs('data/PileUpTemplate/MCTemplate2017_WJets_nTruePU_1000bins.root')

def makeMCPUTemplate( ) :
    # 25ns pileup distributions found here: https://github.com/cms-sw/cmssw/blob/CMSSW_7_4_X/SimGeneral/MixingModule/python/mix_2015_25ns_Startup_PoissonOOTPU_cfi.py
    # 25ns PU for 80X (this is out of time, so we add a 0 at the bottom: https://github.com/cms-sw/cmssw/blob/CMSSW_8_0_X/SimGeneral/MixingModule/python/mix_2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU_cfi.py#L25
    # 25ns pileup distributions for 94X found here:https://github.com/cms-sw/cmssw/blob/CMSSW_9_4_X/SimGeneral/MixingModule/python/mix_2017_25ns_WinterMC_PUScenarioV1_PoissonOOTPU_cfi.py
    MCDist = [
         3.39597497605e-05,
         6.63688402133e-06,
         1.39533611284e-05,
         3.64963078209e-05,
         6.00872171664e-05,
         9.33932578027e-05,
         0.000120591524486,
         0.000128694546198,
         0.000361697233219,
         0.000361796847553,
         0.000702474896113,
         0.00133766053707,
         0.00237817050805,
         0.00389825605651,
         0.00594546732588,
         0.00856825906255,
         0.0116627396044,
         0.0148793350787,
         0.0179897368379,
         0.0208723871946,
         0.0232564170641,
         0.0249826433945,
         0.0262245860346,
         0.0272704617569,
         0.0283301107549,
         0.0294006137386,
         0.0303026836965,
         0.0309692426278,
         0.0308818046328,
         0.0310566806228,
         0.0309692426278,
         0.0310566806228,
         0.0310566806228,
         0.0310566806228,
         0.0307696426944,
         0.0300103336052,
         0.0288355370103,
         0.0273233309106,
         0.0264343533951,
         0.0255453758796,
         0.0235877272306,
         0.0215627588047,
         0.0195825559393,
         0.0177296309658,
         0.0160560731931,
         0.0146022004183,
         0.0134080690078,
         0.0129586991411,
         0.0125093292745,
         0.0124360740539,
         0.0123547104433,
         0.0123953922486,
         0.0124360740539,
         0.0124360740539,
         0.0123547104433,
         0.0124360740539,
         0.0123387597772,
         0.0122414455005,
         0.011705203844,
         0.0108187105305,
         0.00963985508986,
         0.00827210065136,
         0.00683770076341,
         0.00545237697118,
         0.00420456901556,
         0.00367513566191,
         0.00314570230825,
         0.0022917978982,
         0.00163221454973,
         0.00114065309494,
         0.000784838366118,
         0.000533204105387,
         0.000358474034915,
         0.000238881117601,
         0.0001984254989,
         0.000157969880198,
         0.00010375646169,
         6.77366175538e-05,
         4.39850477645e-05,
         2.84298066026e-05,
         1.83041729561e-05,
         1.17473542058e-05,
         7.51982735129e-06,
         6.16160108867e-06,
         4.80337482605e-06,
         3.06235473369e-06,
         1.94863396999e-06,
         1.23726800704e-06,
         7.83538083774e-07,
         4.94602064224e-07,
         3.10989480331e-07,
         1.94628487765e-07,
         1.57888581037e-07,
         1.2114867431e-07,
         7.49518929908e-08,
         4.6060444984e-08,
         2.81008884326e-08,
         1.70121486128e-08,
         1.02159894812e-08]

    nBins = len(MCDist)
    print "MC # Bins:",nBins
    dHist = ROOT.TH1F('pileup', 'pileup', nBins*10, 0, nBins)
    for i in range( 1, (nBins*10)+1 ) :
        print "bin: %i, MC position: %i" % (i, math.floor((i-1)/10) )
        dHist.SetBinContent( i, MCDist[ (i-1)/10 ] )
    dHist.SaveAs('data/PileUpTemplate/MCTemplate2017_99bins.root')



if __name__ == '__main__' :

    cert = 'ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt' #~42 fb^{-1}
    year = '17'
    makeDataPUTemplate( cert, 'pileup_latest.txt', year )
    makeMCPUTemplate()
    makeMCPUTemplateUsingNTruePU()

