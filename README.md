JMEDAS
======

JME POG CMS Data Analysis School (CMSDAS) exercise
Main exercise instructions: https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolHamburg2018JetExercise

```
cmsrel CMSSW_9_4_9
cd CMSSW_9_4_9/src
git clone https://github.com/raggleton/JMEDAS.git Analysis/JMEDAS
cd Analysis/JMEDAS
scram b -j 10
cd test
voms-proxy-init -voms cms
```
