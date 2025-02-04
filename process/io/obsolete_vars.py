"""Dict of obsolete vars and their new names for the input validator.

This is used by the input_validator module to find any obsolete variables in the
input file (which have since been renamed in the current version of the source).
If the input validator finds an obsolete var, it can then suggest the new name
of that variable, based on this dictionary. This should make migration of old
input files easier, and variable renaming less painful.

Each key is an obsolete var, the value is either the new var name or None if the
var is deprecated.

Note: this is now relied upon by Blueprint, pending implementing a proper API.
"""
OBS_VARS = {
    "snull": "i_single_null",
    "tfno": "n_tf",
    "itfsup": "i_tf_sup",
    "r_tf_inleg_mid": "r_tf_inboard_mid",
    "rtot": "r_tf_outboard_mid",
    "a_tf_inboard": "tfareain",
    "r_tf_inleg_in": "r_tf_inleg_in",
    "r_tf_inleg_out": "r_tf_inleg_out",
    "a_tf_wp": "awpc",
    "sigttf": "sig_tf_t",
    "sigtcon": "sig_tf_t",
    "sigrtf": "sig_tf_r",
    "sigrcon": "sig_tf_r",
    "sigvert": "sig_tf_z",
    "sig_vmises_case": "sig_tf_vmises",
    "sig_vmises_cond": "sig_tf_vmises",
    "sig_tresca_case": "sig_tf_treca",
    "sig_tresca_cond": "sig_tf_treca",
    "sigver": None,
    "sigrad": None,
    "poisson": "poisson_steel",
    "eywp": "eyoung_winding",
    "eyins": "eyoung_ins",
    "eystl": "eyoung_steel",
    "isumattf": "i_tf_sc_mat",
    "turnstf": "n_tf_turn",
    "awptf": "a_tf_wp",
    "dr_tf_case_in": "thkcas",
    "f_tf_case_out": "casthi_fraction",
    "dr_tf_case_out": "casthi",
    "eyoung_reinforced_al": "eyoung_nibron",
    "thkwp": "dr_tf_wp",
    "leni": "t_cable",
    "leno": "t_turn",
    "conductor_width": "t_conductor",
    "deltf": "tftsgap",
    "ddwi": "d_vv_out",
    "pnuccp": "pnuc_cp",
    "nuc_pow_dep_tot": "pnuc_tot_blk_sector",
    "t_turn": "t_turn_tf",
    "ratecdol": "discount_rate",
    "strtf1": "sig_tf_case",
    "strtf2": "sig_tf_wp",
    "alstrtf": ["sig_tf_case_max", "sig_tf_wp_max"],
    "strtf0": "sig_tf_cs_bucked",
    "eyoung_winding": ["eyoung_cond_axial", "eyoung_cond_trans"],
    "i_tf_plane_stress": "i_tf_stress_model",
    "windstrain": "strncon_tf",
    "eyzwp": "eyoung_wp_z_eff",
    "strncon_cs": "str_cs_con_res",
    "strncon_pf": "str_pf_con_res",
    "strncon_tf": "str_tf_con_res",
    "i_strain_wp": "i_str_wp",
    "strain_wp_max": "str_wp_max",
    "strain_wp": "str_wp",
    "fstrain_wp": "fstr_wp",
    "rad_fraction": "rad_fraction_total",
    "pcoreradmw": "pinnerzoneradmw",
    "pedgeradmw": "pouterzoneradmw",
    "rad_fraction_core": "rad_fraction_LCFS",
    "thshield": ["thshield_ib", "thshield_ob", "thshield_vb"],
    "igeom": None,
}
