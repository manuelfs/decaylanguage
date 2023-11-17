# Copyright (c) 2018-2023, Eduardo Rodrigues and Henry Schreiner.
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or https://github.com/scikit-hep/decaylanguage for details.

"""
Collection of enums and info to help characterising .dec decay files.
"""

from __future__ import annotations

from enum import IntEnum


class PhotosEnum(IntEnum):
    no = 0
    yes = 1


# This list should match the list specified in the decay file parser file
# 'decaylanguage/data/decfile.lark'!
known_decay_models = (
    "BaryonPCR",
    "BC_SMN",
    "BC_TMN",
    "BC_VHAD",
    "BC_VMN",
    "BCL",
    "BGL",
    "BLLNUL",
    "BNOCB0TO4PICP",
    "BNOCBPTO3HPI0",
    "BNOCBPTOKSHHH",
    "BS_MUMUKK",
    "BSTOGLLISRFSR",
    "BSTOGLLMNT",
    "BT02PI_CP_ISO",
    "BTO3PI_CP",
    "BTODDALITZCPK",
    "BToDiBaryonlnupQCD",
    "BTOSLLALI",
    "BTOSLLBALL",
    "BTOSLLMS",
    "BTOSLLMSEXT",
    "BTOVLNUBALL",
    "BTOXSGAMMA",
    "BTOXELNU",
    "BTOXSLL",
    "BQTOLLLLHYPERCP",
    "BQTOLLLL",
    "CB3PI-MPP",
    "CB3PI-P00",
    "D_DALITZ",
    "D_hhhh",
    "D0GAMMADALITZ",
    "D0MIXDALITZ",
    "DToKpienu",
    "ETAPRIME_DALITZ",
    "ETA_DALITZ",
    "ETA_FULLDALITZ",
    "ETA_LLPIPI",
    "ETA_PI0DALITZ",
    "FLATQ2",
    "FLATSQDALITZ",
    "FOURBODYPHSP",
    "GENERIC_DALITZ",
    "GOITY_ROBERTS",
    "HELAMP",
    "HQET3",
    "HQET2",
    "HQET",
    "ISGW2",
    "ISGW",
    "KS_PI0MUMU",
    "Lb2Baryonlnu",
    "Lb2plnuLCSR",
    "Lb2plnuLQCD",
    "LbAmpGen",
    "LLSW",
    "LNUGAMMA",
    "MELIKHOV",
    "OMEGA_DALITZ",
    "PARTWAVE",
    "PHI_DALITZ",
    "PHSPDECAYTIMECUT",
    "PHSPFLATLIFETIME",
    "PHSP",
    "PI0_DALITZ",
    "PROPSLPOLE",
    "PTO3P",
    "PVV_CPLH",
    "PYCONT",
    "PYTHIA",
    "RareLbToLll",
    "SLBKPOLE",
    "SLL",
    "SLN",
    "SLPOLE",
    "SSD_CP",
    "SSD_DirectCP",
    "SSS_CP_PNG",
    "SSS_CP",
    "SSS_CPT",
    "STS_CP",
    "STS",
    "SVP_CP",
    "SVP_HELAMP",
    "SVP",
    "SVS_CP_ISO",
    "SVS_CPLH",
    "SVS_CP",
    "SVS_NONCPEIGEN",
    "SVS",
    "SVV_CPLH",
    "SVV_CP",
    "SVV_HELAMP",
    "SVV_NONCPEIGEN",
    "SVVHELCPMIX",
    "TAUHADNU",
    "TAULNUNU",
    "TAUOLA",
    "TAUSCALARNU",
    "TAUVECTORNU",
    "THREEBODYPHSP",
    "TSS",
    "TVP",
    "TVS_PWAVE",
    "VLL",
    "VSP_PWAVE",
    "VSS_BMIX",
    "VSS_MIX",
    "VSS",
    "VTOSLL",
    "VUB",
    "VVPIPI",
    "VVP",
    "VVS_PWAVE",
    "XLL",
    "YMSTOYNSPIPICLEO",
    "YMSTOYNSPIPICLEOBOOST",
)
