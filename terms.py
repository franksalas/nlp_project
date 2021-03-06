
'''
ORIGINAL SOURCE: https://www.biggerpockets.com/rei/real-estate-abbreviationS/
Purpose: to be used for term replacement given domain.
edits: Strip text from site, created dictionary from dict comprehension
example:
dict((k.strip(), v.strip()) for k,v in 
              (item.split('  ') for item in long_string.split('\n')))
    
author: F.Salas
'''

REA_MAP = {
    'CBDs': 'Central Business District',
    'MH': 'Manufactured Housing',
    'REIT': 'Real Estate Investment Trust',
    'MOB': 'Medical Office Buildings',
    'M&A':' Mergers and Acquisitions',
}

RE_MAP = {
 # Real Estate Investing Abbreviations
 'ARV': 'After-Repaired Value',
 'CCIM': 'Certified Commercial Investment Member',
 'COO': 'Certificate of Occupancy',
 'CMA': 'Comparative Market Analysis',
 'COCR': 'Cash on Cash Return',
 'COF': 'Cost of Funds',
 'CRE': 'Commercial Real Estate',
 #'DCR or DSCR or DSR': 'Debt Service Coverage Ratio',
 'DCR': 'Debt Service Coverage Ratio',
 'DTI': 'Debt to Income Ratio',
 'FHA': 'Federal Housing Administration',
 'FMR': 'Fair Market Rent',
 'FMV': 'Fair Market Value',
 'FSBO': 'For Sale by Owner',
 'GNMA': 'Ginnie Mae (Government National Mortgage Association)',
 'GRM': 'Gross Rent Multiplier',
 'HML': 'Hard Money Lender',
 'HOA': 'Homeowners Association',
 'HUD': 'Housing and Urban Development',
 'IRA': 'Individual Retirement Account',
 'IRR': 'Internal Rate of Return',
 'JV': 'Joint Venture',
 'L/O': 'Lease Option',
 'LLC': 'Limited Liability Company',
 'LLP': 'Limited Liability Partnership',
 'LTV': 'Loan to Value',
 'MAO': 'Maximum Allowable Offer',
 'MLS': 'Multiple Listing Service',
 'NNN': 'Triple Net Lease',
 'NOI': 'Net Operating Income',
 'NOO': 'Non-Owner Occupied',
 'OO': 'Owner Occupied',
 'O/F': 'Owner Finance',
 'P&S': 'Purchase and Sale',
 'PCF': 'Price to Cash Flow (ratio)',
 'PITI': 'Principal, Interest, Taxes and Insurance',
 'PUD': 'Planned Unit Development',
 'REI': 'Real Estate Investing',
 'REIA': 'Real Estate Investors Association',
 'REO': 'Real Estate Owned',
 'ROI': 'Return On Investment',
 'RTO': 'Rent to Own',
 'SFH': 'Single Family House',
 'SFR': 'Single Family Residence',
 'VA': 'Department of Veterans Affairs / Veterans Administration',
 # Real Estate Financing & Contract Abbreviations
 'AMORT': 'Amortization',
 'APR': 'Annual Percentage Rate',
 'ARM': 'Adjustable Rate Mortgage',
 'CCR': 'Conditions, Covenants, and Restrictions',
 'CFD': 'Contract for Deed',
 'CLTV': 'Combined Loan To Value',
 'CAP': 'Capitalization',
 'DBA': 'Doing Business As',
 'DOS': 'Due On Sale Clause',
 'DOT': 'Deed of Trust',
 'EMC': 'Earnest money contract',
 'FCRA': 'Fair Credit Reporting Act',
 'FDIC': 'Federal Deposit Insurance Corporation',
 'FEMA': 'Federal Emergency Management Agency',
 'FHLMC': 'Freddie Mac (Federal Home Loan Mortgage Corporation)',
 'I/O': 'Interest Only (loan)',
 'LOC': 'Line of Credit',
 'LOI': 'Letter of Intent',
 'LPOA': 'Limited Power of Attorney',
 'MAO': 'Maximum Allowable Offer',
 'PMI': 'Private Mortgage Insurance',
 'POA': 'Power of Attorney',
 'POF': 'Proof of Funds',
 'Sub2': 'Subject to existing financing',
 'TIL': 'Truth In Lending',
 # Real Estate Listing Abbreviations
 'AC': 'Acre',
 'A/C': 'Air Conditioning',
 'Actv': 'Active',
 'APT': 'Apartment',
 'ASM': 'Assumptions',
 'BCH': 'Beach',
 'BKPORCH': 'Back Porch',
 'BLDRS REDO': 'Builder’s Renovation',
 'BLT': 'Built-in',
 'BOT': 'Boat Slip',
 'BR': 'Bedroom',
 'Brk': 'Brick',
 'Bsmt': 'Basement',
 'Bulk': 'Bulkhead',
 'Bung': 'Bungalow',
 'CAC': 'Central Air Conditioning',
 'CCR': 'Conditions, Covenants, and Restrictions',
 'Cldsc': 'Cul-de-sac',
 'Clus': 'Cluster',
 'Cnl': 'Canal',
 'Col': 'Colonial',
 'Cont': 'Contemporary',
 'Crk': 'Creek',
 'DEDRS': 'Deed Restrictions',
 'DLM': 'Seller Disclaimer',
 'DLO': 'Seller Disclosure',
 'DWAC': 'Deep Water Access',
 'EA': 'exclusive agency',
 'ELE': 'Electric',
 'ELV': 'Elevator',
 'END': 'End Unit',
 'ERS': 'exclusive right to sell',
 'Exr': 'Exercise Room',
 'Farm': 'Farmhouse',
 'FRBO': 'for rent by owner',
 'FFE': 'furniture, fixture, and equipment',
 'FHA': 'Federal Housing Administration',
 'FLR': 'Floor Furnace',
 'FIN LL': 'Finished lower level',
 'FM RM': 'Family Room',
 'FML': 'Formal',
 'Foyr': 'Foyer',
 'FR': 'Family room',
 'FSBO': 'For Sale by Owner',
 'FXR': 'Fixer Upper',
 'GAR': 'Garage',
 'GARB': 'Garbage',
 'GLF': 'Golf Course',
 'GMT Kitchen': 'Gourmet kitchen',
 'GRNO': 'Ground Maintenance',
 'HB': 'Half Bath (toilet + sink)',
 'HBR': 'Harbor',
 'HIST': 'Historical District',
 'HOA': 'Homeowner’s association',
 'HP': 'Heat Pump',
 'HPWA': 'Water/Air Ht Pump',
 'HRS': 'Horses Allowed',
 'HSF': 'Heated square feet',
 'HUD': 'Department of Housing and Urban Development',
 'INLW': 'In-Law Suite',
 'LFT': 'Loft',
 'LRG': 'Large',
 'LR': 'Living Room',
 'LTV': 'loan to value',
 'MAR': 'Marble',
 'MCOA': 'Min $ on Assumption',
 'MEIK': 'Modern eat-in kitchen',
 'MIC': 'Mint Condition',
 'MLS': 'multiple listing service',
 'MO': 'Month',
 'MOPOA': 'Monthly POA Fee',
 'MRSH': 'Marsh',
 'MSN': 'Masonry',
 'MTG': 'Mortgage',
 'MYOB': 'Mind Your Own Business',
 'NAR': 'National Association of Realtors',
 'NBHD': 'Neighborhood',
 'NGS': 'Natural Gas',
 'NONQ': 'Non-Qualifying',
 'NYSAR': 'New York State Association of Realtors',
 'OA': 'Owner Agent',
 'OBO': 'Or Best Offer',
 'OCN': 'Ocean',
 'O/F': 'Owner Finance',
 'OFC': 'Office/Study',
 'OFF': 'Off Street Parking',
 'OP': 'Occupancy Permit',
 'OVER': 'Oversized Garage',
 'OWN': 'Owner Financing',
 'P&S': 'Purchase and sale',
 'PAR': 'Partially Fenced',
 'PAT': 'Patio',
 'PERM': 'Perm Attic Stairs',
 'PGS': 'Propane',
 'PICK': 'Picket Fence',
 'PILE': 'Pilings',
 'PITI': 'Principal, Interest, Taxes and Insurance',
 'PL/A': 'Above Ground Pool',
 'PL': 'Swimming Pool',
 'PL/1': 'In-Ground Pool',
 'PLAY': 'Playground',
 'PMI': 'Private mortgage insurance',
 'PMP': 'Well Pump',
 'POA': 'Power of Attorney',
 'PRQ': 'Parquet',
 'PRTL': 'Partial',
 'PULL': 'Pull-Down Attic Stair',
 'R/OPT': 'Rent w/Opt-Buy',
 'RDR': 'Radiator',
 'REC': 'Recreation Room',
 'REL': 'Related to Seller',
 'RELO': 'Relocation office',
 'RNCH': 'Ranch',
 'RTO': 'Rent To Own',
 'RVR': 'River',
 'SD': 'Security Deposit',
 'SEC': 'Security System',
 'SEC SYS': 'Security System',
 'SEW': 'Sewer',
 'SHNG': 'Shingle',
 'SHOP': 'Workshop',
 'SKY': 'Skylights',
 'SLT': 'Slate',
 'SN': 'Senior',
 'SMP': 'Sump Pump',
 'SPC': 'Drive parking spaces',
 'SPDED': 'Special Warranty Deed',
 'SPLT': 'Split Level',
 'SMB': 'Split Master Bedroom',
 'SPKLR': 'Sprinkler',
 'SQ FT': 'Square Feet',
 'SD/W': 'Storm Doors & Windows',
 'SRO': 'Single Room Occupancy',
 'STA': 'State',
 'STOR': 'Assigned Storage',
 'STR': 'On Street Parking',
 'SUN': 'Sun Room',
 'SWR': 'Sewer',
 'TEN': 'Tennis Court',
 'TOWN': 'Town House',
 'TRAD': 'Traditional',
 'TRAN': 'Transitional',
 'TRC': 'Trash Compactor',
 'TRSH': 'Trash Pickup',
 'TXS': 'Taxes',
 'UNO': 'Unit Number',
 'UTCL': 'Utility Closet',
 'UTLVL': 'Utility Room Level',
 'UTRM': 'Utility Room',
 'VYL': 'Vinyl',
 'WAR': 'Warranty Plan',
 'WBS': 'Wood-Burning Stove',
 'WBFP': 'Wood Burning Fireplace',
 'W/D': 'Washer/Dryer',
 'W/D HKUP': 'Washer/Dryer hookup',
 'WF': 'Waterfront',
 'WDSTV': 'Wood Burn Stove',
 'WHF': 'Whole House Fan',
 'WHKP': 'Washer Hookup',
 'WIN': 'Window/Wall Unit',
 'WINDT': 'Window Treatment',
 'WLKIN': 'Walk-in Closet',
 'WSH': 'Washer',
 'WTR': 'Water',
 'WTR PD': 'Water paid',
 'W/W CRPT': 'Wall To Wall Carpet',
 'YD': 'Yard',
 # Real Estate Agent Certifications & Abbreviations
 'ABR': 'Accredited Buyer Representative',
 'AMO': 'Accredited Management Organization',
 'CBR': 'Certified Buyer Representative',
 'CHMS': 'Certified Home Marketing Specialist',
 'CLHMS': 'Certified Luxury Home Marketing Specialist',
 'CNS': 'Certified Negotiation Specialist',
 'CPM': 'Certified Property Manager',
 'CRB': 'Certified Real Estate Broker',
 'CRS': 'Certified Residential Specialist',
 'e-PRO': 'Internet Professional',
 'GRI': 'Graduate REALTOR Institute',
 'GRES': 'Graduate Real Estate Society',
 'NAR': 'National Association of Realtors',
 'REALTOR': 'Member of the National Association of Realtors',
 'REBNY': 'Real Estate Board of New York',
 'RPAC': 'Realtors Political Action Committe',
 'SRES': 'Senior Real Estate Specialist'}

