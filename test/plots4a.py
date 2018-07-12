from ROOT import *

gROOT.Macro("rootlogon.C")

f = TFile("grav_ww_3000.root")

h_mAK8   = f.Get("h_mAK8")
h_msoftdropAK8 = f.Get("h_msoftdropAK8")
h_mprunedAK8 = f.Get("h_mprunedAK8")
h_mpuppiAK8 = f.Get("h_mpuppiAK8")
h_mSDpuppiAK8 = f.Get("h_mSDpuppiAK8")

h_msoftdropAK8.SetLineColor(kRed)
# h_msoftdropAK8.SetLineStyle(2)

h_mprunedAK8.SetLineColor(kGreen+3) 
h_mprunedAK8.SetLineStyle(2) 

h_mpuppiAK8.SetLineColor(kMagenta)

h_mSDpuppiAK8.SetLineColor(kAzure+1)
# h_mSDpuppiAK8.SetLineStyle(3) 


leg = TLegend(0.35, 0.82, 0.8, 0.99)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.AddEntry( h_mAK8, "Ungroomed", 'l')
leg.AddEntry( h_msoftdropAK8, "Soft Drop", 'l')
leg.AddEntry( h_mprunedAK8, "Pruned", 'l')
leg.AddEntry( h_mpuppiAK8, "PUPPI", 'l')
leg.AddEntry( h_mSDpuppiAK8, "PUPPI+SD", 'l')
leg.SetNColumns(3)

c = TCanvas('c', 'c')
h_mprunedAK8.Draw()
h_mprunedAK8.GetXaxis().SetRangeUser(0, 300)
h_msoftdropAK8.Draw("same") 
h_mAK8.Draw("same") 
h_mpuppiAK8.Draw("same")
h_mSDpuppiAK8.Draw("same")
h_mprunedAK8.SetMaximum( h_msoftdropAK8.GetMaximum()*1.6 )

leg.Draw()

c.Print('plots4a.png', 'png')
c.Print('plots4a.pdf', 'pdf')
