import yaml

pubs = [
(2025,"Toddes C, Golden SA.","Behavioral neuroscience: Dominance in the absence of competition.","Curr Biol.","2025 Jul 21;35(14):R706-R708.","10.1016/j.cub.2025.05.058"),
(2025,"Simon RC, Fleming WT, Briones BA, et al.","Opioid-driven disruption of the septum reveals a role for neurotensin-expressing neurons in withdrawal.","Neuron.","2025 May 14:S0896-6273(25)00307-1.","10.1016/j.neuron.2025.04.024"),
(2025,"Luskin AT, Li L, Fu X, et al.","Heterogeneous pericoerulear neurons tune arousal and exploratory behaviours.","Nature.","2025 May 7.","10.1038/s41586-025-08952-w"),
(2025,"Ishii KK, Hashikawa K, Chea J, et al.","Post-ejaculatory inhibition of female sexual drive via heterogeneous neuronal ensembles in the medial preoptic area.","eLife.","2025 12:RP91765.","10.7554/eLife.91765.3"),
(2025,"Caprioli D, Golden SA, Baunez C, Venniro M.","Editorial: Spanning the spectrum of social behavior: towards more translationally relevant animal models.","Psychopharmacology (Berl).","2025 May;242(5):885-887.","10.1007/s00213-025-06755-5"),
(2024,"Elum JE, Szelenyi ER, Juarez B, et al.","Distinct dynamics and intrinsic properties in ventral tegmental area populations mediate reward association and motivation.","Cell Rep.","2024 Aug 27;43(9):114668.","10.1016/j.celrep.2024.114668"),
(2024,"Goodwin NL, Golden SA.","Keeping it simple – a Simple Behavioral Analysis (SimBA) primer.","NPP—Digital Psychiatry and Neuroscience","2, 13 (2024).","10.1038/s44277-024-00014-9"),
(2024,"Szelenyi ER, Navarrete JS, Murry AD, et al.","An arginine-rich nuclear localization signal (ArgiNLS) strategy for streamlined image segmentation of single cells.","Proc Natl Acad Sci U S A.","2024 Aug 6;121(32):e2320250121.","10.1073/pnas.2320250121"),
(2024,"Goodwin NL, Choong JJ, Hwang S, et al.","Simple Behavioral Analysis (SimBA) as a platform for explainable machine learning in behavioral neuroscience.","Nature Neuroscience.","2024 May 22.","10.1038/s41593-024-01649-9"),
(2024,"Ouyang W, Kilner KJ, Xavier RMP, et al.","An implantable device for wireless monitoring of diverse physio-behavioral characteristics in freely behaving small animals and interacting groups.","Neuron.","2024 Jun 5;112(11):1764-1777.e5.","10.1016/j.neuron.2024.02.020"),
(2024,"Navarrete J, Schneider KN, Smith BM, et al.","Individual Differences in Volitional Social Self-Administration and Motivation in Male and Female Mice Following Social Stress.","Biol Psychiatry.","2024 Jan 18:S0006-3223(24)00033-7.","10.1016/j.biopsych.2024.01.007"),
(2023,"Wohlschlegel J, Finkbeiner C, Hoffer D, et al.","ASCL1 induces neurogenesis in human Müller glia.","Stem Cell Reports.","2023 Dec 12;18(12):2400-2417.","10.1016/j.stemcr.2023.10.021"),
(2023,"Ishii KK, Hashikawa K, Chea J, et al.","Post-Mating Inhibition of Female Sexual Drive via Heterogeneous Neuronal Ensembles in the Medial Preoptic Area.","eLife.","2023 Nov 14; eLife12:RP91765.",""),
(2023,"Newton KC, Kacev D, Nilsson SRO, et al.","Lateral line ablation by ototoxic compounds results in distinct rheotaxis profiles in larval zebrafish.","Commun Biol.","2023 Jan 21;6(1):84.","10.1038/s42003-023-04449-2"),
(2022,"Madangopal R, Szelenyi ER, Nguyen J, et al.","Incubation of palatable food craving is associated with brain-wide neuronal activation in mice.","Proc Natl Acad Sci U S A.","2022 Nov 8;119(45):e2209382119.","10.1073/pnas.2209382119"),
(2022,"Aubry AV, Joseph Burnett C, Goodwin NL, et al.","Sex differences in appetitive and reactive aggression.","Neuropsychopharmacology.","2022 Sep;47(10):1746-1754.","10.1038/s41386-022-01375-5"),
(2022,"Goodwin NL, Nilsson SRO, Choong JJ, Golden SA.","Toward the explainability, transparency, and universality of machine learning for behavioral classification in neuroscience.","Curr Opin Neurobiol.","2022 Apr;73:102544.","10.1016/j.conb.2022.102544"),
(2022,"Jin M, Nguyen JD, Weber SJ, et al.","SMART: An Open-Source Extension of WholeBrain for Intact Mouse Brain Registration and Segmentation.","eNeuro.","2022 May 3;9(3):ENEURO.0482-21.2022.","10.1523/ENEURO.0482-21.2022"),
(2022,"Marks RB, Wee JY, Jacobson SV, et al.","The Role of the Lateral Habenula in Suicide: A Call for Further Exploration.","Front Behav Neurosci.","2022 Mar 14;16:812952.","10.3389/fnbeh.2022.812952"),
(2022,"Winters C, Gorssen W, Ossorio-Salazar VA, et al.","Automated procedure to assess pup retrieval in laboratory mice.","Sci Rep.","2022 Jan 31;12(1):1663.","10.1038/s41598-022-05641-w"),
(2021,"Szelenyi ER, Goodwin NL, Golden SA.","Social mice seeking circuits.","Nature Neuroscience.","2021 Jun;24(6):761-762.","10.1038/s41593-021-00861-1"),
(2021,"Kwiatkowski CC, Akaeze H, Ndlebe I, et al.","Quantitative standardization of resident mouse behavior for studies of aggression and social defeat.","Neuropsychopharmacology.","2021 Aug;46(9):1584-1593.","10.1038/s41386-021-01018-1"),
(2020,"Goodwin NL, Nilsson SRO, Golden SA.","Rage Against the Machine: Advancing the study of aggression ethology via machine learning.","Psychopharmacology (Berl).","2020 Sep;237(9):2569-2588.","10.1007/s00213-020-05577-x"),
(2020,"Heshmati M, Christoffel DJ, LeClair K, et al.","Depression and Social Defeat Stress Are Associated with Inhibitory Synaptic Changes in the Nucleus Accumbens.","J Neurosci.","2020 Aug 5;40(32):6228-6233.","10.1523/JNEUROSCI.2568-19.2020"),
(2020,"Flanigan ME, Aleyasin H, Li L, et al.","Orexin signaling in GABAergic lateral habenula neurons modulates aggressive behavior in male mice.","Nat Neurosci.","2020 May;23(5):638-650.","10.1038/s41593-020-0617-7"),
(2020,"Dudek KA, Dion-Albert L, Lebel M, et al.","Molecular adaptations of the blood-brain barrier promote stress resilience vs. depression.","Proc Natl Acad Sci U S A.","2020 Feb 11;117(6):3326-3336.","10.1073/pnas.1914655117"),
(2021,"Labonté B, Abdallah K, Maussion G, et al.","Regulation of impulsive and aggressive behaviours by a novel lncRNA.","Mol Psychiatry.","2021 Aug;26(8):3751-3764.","10.1038/s41380-019-0637-4"),
(2020,"Venniro M, Golden SA.","Taking action: empathy and social interaction in rats.","Neuropsychopharmacology.","2020 Jun;45(7):1081-1082.","10.1038/s41386-019-0596-0"),
(2019,"Golden SA, Jin M, Shaham Y.","Animal models of (or for) aggression reward, addiction, and relapse: behavior and circuits.","The Journal of Neuroscience.","2019 May 22;39(21):3996-4008.","10.1523/JNEUROSCI.0151-19.2019"),
(2019,"Golden SA, Jin M, Heins C, et al.","Nucleus accumbens Drd1-expressing neurons control aggression self-administration and aggression seeking in mice.","The Journal of Neuroscience.","2019 Mar 27;39(13):2482-2496.","10.1523/JNEUROSCI.2409-18.2019"),
(2018,"Venniro M, Zhang M, Caprioli D, et al.","Volitional social interaction prevents drug addiction in rat models.","Nature Neuroscience.","2018 Oct 15.","10.1038/s41593-018-0246-6"),
(2018,"Aleyasin H, Flanigan ME, Golden SA, et al.","Cell-Type-Specific Role of ΔFosB in Nucleus Accumbens in Modulating Intermale Aggression.","J Neurosci.","2018 Jun 27;38(26):5913-5924.","10.1523/JNEUROSCI.0296-18.2018"),
(2018,"Wang J, Hodes GE, Zhang H, et al.","Epigenetic modulation of inflammation and synaptic plasticity promotes resilience against stress in mice.","Nat Commun.","2018 Feb 2;9(1):477.","10.1038/s41467-017-02794-5"),
(2018,"Heshmati M, Aleyasin H, Menard C, et al.","Cell-type-specific role for nucleus accumbens neuroligin-2 in depression and stress susceptibility.","Proc Natl Acad Sci U S A.","2018 Jan 30;115(5):1111-1116.","10.1073/pnas.1719014115"),
(2018,"Golden SA, Shaham Y.","Aggression addiction and relapse: a new frontier in psychiatry.","Neuropsychopharmacology.","2018 Jan;43(1):224-225.","10.1038/npp.2017.173"),
(2018,"Golden SA, Takahashi A.","Combinatorial psycho-pharmacological approaches for the treatment of abnormal aggression.","Neuropsychopharmacology.","2018 Jan;43(2):233-234.","10.1038/npp.2017.174"),
(2017,"Chandra R, Engeln M, Schiefer C, et al.","Drp1 Mitochondrial Fission in D1 Neurons Mediates Behavioral and Cellular Plasticity during Early Cocaine Abstinence.","Neuron.","2017 Dec 20;96(6):1327-1341.e6.","10.1016/j.neuron.2017.11.037"),
(2017,"Menard C, Pfau ML, Hodes GE, et al.","Social stress induces neurovascular pathology promoting depression.","Nat Neurosci.","2017 Dec;20(12):1752-1760.","10.1038/s41593-017-0010-3"),
(2017,"Flanigan M, Aleyasin H, Takahashi A, et al.","An emerging role for the lateral habenula in aggressive behavior.","Pharmacol Biochem Behav.","2017 Nov;162:79-86.","10.1016/j.pbb.2017.05.003"),
(2017,"Golden SA, Heins C, Venniro M, et al.","Compulsive addiction-like aggressive behavior in mice.","Biol Psychiatry.","2017 Aug 15;82(4):239-248.","10.1016/j.biopsych.2017.03.004"),
(2017,"Golden SA, Aleyasin H, Heins R, et al.","Persistent conditioned place preference to aggression experience in adult male sexually-experienced CD-1 mice.","Genes Brain Behav.","2017 Jan;16(1):44-55.","10.1111/gbb.12310"),
(2016,"Pfau ML, Purushothaman I, Feng J, et al.","Integrative Analysis of Sex-Specific microRNA Networks Following Stress in Mouse Nucleus Accumbens.","Front Mol Neurosci.","2016 Dec 23;9:144.","10.3389/fnmol.2016.00144"),
(2016,"Golden SA, Heshmati M, Flanigan M, et al.","Basal forebrain projections to the lateral habenula modulate aggression reward.","Nature.","2016 Jun 30;534(7609):688-92.","10.1038/nature18601"),
(2016,"Heshmati M, Golden SA, Pfau ML, et al.","Mefloquine in the nucleus accumbens promotes social avoidance and anxiety-like behavior in mice.","Neuropharmacology.","2016 Feb;101:351-7.","10.1016/j.neuropharm.2015.10.013"),
(2015,"Hodes GE, Pfau ML, Purushothaman I, et al.","Sex Differences in Nucleus Accumbens Transcriptome Profiles Associated with Susceptibility versus Resilience to Subchronic Variable Stress.","J Neurosci.","2015 Dec 16;35(50):16362-76.","10.1523/JNEUROSCI.1392-15.2015"),
(2015,"Sun H, Damez-Werno DM, Scobie KN, et al.","ACF chromatin-remodeling complex mediates stress-induced depressive-like behavior.","Nat Med.","2015 Oct;21(10):1146-53.","10.1038/nm.3939"),
(2015,"Donahue RJ, Landino SM, Golden SA, et al.","Effects of acute and chronic social defeat stress are differentially mediated by the dynorphin/kappa-opioid receptor system.","Behav Pharmacol.","2015 Oct;26(7 Spec No):654-63.","10.1097/FBP.0000000000000155"),
(2015,"Christoffel DJ, Golden SA, Walsh JJ, et al.","Excitatory transmission at thalamo-striatal synapses mediates susceptibility to social stress.","Nat Neurosci.","2015 Jul;18(7):962-4.","10.1038/nn.4034"),
(2014,"Heller EA, Cates HM, Peña CJ, et al.","Locus-specific epigenetic remodeling controls addiction- and depression-related behaviors.","Nat Neurosci.","2014 Dec;17(12):1720-7.","10.1038/nn.3871"),
]

out = []
for year, authors, title, journal, detail, doi in pubs:
    out.append({
        "year": year,
        "authors": authors,
        "title": title,
        "journal": journal,
        "detail": detail,
        "doi": doi,
    })

with open("/home/claude/lab-site-migration/site/content/publications.yaml", "w") as f:
    yaml.dump({"publications": out}, f, sort_keys=False, allow_unicode=True, width=1000)

print(f"Wrote {len(out)} publications")
