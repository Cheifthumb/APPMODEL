# track_betting_config.py

track_betting_config = {
    "NEWMARKET": {
        "single": {
            "bankroll_perc": 0.1,
            "min_ev_threshold": 0.1,
            "min_kelly_fraction": 0.04,
            "max_odds_threshold": 10.1,
            "min_odds_threshold": 1.5,
            "stake_mode": "kelly",              # 'kelly', 'fixed', or 'winrate'
            "fixed_stake_perc": 0.01,
            "winrate_filter_type": "none",      # 'none', 'fixed', or 'dynamic'
            "fixed_winrate_threshold": 0.03,
            "allowed_predicted_ranks": [3, 4],
            "allowed_field_sizes": [6, 7],
        },
        "reverse_forecast_a": {
            "allowed_field_sizes": [6],
            "allowed_predicted_ranks": [1, 4],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
            "stake_mode": "split_half",  # special logic: A→B + B→A
        }
    },
    "RIPON": {
        "reverse_forecast_a": {
            "allowed_field_sizes": [6],
            "allowed_predicted_ranks": [1, 2],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
            "stake_mode": "split_half"
        }
    },
    "NEWTON ABBOT": {
        "reverse_forecast_a": {
            "allowed_field_sizes": [5, 6],
            "allowed_predicted_ranks": [2, 3],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
            "stake_mode": "split_half"
        }
    },
    "REDCAR": {
        "reverse_forecast_a": {
            "allowed_field_sizes": [8, 9],
            "allowed_predicted_ranks": [1, 3],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
            "stake_mode": "split_half"
        }
     },
    "NEWBURY": {
        "single": {
            "bankroll_perc": 0.1,
            "min_ev_threshold": 0.00,
            "min_kelly_fraction": 0.00,
            "max_odds_threshold": 15.1,
            "min_odds_threshold": 5.01,
            "stake_mode": "kelly",              # 'kelly', 'fixed', or 'winrate'
            "fixed_stake_perc": 0.01,
            "winrate_filter_type": "none",      # 'none', 'fixed', or 'dynamic'
            "fixed_winrate_threshold": 0.03,
            "allowed_predicted_ranks": [2,4],
            "allowed_field_sizes": [7],
        },
        "reverse_forecast_a": {
            "allowed_field_sizes": [6,7,8],
            "allowed_predicted_ranks": [1,4],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -1,
            "stake_mode": "split_half"   
     
        }
     },
     "ASCOT": {
        "single": {
            "bankroll_perc": 0.1,
            "min_ev_threshold": 0.1,
            "min_kelly_fraction": 0.025,
            "max_odds_threshold": 15.1,
            "min_odds_threshold": 1.5,
            "stake_mode": "kelly",              # 'kelly', 'fixed', or 'winrate'
            "fixed_stake_perc": 0.01,
            "winrate_filter_type": "none",      # 'none', 'fixed', or 'dynamic'
            "fixed_winrate_threshold": 0.03,
            "allowed_predicted_ranks": [1,2,3,4,5],
            "allowed_field_sizes": [4,5,6, 7],
        },
        "reverse_forecast_a": {
            "allowed_field_sizes": [7],
            "allowed_predicted_ranks": [1, 4],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
            "stake_mode": "split_half",  # special logic: A→B + B→A
        },
        "reverse_forecast_B": {
            "allowed_field_sizes": [4,5,6],
            "allowed_predicted_ranks": [2,3],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
            "stake_mode": "split_half",  # special logic: A→B + B→A
        }    
     },
     "SANDOWN": {
        "single": {
            "bankroll_perc": 0.1,
            "min_ev_threshold": 0.1,
            "min_kelly_fraction": 1,
            "max_odds_threshold": 15.1,
            "min_odds_threshold": 1.5,
            "stake_mode": "kelly",              # 'kelly', 'fixed', or 'winrate'
            "fixed_stake_perc": 0.01,
            "winrate_filter_type": "none",      # 'none', 'fixed', or 'dynamic'
            "fixed_winrate_threshold": 0.03,
            "allowed_predicted_ranks": [1,2,3,4,5],
            "allowed_field_sizes": [4,5,6, 7],
        },
        "reverse_forecast_a": {
            "allowed_field_sizes": [6,7],
            "allowed_predicted_ranks": [2,3],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
            "stake_mode": "split_half",  # special logic: A→B + B→A
        },
        "reverse_forecast_B": {
            "allowed_field_sizes": [4],
            "allowed_predicted_ranks": [2,3],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
            "stake_mode": "split_half",  # special logic: A→B + B→A
        } 
     }
}
