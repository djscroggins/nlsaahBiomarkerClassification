# %%
import os
import pandas as pd
import numpy as np

# %% Biomarker data
path = '~/Documents/GitHub/nlsaahBiomarkerClassification/rebuild/preprocessing/rawDataSets/'
# path = os.path.dirname(os.path.abspath(__file__))

# gluc_homeo = pd.read_csv(path + 'glucoseHomeostasis.tsv', sep='\t', header=0, na_values=' ')
# inf_imm_func = pd.read_csv(path + 'inflammationAndImmuneFunction.tsv', sep='\t', header=0, na_values=' ')
# lipids = pd.read_csv(path + 'lipids.tsv', sep='\t', header=0, na_values=' ')

# %% Wave data

wave_1 = pd.read_csv(path + 'wave1_inHomeQuest.tsv', sep='\t', header=0, na_values=' ')
# wave_2 = pd.read_csv(path + 'wave1_inHomeQuest.tsv', sep='\t', header=0, na_values=' ')
# wave_3 = pd.read_csv(path + 'wave1_inHomeQuest.tsv', sep='\t', header=0, na_values=' ')
# wave_4 = pd.read_csv(path + 'wave1_inHomeQuest.tsv', sep='\t', header=0, na_values=' ')

# %% Public Use Contextual database

wave1_public_use = pd.read_csv(path + 'wave1_publicUseContDB.tsv', sep='\t', header=0, na_values=' ')
# wave2_public_use = pd.read_csv(path + 'wave2_publicUseContDB.tsv', sep='\t', header=0, na_values=' ')

# %% Merging waves 1 & 2 with PUCD

wave_1 = pd.merge(left=wave_1, right=wave1_public_use, left_on='AID', right_on='AID')
# wave_2 = pd.merge(left=wave_2, right=wave2_public_use, left_on='AID', right_on='AID')

# %% Merging waves with biomarkers

# wave_1_gluc = pd.merge(left=wave_1, right=gluc_homeo, left_on='AID', right_on='AID')
# wave_1_infImm = pd.merge(left=wave_1, right=inf_imm_func, left_on='AID', right_on='AID')
# wave_1_lipids = pd.merge(left=wave_1, right=lipids, left_on='AID', right_on='AID')
#
# wave_2_gluc = pd.merge(left=wave_2, right=gluc_homeo, left_on='AID', right_on='AID')
# wave_2_infImm = pd.merge(left=wave_2, right=inf_imm_func, left_on='AID', right_on='AID')
# wave_2_lipids = pd.merge(left=wave_2, right=lipids, left_on='AID', right_on='AID')
#
# wave_3_gluc = pd.merge(left=wave_3, right=gluc_homeo, left_on='AID', right_on='AID')
# wave_3_infImm = pd.merge(left=wave_3, right=inf_imm_func, left_on='AID', right_on='AID')
# wave_3_lipids = pd.merge(left=wave_3, right=lipids, left_on='AID', right_on='AID')
#
# wave_4_gluc = pd.merge(left=wave_4, right=gluc_homeo, left_on='AID', right_on='AID')
# wave_4_infImm = pd.merge(left=wave_4, right=inf_imm_func, left_on='AID', right_on='AID')
# wave_4_lipids = pd.merge(left=wave_4, right=lipids, left_on='AID', right_on='AID')

# %% Filtering for desired features

# SELECTED FEATURES (SEE 21600-0001-Codebook_Questionnaire.pdf for more details):
    # H1GI: General Introductory (age, residence, ethnicity etc.)
    # H1FS: Feelings Scale
    # H1WP: Relations with Parents
    # H1MO: Motivations to Engage in Risky Behaviors
    # H1PF: Personality and Family
    # H1FV: Fighting and Violence
    # H1PA: Parent's Attitudes
    # H1PR: Protective Factors
    # H1NB: Neighorhood
    # H1EE: Expectations, Employment, Income


selected_sections = ['H1GI', 'H1FS', 'H1WP1', 'H1MO', 'H1PF', 'H1FV', 'H1PA', 'H1PR', 'H1NB', 'H1EE']
df_cols = list(wave_1.columns)
selected_features = [feat for feat in df_cols for sect in selected_sections if feat.startswith(sect)]
wave_1 = wave_1.filter(selected_features)

# %% Dealing with missing data
b = wave_1.isna().sum().sum()
print(b)

a = wave_1.columns[wave_1.isna().any()].tolist()
print(a)

# %% Write to filte

wave_1.to_csv('wave_1_clean.csv')
