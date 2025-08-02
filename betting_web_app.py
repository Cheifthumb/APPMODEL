import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib
from sklearn.preprocessing import LabelEncoder
from config.track_betting_config import track_betting_config, track_model_map

# Run with: python -m streamlit run betting_web_app.py

st.set_page_config(page_title="Horse Racing Bets", layout="wide")
st.title("🏇 Horse Racing Prediction and Bet Selector")

# 💰 Bankroll input comes first — sticky in session
st.subheader("💰 Bankroll Setup")
if 'bankroll' not in st.session_state:
    st.session_state['bankroll'] = 1000.0  # default

st.session_state['bankroll'] = st.number_input(
    "Enter your bankroll for today (£):",
    min_value=0.0,
    value=st.session_state['bankroll'],
    step=50.0,
    format="%.2f"
)
st.caption(f"💡 1% of bankroll: £{st.session_state['bankroll'] * 0.01:.2f}")

# Upload Excel race file
uploaded_file = st.file_uploader("📤 Upload your Excel race file", type=["xlsx"])


if uploaded_file:
    file_name = uploaded_file.name
    input_path = f"Daily_Bets/{file_name}"
    os.makedirs("Daily_Bets", exist_ok=True)
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded {file_name}")
    
    df = pd.read_excel(input_path)
    df['Industry SP'] = pd.to_numeric(df['Industry SP'], errors='coerce')

    editable_cols = ['Date of Race', 'Track', 'Time', 'Horse', 'Industry SP']
    edit_df = df[editable_cols].copy()

    if 'sp_preview' not in st.session_state:
        st.session_state['sp_preview'] = pd.DataFrame()

    st.subheader("✍️ Update Industry SPs Before Prediction")
    edited_df = st.data_editor(edit_df, num_rows="dynamic", use_container_width=True, key="editable_sp")

    # Button to recalculate SP Fav (as rank numbers)
    if st.button("🔄 Recalculate SP Fav (Rank Numbers)"):
        # Update df with SP edits
        df.set_index(['Date of Race', 'Time', 'Horse'], inplace=True)
        edited_df.set_index(['Date of Race', 'Time', 'Horse'], inplace=True)
        df.update(edited_df)
        df.reset_index(inplace=True)
        edited_df.reset_index(inplace=True)

        # Create Race_ID and calculate rank
        df['Race_ID'] = df['Date of Race'].astype(str) + "_" + df['Time'].astype(str) + "_" + df['Track'].astype(str)
        df['Industry SP'] = pd.to_numeric(df['Industry SP'], errors='coerce')

        # ✅ Assign numeric SP rank to the SP Fav column
        df['SP Fav'] = df.groupby('Race_ID')['Industry SP'].rank(method='min')

        # Optional: also assign Is Favourite (for your eyes)
        df['Is Favourite'] = df['SP Fav'].apply(lambda x: 1 if x == 1 else 0)

        # Show preview
        preview = df[['Date of Race', 'Time', 'Track', 'Horse', 'Industry SP', 'SP Fav']]
        st.session_state['sp_preview'] = preview.copy()

    # Show the SP Fav rank preview
    if not st.session_state['sp_preview'].empty:
        st.subheader("📊 SP Fav Rank Preview (1 = favourite)")
        st.dataframe(st.session_state['sp_preview'])

    # Confirm to update and proceed
    if st.button("✅ Confirm SP Updates and Run Model"):
        df.set_index(['Date of Race', 'Time', 'Horse'], inplace=True)
        edited_df.set_index(['Date of Race', 'Time', 'Horse'], inplace=True)
        df.update(edited_df)
        df.reset_index(inplace=True)



    numeric_cols = [
        'Forecasted Odds', 'Industry SP', 'SP Win Return',
        'Betfair Lay Return', 'Wins Last 5 races', 'Runs last 18 months',
        'Course Wins', 'Distance Wins', 'Total Prev Races'
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    if 'Days Since Last time out' not in df.columns and 'Date of Race' in df.columns and 'Horse' in df.columns:
        df = df.sort_values(['Horse', 'Date of Race'])
        df['Days Since Last time out'] = df.groupby('Horse')['Date of Race'].diff().dt.days

    df['Log Industry SP'] = df['Industry SP'].apply(lambda x: pd.NA if pd.isna(x) or x <= 0 else np.log(x))
    
    if 'Up in Trip' in df.columns:
        df['Up in Trip'] = df['Up in Trip'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)
    
        # ✅ Recalculate SP Rank and Fav after cleaning
    df['Race_ID'] = df['Date of Race'].astype(str) + "_" + df['Time'].astype(str) + "_" + df['Track'].astype(str)

    df['SP Fav'] = df.groupby('Race_ID')['Industry SP'].rank(method='min')
    df['Race_ID'] = df['Date of Race'].astype(str) + "_" + df['Time'].astype(str) + "_" + df['Track'].astype(str)
    df['SP Rank'] = df.groupby('Race_ID')['Industry SP'].rank(method='min')
    df['Is Favourite'] = df['SP Fav'].apply(lambda x: 1 if str(x).strip().lower() == 'fav' else 0)

    # Feature engineering
    df['Win Rate Last 5'] = df['Wins Last 5 races'] / df['Total Prev Races'].replace(0, pd.NA)
    df['Adjusted Win Rate'] = df['Wins Last 5 races'] / df['Runs last 18 months'].replace(0, pd.NA)
    df['Course Win Ratio'] = df['Course Wins'] / df['Total Prev Races'].replace(0, pd.NA)
    df['Distance Win Ratio'] = df['Distance Wins'] / df['Total Prev Races'].replace(0, pd.NA)
    df['Value Indicator'] = df['Forecasted Odds'] - df['Industry SP']
    df['Lay Pressure %'] = (df['Betfair Lay Return'] - df['SP Win Return']) / df['SP Win Return'].replace(0, pd.NA)

    # Prediction setup
    info_cols = ['Date of Race', 'Time', 'Track', 'Horse', 'Distance', 'Place', 'Industry SP', 'Betfair SP']
    feature_cols = [
        'Going', 'Distance', 'Class', 'Stall', 'Official Rating', 'Age',
        'SP Fav', 'Industry SP', 'Forecasted Odds',
        'Runs last 18 months', 'Wins Last 5 races',
        'Avg % SP Drop Last 5 races', 'Avg % SP Drop last 18 mths',
        'RBD Rating', 'RBD Rank', 'Total Prev Races',
        'Days Since Last time out', 'Course Wins', 'Distance Wins', 'Class Wins', 'Going Wins',
        'Up in Trip'
    ]

    all_predictions = []

    for track in df['Track'].dropna().str.upper().unique():
        track_df = df[df['Track'].str.upper() == track].copy()

        if track not in track_betting_config:
            st.warning(f"⚠️ No config for {track} — skipping.")
            continue

        model_name = track_model_map.get(track)
        if not model_name:
            st.warning(f"⚠️ No model for {track} — skipping.")
            continue

        model_path = f"models/{model_name}.pkl"


        try:
            model = joblib.load(model_path)
        except Exception as e:
            st.warning(f"⚠️ Failed to load model for {track}: {e}")
            continue

        for mode, config in track_betting_config[track].items():
            st.info(f"🧠 Running model + config for {track} — mode: {mode}")

            features = [f for f in feature_cols if f in track_df.columns]
            X = track_df[features].copy()
            for col in X.select_dtypes(include='object'):
                le = LabelEncoder()
                X[col] = le.fit_transform(X[col].astype(str))
            X = X.fillna(-999)

            win_probs = model.predict_proba(X)[:, 1]

            preds = track_df[info_cols].copy()
            preds['Predicted_Win_Probability'] = win_probs
            preds['Race_ID'] = preds['Date of Race'].astype(str) + "_" + preds['Time'].astype(str)
            preds['Odds_To_Use'] = preds['Industry SP']
            preds['Predicted_Win_Probability'] = preds.groupby('Race_ID')['Predicted_Win_Probability'].transform(lambda x: x / x.sum())
            preds['Predicted_Rank'] = preds.groupby('Race_ID')['Predicted_Win_Probability'].rank(method='first', ascending=False)

            field_sizes = preds.groupby('Race_ID')['Horse'].count().rename('Field_Size')
            preds = preds.merge(field_sizes, left_on='Race_ID', right_index=True)

            preds['Reject_Reason'] = ''
            preds['Expected_Value'] = (preds['Predicted_Win_Probability'] * (preds['Odds_To_Use'] - 1)) - (1 - preds['Predicted_Win_Probability'])
            preds['Kelly_Fraction'] = preds['Expected_Value'] / (preds['Odds_To_Use'] - 1)

            preds.loc[~preds['Predicted_Rank'].isin(config.get("allowed_predicted_ranks", [])), 'Reject_Reason'] += 'rank_low|'
            preds.loc[preds['Expected_Value'] <= config.get("min_ev_threshold", -100), 'Reject_Reason'] += 'ev_low|'
            preds.loc[preds['Kelly_Fraction'] <= config.get("min_kelly_fraction", -100), 'Reject_Reason'] += 'kelly_low|'
            preds.loc[preds['Odds_To_Use'] > config.get("max_odds_threshold", 100), 'Reject_Reason'] += 'odds_high|'
            preds.loc[preds['Odds_To_Use'] < config.get("min_odds_threshold", 0), 'Reject_Reason'] += 'odds_low|'
            preds.loc[~preds['Field_Size'].isin(config.get("allowed_field_sizes", range(1, 100))), 'Reject_Reason'] += 'field_size|'
            
            # ✅ Optional SP Range filter
            min_sp = config.get("min_sp", None)
            max_sp = config.get("max_sp", None)

            if min_sp is not None:
                preds.loc[preds['Odds_To_Use'] < min_sp, 'Reject_Reason'] += 'sp_below_min|'
            if max_sp is not None:
                preds.loc[preds['Odds_To_Use'] > max_sp, 'Reject_Reason'] += 'sp_above_max|'

            winrate_type = config.get("winrate_filter_type", "none")
            if winrate_type == "fixed":
                preds['Winrate_Threshold'] = config.get("fixed_winrate_threshold", 0.0)
            elif winrate_type == "dynamic":
                preds['Winrate_Threshold'] = 1 / preds['Field_Size']
            else:
                preds['Winrate_Threshold'] = 0

            preds.loc[preds['Predicted_Win_Probability'] <= preds['Winrate_Threshold'], 'Reject_Reason'] += 'winrate_low|'
            preds['Bet_Recommended'] = preds['Reject_Reason'] == ''

            bankroll = st.session_state['bankroll']
            stake_pool = bankroll * config.get("bankroll_perc", 0.1)
            preds['Recommended_Stake'] = 0
            for race_id, group in preds.groupby('Race_ID'):
                group['Stake_Unscaled'] = group['Kelly_Fraction'] * stake_pool
                total_stake = group.loc[group['Bet_Recommended'], 'Stake_Unscaled'].sum()
                if total_stake > stake_pool:
                    scale = stake_pool / total_stake
                    group.loc[group['Bet_Recommended'], 'Recommended_Stake'] = group['Stake_Unscaled'] * scale
                else:
                    group.loc[group['Bet_Recommended'], 'Recommended_Stake'] = group['Stake_Unscaled']
                preds.loc[group.index, 'Recommended_Stake'] = group['Recommended_Stake']

            preds['Betting_Mode'] = mode
            all_predictions.append(preds)


    if not all_predictions:
        st.error("❌ No valid tracks with model+config found.")
        st.stop()

    final_df = pd.concat(all_predictions).reset_index(drop=True)

    # SINGLE BETS
    st.subheader("✅ Final Single Bets")
    single_bets = final_df[(final_df['Bet_Recommended']) & (final_df['Betting_Mode'] == 'single')]
    st.dataframe(single_bets[
        ['Date of Race', 'Time', 'Track', 'Horse', 'Industry SP', 'Predicted_Win_Probability',
         'Expected_Value', 'Kelly_Fraction', 'Predicted_Rank', 'Field_Size', 'Recommended_Stake']
    ])

    # REVERSE FORECAST BETS — PAIRED DISPLAY
    st.subheader("🔁 Final Reverse Forecast Bets (Paired)")

    reverse_bets = final_df[
        (final_df['Bet_Recommended']) & 
        (final_df['Betting_Mode'].str.startswith("reverse_forecast"))
    ].copy()

    pairs = []
    for race_id, group in reverse_bets.groupby('Race_ID'):
        top_two = group.nsmallest(2, 'Predicted_Rank')
        if len(top_two) == 2:
            horse_a = top_two.iloc[0]
            horse_b = top_two.iloc[1]
            pairs.append({
                'Date': horse_a['Date of Race'],
                'Time': horse_a['Time'],
                'Track': horse_a['Track'],
                'Horse A': horse_a['Horse'],
                'SP A': horse_a['Industry SP'],
                'Horse B': horse_b['Horse'],
                'SP B': horse_b['Industry SP'],
                'Field Size': horse_a['Field_Size']
            })

    reverse_df = pd.DataFrame(pairs)
    if not reverse_df.empty:
        st.dataframe(reverse_df)
    else:
        st.info("No valid reverse forecast pairings found.")


    # REJECTED
    st.subheader("❌ Rejected Bets")
    rejected_bets = final_df[~final_df['Bet_Recommended']]
    st.dataframe(rejected_bets[
        ['Date of Race', 'Time', 'Track', 'Horse', 'Industry SP', 'Predicted_Win_Probability',
         'Expected_Value', 'Kelly_Fraction', 'Predicted_Rank', 'Field_Size', 'Reject_Reason', 'Betting_Mode']
    ])

    st.info(f"📊 Total runners processed: {len(final_df)}")

