from ROOT import *

gROOT.Macro("rootlogon.C")

f1 = TFile("qcd_1400.root")
f2 = TFile("grav_ww_3000.root")

h_tau21AK8_1 = f1.Get("h_tau21AK8")
h_tau21AK8_2 = f2.Get("h_tau21AK8")

h_tau21AK8_1.SetLineColor(1)
h_tau21AK8_2.SetLineColor(2)

leg = TLegend(0.15, 0.65, 0.35, 0.85)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.AddEntry( h_tau21AK8_1, "QCD", 'l')
leg.AddEntry( h_tau21AK8_2, "G* #rightarrow WW", 'l')

h_tau21AK8_1.Sumw2()
h_tau21AK8_1.Rebin(4)
h_tau21AK8_1.Scale( 1.0 / h_tau21AK8_1.Integral() )
h_tau21AK8_2.Sumw2()
h_tau21AK8_2.Rebin(4)
h_tau21AK8_2.Scale( 1.0 / h_tau21AK8_2.Integral() )

c = TCanvas('c', 'c') 
h_tau21AK8_2.Draw("hist")
h_tau21AK8_1.Draw("same hist")
h_tau21AK8_2.SetMaximum( h_tau21AK8_2.GetMaximum()*1.6 )


leg.Draw()

c.Print('plots8.png', 'png')
c.Print('plots8.pdf', 'pdf')
