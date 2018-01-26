#!/usr/bin/python
#
from ROOT import *
from array import array
import numpy as n
import os

import datetime
today=datetime.date.today().strftime("%Y-%m-%d")
date=today

filename='/afs/cern.ch/user/h/hsert/TriggerStudies/ForkedRepo/Samples/2018_01_14/NTuple_DYJets_RunIIFall17MiniAOD-RECOSIMstep_94X_mc2017_realistic_v10-v1_14_01_2018_PU.root'

file = TFile.Open(filename)
tree = file.Get('Ntuplizer/TagAndProbe')
triggerNamesTree = file.Get("Ntuplizer/triggerNames")

histoPU = TH2F ("puweight", "puweight:pu", 100, 0, 100, 50, 0, 5)

for iEv in range (0, tree.GetEntries()):
	tree.GetEntry(iEv)
		
	nTruePU= tree.nTruePU
	puweight = tree.puweight
	
	histoPU.Fill(nTruePU, puweight)
	print "event:", iEv, " PUweight:", puweight, " PU", nTruePU
	

c1 = TCanvas ("c1", "c1", 1000, 900)
histoPU.Draw("colz")
histoPU.GetXaxis().SetTitle("N_{PU}^{true}")
histoPU.GetYaxis().SetTitle("puweight")

c1.Print("PUweightvstruePU.png", "png")

raw_input()
