# This is a python3 file:
#     - The object defined here is a python3 dictionary.
#     - It can be imported into python3 code with the code:
#         `return_dict = ast.literal_eval('/pathto/high-level-triggers.py')`
#     where `ast` is a python3 module available in `pip3`
#
# This file define the triggers used in Sirius operation system and
# maps them with several important properties.
{
    'SI-Glob:TI-Corrs': {
        'database': {
            'Src': {'value': 0, 'enums': ('MigSI', 'OrbSI', 'Cycle', 'Study')},
            'Delay': {'value': 0.0, 'hilim': 1.0, 'high': 1.0, 'hihi': 1.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {
                'value': 3920, 'hilim': 4001, 'high': 4001, 'hihi': 4001},
            'Duration': {'value': 2000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'SI-01M1:PS-CH:RS485',    'SI-01M1:PS-CV:RS485',
            'SI-01M2:PS-CH:RS485',    'SI-01M2:PS-CV:RS485',
            'SI-01C1:PS-CH:RS485',    'SI-01C1:PS-CV:RS485',
            'SI-01C2:PS-CH:RS485',    'SI-01C2:PS-CV-1:RS485',
            'SI-01C2:PS-CV-2:RS485',
            'SI-01C3:PS-CH:RS485',    'SI-01C3:PS-CV-1:RS485',
            'SI-01C3:PS-CV-2:RS485',
            'SI-01C4:PS-CH:RS485',    'SI-01C4:PS-CV:RS485',

            'SI-02M1:PS-CH:RS485',    'SI-02M1:PS-CV:RS485',
            'SI-02M2:PS-CH:RS485',    'SI-02M2:PS-CV:RS485',
            'SI-02C1:PS-CH:RS485',    'SI-02C1:PS-CV:RS485',
            'SI-02C2:PS-CH:RS485',    'SI-02C2:PS-CV-1:RS485',
            'SI-02C2:PS-CV-2:RS485',
            'SI-02C3:PS-CH:RS485',    'SI-02C3:PS-CV-1:RS485',
            'SI-02C3:PS-CV-2:RS485',
            'SI-02C4:PS-CH:RS485',    'SI-02C4:PS-CV:RS485',

            'SI-03M1:PS-CH:RS485',    'SI-03M1:PS-CV:RS485',
            'SI-03M2:PS-CH:RS485',    'SI-03M2:PS-CV:RS485',
            'SI-03C1:PS-CH:RS485',    'SI-03C1:PS-CV:RS485',
            'SI-03C2:PS-CH:RS485',    'SI-03C2:PS-CV-1:RS485',
            'SI-03C2:PS-CV-2:RS485',
            'SI-03C3:PS-CH:RS485',    'SI-03C3:PS-CV-1:RS485',
            'SI-03C3:PS-CV-2:RS485',
            'SI-03C4:PS-CH:RS485',    'SI-03C4:PS-CV:RS485',

            'SI-04M1:PS-CH:RS485',    'SI-04M1:PS-CV:RS485',
            'SI-04M2:PS-CH:RS485',    'SI-04M2:PS-CV:RS485',
            'SI-04C1:PS-CH:RS485',    'SI-04C1:PS-CV:RS485',
            'SI-04C2:PS-CH:RS485',    'SI-04C2:PS-CV-1:RS485',
            'SI-04C2:PS-CV-2:RS485',
            'SI-04C3:PS-CH:RS485',    'SI-04C3:PS-CV-1:RS485',
            'SI-04C3:PS-CV-2:RS485',
            'SI-04C4:PS-CH:RS485',    'SI-04C4:PS-CV:RS485',

            'SI-05M1:PS-CH:RS485',    'SI-05M1:PS-CV:RS485',
            'SI-05M2:PS-CH:RS485',    'SI-05M2:PS-CV:RS485',
            'SI-05C1:PS-CH:RS485',    'SI-05C1:PS-CV:RS485',
            'SI-05C2:PS-CH:RS485',    'SI-05C2:PS-CV-1:RS485',
            'SI-05C2:PS-CV-2:RS485',
            'SI-05C3:PS-CH:RS485',    'SI-05C3:PS-CV-1:RS485',
            'SI-05C3:PS-CV-2:RS485',
            'SI-05C4:PS-CH:RS485',    'SI-05C4:PS-CV:RS485',

            'SI-06M1:PS-CH:RS485',    'SI-06M1:PS-CV:RS485',
            'SI-06M2:PS-CH:RS485',    'SI-06M2:PS-CV:RS485',
            'SI-06C1:PS-CH:RS485',    'SI-06C1:PS-CV:RS485',
            'SI-06C2:PS-CH:RS485',    'SI-06C2:PS-CV-1:RS485',
            'SI-06C2:PS-CV-2:RS485',
            'SI-06C3:PS-CH:RS485',    'SI-06C3:PS-CV-1:RS485',
            'SI-06C3:PS-CV-2:RS485',
            'SI-06C4:PS-CH:RS485',    'SI-06C4:PS-CV:RS485',

            'SI-07M1:PS-CH:RS485',    'SI-07M1:PS-CV:RS485',
            'SI-07M2:PS-CH:RS485',    'SI-07M2:PS-CV:RS485',
            'SI-07C1:PS-CH:RS485',    'SI-07C1:PS-CV:RS485',
            'SI-07C2:PS-CH:RS485',    'SI-07C2:PS-CV-1:RS485',
            'SI-07C2:PS-CV-2:RS485',
            'SI-07C3:PS-CH:RS485',    'SI-07C3:PS-CV-1:RS485',
            'SI-07C3:PS-CV-2:RS485',
            'SI-07C4:PS-CH:RS485',    'SI-07C4:PS-CV:RS485',

            'SI-08M1:PS-CH:RS485',    'SI-08M1:PS-CV:RS485',
            'SI-08M2:PS-CH:RS485',    'SI-08M2:PS-CV:RS485',
            'SI-08C1:PS-CH:RS485',    'SI-08C1:PS-CV:RS485',
            'SI-08C2:PS-CH:RS485',    'SI-08C2:PS-CV-1:RS485',
            'SI-08C2:PS-CV-2:RS485',
            'SI-08C3:PS-CH:RS485',    'SI-08C3:PS-CV-1:RS485',
            'SI-08C3:PS-CV-2:RS485',
            'SI-08C4:PS-CH:RS485',    'SI-08C4:PS-CV:RS485',

            'SI-09M1:PS-CH:RS485',    'SI-09M1:PS-CV:RS485',
            'SI-09M2:PS-CH:RS485',    'SI-09M2:PS-CV:RS485',
            'SI-09C1:PS-CH:RS485',    'SI-09C1:PS-CV:RS485',
            'SI-09C2:PS-CH:RS485',    'SI-09C2:PS-CV-1:RS485',
            'SI-09C2:PS-CV-2:RS485',
            'SI-09C3:PS-CH:RS485',    'SI-09C3:PS-CV-1:RS485',
            'SI-09C3:PS-CV-2:RS485',
            'SI-09C4:PS-CH:RS485',    'SI-09C4:PS-CV:RS485',

            'SI-10M1:PS-CH:RS485',    'SI-10M1:PS-CV:RS485',
            'SI-10M2:PS-CH:RS485',    'SI-10M2:PS-CV:RS485',
            'SI-10C1:PS-CH:RS485',    'SI-10C1:PS-CV:RS485',
            'SI-10C2:PS-CH:RS485',    'SI-10C2:PS-CV-1:RS485',
            'SI-10C2:PS-CV-2:RS485',
            'SI-10C3:PS-CH:RS485',    'SI-10C3:PS-CV-1:RS485',
            'SI-10C3:PS-CV-2:RS485',
            'SI-10C4:PS-CH:RS485',    'SI-10C4:PS-CV:RS485',

            'SI-11M1:PS-CH:RS485',    'SI-11M1:PS-CV:RS485',
            'SI-11M2:PS-CH:RS485',    'SI-11M2:PS-CV:RS485',
            'SI-11C1:PS-CH:RS485',    'SI-11C1:PS-CV:RS485',
            'SI-11C2:PS-CH:RS485',    'SI-11C2:PS-CV-1:RS485',
            'SI-11C2:PS-CV-2:RS485',
            'SI-11C3:PS-CH:RS485',    'SI-11C3:PS-CV-1:RS485',
            'SI-11C3:PS-CV-2:RS485',
            'SI-11C4:PS-CH:RS485',    'SI-11C4:PS-CV:RS485',

            'SI-12M1:PS-CH:RS485',    'SI-12M1:PS-CV:RS485',
            'SI-12M2:PS-CH:RS485',    'SI-12M2:PS-CV:RS485',
            'SI-12C1:PS-CH:RS485',    'SI-12C1:PS-CV:RS485',
            'SI-12C2:PS-CH:RS485',    'SI-12C2:PS-CV-1:RS485',
            'SI-12C2:PS-CV-2:RS485',
            'SI-12C3:PS-CH:RS485',    'SI-12C3:PS-CV-1:RS485',
            'SI-12C3:PS-CV-2:RS485',
            'SI-12C4:PS-CH:RS485',    'SI-12C4:PS-CV:RS485',

            'SI-13M1:PS-CH:RS485',    'SI-13M1:PS-CV:RS485',
            'SI-13M2:PS-CH:RS485',    'SI-13M2:PS-CV:RS485',
            'SI-13C1:PS-CH:RS485',    'SI-13C1:PS-CV:RS485',
            'SI-13C2:PS-CH:RS485',    'SI-13C2:PS-CV-1:RS485',
            'SI-13C2:PS-CV-2:RS485',
            'SI-13C3:PS-CH:RS485',    'SI-13C3:PS-CV-1:RS485',
            'SI-13C3:PS-CV-2:RS485',
            'SI-13C4:PS-CH:RS485',    'SI-13C4:PS-CV:RS485',

            'SI-14M1:PS-CH:RS485',    'SI-14M1:PS-CV:RS485',
            'SI-14M2:PS-CH:RS485',    'SI-14M2:PS-CV:RS485',
            'SI-14C1:PS-CH:RS485',    'SI-14C1:PS-CV:RS485',
            'SI-14C2:PS-CH:RS485',    'SI-14C2:PS-CV-1:RS485',
            'SI-14C2:PS-CV-2:RS485',
            'SI-14C3:PS-CH:RS485',    'SI-14C3:PS-CV-1:RS485',
            'SI-14C3:PS-CV-2:RS485',
            'SI-14C4:PS-CH:RS485',    'SI-14C4:PS-CV:RS485',

            'SI-15M1:PS-CH:RS485',    'SI-15M1:PS-CV:RS485',
            'SI-15M2:PS-CH:RS485',    'SI-15M2:PS-CV:RS485',
            'SI-15C1:PS-CH:RS485',    'SI-15C1:PS-CV:RS485',
            'SI-15C2:PS-CH:RS485',    'SI-15C2:PS-CV-1:RS485',
            'SI-15C2:PS-CV-2:RS485',
            'SI-15C3:PS-CH:RS485',    'SI-15C3:PS-CV-1:RS485',
            'SI-15C3:PS-CV-2:RS485',
            'SI-15C4:PS-CH:RS485',    'SI-15C4:PS-CV:RS485',

            'SI-16M1:PS-CH:RS485',    'SI-16M1:PS-CV:RS485',
            'SI-16M2:PS-CH:RS485',    'SI-16M2:PS-CV:RS485',
            'SI-16C1:PS-CH:RS485',    'SI-16C1:PS-CV:RS485',
            'SI-16C2:PS-CH:RS485',    'SI-16C2:PS-CV-1:RS485',
            'SI-16C2:PS-CV-2:RS485',
            'SI-16C3:PS-CH:RS485',    'SI-16C3:PS-CV-1:RS485',
            'SI-16C3:PS-CV-2:RS485',
            'SI-16C4:PS-CH:RS485',    'SI-16C4:PS-CV:RS485',

            'SI-17M1:PS-CH:RS485',    'SI-17M1:PS-CV:RS485',
            'SI-17M2:PS-CH:RS485',    'SI-17M2:PS-CV:RS485',
            'SI-17C1:PS-CH:RS485',    'SI-17C1:PS-CV:RS485',
            'SI-17C2:PS-CH:RS485',    'SI-17C2:PS-CV-1:RS485',
            'SI-17C2:PS-CV-2:RS485',
            'SI-17C3:PS-CH:RS485',    'SI-17C3:PS-CV-1:RS485',
            'SI-17C3:PS-CV-2:RS485',
            'SI-17C4:PS-CH:RS485',    'SI-17C4:PS-CV:RS485',

            'SI-18M1:PS-CH:RS485',    'SI-18M1:PS-CV:RS485',
            'SI-18M2:PS-CH:RS485',    'SI-18M2:PS-CV:RS485',
            'SI-18C1:PS-CH:RS485',    'SI-18C1:PS-CV:RS485',
            'SI-18C2:PS-CH:RS485',    'SI-18C2:PS-CV-1:RS485',
            'SI-18C2:PS-CV-2:RS485',
            'SI-18C3:PS-CH:RS485',    'SI-18C3:PS-CV-1:RS485',
            'SI-18C3:PS-CV-2:RS485',
            'SI-18C4:PS-CH:RS485',    'SI-18C4:PS-CV:RS485',

            'SI-19M1:PS-CH:RS485',    'SI-19M1:PS-CV:RS485',
            'SI-19M2:PS-CH:RS485',    'SI-19M2:PS-CV:RS485',
            'SI-19C1:PS-CH:RS485',    'SI-19C1:PS-CV:RS485',
            'SI-19C2:PS-CH:RS485',    'SI-19C2:PS-CV-1:RS485',
            'SI-19C2:PS-CV-2:RS485',
            'SI-19C3:PS-CH:RS485',    'SI-19C3:PS-CV-1:RS485',
            'SI-19C3:PS-CV-2:RS485',
            'SI-19C4:PS-CH:RS485',    'SI-19C4:PS-CV:RS485',

            'SI-20M1:PS-CH:RS485',    'SI-20M1:PS-CV:RS485',
            'SI-20M2:PS-CH:RS485',    'SI-20M2:PS-CV:RS485',
            'SI-20C1:PS-CH:RS485',    'SI-20C1:PS-CV:RS485',
            'SI-20C2:PS-CH:RS485',    'SI-20C2:PS-CV-1:RS485',
            'SI-20C2:PS-CV-2:RS485',
            'SI-20C3:PS-CH:RS485',    'SI-20C3:PS-CV-1:RS485',
            'SI-20C3:PS-CV-2:RS485',
            'SI-20C4:PS-CH:RS485',    'SI-20C4:PS-CV:RS485',
            ),
        },
    'SI-Glob:TI-Quads': {
        'database': {
            'Src': {'value': 0, 'enums': ('MigSI', 'TunSI', 'Cycle', 'Study')},
            'Delay': {'value': 0.0, 'hilim': 1.0, 'high': 1.0, 'hihi': 1.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {
                'value': 3920, 'hilim': 4001, 'high': 4001, 'hihi': 4001},
            'Duration': {'value': 2000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'SI-Fam:PS-QDA:RS485',
            'SI-Fam:PS-QFA:RS485',

            'SI-Fam:PS-QDB1:RS485',
            'SI-Fam:PS-QDB2:RS485',
            'SI-Fam:PS-QFB:RS485',

            'SI-Fam:PS-QDP1:RS485',
            'SI-Fam:PS-QDP2:RS485',
            'SI-Fam:PS-QFP:RS485',

            'SI-Fam:PS-Q1:RS485',
            'SI-Fam:PS-Q2:RS485',
            'SI-Fam:PS-Q3:RS485',
            'SI-Fam:PS-Q4:RS485',

            # 'SI-Fam:PS-QB1:RS485',
            # 'SI-Fam:PS-QB2:RS485',

            'SI-01C1:PS-Q1:RS485',        'SI-01C1:PS-Q2:RS485',
            'SI-01C2:PS-Q3:RS485',        'SI-01C2:PS-Q4:RS485',
            'SI-01C3:PS-Q4:RS485',        'SI-01C3:PS-Q3:RS485',
            'SI-01C4:PS-Q2:RS485',        'SI-01C4:PS-Q1:RS485',
            'SI-01M1:PS-QFA:RS485',       'SI-01M1:PS-QDA:RS485',
            'SI-01M2:PS-QFA:RS485',       'SI-01M2:PS-QDA:RS485',

            'SI-02C1:PS-Q1:RS485',        'SI-02C1:PS-Q2:RS485',
            'SI-02C2:PS-Q3:RS485',        'SI-02C2:PS-Q4:RS485',
            'SI-02C3:PS-Q4:RS485',        'SI-02C3:PS-Q3:RS485',
            'SI-02C4:PS-Q2:RS485',        'SI-02C4:PS-Q1:RS485',
            'SI-02M1:PS-QFB:RS485',       'SI-02M1:PS-QDB1:RS485',
            'SI-02M1:PS-QDB2:RS485',      'SI-02M2:PS-QFB:RS485',
            'SI-02M2:PS-QDB1:RS485',      'SI-02M2:PS-QDB2:RS485',

            'SI-03C1:PS-Q1:RS485',        'SI-03C1:PS-Q2:RS485',
            'SI-03C2:PS-Q3:RS485',        'SI-03C2:PS-Q4:RS485',
            'SI-03C3:PS-Q4:RS485',        'SI-03C3:PS-Q3:RS485',
            'SI-03C4:PS-Q2:RS485',        'SI-03C4:PS-Q1:RS485',
            'SI-03M1:PS-QFP:RS485',       'SI-03M1:PS-QDP1:RS485',
            'SI-03M1:PS-QDP2:RS485',
            'SI-03M2:PS-QFP:RS485',       'SI-03M2:PS-QDP1:RS485',
            'SI-03M2:PS-QDP2:RS485',

            'SI-04C1:PS-Q1:RS485',        'SI-04C1:PS-Q2:RS485',
            'SI-04C2:PS-Q3:RS485',        'SI-04C2:PS-Q4:RS485',
            'SI-04C3:PS-Q4:RS485',        'SI-04C3:PS-Q3:RS485',
            'SI-04C4:PS-Q2:RS485',        'SI-04C4:PS-Q1:RS485',
            'SI-04M1:PS-QFB:RS485',       'SI-04M1:PS-QDB1:RS485',
            'SI-04M1:PS-QDB2:RS485',      'SI-04M2:PS-QFB:RS485',
            'SI-04M2:PS-QDB1:RS485',      'SI-04M2:PS-QDB2:RS485',

            'SI-05C1:PS-Q1:RS485',        'SI-05C1:PS-Q2:RS485',
            'SI-05C2:PS-Q3:RS485',        'SI-05C2:PS-Q4:RS485',
            'SI-05C3:PS-Q4:RS485',        'SI-05C3:PS-Q3:RS485',
            'SI-05C4:PS-Q2:RS485',        'SI-05C4:PS-Q1:RS485',
            'SI-05M1:PS-QFA:RS485',       'SI-05M1:PS-QDA:RS485',
            'SI-05M2:PS-QFA:RS485',       'SI-05M2:PS-QDA:RS485',

            'SI-06C1:PS-Q1:RS485',        'SI-06C1:PS-Q2:RS485',
            'SI-06C2:PS-Q3:RS485',        'SI-06C2:PS-Q4:RS485',
            'SI-06C3:PS-Q4:RS485',        'SI-06C3:PS-Q3:RS485',
            'SI-06C4:PS-Q2:RS485',        'SI-06C4:PS-Q1:RS485',
            'SI-06M1:PS-QFB:RS485',       'SI-06M1:PS-QDB1:RS485',
            'SI-06M1:PS-QDB2:RS485',
            'SI-06M2:PS-QFB:RS485',       'SI-06M2:PS-QDB1:RS485',
            'SI-06M2:PS-QDB2:RS485',

            'SI-07C1:PS-Q1:RS485',        'SI-07C1:PS-Q2:RS485',
            'SI-07C2:PS-Q3:RS485',        'SI-07C2:PS-Q4:RS485',
            'SI-07C3:PS-Q4:RS485',        'SI-07C3:PS-Q3:RS485',
            'SI-07C4:PS-Q2:RS485',        'SI-07C4:PS-Q1:RS485',
            'SI-07M1:PS-QFP:RS485',       'SI-07M1:PS-QDP1:RS485',
            'SI-07M1:PS-QDP2:RS485',
            'SI-07M2:PS-QFP:RS485',       'SI-07M2:PS-QDP1:RS485',
            'SI-07M2:PS-QDP2:RS485',

            'SI-08C1:PS-Q1:RS485',        'SI-08C1:PS-Q2:RS485',
            'SI-08C2:PS-Q3:RS485',        'SI-08C2:PS-Q4:RS485',
            'SI-08C3:PS-Q4:RS485',        'SI-08C3:PS-Q3:RS485',
            'SI-08C4:PS-Q2:RS485',        'SI-08C4:PS-Q1:RS485',
            'SI-08M1:PS-QFB:RS485',       'SI-08M1:PS-QDB1:RS485',
            'SI-08M1:PS-QDB2:RS485',
            'SI-08M2:PS-QFB:RS485',       'SI-08M2:PS-QDB1:RS485',
            'SI-08M2:PS-QDB2:RS485',

            'SI-09C1:PS-Q1:RS485',        'SI-09C1:PS-Q2:RS485',
            'SI-09C2:PS-Q3:RS485',        'SI-09C2:PS-Q4:RS485',
            'SI-09C3:PS-Q4:RS485',        'SI-09C3:PS-Q3:RS485',
            'SI-09C4:PS-Q2:RS485',        'SI-09C4:PS-Q1:RS485',
            'SI-09M1:PS-QFA:RS485',       'SI-09M1:PS-QDA:RS485',
            'SI-09M2:PS-QFA:RS485',       'SI-09M2:PS-QDA:RS485',

            'SI-10C1:PS-Q1:RS485',        'SI-10C1:PS-Q2:RS485',
            'SI-10C2:PS-Q3:RS485',        'SI-10C2:PS-Q4:RS485',
            'SI-10C3:PS-Q4:RS485',        'SI-10C3:PS-Q3:RS485',
            'SI-10C4:PS-Q2:RS485',        'SI-10C4:PS-Q1:RS485',
            'SI-10M1:PS-QFB:RS485',       'SI-10M1:PS-QDB1:RS485',
            'SI-10M1:PS-QDB2:RS485',      'SI-10M2:PS-QFB:RS485',
            'SI-10M2:PS-QDB1:RS485',      'SI-10M2:PS-QDB2:RS485',

            'SI-11C1:PS-Q1:RS485',        'SI-11C1:PS-Q2:RS485',
            'SI-11C2:PS-Q3:RS485',        'SI-11C2:PS-Q4:RS485',
            'SI-11C3:PS-Q4:RS485',        'SI-11C3:PS-Q3:RS485',
            'SI-11C4:PS-Q2:RS485',        'SI-11C4:PS-Q1:RS485',
            'SI-11M1:PS-QFP:RS485',       'SI-11M1:PS-QDP1:RS485',
            'SI-11M1:PS-QDP2:RS485',
            'SI-11M2:PS-QFP:RS485',       'SI-11M2:PS-QDP1:RS485',
            'SI-11M2:PS-QDP2:RS485',

            'SI-12C1:PS-Q1:RS485',        'SI-12C1:PS-Q2:RS485',
            'SI-12C2:PS-Q3:RS485',        'SI-12C2:PS-Q4:RS485',
            'SI-12C3:PS-Q4:RS485',        'SI-12C3:PS-Q3:RS485',
            'SI-12C4:PS-Q2:RS485',        'SI-12C4:PS-Q1:RS485',
            'SI-12M1:PS-QFB:RS485',       'SI-12M1:PS-QDB1:RS485',
            'SI-12M1:PS-QDB2:RS485',
            'SI-12M2:PS-QFB:RS485',       'SI-12M2:PS-QDB1:RS485',
            'SI-12M2:PS-QDB2:RS485',

            'SI-13C1:PS-Q1:RS485',        'SI-13C1:PS-Q2:RS485',
            'SI-13C2:PS-Q3:RS485',        'SI-13C2:PS-Q4:RS485',
            'SI-13C3:PS-Q4:RS485',        'SI-13C3:PS-Q3:RS485',
            'SI-13C4:PS-Q2:RS485',        'SI-13C4:PS-Q1:RS485',
            'SI-13M1:PS-QFA:RS485',       'SI-13M1:PS-QDA:RS485',
            'SI-13M2:PS-QFA:RS485',       'SI-13M2:PS-QDA:RS485',

            'SI-14C1:PS-Q1:RS485',        'SI-14C1:PS-Q2:RS485',
            'SI-14C2:PS-Q3:RS485',        'SI-14C2:PS-Q4:RS485',
            'SI-14C3:PS-Q4:RS485',        'SI-14C3:PS-Q3:RS485',
            'SI-14C4:PS-Q2:RS485',        'SI-14C4:PS-Q1:RS485',
            'SI-14M1:PS-QFB:RS485',       'SI-14M1:PS-QDB1:RS485',
            'SI-14M1:PS-QDB2:RS485',
            'SI-14M2:PS-QFB:RS485',       'SI-14M2:PS-QDB1:RS485',
            'SI-14M2:PS-QDB2:RS485',

            'SI-15C1:PS-Q1:RS485',        'SI-15C1:PS-Q2:RS485',
            'SI-15C2:PS-Q3:RS485',        'SI-15C2:PS-Q4:RS485',
            'SI-15C3:PS-Q4:RS485',        'SI-15C3:PS-Q3:RS485',
            'SI-15C4:PS-Q2:RS485',        'SI-15C4:PS-Q1:RS485',
            'SI-15M1:PS-QFP:RS485',       'SI-15M1:PS-QDP1:RS485',
            'SI-15M1:PS-QDP2:RS485',
            'SI-15M2:PS-QFP:RS485',       'SI-15M2:PS-QDP1:RS485',
            'SI-15M2:PS-QDP2:RS485',

            'SI-16C1:PS-Q1:RS485',        'SI-16C1:PS-Q2:RS485',
            'SI-16C2:PS-Q3:RS485',        'SI-16C2:PS-Q4:RS485',
            'SI-16C3:PS-Q4:RS485',        'SI-16C3:PS-Q3:RS485',
            'SI-16C4:PS-Q2:RS485',        'SI-16C4:PS-Q1:RS485',
            'SI-16M1:PS-QFB:RS485',       'SI-16M1:PS-QDB1:RS485',
            'SI-16M1:PS-QDB2:RS485',
            'SI-16M2:PS-QFB:RS485',       'SI-16M2:PS-QDB1:RS485',
            'SI-16M2:PS-QDB2:RS485',

            'SI-17C1:PS-Q1:RS485',        'SI-17C1:PS-Q2:RS485',
            'SI-17C2:PS-Q3:RS485',        'SI-17C2:PS-Q4:RS485',
            'SI-17C3:PS-Q4:RS485',        'SI-17C3:PS-Q3:RS485',
            'SI-17C4:PS-Q2:RS485',        'SI-17C4:PS-Q1:RS485',
            'SI-17M1:PS-QFA:RS485',       'SI-17M1:PS-QDA:RS485',
            'SI-17M2:PS-QFA:RS485',       'SI-17M2:PS-QDA:RS485',

            'SI-18C1:PS-Q1:RS485',        'SI-18C1:PS-Q2:RS485',
            'SI-18C2:PS-Q3:RS485',        'SI-18C2:PS-Q4:RS485',
            'SI-18C3:PS-Q4:RS485',        'SI-18C3:PS-Q3:RS485',
            'SI-18C4:PS-Q2:RS485',        'SI-18C4:PS-Q1:RS485',
            'SI-18M1:PS-QFB:RS485',       'SI-18M1:PS-QDB1:RS485',
            'SI-18M1:PS-QDB2:RS485',
            'SI-18M2:PS-QFB:RS485',       'SI-18M2:PS-QDB1:RS485',
            'SI-18M2:PS-QDB2:RS485',

            'SI-19C1:PS-Q1:RS485',        'SI-19C1:PS-Q2:RS485',
            'SI-19C2:PS-Q3:RS485',        'SI-19C2:PS-Q4:RS485',
            'SI-19C3:PS-Q4:RS485',        'SI-19C3:PS-Q3:RS485',
            'SI-19C4:PS-Q2:RS485',        'SI-19C4:PS-Q1:RS485',
            'SI-19M1:PS-QFP:RS485',       'SI-19M1:PS-QDP1:RS485',
            'SI-19M1:PS-QDP2:RS485',
            'SI-19M2:PS-QFP:RS485',       'SI-19M2:PS-QDP1:RS485',
            'SI-19M2:PS-QDP2:RS485',

            'SI-20C1:PS-Q1:RS485',        'SI-20C1:PS-Q2:RS485',
            'SI-20C2:PS-Q3:RS485',        'SI-20C2:PS-Q4:RS485',
            'SI-20C3:PS-Q4:RS485',        'SI-20C3:PS-Q3:RS485',
            'SI-20C4:PS-Q2:RS485',        'SI-20C4:PS-Q1:RS485',
            'SI-20M1:PS-QFB:RS485',       'SI-20M1:PS-QDB1:RS485',
            'SI-20M1:PS-QDB2:RS485',
            'SI-20M2:PS-QFB:RS485',       'SI-20M2:PS-QDB1:RS485',
            'SI-20M2:PS-QDB2:RS485',
            ),
        },
    'SI-Glob:TI-Skews': {
        'database': {
            'Src': {'value': 0, 'enums': ('MigSI', 'CplSI', 'Cycle', 'Study')},
            'Delay': {'value': 0.0, 'hilim': 1.0, 'high': 1.0, 'hihi': 1.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {
                'value': 3920, 'hilim': 4001, 'high': 4001, 'hihi': 4001},
            'Duration': {'value': 2000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'SI-01M1:PS-QS:RS485',
            'SI-01M2:PS-QS:RS485',
            'SI-01C1:PS-QS:RS485',
            'SI-01C2:PS-QS:RS485',
            'SI-01C3:PS-QS:RS485',

            'SI-02M1:PS-QS:RS485',
            'SI-02M2:PS-QS:RS485',
            'SI-02C1:PS-QS:RS485',
            'SI-02C2:PS-QS:RS485',
            'SI-02C3:PS-QS:RS485',

            'SI-03M1:PS-QS:RS485',
            'SI-03M2:PS-QS:RS485',
            'SI-03C1:PS-QS:RS485',
            'SI-03C2:PS-QS:RS485',
            'SI-03C3:PS-QS:RS485',

            'SI-04M1:PS-QS:RS485',
            'SI-04M2:PS-QS:RS485',
            'SI-04C1:PS-QS:RS485',
            'SI-04C2:PS-QS:RS485',
            'SI-04C3:PS-QS:RS485',

            'SI-05M1:PS-QS:RS485',
            'SI-05M2:PS-QS:RS485',
            'SI-05C1:PS-QS:RS485',
            'SI-05C2:PS-QS:RS485',
            'SI-05C3:PS-QS:RS485',

            'SI-06M1:PS-QS:RS485',
            'SI-06M2:PS-QS:RS485',
            'SI-06C1:PS-QS:RS485',
            'SI-06C2:PS-QS:RS485',
            'SI-06C3:PS-QS:RS485',

            'SI-07M1:PS-QS:RS485',
            'SI-07M2:PS-QS:RS485',
            'SI-07C1:PS-QS:RS485',
            'SI-07C2:PS-QS:RS485',
            'SI-07C3:PS-QS:RS485',

            'SI-08M1:PS-QS:RS485',
            'SI-08M2:PS-QS:RS485',
            'SI-08C1:PS-QS:RS485',
            'SI-08C2:PS-QS:RS485',
            'SI-08C3:PS-QS:RS485',

            'SI-09M1:PS-QS:RS485',
            'SI-09M2:PS-QS:RS485',
            'SI-09C1:PS-QS:RS485',
            'SI-09C2:PS-QS:RS485',
            'SI-09C3:PS-QS:RS485',

            'SI-10M1:PS-QS:RS485',
            'SI-10M2:PS-QS:RS485',
            'SI-10C1:PS-QS:RS485',
            'SI-10C2:PS-QS:RS485',
            'SI-10C3:PS-QS:RS485',

            'SI-11M1:PS-QS:RS485',
            'SI-11M2:PS-QS:RS485',
            'SI-11C1:PS-QS:RS485',
            'SI-11C2:PS-QS:RS485',
            'SI-11C3:PS-QS:RS485',

            'SI-12M1:PS-QS:RS485',
            'SI-12M2:PS-QS:RS485',
            'SI-12C1:PS-QS:RS485',
            'SI-12C2:PS-QS:RS485',
            'SI-12C3:PS-QS:RS485',

            'SI-13M1:PS-QS:RS485',
            'SI-13M2:PS-QS:RS485',
            'SI-13C1:PS-QS:RS485',
            'SI-13C2:PS-QS:RS485',
            'SI-13C3:PS-QS:RS485',

            'SI-14M1:PS-QS:RS485',
            'SI-14M2:PS-QS:RS485',
            'SI-14C1:PS-QS:RS485',
            'SI-14C2:PS-QS:RS485',
            'SI-14C3:PS-QS:RS485',

            'SI-15M1:PS-QS:RS485',
            'SI-15M2:PS-QS:RS485',
            'SI-15C1:PS-QS:RS485',
            'SI-15C2:PS-QS:RS485',
            'SI-15C3:PS-QS:RS485',

            'SI-16M1:PS-QS:RS485',
            'SI-16M2:PS-QS:RS485',
            'SI-16C1:PS-QS:RS485',
            'SI-16C2:PS-QS:RS485',
            'SI-16C3:PS-QS:RS485',

            'SI-17M1:PS-QS:RS485',
            'SI-17M2:PS-QS:RS485',
            'SI-17C1:PS-QS:RS485',
            'SI-17C2:PS-QS:RS485',
            'SI-17C3:PS-QS:RS485',

            'SI-18M1:PS-QS:RS485',
            'SI-18M2:PS-QS:RS485',
            'SI-18C1:PS-QS:RS485',
            'SI-18C2:PS-QS:RS485',
            'SI-18C3:PS-QS:RS485',

            'SI-19M1:PS-QS:RS485',
            'SI-19M2:PS-QS:RS485',
            'SI-19C1:PS-QS:RS485',
            'SI-19C2:PS-QS:RS485',
            'SI-19C3:PS-QS:RS485',

            'SI-20M1:PS-QS:RS485',
            'SI-20M2:PS-QS:RS485',
            'SI-20C1:PS-QS:RS485',
            'SI-20C2:PS-QS:RS485',
            'SI-20C3:PS-QS:RS485',
            ),
        },
    'SI-Glob:TI-Dips': {
        'database': {
            'Src': {'value': 0, 'enums': ('MigSI', 'Cycle', 'Study')},
            'Delay': {'value': 0.0, 'hilim': 1.0, 'high': 1.0, 'hihi': 1.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {
                'value': 3920, 'hilim': 4001, 'high': 4001, 'hihi': 4001},
            'Duration': {'value': 2000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'SI-Fam:PS-B1B2-1:RS485',
            'SI-Fam:PS-B1B2-2:RS485',
            ),
        },
    'SI-Glob:TI-Sexts': {
        'database': {
            'Src': {'value': 0, 'enums': ('MigSI', 'Cycle', 'Study')},
            'Delay': {'value': 0.0, 'hilim': 1.0, 'high': 1.0, 'hihi': 1.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {
                'value': 3920, 'hilim': 4001, 'high': 4001, 'hihi': 4001},
            'Duration': {'value': 2000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'SI-Fam:PS-SFA0:RS485',    'SI-Fam:PS-SFA1:RS485',
            'SI-Fam:PS-SFA2:RS485',
            'SI-Fam:PS-SDA0:RS485',    'SI-Fam:PS-SDA1:RS485',
            'SI-Fam:PS-SDA2:RS485',    'SI-Fam:PS-SDA3:RS485',
            'SI-Fam:PS-SFB0:RS485',    'SI-Fam:PS-SFB1:RS485',
            'SI-Fam:PS-SFB2:RS485',
            'SI-Fam:PS-SDB0:RS485',    'SI-Fam:PS-SDB1:RS485',
            'SI-Fam:PS-SDB2:RS485',    'SI-Fam:PS-SDB3:RS485',
            'SI-Fam:PS-SFP0:RS485',    'SI-Fam:PS-SFP1:RS485',
            'SI-Fam:PS-SFP2:RS485',
            'SI-Fam:PS-SDP0:RS485',    'SI-Fam:PS-SDP1:RS485',
            'SI-Fam:PS-SDP2:RS485',    'SI-Fam:PS-SDP3:RS485',
            ),
        },
    'BO-Glob:TI-Mags': {
        'database': {
            'Src': {'value': 0, 'enums': ('RmpBO', 'Cycle', 'Study')},
            'Delay': {'value': 0.0, 'hilim': 1.0, 'high': 1.0, 'hihi': 1.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {
                'value': 3920, 'hilim': 4001, 'high': 4001, 'hihi': 4001},
            'Duration': {
                'value': 490000,
                'hilim': 495000, 'high': 495000, 'hihi': 500000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'BO-Fam:PS-B-1:RS485',    'BO-Fam:PS-B-2:RS485',
            'BO-Fam:PS-QF:RS485',     'BO-Fam:PS-QD:RS485',
            'BO-Fam:PS-SF:RS485',     'BO-Fam:PS-SD:RS485',
            ),
        },
    'BO-Glob:TI-Corrs': {
        'database': {
            'Src': {'value': 0, 'enums': ('RmpBO', 'OrbBO', 'Cycle', 'Study')},
            'Delay': {'value': 0.0, 'hilim': 1.0, 'high': 1.0, 'hihi': 1.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {
                'value': 3920, 'hilim': 4001, 'high': 4001, 'hihi': 4001},
            'Duration': {
                'value': 490000,
                'hilim': 495000, 'high': 495000, 'hihi': 500000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'BO-01U:PS-CH:RS485', 'BO-01U:PS-CV:RS485',
            'BO-02D:PS-QS:RS485',
            'BO-03U:PS-CH:RS485', 'BO-03U:PS-CV:RS485',
            'BO-05U:PS-CH:RS485', 'BO-05U:PS-CV:RS485',
            'BO-07U:PS-CH:RS485', 'BO-07U:PS-CV:RS485',
            'BO-09U:PS-CH:RS485', 'BO-09U:PS-CV:RS485',
            'BO-11U:PS-CH:RS485', 'BO-11U:PS-CV:RS485',
            'BO-13U:PS-CH:RS485', 'BO-13U:PS-CV:RS485',
            'BO-15U:PS-CH:RS485', 'BO-15U:PS-CV:RS485',
            'BO-17U:PS-CH:RS485', 'BO-17U:PS-CV:RS485',
            'BO-19U:PS-CH:RS485', 'BO-19U:PS-CV:RS485',
            'BO-21U:PS-CH:RS485', 'BO-21U:PS-CV:RS485',
            'BO-23U:PS-CH:RS485', 'BO-23U:PS-CV:RS485',
            'BO-25U:PS-CH:RS485', 'BO-25U:PS-CV:RS485',
            'BO-27U:PS-CH:RS485', 'BO-27U:PS-CV:RS485',
            'BO-29U:PS-CH:RS485', 'BO-29U:PS-CV:RS485',
            'BO-31U:PS-CH:RS485', 'BO-31U:PS-CV:RS485',
            'BO-33U:PS-CH:RS485', 'BO-33U:PS-CV:RS485',
            'BO-35U:PS-CH:RS485', 'BO-35U:PS-CV:RS485',
            'BO-37U:PS-CH:RS485', 'BO-37U:PS-CV:RS485',
            'BO-39U:PS-CH:RS485', 'BO-39U:PS-CV:RS485',
            'BO-41U:PS-CH:RS485', 'BO-41U:PS-CV:RS485',
            'BO-43U:PS-CH:RS485', 'BO-43U:PS-CV:RS485',
            'BO-45U:PS-CH:RS485', 'BO-45U:PS-CV:RS485',
            'BO-47U:PS-CH:RS485', 'BO-47U:PS-CV:RS485',
            'BO-49D:PS-CH:RS485', 'BO-49U:PS-CV:RS485',
            ),
        },
    'LI-01:TI-EGun-MultBun': {
        'database': {
            'Src': {'value': 0, 'enums': ('Linac', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 300, 'high': 300, 'hihi': 400},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (0, 2)},
            },
        'channels': ('LI-01:EG-EGun:MULTIPULSEAMPLIFIER', ),
        },
    'LI-01:TI-EGun-SglBun': {
        'database': {
            'Src': {'value': 0, 'enums': ('Linac', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 300, 'high': 300, 'hihi': 400},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (0, 2)},
            },
        'channels': ('LI-01:EG-EGun:SINGLEPULSEAMPLIFIER', ),
        },
    'LI-01:TI-Modltr-1': {
        'database': {
            'Src': {'value': 0, 'enums': ('Linac', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 0, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 5000, 'high': 5000, 'hihi': 6000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('LI-RaMD01:MD-PPS:TRIGIN', ),
        },
    'LI-01:TI-Modltr-2': {
        'database': {
            'Src': {'value': 0, 'enums': ('Linac', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 5000, 'high': 5000, 'hihi': 6000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('LI-RaMD02:MD-PPS:TRIGIN', ),
        },
    'LI-Glob:TI-SSAmp-SHB': {
        'database': {
            'Src': {'value': 0, 'enums': ('Linac', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 5000, 'high': 5000, 'hihi': 6000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('LI-RaRF02:RF-SSAmp-1:TRIG500MHZ', ),
        },
    'LI-Glob:TI-SSAmp-Kly1': {
        'database': {
            'Src': {'value': 0, 'enums': ('Linac', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 5000, 'high': 5000, 'hihi': 6000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('LI-RaRF02:RF-SSAmp-2:TRIG3GHZ', ),
        },
    'LI-Glob:TI-SSAmp-Kly2': {
        'database': {
            'Src': {'value': 0, 'enums': ('Linac', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 5000, 'high': 5000, 'hihi': 6000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('LI-RaRF02:RF-SSAmp-3:TRIG3GHZ', ),
        },
    'LI-Glob:TI-LLRF-SHB': {
        'database': {
            'Src': {'value': 0, 'enums': ('Linac', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 5000, 'high': 5000, 'hihi': 6000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('LI-RaRF01:RF-LLRFProc:TRIG1', ),
        },
    'LI-Glob:TI-LLRF-Kly1': {
        'database': {
            'Src': {'value': 0, 'enums': ('Linac', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 5000, 'high': 5000, 'hihi': 6000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('LI-RaRF01:RF-LLRFProc:TRIG2', ),
        },
    'LI-Glob:TI-LLRF-Kly2': {
        'database': {
            'Src': {'value': 0, 'enums': ('Linac', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 5000, 'high': 5000, 'hihi': 6000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('LI-RaRF01:RF-LLRFProc:TRIG3', ),
        },
    'TB-04:TI-InjSept': {
        'database': {
            'Src': {'value': 0, 'enums': ('InjBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (2, 0)},  # EVR-OTP port
            },
        'channels': ('TB-04:PU-InjSeptCtrl:TRIGIN', ),
        },
    'TB-Glob:TI-Mags': {
        'database': {
            'Src': {'value': 0, 'enums': ('Cycle', 'Study')},
            'Delay': {'value': 0.0, 'hilim': 1.0, 'high': 1.0, 'hihi': 1.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {
                'value': 3920, 'hilim': 4001, 'high': 4001, 'hihi': 4001},
            'Duration': {
                'value': 490000,
                'hilim': 495000, 'high': 495000, 'hihi': 500000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'TB-01:PS-CV-1:RS485',  'TB-01:PS-CH-1:RS485',
            'TB-01:PS-CV-2:RS485',  'TB-01:PS-CH-2:RS485',
            'TB-02:PS-CV-1:RS485',  'TB-02:PS-CH-1:RS485',
            'TB-02:PS-CV-2:RS485',  'TB-02:PS-CH-2:RS485',
            'TB-04:PS-CV-1:RS485',  'TB-04:PS-CH:RS485',
            'TB-04:PS-CV-2:RS485',
            'TB-01:PS-QD1:RS485',   'TB-01:PS-QF1:RS485',
            'TB-02:PS-QD2A:RS485',  'TB-02:PS-QD2B:RS485',
            'TB-02:PS-QF2A:RS485',  'TB-02:PS-QF2B:RS485',
            'TB-03:PS-QD3:RS485',   'TB-03:PS-QF3:RS485',
            'TB-04:PS-QD4:RS485',   'TB-04:PS-QF4:RS485',
            'TB-Fam:PS-B:RS485',
            ),
        },
    'BO-01D:TI-InjKckr': {
        'database': {
            'Src': {'value': 0, 'enums': ('InjBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (2, 0)},  # EVR-OTP port
            },
        'channels': ('BO-01D:PU-InjKckrCtrl:TRIGIN', ),
        },
    'AS-Glob:TI-Osc-InjBO': {  # 10.0.38.74
        'database': {
            'Src': {'value': 0, 'enums': (
                    'DigLI', 'DigTB', 'DigBO', 'Linac', 'InjBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (2, 0)},  # EVR-OTP port
            },
        'channels': ('IA-01RaInj01:PU-Osc:CH1', ),
        },
    'AS-Glob:TI-Osc-EjeBO': {
        'database': {
            'Src': {'value': 0, 'enums': (
                    'DigTS', 'DigSI', 'DigBO', 'InjSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (2, 0)},  # EVR-OTP port
            },
        'channels': ('IA-20RaInj03:PU-Osc:CH1', ),
        },
    'AS-Glob:TI-Osc-InjSI': {
        'database': {
            'Src': {'value': 0, 'enums': (
                    'DigTS', 'DigSI', 'DigBO', 'InjSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (2, 0)},  # EVR-OTP port
            },
        'channels': ('IA-01RaInj04:PU-Osc:CH1', ),
        },
    'BO-Glob:TI-LLRF-Rmp': {
        'database': {
            'Src': {'value': 0, 'enums': ('InjBO', 'RmpBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('RA-RaBO01:RF-DigPatch:RAMPA', ),
        },
    'BO-Glob:TI-LLRF-PsMtn': {
        'database': {
            'Src': {'value': 0, 'enums': ('InjBO', 'RmpBO', 'Study', 'PsMtn')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('RA-RaBO01:RF-DigPatch:POSTMORTEN', ),
        },
    'BO-48D:TI-EjeKckr': {
        'database': {
            'Src': {'value': 0, 'enums': ('InjSI', 'RmpBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 0, 'states': (0, 2)},  # EVR-OUT port
            },
        'channels': ('BO-48D:PU-EjeKckrCtrl:TRIGIN', ),
        },
    'TS-Fam:TI-EjeSept': {
        'database': {
            'Src': {'value': 0, 'enums': ('InjSI', 'RmpBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 0, 'states': (0, 2)},  # EVR-OUT port
            },
        'channels': (
            'TS-01:PU-EjeSeptGCtrl-1:TRIGIN',
            'TS-01:PU-EjeSeptGCtrl-2:TRIGIN',
            ),
        },
    'TS-Fam:TI-InjSeptG': {
        'database': {
            'Src': {'value': 0, 'enums': ('InjSI', 'RmpBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (2, 0)},  # EVR-OTP port
            },
        'channels': (
            'TS-04:PU-InjSeptGCtrl-1:TRIGIN',
            'TS-04:PU-InjSeptGCtrl-2:TRIGIN',
            ),
        },
    'TS-04:TI-InjSeptF': {
        'database': {
            'Src': {'value': 0, 'enums': ('InjSI', 'RmpBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (2, 0)},  # EVR-OTP port
            },
        'channels': ('TS-04:PU-InjSeptFCtrl:TRIGIN', ),
        },
    'TS-Glob:TI-Mags': {
        'database': {
            'Src': {'value': 0, 'enums': ('Cycle', 'Study')},
            'Delay': {'value': 0.0, 'hilim': 1.0, 'high': 1.0, 'hihi': 1.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {
                'value': 3920, 'hilim': 4001, 'high': 4001, 'hihi': 4001},
            'Duration': {
                'value': 490000,
                'hilim': 495000, 'high': 495000, 'hihi': 500000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
             'TS-01:PS-CV-1:RS485',   'TS-01:PS-CH:RS485',
             'TS-01:PS-CV-2:RS485',
             'TS-02:PS-CV:RS485',     'TS-02:PS-CH:RS485',
             'TS-03:PS-CV:RS485',     'TS-03:PS-CH:RS485',
             'TS-04:PS-CV-1:RS485',   'TS-04:PS-CH:RS485',
             'TS-04:PS-CV-2:RS485',
             'TS-01:PS-QF1A:RS485',   'TS-01:PS-QF1B:RS485',
             'TS-02:PS-QD2:RS485',    'TS-02:PS-QF2:RS485',
             'TS-03:PS-QF3:RS485',
             'TS-04:PS-QD4A:RS485',   'TS-04:PS-QD4B:RS485',
             'TS-04:PS-QF4:RS485',
             'TS-Fam:PS-B:RS485',
            ),
        },
    'SI-01SA:TI-InjDpKckr': {
        'database': {
            'Src': {'value': 0, 'enums': ('InjSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},  # EVR-OTP port
            },
        'channels': ('SI-01SA:PU-InjDpKckrCtrl:TRIGIN', ),
        },
    'SI-01SA:TI-InjNLKckr': {
        'database': {
            'Src': {'value': 0, 'enums': ('InjSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},  # EVR-OTP port
            },
        'channels': ('SI-01SA:PU-InjNLKckrCtrl:TRIGIN', ),
        },
    'SI-19C4:TI-PingV': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 30, 'high': 30, 'hihi': 30},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (0, 1)},  # EVR-OUT port
            },
        'channels': ('SI-19C4:PU-PingVCtrl:TRIGIN', ),
        },
    'SI-01SA:TI-PingH': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 30, 'high': 30, 'hihi': 30},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},  # EVR-OTP port
            },
        'channels': ('SI-01SA:PU-PingHCtrl:TRIGIN', ),
        },
    'SI-Glob:TI-LLRF-Rmp': {
        'database': {
            'Src': {'value': 0, 'enums': ('InjSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'RA-RaSIA01:RF-DigPatch:RAMPA',
            'RA-RaSIB01:RF-DigPatch:RAMPA',
            ),
        },
    'SI-Glob:TI-LLRF-PsMtn': {
        'database': {
            'Src': {'value': 0, 'enums': ('InjSI', 'Study', 'PsMtn')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'RA-RaSIA01:RF-DigPatch:POSTMORTEN',
            'RA-RaSIB01:RF-DigPatch:POSTMORTEN',
            ),
        },
    # #### DIAGNOSTICS ######
    'LI-Fam:TI-BPM': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigLI', 'Linac', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'LI-RaDiag02:TI-TrigFout:TRIGINIV',
            'LA-BIH01RACK2:DI-Osc-2:TRIGIN',
            ),
        },
    'LI-Fam:TI-Scrn': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigLI', 'Linac', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('LI-RaDiag02:TI-TrigFout:TRIGINI', ),
        },
    'LI-Fam:TI-ICT': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigLI', 'Linac', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('LA-BIH01RACK2:DI-Osc-1:TRIGIN', ),
        },
    'LI-01:DI-Osc-Modltr': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigLI', 'Linac', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('LA-MD:DI-Osc:TRIGIN', ),
        },
    'AS-Fam:TI-Scrn-TBBO': {
        'database': {
            'Src': {'value': 1, 'enums': (
                                'Linac', 'InjBO', 'DigTB', 'DigBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'TB-01:DI-ScrnCam-1:TRIGIN',
            'TB-01:DI-ScrnCam-2:TRIGIN',
            'TB-02:DI-ScrnCam-1:TRIGIN',
            'TB-02:DI-ScrnCam-2:TRIGIN',
            'TB-03:DI-ScrnCam:TRIGIN',
            'TB-04:DI-ScrnCam:TRIGIN',
            'BO-01D:DI-ScrnCam-1:TRIGIN',
            'BO-01D:DI-ScrnCam-2:TRIGIN',
            'BO-02U:DI-ScrnCam:TRIGIN',
            ),
        },
    'TB-Fam:TI-ICT-Integ': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigTB', 'Linac', 'InjBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'TB-02:DI-ICTSigCond:TRIGIN',
            'TB-04:DI-ICTSigCond:TRIGIN',
            ),
        },
    'TB-Fam:TI-ICT-Digit': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigTB', 'Linac', 'InjBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'TB-02:DI-ICTDig:TRIGIN',
            'TB-04:DI-ICTDig:TRIGIN',
            ),
        },
    'BO-50U:TI-VLightCam': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigBO', 'DigTB', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 30, 'high': 30, 'hihi': 30},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'BO-50U:DI-VLightCam:TRIGIN',
            ),
        },
    'BO-Glob:TI-TuneProc': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 30, 'high': 30, 'hihi': 30},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'BO-Glob:DI-TuneProc-H:TRIGIN',
            'BO-Glob:DI-TuneProc-V:TRIGIN',
            ),
        },
    'BO-35D:TI-DCCT': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('BO-35D:DI-DCCTDig:TRIGIN', ),
        },
    'BO-RaPSE05:TI-Osc': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigBO', 'InjBO', 'RmpBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {'value': 150, 'hilim': 550, 'high': 550, 'hihi': 600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (2, 0)},
            },
        'channels': ('PA-RaPSE05:DI-Osc-BO:TIMIN', ),
        },
    'TS-Fam:TI-Scrn': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigTS', 'InjSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'TS-01:DI-ScrnCam:TRIGIN',
            'TS-02:DI-ScrnCam:TRIGIN',
            'TS-03:DI-ScrnCam:TRIGIN',
            'TS-04:DI-ScrnCam-1:TRIGIN',
            'TS-04:DI-ScrnCam-2:TRIGIN',
            # ## one screen left:
            # According to João Leandro, no requirement has been made for a
            # timing signal for the last camera
            ),
        },
    'TS-Fam:TI-ICT-Integ': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigTS', 'InjSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'TS-01:DI-ICTSigCond:TRIGIN',
            'TS-04:DI-ICTSigCond:TRIGIN',
            ),
        },
    'TS-Fam:TI-ICT-Digit': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigTS', 'InjSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'TS-01:DI-ICTDig:TRIGIN',
            'TS-04:DI-ICTDig:TRIGIN',
            ),
        },
    'SI-Glob:TI-StrkCam-Trig1': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('SI-Glob:DI-StrkCam:TRIG1', ),
        },
    'SI-Glob:TI-StrkCam-Trig2': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('SI-Glob:DI-StrkCam:TRIG2', ),
        },
    'SI-Glob:TI-BbBProcH-Trig1': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('SI-Glob:DI-BbBProc-H:TRIG1', ),
        },
    'SI-Glob:TI-BbBProcH-Trig2': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('SI-Glob:DI-BbBProc-H:TRIG2', ),
        },
    'SI-Glob:TI-BbBProcV-Trig1': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('SI-Glob:DI-BbBProc-V:TRIG1', ),
        },
    'SI-Glob:TI-BbBProcV-Trig2': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('SI-Glob:DI-BbBProc-V:TRIG2', ),
        },
    'SI-Glob:TI-BbBProcL-Trig1': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('SI-Glob:DI-BbBProc-L:TRIG1', ),
        },
    'SI-Glob:TI-BbBProcL-Trig2': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('SI-Glob:DI-BbBProc-L:TRIG2', ),
        },
    'SI-Glob:TI-BbBProcH-Fid': {
        'database': {
            'Src': {'value': 7, 'enums': ('DigSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('SI-Glob:DI-BbBProc-H:FID', ),
        },
    'SI-Glob:TI-BbBProcV-Fid': {
        'database': {
            'Src': {'value': 7, 'enums': ('DigSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('SI-Glob:DI-BbBProc-V:FID', ),
        },
    'SI-Glob:TI-BbBProcL-Fid': {
        'database': {
            'Src': {'value': 7, 'enums': ('DigSI', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('SI-Glob:DI-BbBProc-L:FID', ),
        },
    'SI-13C4:TI-DCCT': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigSI', 'PsMtn', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('SI-13SA:DI-DCCTDig:TRIGIN', ),
        },
    'SI-14C4:TI-DCCT': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigSI', 'PsMtn', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('SI-14SB:DI-DCCTDig:TRIGIN', ),
        },
    'AS-Glob:TI-FCT': {
        # This trigger will work for both FCTs, from TB and TS transpor lines.
        # Two triggers must be sent for each injection pulse, the first will
        # serve as trigger for the TB FCT and the other for the TS.
        # The delay and duration must be adjusted accordingly to the time it
        # takes for the beam to pass by them.
        'database': {
            'Src': {'value': 0, 'enums': ('DigTB', 'DigTS', 'RmpBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 2, 'hilim': 3, 'high': 3, 'hihi': 3},
            'Duration': {
                'value': 350, 'hilim': 500, 'high': 500, 'hihi': 500},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('AS-Glob:DI-FCTDig:CH4', ),
        },
    'AS-Glob:TI-FillPtrnMon': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigTS', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 2, 'high': 2, 'hihi': 2},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': ('AS-Glob:DI-FPMDig:CH4', ),
        },
    'AS-Glob:TI-BPM-TBTS': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigTB', 'DigTS', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 30, 'high': 30, 'hihi': 30},
            'Duration': {
                'value': 150, 'hilim': 1550, 'high': 1550, 'hihi': 1600},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'TS-01:DI-BPM:CRT0',    'TS-02:DI-BPM:CRT0',
            'TS-03:DI-BPM:CRT0',
            'TS-04:DI-BPM-1:CRT0',  'TS-04:DI-BPM-2:CRT0',
            'TB-01:DI-BPM-1:CRT0',  'TB-01:DI-BPM-2:CRT0',
            'TB-02:DI-BPM-1:CRT0',  'TB-02:DI-BPM-2:CRT0',
            'TB-03:DI-BPM:CRT0',
            'TB-04:DI-BPM:CRT0',
            ),
        },
    'AS-Glob:TI-BPM-SIBO': {
        'database': {
            'Src': {'value': 0, 'enums': ('DigBO', 'DigSI', 'RmpBO', 'Study')},
            'Delay': {'value': 0.0},
            'RFDelayType': {'value': 1, 'states': (2, 0)},
            'NrPulses': {'value': 1, 'hilim': 30, 'high': 30, 'hihi': 30},
            'Duration': {
                'value': 150,
                'hilim': 500000, 'high': 500000, 'hihi': 500000},
            'State': {'value': 0},
            'Polarity': {'value': 1, 'states': (1, 0)},
            },
        'channels': (
            'SI-01M1:DI-BPM:CRT0',     'SI-01M2:DI-BPM:CRT0',
            'SI-01C1:DI-BPM-1:CRT0',   'SI-01C1:DI-BPM-2:CRT0',
            'SI-01C2:DI-BPM:CRT0',     'SI-01C3:DI-BPM-1:CRT0',
            'SI-01C3:DI-BPM-2:CRT0',   'SI-01C4:DI-BPM:CRT0',

            'SI-02M1:DI-BPM:CRT0',     'SI-02M2:DI-BPM:CRT0',
            'SI-02C1:DI-BPM-1:CRT0',   'SI-02C1:DI-BPM-2:CRT0',
            'SI-02C2:DI-BPM:CRT0',     'SI-02C3:DI-BPM-1:CRT0',
            'SI-02C3:DI-BPM-2:CRT0',   'SI-02C4:DI-BPM:CRT0',

            'SI-03M1:DI-BPM:CRT0',     'SI-03M2:DI-BPM:CRT0',
            'SI-03C1:DI-BPM-1:CRT0',   'SI-03C1:DI-BPM-2:CRT0',
            'SI-03C2:DI-BPM:CRT0',     'SI-03C3:DI-BPM-1:CRT0',
            'SI-03C3:DI-BPM-2:CRT0',   'SI-03C4:DI-BPM:CRT0',

            'SI-04M1:DI-BPM:CRT0',     'SI-04M2:DI-BPM:CRT0',
            'SI-04C1:DI-BPM-1:CRT0',   'SI-04C1:DI-BPM-2:CRT0',
            'SI-04C2:DI-BPM:CRT0',     'SI-04C3:DI-BPM-1:CRT0',
            'SI-04C3:DI-BPM-2:CRT0',   'SI-04C4:DI-BPM:CRT0',

            'SI-05M1:DI-BPM:CRT0',     'SI-05M2:DI-BPM:CRT0',
            'SI-05C1:DI-BPM-1:CRT0',   'SI-05C1:DI-BPM-2:CRT0',
            'SI-05C2:DI-BPM:CRT0',     'SI-05C3:DI-BPM-1:CRT0',
            'SI-05C3:DI-BPM-2:CRT0',   'SI-05C4:DI-BPM:CRT0',

            'SI-06M1:DI-BPM:CRT0',     'SI-06M2:DI-BPM:CRT0',
            'SI-06C1:DI-BPM-1:CRT0',   'SI-06C1:DI-BPM-2:CRT0',
            'SI-06C2:DI-BPM:CRT0',     'SI-06C3:DI-BPM-1:CRT0',
            'SI-06C3:DI-BPM-2:CRT0',   'SI-06C4:DI-BPM:CRT0',

            'SI-07M1:DI-BPM:CRT0',     'SI-07M2:DI-BPM:CRT0',
            'SI-07C1:DI-BPM-1:CRT0',   'SI-07C1:DI-BPM-2:CRT0',
            'SI-07C2:DI-BPM:CRT0',     'SI-07C3:DI-BPM-1:CRT0',
            'SI-07C3:DI-BPM-2:CRT0',   'SI-07C4:DI-BPM:CRT0',

            'SI-08M1:DI-BPM:CRT0',     'SI-08M2:DI-BPM:CRT0',
            'SI-08C1:DI-BPM-1:CRT0',   'SI-08C1:DI-BPM-2:CRT0',
            'SI-08C2:DI-BPM:CRT0',     'SI-08C3:DI-BPM-1:CRT0',
            'SI-08C3:DI-BPM-2:CRT0',   'SI-08C4:DI-BPM:CRT0',

            'SI-09M1:DI-BPM:CRT0',     'SI-09M2:DI-BPM:CRT0',
            'SI-09C1:DI-BPM-1:CRT0',   'SI-09C1:DI-BPM-2:CRT0',
            'SI-09C2:DI-BPM:CRT0',     'SI-09C3:DI-BPM-1:CRT0',
            'SI-09C3:DI-BPM-2:CRT0',   'SI-09C4:DI-BPM:CRT0',

            'SI-10M1:DI-BPM:CRT0',     'SI-10M2:DI-BPM:CRT0',
            'SI-10C1:DI-BPM-1:CRT0',   'SI-10C1:DI-BPM-2:CRT0',
            'SI-10C2:DI-BPM:CRT0',     'SI-10C3:DI-BPM-1:CRT0',
            'SI-10C3:DI-BPM-2:CRT0',   'SI-10C4:DI-BPM:CRT0',

            'SI-11M1:DI-BPM:CRT0',     'SI-11M2:DI-BPM:CRT0',
            'SI-11C1:DI-BPM-1:CRT0',   'SI-11C1:DI-BPM-2:CRT0',
            'SI-11C2:DI-BPM:CRT0',     'SI-11C3:DI-BPM-1:CRT0',
            'SI-11C3:DI-BPM-2:CRT0',   'SI-11C4:DI-BPM:CRT0',

            'SI-12M1:DI-BPM:CRT0',     'SI-12M2:DI-BPM:CRT0',
            'SI-12C1:DI-BPM-1:CRT0',   'SI-12C1:DI-BPM-2:CRT0',
            'SI-12C2:DI-BPM:CRT0',     'SI-12C3:DI-BPM-1:CRT0',
            'SI-12C3:DI-BPM-2:CRT0',   'SI-12C4:DI-BPM:CRT0',

            'SI-13M1:DI-BPM:CRT0',     'SI-13M2:DI-BPM:CRT0',
            'SI-13C1:DI-BPM-1:CRT0',   'SI-13C1:DI-BPM-2:CRT0',
            'SI-13C2:DI-BPM:CRT0',     'SI-13C3:DI-BPM-1:CRT0',
            'SI-13C3:DI-BPM-2:CRT0',   'SI-13C4:DI-BPM:CRT0',

            'SI-14M1:DI-BPM:CRT0',     'SI-14M2:DI-BPM:CRT0',
            'SI-14C1:DI-BPM-1:CRT0',   'SI-14C1:DI-BPM-2:CRT0',
            'SI-14C2:DI-BPM:CRT0',     'SI-14C3:DI-BPM-1:CRT0',
            'SI-14C3:DI-BPM-2:CRT0',   'SI-14C4:DI-BPM:CRT0',

            'SI-15M1:DI-BPM:CRT0',     'SI-15M2:DI-BPM:CRT0',
            'SI-15C1:DI-BPM-1:CRT0',   'SI-15C1:DI-BPM-2:CRT0',
            'SI-15C2:DI-BPM:CRT0',     'SI-15C3:DI-BPM-1:CRT0',
            'SI-15C3:DI-BPM-2:CRT0',   'SI-15C4:DI-BPM:CRT0',

            'SI-16M1:DI-BPM:CRT0',     'SI-16M2:DI-BPM:CRT0',
            'SI-16C1:DI-BPM-1:CRT0',   'SI-16C1:DI-BPM-2:CRT0',
            'SI-16C2:DI-BPM:CRT0',     'SI-16C3:DI-BPM-1:CRT0',
            'SI-16C3:DI-BPM-2:CRT0',   'SI-16C4:DI-BPM:CRT0',

            'SI-17M1:DI-BPM:CRT0',     'SI-17M2:DI-BPM:CRT0',
            'SI-17C1:DI-BPM-1:CRT0',   'SI-17C1:DI-BPM-2:CRT0',
            'SI-17C2:DI-BPM:CRT0',     'SI-17C3:DI-BPM-1:CRT0',
            'SI-17C3:DI-BPM-2:CRT0',   'SI-17C4:DI-BPM:CRT0',

            'SI-18M1:DI-BPM:CRT0',     'SI-18M2:DI-BPM:CRT0',
            'SI-18C1:DI-BPM-1:CRT0',   'SI-18C1:DI-BPM-2:CRT0',
            'SI-18C2:DI-BPM:CRT0',     'SI-18C3:DI-BPM-1:CRT0',
            'SI-18C3:DI-BPM-2:CRT0',   'SI-18C4:DI-BPM:CRT0',

            'SI-19M1:DI-BPM:CRT0',     'SI-19M2:DI-BPM:CRT0',
            'SI-19C1:DI-BPM-1:CRT0',   'SI-19C1:DI-BPM-2:CRT0',
            'SI-19C2:DI-BPM:CRT0',     'SI-19C3:DI-BPM-1:CRT0',
            'SI-19C3:DI-BPM-2:CRT0',   'SI-19C4:DI-BPM:CRT0',

            'SI-20M1:DI-BPM:CRT0',     'SI-20M2:DI-BPM:CRT0',
            'SI-20C1:DI-BPM-1:CRT0',   'SI-20C1:DI-BPM-2:CRT0',
            'SI-20C2:DI-BPM:CRT0',     'SI-20C3:DI-BPM-1:CRT0',
            'SI-20C3:DI-BPM-2:CRT0',   'SI-20C4:DI-BPM:CRT0',

            'BO-01U:DI-BPM:CRT0',      'BO-02U:DI-BPM:CRT0',
            'BO-03U:DI-BPM:CRT0',      'BO-04U:DI-BPM:CRT0',
            'BO-05U:DI-BPM:CRT0',      'BO-06U:DI-BPM:CRT0',
            'BO-07U:DI-BPM:CRT0',      'BO-08U:DI-BPM:CRT0',
            'BO-09U:DI-BPM:CRT0',      'BO-10U:DI-BPM:CRT0',
            'BO-11U:DI-BPM:CRT0',      'BO-12U:DI-BPM:CRT0',
            'BO-13U:DI-BPM:CRT0',      'BO-14U:DI-BPM:CRT0',
            'BO-15U:DI-BPM:CRT0',      'BO-16U:DI-BPM:CRT0',
            'BO-17U:DI-BPM:CRT0',      'BO-18U:DI-BPM:CRT0',
            'BO-19U:DI-BPM:CRT0',      'BO-20U:DI-BPM:CRT0',
            'BO-21U:DI-BPM:CRT0',      'BO-22U:DI-BPM:CRT0',
            'BO-23U:DI-BPM:CRT0',      'BO-24U:DI-BPM:CRT0',
            'BO-25U:DI-BPM:CRT0',      'BO-26U:DI-BPM:CRT0',
            'BO-27U:DI-BPM:CRT0',      'BO-28U:DI-BPM:CRT0',
            'BO-29U:DI-BPM:CRT0',      'BO-30U:DI-BPM:CRT0',
            'BO-31U:DI-BPM:CRT0',      'BO-32U:DI-BPM:CRT0',
            'BO-33U:DI-BPM:CRT0',      'BO-34U:DI-BPM:CRT0',
            'BO-35U:DI-BPM:CRT0',      'BO-36U:DI-BPM:CRT0',
            'BO-37U:DI-BPM:CRT0',      'BO-38U:DI-BPM:CRT0',
            'BO-39U:DI-BPM:CRT0',      'BO-40U:DI-BPM:CRT0',
            'BO-41U:DI-BPM:CRT0',      'BO-42U:DI-BPM:CRT0',
            'BO-43U:DI-BPM:CRT0',      'BO-44U:DI-BPM:CRT0',
            'BO-45U:DI-BPM:CRT0',      'BO-46U:DI-BPM:CRT0',
            'BO-47U:DI-BPM:CRT0',      'BO-48U:DI-BPM:CRT0',
            'BO-49U:DI-BPM:CRT0',      'BO-50U:DI-BPM:CRT0',
            ),
        },
}
