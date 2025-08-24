# 1. IMPORTS
import pandas as pd
from datetime import datetime


# 2. CONFIGURATION & CONSTANTS
FILE_PATH = r'C:\Users\rgvka\Downloads\sample_data.csv'
SUPPORTED_DATE_FORMATS = ["%m/%d/%Y", "%m-%d-%Y"]
CURRENT_DATE = pd.to_datetime("2025-08-23")
MILESTONE_DAYS = [7, 15, 30, 50, 75]

# Dictionary of milestone-specific messages
MILESTONE_MESSAGES = {
    7: (
        "जय श्री श्याम 🙏\n"
        "प्रिय {name},\n"
        "आपकी अरजी को आज 7 दिन पूरे हो गए हैं। "
        "बाबा के दरबार में पहला सप्ताह बहुत शुभ माना जाता है। "
        "हम प्रार्थना करते हैं कि आपके मन की पुकार बाबा तक पहुँच चुकी हो।\n"
        "जय श्री श्याम।"
    ),
    15: (
        "जय श्री श्याम 🙏\n"
        "प्रिय {name},\n"
        "पिछले 15 दिनों से आपकी अरजी बाबा के चरणों में लग रही है। "
        "यह निरंतरता आपके विश्वास और समर्पण का प्रमाण है। "
        "बाबा निश्चित ही आपके धैर्य और श्रद्धा को आशीर्वाद में बदलेंगे।\n"
        "जय श्री श्याम।"
    ),
    30: (
        "जय श्री श्याम 🙏\n"
        "प्रिय {name},\n"
        "आपकी अरजी को आज 30 दिन पूर्ण हुए हैं। "
        "एक पूरा महीना बाबा के चरणों में साधना और प्रार्थना का बहुत महत्व है। "
        "हम प्रार्थना करते हैं कि बाबा आपके जीवन में सुख-समृद्धि और शांति प्रदान करें।\n"
        "जय श्री श्याम।"
    ),
    50: (
        "जय श्री श्याम 🙏\n"
        "प्रिय {name},\n"
        "पिछले 50 दिनों से आपकी अरजी लगातार बाबा के दरबार में जा रही है। "
        "इतना लंबा समय केवल सच्चे विश्वास और समर्पण से ही संभव है। "
        "बाबा अवश्य ही आपकी पुकार का उत्तर देंगे और जीवन में नई राह दिखाएँगे।\n"
        "जय श्री श्याम।"
    ),
    75: (
        "जय श्री श्याम 🙏\n"
        "प्रिय {name},\n"
        "आज आपकी अरजी को 75 दिन पूर्ण हुए हैं। "
        "यह साधना केवल अरजी नहीं, बल्कि आपके विश्वास की शक्ति का प्रतीक है। "
        "बाबा आपको आशीर्वाद दें और आपके जीवन को प्रकाश और आनंद से भर दें।\n"
        "जय श्री श्याम।"
    )
}


# 3. FUNCTION DEFINITIONS
def parse_dates_with_multiple_formats(date_series, formats):
    parsed_dates = []
    for date_string in date_series:
        parsed_datetime = None
        for date_format in formats:
            try:
                parsed_datetime = datetime.strptime(date_string, date_format)
                break
            except (ValueError, TypeError):
                continue
        parsed_dates.append(parsed_datetime if parsed_datetime else date_string)
    return pd.Series(parsed_dates)


# 4. DATA LOADING & PROCESSING
prayers_df = pd.read_csv(FILE_PATH, encoding='utf-8')

prayers_df['date'] = prayers_df['date'].str.split(' ').str[0]
prayers_df['date'] = parse_dates_with_multiple_formats(prayers_df['date'].astype(str), SUPPORTED_DATE_FORMATS)

sorted_prayers_df = prayers_df.sort_values(by='date', ignore_index=True)
sorted_prayers_df['days_since_prayer'] = (CURRENT_DATE - sorted_prayers_df['date']).dt.days


# 5. MESSAGE GENERATION
milestone_prayers_df = sorted_prayers_df[sorted_prayers_df['days_since_prayer'].isin(MILESTONE_DAYS)].copy()

milestone_prayers_df.loc[:, "message"] = milestone_prayers_df.apply(
    lambda row: MILESTONE_MESSAGES.get(row["days_since_prayer"], "").format(
        name=row["name"]
    ),
    axis=1
)


# 6. OUTPUT
if not milestone_prayers_df.empty:
    print("--- Sample Message ---")
    print(milestone_prayers_df.iloc[0]['message'])
    print("--- Sample Message ---")
    print(milestone_prayers_df.iloc[2]['message'])
else:
    print("No messages to generate for today's milestones.")
