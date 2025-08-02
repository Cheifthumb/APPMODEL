# track_betting_config.py
track_model_map = {
    "SANDOWN": "NATIONAL_HUNT_model",
    "FFOS LAS": "NATIONAL_HUNT_model",
    "DONCASTER": "NATIONAL_HUNT_model",
    "ASCOT": "ASCOT_model",
    "SALISBURY": "SALISBURY_model",
    "NEWBURY": "NEWBURY_model",
    "NEWMARKET": "NEWMARKET_model",
    "WINDSOR": "WINDSOR_model",
    "RIPON": "RIPON_model",
    "REDCAR": "REDCAR_model",
    "NEWTON ABBOT": "NEWTON_ABBOT_model",
    "EPSOM": "FLAT_model",
    "BATH": "FLAT_model"
    # Add more as needed
}



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
    "BATH": {
        "reverse_forecast_a": {
            "allowed_field_sizes": [8],
            "allowed_predicted_ranks": [1, 4],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
            "stake_mode": "split_half"
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
            "min_kelly_fraction": -1,
            "stake_mode": "split_half"
        },
        "reverse_forecast_b": {
            "allowed_field_sizes": [6],
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
    "EPSOM": {
        "single": {
            "bankroll_perc": 0.1,
            "min_ev_threshold": 0.00,
            "min_kelly_fraction": 5,
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
            "allowed_field_sizes": [6],
            "allowed_predicted_ranks": [1,4],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -1,
            "stake_mode": "split_half"   
     
        }  
    },
    "DONCASTER": {
        "single": {
            "bankroll_perc": 0.1,
            "min_ev_threshold": 0.00,
            "min_kelly_fraction": 0.001,
            "max_odds_threshold": 15.1,
            "min_odds_threshold": 5.1,
            "stake_mode": "kelly",              # 'kelly', 'fixed', or 'winrate'
            "fixed_stake_perc": 0.01,
            "winrate_filter_type": "none",      # 'none', 'fixed', or 'dynamic'
            "fixed_winrate_threshold": 0.03,
            "allowed_predicted_ranks": [1,2,3,4,5],
            "allowed_field_sizes": [7],
        },
        "reverse_forecast_a": {
            "allowed_field_sizes": [7],
            "allowed_predicted_ranks": [1,5],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
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
            "min_ev_threshold": 0.00,
            "min_kelly_fraction": 0.02,
            "max_odds_threshold": 10.1,
            "min_odds_threshold": 5,
            "stake_mode": "kelly",              # 'kelly', 'fixed', or 'winrate'
            "fixed_stake_perc": 0.01,
            "winrate_filter_type": "none",      # 'none', 'fixed', or 'dynamic'
            "fixed_winrate_threshold": 0.03,
            "allowed_predicted_ranks": [1,2,3,4],
            "allowed_field_sizes": [4,6],
        },
        "reverse_forecast_a": {
            "allowed_field_sizes": [6,7],
            "allowed_predicted_ranks": [2,3],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
            "stake_mode": "split_half",  # special logic: A→B + B→A
        },
        "reverse_forecast_B": {
            "allowed_field_sizes": [8],
            "allowed_predicted_ranks": [1,4],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -1.0,
            "stake_mode": "split_half",  # special logic: A→B + B→A
        } 
      },
      "SALISBURY": {
        "single": {
            "bankroll_perc": 0.1,
            "min_ev_threshold": 0.00,
            "min_kelly_fraction": 0.00,
            "max_odds_threshold": 10.1,
            "min_odds_threshold": 1.5,
            "stake_mode": "kelly",              # 'kelly', 'fixed', or 'winrate'
            "fixed_stake_perc": 0.01,
            "winrate_filter_type": "none",      # 'none', 'fixed', or 'dynamic'
            "fixed_winrate_threshold": 0.03,
            "allowed_predicted_ranks": [1,2,3,4,5],
            "allowed_field_sizes": [5],
        },
        "reverse_forecast_a": {
            "allowed_field_sizes": [5,6,7],
            "allowed_predicted_ranks": [1,4],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
            "stake_mode": "split_half",  # special logic: A→B + B→A
        },
        "reverse_forecast_B": {
            "allowed_field_sizes": [7],
            "allowed_predicted_ranks": [1,2],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": 1,
            "stake_mode": "split_half",  # special logic: A→B + B→A  
        }
    
        },
        "WINDSOR":  {
        "single": {
            "bankroll_perc": 0.1,
            "min_ev_threshold": 0.00,
            "min_kelly_fraction": 1,
            "max_odds_threshold": 10.1,
            "min_odds_threshold": 1.5,
            "stake_mode": "kelly",              # 'kelly', 'fixed', or 'winrate'
            "fixed_stake_perc": 0.01,
            "winrate_filter_type": "none",      # 'none', 'fixed', or 'dynamic'
            "fixed_winrate_threshold": 0.03,
            "allowed_predicted_ranks": [1],
            "allowed_field_sizes": [2],
        },
        "reverse_forecast_a": {
            "allowed_field_sizes": [10,11],
            "allowed_predicted_ranks": [1,2],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -1,
            "stake_mode": "split_half",  # special logic: A→B + B→A
        },
        "reverse_forecast_B": {
            "allowed_field_sizes": [2],
            "allowed_predicted_ranks": [1],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": 1,
            "stake_mode": "split_half",  # special logic: A→B + B→A  
        }
    
        },
        "FFOS LAS":  {
        "single": {
            "bankroll_perc": 0.1,
            "min_ev_threshold": 0.00,
            "min_kelly_fraction": 1,
            "max_odds_threshold": 10.1,
            "min_odds_threshold": 1.5,
            "stake_mode": "kelly",              # 'kelly', 'fixed', or 'winrate'
            "fixed_stake_perc": 0.01,
            "winrate_filter_type": "none",      # 'none', 'fixed', or 'dynamic'
            "fixed_winrate_threshold": 0.03,
            "allowed_predicted_ranks": [1],
            "allowed_field_sizes": [2],
        },
        "reverse_forecast_a": {
            "allowed_field_sizes": [6],
            "allowed_predicted_ranks": [1,3],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
            "stake_mode": "split_half",  # special logic: A→B + B→A
        },
        "reverse_forecast_B": {
            "allowed_field_sizes": [7],
            "allowed_predicted_ranks": [1,2],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
            "stake_mode": "split_half",  # special logic: A→B + B→A
   
        },
        "reverse_forecast_C": {
            "allowed_field_sizes": [9],
            "allowed_predicted_ranks": [1,2],
            "min_ev_threshold": -5.0,
            "min_kelly_fraction": -0.5,
            "stake_mode": "split_half",  # special logic: A→B + B→A
      }

    }
}
