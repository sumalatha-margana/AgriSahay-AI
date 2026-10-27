import streamlit as st

st.set_page_config(
    page_title="AgriSahay AI",
    page_icon="🌱",
    layout="wide"
)

# -------------------- DESIGN --------------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #e8f5e9, #c8e6c9, #fffde7);
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1 {
    color: #1b5e20 !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #2e7d32 !important;
}

p {
    color: #37474f;
    font-size: 16px;
}

div.stButton > button {
    background-color: #2e7d32;
    color: white !important;
    border: none;
    border-radius: 10px;
    padding: 10px 16px;
    font-weight: 600;
    width: 100%;
}

div.stButton > button:hover {
    background-color: #1b5e20;
    color: white !important;
}

.scheme-card {
    background-color: #ffffff;
    border: 1px solid #c8e6c9;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 12px;
    min-height: 190px;
    box-shadow: 0 4px 12px rgba(46, 125, 50, 0.12);
}

.scheme-card h3 {
    color: #1b5e20 !important;
    font-size: 19px;
    margin-top: 0;
}

.scheme-card p {
    color: #455a64;
    font-size: 14px;
    line-height: 1.6;
}

.hero {
    background: linear-gradient(120deg, #1b5e20, #43a047);
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 25px;
}

.hero h1 {
    color: white !important;
    font-size: 38px;
}

.hero p {
    color: white !important;
    font-size: 17px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)


# -------------------- SCHEME INFORMATION --------------------

schemes = {
    "PM-KISAN": {
        "icon": "💰",
        "English": {
            "short": "Financial assistance for eligible farmer families.",
            "about": (
                "PM-KISAN is a Central Government scheme that provides "
                "eligible landholding farmer families with financial "
                "assistance of ₹6,000 per year, subject to scheme rules."
            ),
            "benefits": [
                "₹6,000 annual assistance for eligible farmer families.",
                "Generally paid in three instalments.",
                "Payments are made through Direct Benefit Transfer."
            ],
            "eligibility": (
                "Eligibility depends on landholding and scheme conditions. "
                "Certain categories are excluded under government rules."
            ),
            "apply": (
                "Visit the official PM-KISAN portal to check eligibility, "
                "registration, e-KYC and beneficiary status."
            ),
            "url": "https://pmkisan.gov.in/"
        },
        "తెలుగు": {
            "short": "అర్హులైన రైతు కుటుంబాలకు ఆర్థిక సహాయం.",
            "about": (
                "PM-KISAN పథకం ద్వారా అర్హులైన రైతు కుటుంబాలకు "
                "సంవత్సరానికి ₹6,000 ఆర్థిక సహాయం అందించబడుతుంది. "
                "పథకం నిబంధనలు వర్తిస్తాయి."
            ),
            "benefits": [
                "అర్హులైన రైతు కుటుంబాలకు సంవత్సరానికి ₹6,000 సహాయం.",
                "సాధారణంగా మూడు విడతల్లో చెల్లింపు జరుగుతుంది.",
                "ప్రత్యక్ష నగదు బదిలీ ద్వారా డబ్బు అందుతుంది."
            ],
            "eligibility": (
                "భూమి వివరాలు మరియు పథకం నిబంధనల ప్రకారం అర్హత "
                "నిర్ణయించబడుతుంది. కొన్ని వర్గాలకు మినహాయింపులు ఉంటాయి."
            ),
            "apply": (
                "అర్హత, నమోదు, e-KYC మరియు లబ్ధిదారుల స్థితి కోసం "
                "అధికారిక PM-KISAN వెబ్‌సైట్‌ను సందర్శించండి."
            ),
            "url": "https://pmkisan.gov.in/"
        }
    },

    "Pradhan Mantri Fasal Bima Yojana": {
        "icon": "🌾",
        "English": {
            "short": "Crop insurance against specified crop risks.",
            "about": (
                "PMFBY is a crop insurance scheme intended to protect "
                "eligible farmers against specified crop losses and risks."
            ),
            "benefits": [
                "Insurance protection against specified crop risks.",
                "Coverage depends on notified crops and areas.",
                "Claims are assessed according to scheme rules."
            ],
            "eligibility": (
                "Farmers growing notified crops in notified areas may "
                "be eligible under current scheme guidelines."
            ),
            "apply": (
                "Check the official portal for application methods, "
                "notified crops, insurance details and deadlines."
            ),
            "url": "https://pmfby.gov.in/"
        },
        "తెలుగు": {
            "short": "నిర్దిష్ట పంట ప్రమాదాలకు పంట బీమా.",
            "about": (
                "PMFBY పథకం అర్హులైన రైతులకు నిర్దిష్ట పంట నష్టాలు "
                "మరియు ప్రమాదాలపై బీమా రక్షణ కల్పిస్తుంది."
            ),
            "benefits": [
                "నిర్దిష్ట పంట ప్రమాదాలకు బీమా రక్షణ.",
                "నోటిఫై చేసిన పంటలు మరియు ప్రాంతాలకు అనుగుణంగా కవరేజ్ ఉంటుంది.",
                "పరిహారం పథకం నిబంధనల ప్రకారం నిర్ణయించబడుతుంది."
            ],
            "eligibility": (
                "నోటిఫై చేసిన ప్రాంతాల్లో నోటిఫై చేసిన పంటలు సాగు చేసే "
                "రైతులు ప్రస్తుత మార్గదర్శకాల ప్రకారం అర్హులు కావచ్చు."
            ),
            "apply": (
                "దరఖాస్తు విధానం, పంటలు, బీమా వివరాలు మరియు చివరి తేదీల "
                "కోసం అధికారిక PMFBY వెబ్‌సైట్‌ను చూడండి."
            ),
            "url": "https://pmfby.gov.in/"
        }
    },

    "Kisan Credit Card": {
        "icon": "💳",
        "English": {
            "short": "Credit facilities for eligible agricultural needs.",
            "about": (
                "The Kisan Credit Card scheme helps eligible farmers "
                "access credit for agricultural and related needs."
            ),
            "benefits": [
                "Access to eligible agricultural credit.",
                "Helps meet approved farming expenses.",
                "Credit limits and interest conditions depend on applicable rules."
            ],
            "eligibility": (
                "Eligibility depends on farming activities, bank requirements "
                "and applicable scheme guidelines."
            ),
            "apply": (
                "Contact a participating bank or consult the official "
                "government portal for application instructions."
            ),
            "url": "https://fasalrin.gov.in/"
        },
        "తెలుగు": {
            "short": "వ్యవసాయ అవసరాల కోసం రుణ సదుపాయం.",
            "about": (
                "కిసాన్ క్రెడిట్ కార్డ్ పథకం ద్వారా అర్హులైన రైతులు "
                "వ్యవసాయ మరియు సంబంధిత అవసరాలకు రుణ సదుపాయం పొందవచ్చు."
            ),
            "benefits": [
                "అర్హత ఉన్న వ్యవసాయ రుణ సదుపాయం.",
                "ఆమోదించబడిన వ్యవసాయ ఖర్చులకు సహాయం.",
                "రుణ పరిమితి మరియు వడ్డీ నిబంధనలు వర్తించే నియమాలపై ఆధారపడతాయి."
            ],
            "eligibility": (
                "వ్యవసాయ కార్యకలాపాలు, బ్యాంకు నిబంధనలు మరియు "
                "పథకం మార్గదర్శకాల ప్రకారం అర్హత నిర్ణయించబడుతుంది."
            ),
            "apply": (
                "దరఖాస్తు విధానం మరియు అవసరమైన పత్రాల కోసం "
                "పాల్గొనే బ్యాంకును లేదా అధికారిక ప్రభుత్వ పోర్టల్‌ను సంప్రదించండి."
            ),
            "url": "https://fasalrin.gov.in/"
        }
    },

    "Soil Health Card Scheme": {
        "icon": "🪴",
        "English": {
            "short": "Information about soil health and nutrients.",
            "about": (
                "The Soil Health Card scheme helps farmers understand "
                "soil nutrient status and receive recommendations for "
                "appropriate soil nutrient management."
            ),
            "benefits": [
                "Information about soil nutrient status.",
                "Recommendations for balanced nutrient application.",
                "Supports informed soil management decisions."
            ],
            "eligibility": (
                "Farmers can contact the agriculture department or a "
                "soil testing laboratory for local availability."
            ),
            "apply": (
                "Contact your local agriculture office or soil testing "
                "laboratory to learn about soil sample testing."
            ),
            "url": "https://soilhealth.dac.gov.in/"
        },
        "తెలుగు": {
            "short": "నేల ఆరోగ్యం మరియు పోషకాల వివరాలు.",
            "about": (
                "సాయిల్ హెల్త్ కార్డ్ పథకం ద్వారా నేలలోని పోషకాల స్థితి "
                "మరియు నేల నిర్వహణకు సంబంధించిన సూచనలు తెలుసుకోవచ్చు."
            ),
            "benefits": [
                "నేలలోని పోషకాల వివరాలు తెలుసుకోవచ్చు.",
                "సమతుల్య పోషకాల వినియోగానికి సూచనలు పొందవచ్చు.",
                "నేల నిర్వహణపై సరైన నిర్ణయాలకు సహాయపడుతుంది."
            ],
            "eligibility": (
                "స్థానికంగా ఈ సేవ ఎలా అందుబాటులో ఉందో వ్యవసాయ శాఖ "
                "లేదా నేల పరీక్షా ప్రయోగశాలను సంప్రదించి తెలుసుకోండి."
            ),
            "apply": (
                "నేల నమూనాల సేకరణ మరియు పరీక్షా విధానం కోసం "
                "స్థానిక వ్యవసాయ కార్యాలయాన్ని సంప్రదించండి."
            ),
            "url": "https://soilhealth.dac.gov.in/"
        }
    },

    "Paramparagat Krishi Vikas Yojana": {
        "icon": "🌿",
        "English": {
            "short": "Support for organic farming practices.",
            "about": (
                "Paramparagat Krishi Vikas Yojana promotes organic farming "
                "and related practices under applicable programme guidelines."
            ),
            "benefits": [
                "Encourages organic farming practices.",
                "Supports participating farmer groups under programme guidelines.",
                "Promotes awareness of organic production."
            ],
            "eligibility": (
                "Participation depends on current programme guidelines "
                "and implementation arrangements in the area."
            ),
            "apply": (
                "Contact your local agriculture department to check "
                "availability and application procedures."
            ),
            "url": "https://agricoop.nic.in/"
        },
        "తెలుగు": {
            "short": "సేంద్రియ వ్యవసాయ పద్ధతులకు ప్రోత్సాహం.",
            "about": (
                "పరంపరాగత్ కృషి వికాస్ యోజన పథకం మార్గదర్శకాల ప్రకారం "
                "సేంద్రియ వ్యవసాయ పద్ధతులను ప్రోత్సహిస్తుంది."
            ),
            "benefits": [
                "సేంద్రియ వ్యవసాయ పద్ధతులను ప్రోత్సహిస్తుంది.",
                "నిబంధనలకు అనుగుణంగా రైతు సమూహాలకు మద్దతు అందించవచ్చు.",
                "సేంద్రియ ఉత్పత్తిపై అవగాహన పెంచుతుంది."
            ],
            "eligibility": (
                "ప్రస్తుత పథకం మార్గదర్శకాలు మరియు స్థానిక అమలు విధానంపై "
                "అర్హత ఆధారపడి ఉంటుంది."
            ),
            "apply": (
                "ప్రస్తుత పథకం వివరాలు మరియు దరఖాస్తు విధానం కోసం "
                "స్థానిక వ్యవసాయ శాఖను సంప్రదించండి."
            ),
            "url": "https://agricoop.nic.in/"
        }
    },

    "Agriculture Infrastructure Fund": {
        "icon": "🏗️",
        "English": {
            "short": "Financing support for eligible farm infrastructure.",
            "about": (
                "The Agriculture Infrastructure Fund supports eligible "
                "projects related to post-harvest management infrastructure "
                "and community farming assets."
            ),
            "benefits": [
                "Financing support for eligible infrastructure projects.",
                "May support storage and post-harvest facilities.",
                "Terms depend on scheme guidelines and lender approval."
            ],
            "eligibility": (
                "Eligibility depends on project type, applicant category "
                "and current scheme guidelines."
            ),
            "apply": (
                "Review the official portal and consult a participating "
                "bank about eligible projects."
            ),
            "url": "https://agriinfra.dac.gov.in/"
        },
        "తెలుగు": {
            "short": "వ్యవసాయ మౌలిక సదుపాయాలకు ఆర్థిక మద్దతు.",
            "about": (
                "అగ్రికల్చర్ ఇన్‌ఫ్రాస్ట్రక్చర్ ఫండ్ పథకం ద్వారా పంట అనంతర "
                "నిర్వహణ మరియు వ్యవసాయ సదుపాయాలకు సంబంధించిన అర్హమైన "
                "ప్రాజెక్టులకు ఆర్థిక మద్దతు అందించబడుతుంది."
            ),
            "benefits": [
                "అర్హమైన మౌలిక సదుపాయాల ప్రాజెక్టులకు ఆర్థిక మద్దతు.",
                "నిల్వ మరియు పంట అనంతర సదుపాయాలకు సహాయం ఉండవచ్చు.",
                "నిబంధనలు మరియు రుణదాత ఆమోదం వర్తిస్తాయి."
            ],
            "eligibility": (
                "ప్రాజెక్టు రకం, దరఖాస్తుదారుల వర్గం మరియు ప్రస్తుత "
                "పథకం మార్గదర్శకాల ప్రకారం అర్హత నిర్ణయించబడుతుంది."
            ),
            "apply": (
                "అర్హమైన ప్రాజెక్టులు మరియు దరఖాస్తు విధానం కోసం "
                "అధికారిక పోర్టల్‌ను పరిశీలించండి."
            ),
            "url": "https://agriinfra.dac.gov.in/"
        }
    },

    "Per Drop More Crop": {
        "icon": "💧",
        "English": {
            "short": "Promotes efficient water use in agriculture.",
            "about": (
                "Per Drop More Crop promotes efficient agricultural water "
                "use and eligible micro-irrigation practices under applicable "
                "programme guidelines."
            ),
            "benefits": [
                "Encourages efficient use of irrigation water.",
                "May support eligible micro-irrigation systems.",
                "Assistance depends on current state programme rules."
            ],
            "eligibility": (
                "Eligibility and assistance depend on current state "
                "implementation guidelines."
            ),
            "apply": (
                "Contact the state agriculture or horticulture department "
                "for current application procedures."
            ),
            "url": "https://pmksy.gov.in/"
        },
        "తెలుగు": {
            "short": "వ్యవసాయంలో నీటి సమర్థ వినియోగానికి ప్రోత్సాహం.",
            "about": (
                "పర్ డ్రాప్ మోర్ క్రాప్ కార్యక్రమం వ్యవసాయంలో నీటిని "
                "సమర్థంగా ఉపయోగించడాన్ని ప్రోత్సహిస్తుంది."
            ),
            "benefits": [
                "నీటి సమర్థ వినియోగాన్ని ప్రోత్సహిస్తుంది.",
                "అర్హమైన సూక్ష్మ నీటిపారుదల పరికరాలకు మద్దతు ఉండవచ్చు.",
                "సహాయం రాష్ట్ర పథకం నిబంధనలపై ఆధారపడి ఉంటుంది."
            ],
            "eligibility": (
                "అర్హత మరియు సహాయం ప్రస్తుత రాష్ట్ర మార్గదర్శకాలపై "
                "ఆధారపడి ఉంటాయి."
            ),
            "apply": (
                "దరఖాస్తు విధానం కోసం రాష్ట్ర వ్యవసాయ లేదా ఉద్యానవన "
                "శాఖను సంప్రదించండి."
            ),
            "url": "https://pmksy.gov.in/"
        }
    },

    "Agricultural Mechanization": {
        "icon": "🚜",
        "English": {
            "short": "Promotes access to modern agricultural machinery.",
            "about": (
                "The Sub-Mission on Agricultural Mechanization promotes "
                "access to suitable agricultural machinery under government "
                "programme guidelines."
            ),
            "benefits": [
                "Promotes modern agricultural equipment.",
                "May support eligible machinery and custom hiring centres.",
                "Support depends on current state programme rules."
            ],
            "eligibility": (
                "Eligibility depends on applicant category, equipment "
                "and state-level guidelines."
            ),
            "apply": (
                "Contact the local agriculture department to check "
                "machinery options and subsidy rules."
            ),
            "url": "https://agrimachinery.nic.in/"
        },
        "తెలుగు": {
            "short": "ఆధునిక వ్యవసాయ యంత్రాల వినియోగానికి ప్రోత్సాహం.",
            "about": (
                "వ్యవసాయ యాంత్రీకరణ కార్యక్రమం ప్రభుత్వ మార్గదర్శకాల "
                "ప్రకారం ఆధునిక వ్యవసాయ యంత్రాల వినియోగాన్ని ప్రోత్సహిస్తుంది."
            ),
            "benefits": [
                "ఆధునిక వ్యవసాయ పరికరాల వినియోగానికి ప్రోత్సాహం.",
                "అర్హమైన యంత్రాలకు మద్దతు ఉండవచ్చు.",
                "సహాయం రాష్ట్ర పథకం నిబంధనలపై ఆధారపడి ఉంటుంది."
            ],
            "eligibility": (
                "దరఖాస్తుదారుల వర్గం, పరికరాలు మరియు రాష్ట్ర మార్గదర్శకాల "
                "ప్రకారం అర్హత నిర్ణయించబడుతుంది."
            ),
            "apply": (
                "యంత్రాల వివరాలు మరియు సబ్సిడీ నిబంధనల కోసం "
                "స్థానిక వ్యవసాయ శాఖను సంప్రదించండి."
            ),
            "url": "https://agrimachinery.nic.in/"
        }
    },

    "Horticulture Development": {
        "icon": "🍎",
        "English": {
            "short": "Support for eligible horticulture activities.",
            "about": (
                "The Mission for Integrated Development of Horticulture "
                "supports eligible horticulture development activities "
                "under applicable programme guidelines."
            ),
            "benefits": [
                "May support eligible horticulture development activities.",
                "Support depends on specified activities and rules.",
                "Available assistance depends on the state and project."
            ],
            "eligibility": (
                "Eligibility depends on the activity, applicant category "
                "and current state implementation guidelines."
            ),
            "apply": (
                "Contact the state horticulture department for supported "
                "activities and application procedures."
            ),
            "url": "https://midh.gov.in/"
        },
        "తెలుగు": {
            "short": "అర్హమైన ఉద్యానవన కార్యకలాపాలకు మద్దతు.",
            "about": (
                "ఉద్యానవన అభివృద్ధి కార్యక్రమం మార్గదర్శకాల ప్రకారం "
                "అర్హమైన ఉద్యానవన కార్యకలాపాలకు మద్దతు అందిస్తుంది."
            ),
            "benefits": [
                "అర్హమైన ఉద్యానవన అభివృద్ధికి మద్దతు ఉండవచ్చు.",
                "పథకం నిబంధనల ప్రకారం నిర్దిష్ట కార్యకలాపాలకు సహాయం ఉంటుంది.",
                "సహాయం రాష్ట్రం మరియు ప్రాజెక్టు రకంపై ఆధారపడి ఉంటుంది."
            ],
            "eligibility": (
                "కార్యకలాపం, దరఖాస్తుదారుల వర్గం మరియు రాష్ట్ర "
                "మార్గదర్శకాల ఆధారంగా అర్హత నిర్ణయించబడుతుంది."
            ),
            "apply": (
                "ప్రస్తుత పథకం వివరాలు మరియు దరఖాస్తు విధానం కోసం "
                "రాష్ట్ర ఉద్యానవన శాఖను సంప్రదించండి."
            ),
            "url": "https://midh.gov.in/"
        }
    },

    "National Agriculture Market (e-NAM)": {
        "icon": "🛒",
        "English": {
            "short": "An online platform for agricultural marketing.",
            "about": (
                "e-NAM is an electronic trading platform intended to connect "
                "participating agricultural markets and support transparent "
                "agricultural marketing."
            ),
            "benefits": [
                "Provides an online agricultural market platform.",
                "Supports market information and electronic trading features.",
                "Services depend on participating markets and registration."
            ],
            "eligibility": (
                "Participation depends on market integration and applicable "
                "registration procedures."
            ),
            "apply": (
                "Visit the official e-NAM portal or contact a participating "
                "market for registration instructions."
            ),
            "url": "https://www.enam.gov.in/"
        },
        "తెలుగు": {
            "short": "వ్యవసాయ మార్కెటింగ్ కోసం ఆన్‌లైన్ వేదిక.",
            "about": (
                "e-NAM అనేది పాల్గొనే వ్యవసాయ మార్కెట్లను అనుసంధానించి, "
                "పారదర్శక వ్యవసాయ మార్కెటింగ్‌కు సహాయపడే ఎలక్ట్రానిక్ వేదిక."
            ),
            "benefits": [
                "ఆన్‌లైన్ వ్యవసాయ మార్కెట్ వేదికను అందిస్తుంది.",
                "మార్కెట్ సమాచారం మరియు ఎలక్ట్రానిక్ ట్రేడింగ్‌కు మద్దతు.",
                "సేవలు పాల్గొనే మార్కెట్లు మరియు నమోదు నిబంధనలపై ఆధారపడతాయి."
            ],
            "eligibility": (
                "మార్కెట్ అనుసంధానం మరియు నమోదు విధానం ప్రకారం "
                "సేవలు అందుబాటులో ఉంటాయి."
            ),
            "apply": (
                "నమోదు మరియు వినియోగ విధానం కోసం అధికారిక e-NAM "
                "వెబ్‌సైట్‌ను లేదా పాల్గొనే మార్కెట్‌ను సంప్రదించండి."
            ),
            "url": "https://www.enam.gov.in/"
        }
    }
}


# -------------------- PAGE STATE --------------------

if "page" not in st.session_state:
    st.session_state.page = 1

if "language" not in st.session_state:
    st.session_state.language = "English"

if "selected_scheme" not in st.session_state:
    st.session_state.selected_scheme = "PM-KISAN"


# -------------------- PAGE 1: HOME --------------------

if st.session_state.page == 1:

    st.markdown("""
    <div class="hero">
        <h1>🌱 AgriSahay AI</h1>
        <p>Your Guide to Government Agricultural Schemes</p>
        <p>ప్రభుత్వ వ్యవసాయ పథకాల వివరాలు ఒకే చోట</p>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.2, 1])

    with left:
        st.subheader("🌾 Welcome!")

        st.write(
            "Discover government agricultural schemes, understand "
            "their benefits and find official application information."
        )

        st.write(
            "ప్రభుత్వ వ్యవసాయ పథకాలు, వాటి ప్రయోజనాలు మరియు "
            "దరఖాస్తు వివరాలను తెలుసుకోండి."
        )

        language = st.selectbox(
            "Choose Your Language / మీ భాషను ఎంచుకోండి",
            ["English", "తెలుగు"]
        )

        if st.button("Get Started ➜"):
            st.session_state.language = language
            st.session_state.page = 2
            st.rerun()

    with right:
        st.markdown("""
        <div class="scheme-card">
            <h3>🌱 Explore Schemes</h3>
            <p>Find government agricultural programmes.</p>
            <hr>
            <h3>💰 Understand Benefits</h3>
            <p>Learn about financial assistance, insurance and credit.</p>
            <hr>
            <h3>🌐 Official Information</h3>
            <p>Visit government portals for current rules and applications.</p>
        </div>
        """, unsafe_allow_html=True)


# -------------------- PAGE 2: SCHEMES --------------------

elif st.session_state.page == 2:

    language = st.session_state.language

    if language == "తెలుగు":
        st.title("🌾 ప్రభుత్వ వ్యవసాయ పథకాలు")
        st.write("మీకు కావలసిన పథకాన్ని ఎంచుకోండి.")
        details_button = "వివరాలు చూడండి ➜"
        back_button = "⬅ హోమ్‌కు తిరిగి వెళ్లండి"
    else:
        st.title("🌾 Government Agricultural Schemes")
        st.write("Explore the available government schemes.")
        details_button = "View Details ➜"
        back_button = "⬅ Back to Home"

    st.markdown("### ✨ Available Schemes")

    scheme_names = list(schemes.keys())

    # Display three scheme cards in each row
    for start in range(0, len(scheme_names), 3):
        columns = st.columns(3)

        for column, scheme_name in zip(
            columns, scheme_names[start:start + 3]
        ):
            scheme = schemes[scheme_name]
            details = scheme[language]

            with column:
                st.markdown(
                    f"""
                    <div class="scheme-card">
                        <h3>{scheme['icon']} {scheme_name}</h3>
                        <p>{details['short']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    details_button,
                    key=f"view_{scheme_name}"
                ):
                    st.session_state.selected_scheme = scheme_name
                    st.session_state.page = 3
                    st.rerun()

    if st.button(back_button):
        st.session_state.page = 1
        st.rerun()


# -------------------- PAGE 3: SCHEME DETAILS --------------------

elif st.session_state.page == 3:

    language = st.session_state.language
    scheme_name = st.session_state.selected_scheme
    scheme = schemes[scheme_name]
    details = scheme[language]

    if language == "తెలుగు":
        about_heading = "పథకం గురించి"
        benefits_heading = "ప్రధాన ప్రయోజనాలు"
        eligibility_heading = "అర్హత వివరాలు"
        apply_heading = "ఎలా దరఖాస్తు చేయాలి?"
        official_button = "🌐 అధికారిక వెబ్‌సైట్ తెరవండి"
        back_button = "⬅ పథకాల జాబితాకు తిరిగి వెళ్లండి"
        notice = (
            "గమనిక: అర్హతలు మరియు దరఖాస్తు విధానాలు మారవచ్చు. "
            "తాజా వివరాలను అధికారిక వెబ్‌సైట్‌లో తనిఖీ చేయండి."
        )
    else:
        about_heading = "About the Scheme"
        benefits_heading = "Main Benefits"
        eligibility_heading = "Eligibility"
        apply_heading = "How to Apply"
        official_button = "🌐 Open Official Website"
        back_button = "⬅ Back to All Schemes"
        notice = (
            "Note: Eligibility and application procedures may change. "
            "Check the official website for current information."
        )

    st.markdown(
        f"""
        <div class="hero">
            <h1>{scheme['icon']} {scheme_name}</h1>
            <p>{details['short']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"### 📘 {about_heading}")
    st.write(details["about"])

    st.divider()

    st.markdown(f"### ⭐ {benefits_heading}")

    for benefit in details["benefits"]:
        st.markdown(f"- {benefit}")

    st.divider()

    left, right = st.columns(2)

    with left:
        st.markdown(f"### 👨‍🌾 {eligibility_heading}")
        st.write(details["eligibility"])

    with right:
        st.markdown(f"### 📝 {apply_heading}")
        st.write(details["apply"])

    st.write("")

    st.link_button(
        official_button,
        details["url"]
    )

    st.info(notice)

    if st.button(back_button):
        st.session_state.page = 2
        st.rerun()


# -------------------- FOOTER --------------------

st.divider()

st.markdown("""
<div style="text-align:center; padding:10px;">
    <p><b>🌱 AgriSahay AI</b></p>
    <p>Your Guide to Government Agricultural Schemes</p>
    <p style="font-size:12px;">
        Information is provided for general guidance.
        Please verify current scheme rules on official government portals.
    </p>
</div>
""", unsafe_allow_html=True)
