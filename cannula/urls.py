from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^user_profile_edit$', views.user_profile_edit, name='user_profile_edit'),
    url(r'dashboards/malaria/$', views.malaria_dashboard, name='thematic_malaria'),
    url(r'scorecards/malaria/cases\.php', views.malaria_cases_scorecard, {'org_unit_level': 3}, name='malaria_cases'),
    url(r'scorecards/malaria/cases\.xls', views.malaria_cases_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='malaria_cases_excel'),
    url(r'scorecards/malaria/cases\.csv', views.malaria_cases_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='malaria_cases_csv'),
    url(r'scorecards/malaria/cases_districts\.php', views.malaria_cases_scorecard, {'org_unit_level': 1}, name='malaria_cases_districts'),
    url(r'scorecards/malaria/cases_districts\.xls', views.malaria_cases_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='malaria_cases_districts_excel'),
    url(r'scorecards/malaria/cases_districts\.csv', views.malaria_cases_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='malaria_cases_districts_csv'),
    url(r'scorecards/malaria/compliance\.php', views.malaria_compliance, {'org_unit_level': 3}, name='malaria_compliance'),
    url(r'scorecards/malaria/compliance\.xls', views.malaria_compliance, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='malaria_compliance_excel'),
    url(r'scorecards/malaria/compliance\.csv', views.malaria_compliance, {'org_unit_level': 3, 'output_format': 'CSV'}, name='malaria_compliance_csv'),
    url(r'scorecards/malaria/compliance_districts\.php', views.malaria_compliance, {'org_unit_level': 1}, name='malaria_compliance_districts'),
    url(r'scorecards/malaria/compliance_districts\.xls', views.malaria_compliance, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='malaria_compliance_districts_excel'),
    url(r'scorecards/malaria/compliance_districts\.csv', views.malaria_compliance, {'org_unit_level': 1, 'output_format': 'CSV'}, name='malaria_compliance_districts_csv'),
    url(r'scorecards/malaria/ipt_subcounties\.php', views.malaria_ipt_scorecard, {'org_unit_level': 2}, name='ipt_subcounties'),
    url(r'scorecards/malaria/ipt_subcounties\.xls', views.malaria_ipt_scorecard, {'org_unit_level': 2, 'output_format': 'EXCEL'}, name='ipt_subcounties_excel'),
    url(r'scorecards/malaria/ipt_subcounties\.csv', views.malaria_ipt_scorecard, {'org_unit_level': 2, 'output_format': 'CSV'}, name='ipt_subcounties_csv'),
    url(r'scorecards/malaria/ipt_districts\.php', views.malaria_ipt_scorecard, {'org_unit_level': 1}, name='ipt_districts'),
    url(r'scorecards/malaria/ipt_districts\.xls', views.malaria_ipt_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='ipt_districts_excel'),
    url(r'scorecards/malaria/ipt_districts\.csv', views.malaria_ipt_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='ipt_districts_csv'),
    url(r'validation/(?P<thematic_area>\w+)/rules\.php', views.validation_rule_listing, name='validation_rule_listing'),
    url(r'validation_rule\.php', views.validation_rule, name='validation_rule'),
    url(r'data_workflow_new\.php/(?P<menu_name>.*)/$', views.data_workflow_new, name='data_workflow_new'),
    url(r'validation_rule\.xls', views.validation_rule, {'output_format': 'EXCEL'}, name='validation_rule_excel'),
    url(r'data_workflow\.php', views.data_workflow_detail, name='data_workflow_detail'),
    url(r'data_workflows\.php', views.data_workflow_listing, name='data_workflow_listing'),
    url(r'data_element_alias\.php', views.data_element_alias, name='data_element_alias'),
    url(r'dashboards/hts/$', views.hiv_dashboard, name='thematic_hiv'),
    url(r'scorecards/hts/sites\.php', views.hts_scorecard, {'org_unit_level': 3}, name='hts_sites'),
    url(r'scorecards/hts/sites\.xls', views.hts_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='hts_sites_excel'),
    url(r'scorecards/hts/sites\.csv', views.hts_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='hts_sites_csv'),
    url(r'scorecards/hts/districts\.php', views.hts_scorecard, {'org_unit_level': 1}, name='hts_districts'),
    url(r'scorecards/hts/districts\.xls', views.hts_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='hts_districts_excel'),
    url(r'scorecards/hts/districts\.csv', views.hts_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='hts_districts_csv'),
    url(r'scorecards/art_new/sites\.php', views.art_new_scorecard, {'org_unit_level': 3}, name='art_new_sites'),
    url(r'scorecards/art_new/sites\.xls', views.art_new_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='art_new_sites_excel'),
    url(r'scorecards/art_new/sites\.csv', views.art_new_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='art_new_sites_csv'),
    url(r'scorecards/art_new/districts\.php', views.art_new_scorecard, {'org_unit_level': 1}, name='art_new_districts'),
    url(r'scorecards/art_new/districts\.xls', views.art_new_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='art_new_districts_excel'),
    url(r'scorecards/art_new/districts\.csv', views.art_new_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='art_new_districts_csv'),
    url(r'scorecards/art_active/sites\.php', views.art_active_scorecard, {'org_unit_level': 3}, name='art_active_sites'),
    url(r'scorecards/art_active/sites\.xls', views.art_active_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='art_active_sites_excel'),
    url(r'scorecards/art_active/sites\.csv', views.art_active_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='art_active_sites_csv'),
    url(r'scorecards/art_active/districts\.php', views.art_active_scorecard, {'org_unit_level': 1}, name='art_active_districts'),
    url(r'scorecards/art_active/districts\.xls', views.art_active_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='art_active_districts_excel'),
    url(r'scorecards/art_active/districts\.csv', views.art_active_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='art_active_districts_csv'),
    url(r'scorecards/care_tx/sites\.php', views.care_tx_scorecard, {'org_unit_level': 3}, name='care_tx_sites'),
    url(r'scorecards/care_tx/sites\.xls', views.care_tx_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='care_tx_sites_excel'),
    url(r'scorecards/care_tx/sites\.csv', views.care_tx_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='care_tx_sites_csv'),
    url(r'scorecards/care_tx/districts\.php', views.care_tx_scorecard, {'org_unit_level': 1}, name='care_tx_districts'),
    url(r'scorecards/care_tx/districts\.xls', views.care_tx_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='care_tx_districts_excel'),
    url(r'scorecards/care_tx/districts\.csv', views.care_tx_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='care_tx_districts_csv'),
    url(r'dashboards/pmtct/$', views.index, name='thematic_pmtct'),
    url(r'scorecards/pmtct/sites\.php', views.pmtct_scorecard, {'org_unit_level': 3}, name='pmtct_sites'),
    url(r'scorecards/pmtct/sites\.xls', views.pmtct_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='pmtct_sites_excel'),
    url(r'scorecards/pmtct/sites\.csv', views.pmtct_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='pmtct_sites_csv'),
    url(r'scorecards/pmtct/districts\.php', views.pmtct_scorecard, {'org_unit_level': 1}, name='pmtct_districts'),
    url(r'scorecards/pmtct/districts\.xls', views.pmtct_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='pmtct_districts_excel'),
    url(r'scorecards/pmtct/districts\.csv', views.pmtct_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='pmtct_districts_csv'),
    url(r'dashboards/vmmc/$', views.vmmc_dashboard, name='thematic_vmmc'),
    url(r'scorecards/vmmc/sites\.php', views.vmmc_scorecard, {'org_unit_level': 3}, name='vmmc_sites'),
    url(r'scorecards/vmmc/sites\.xls', views.vmmc_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='vmmc_sites_excel'),
    url(r'scorecards/vmmc/sites\.csv', views.vmmc_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='vmmc_sites_csv'),
    url(r'scorecards/vmmc/districts\.php', views.vmmc_scorecard, {'org_unit_level': 1}, name='vmmc_districts'),
    url(r'scorecards/vmmc/districts\.xls', views.vmmc_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='vmmc_districts_excel'),
    url(r'scorecards/vmmc/districts\.csv', views.vmmc_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='vmmc_districts_csv'),
    url(r'dashboards/lab/$', views.lab_dashboard, name='thematic_lab'),
    url(r'scorecards/lab/sites\.php', views.lab_scorecard, {'org_unit_level': 3}, name='lab_sites'),
    url(r'scorecards/lab/sites\.xls', views.lab_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='lab_sites_excel'),
    url(r'scorecards/lab/sites\.csv', views.lab_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='lab_sites_csv'),
    url(r'scorecards/lab/districts\.php', views.lab_scorecard, {'org_unit_level': 1}, name='lab_districts'),
    url(r'scorecards/lab/districts\.xls', views.lab_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='lab_districts_excel'),
    url(r'scorecards/lab/districts\.csv', views.lab_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='lab_districts_csv'),
    url(r'scorecards/vl/sites\.php', views.vl_scorecard, {'org_unit_level': 3}, name='vl_sites'),
    url(r'scorecards/vl/sites\.xls', views.vl_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='vl_sites_excel'),
    url(r'scorecards/vl/sites\.csv', views.vl_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='vl_sites_csv'),
    url(r'scorecards/vl/districts\.php', views.vl_scorecard, {'org_unit_level': 1}, name='vl_districts'),
    url(r'scorecards/vl/districts\.xls', views.vl_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='vl_districts_excel'),
    url(r'scorecards/vl/districts\.csv', views.vl_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='vl_districts_csv'),
    url(r'dashboards/fp/$', views.index, name='thematic_fp'),
    url(r'scorecards/fp/sites\.php', views.fp_scorecard, {'org_unit_level': 3}, name='fp_sites'),
    url(r'scorecards/fp/sites\.xls', views.fp_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='fp_sites_excel'),
    url(r'scorecards/fp/sites\.csv', views.fp_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='fp_sites_csv'),
    url(r'scorecards/fp/districts\.php', views.fp_scorecard, {'org_unit_level': 1}, name='fp_districts'),
    url(r'scorecards/fp/districts\.xls', views.fp_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='fp_districts_excel'),
    url(r'scorecards/fp/districts\.csv', views.fp_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='fp_districts_csv'),
    url(r'scorecards/fp/cyp_sites\.php', views.fp_cyp_scorecard, {'org_unit_level': 3}, name='fp_cyp_sites'),
    url(r'scorecards/fp/cyp_sites\.xls', views.fp_cyp_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='fp_cyp_sites_excel'),
    url(r'scorecards/fp/cyp_sites\.csv', views.fp_cyp_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='fp_cyp_sites_csv'),
    url(r'scorecards/fp/cyp_districts\.php', views.fp_cyp_scorecard, {'org_unit_level': 1}, name='fp_cyp_districts'),
    url(r'scorecards/fp/cyp_districts\.xls', views.fp_cyp_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='fp_cyp_districts_excel'),
    url(r'scorecards/fp/cyp_districts\.csv', views.fp_cyp_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='fp_cyp_districts_csv'),
    url(r'dashboards/tb/$', views.index, name='thematic_tb'),
    url(r'scorecards/tb/sites\.php', views.tb_scorecard, {'org_unit_level': 3}, name='tb_sites'),
    url(r'scorecards/tb/sites\.xls', views.tb_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='tb_sites_excel'),
    url(r'scorecards/tb/sites\.csv', views.tb_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='tb_sites_csv'),
    url(r'scorecards/tb/districts\.php', views.tb_scorecard, {'org_unit_level': 1}, name='tb_districts'),
    url(r'scorecards/tb/districts\.xls', views.tb_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='tb_districts_excel'),
    url(r'scorecards/tb/districts\.csv', views.tb_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='tb_districts_csv'),
    url(r'dashboards/nutrition/$', views.nutrition_dashboard, name='thematic_nutrition'),
    url(r'scorecards/nutrition/sites\.php', views.nutrition_scorecard, {'org_unit_level': 3}, name='nutrition_sites'),
    url(r'scorecards/nutrition/sites\.xls', views.nutrition_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='nutrition_sites_excel'),
    url(r'scorecards/nutrition/sites\.csv', views.nutrition_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='nutrition_sites_csv'),
    url(r'scorecards/nutrition/districts\.php', views.nutrition_scorecard, {'org_unit_level': 1}, name='nutrition_districts'),
    url(r'scorecards/nutrition/districts\.xls', views.nutrition_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='nutrition_districts_excel'),
    url(r'scorecards/nutrition/districts\.csv', views.nutrition_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='nutrition_districts_csv'),
    url(r'dashboards/gbv/$', views.index, name='thematic_gbv'),
    url(r'scorecards/gbv/sites\.php', views.gbv_scorecard, {'org_unit_level': 3}, name='gbv_sites'),
    url(r'scorecards/gbv/sites\.xls', views.gbv_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='gbv_sites_excel'),
    url(r'scorecards/gbv/sites\.csv', views.gbv_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='gbv_sites_csv'),
    url(r'scorecards/gbv/districts\.php', views.gbv_scorecard, {'org_unit_level': 1}, name='gbv_districts'),
    url(r'scorecards/gbv/districts\.xls', views.gbv_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='gbv_districts_excel'),
    url(r'scorecards/gbv/districts\.csv', views.gbv_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='gbv_districts_csv'),
    # url(r'scorecards/gbv/pep_sites\.php', views.gbv_pep_by_site, name='gbv_pep_sites'),
    # url(r'scorecards/gbv/pep_districts\.php', views.gbv_pep_by_district, name='gbv_pep_districts'),
    url(r'dashboards/sc/$', views.index, name='thematic_sc'),
    url(r'scorecards/sc/mos_sites\.php', views.sc_mos_by_site, name='sc_mos_sites'),
    url(r'scorecards/sc/mos_sites\.xls', views.sc_mos_by_site, {'output_format': 'EXCEL'}, name='sc_mos_sites_excel'),
    url(r'scorecards/sc/mos_sites\.csv', views.sc_mos_by_site, {'output_format': 'CSV'}, name='sc_mos_sites_csv'),
    url(r'dashboards/mnch/$', views.mnch_dashboard, name='thematic_mnch'),
    url(r'scorecards/mnch/preg_birth_subcounties\.php', views.mnch_preg_birth_scorecard, {'org_unit_level': 2}, name='mnch_preg_birth_subcounties'),
    url(r'scorecards/mnch/preg_birth_subcounties\.xls', views.mnch_preg_birth_scorecard, {'org_unit_level': 2, 'output_format': 'EXCEL'}, name='mnch_preg_birth_subcounties_excel'),
    url(r'scorecards/mnch/preg_birth_subcounties\.csv', views.mnch_preg_birth_scorecard, {'org_unit_level': 2, 'output_format': 'CSV'}, name='mnch_preg_birth_subcounties_csv'),
    url(r'scorecards/mnch/preg_birth_districts\.php', views.mnch_preg_birth_scorecard, {'org_unit_level': 1}, name='mnch_preg_birth_districts'),
    url(r'scorecards/mnch/preg_birth_districts\.xls', views.mnch_preg_birth_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='mnch_preg_birth_districts_excel'),
    url(r'scorecards/mnch/preg_birth_districts\.csv', views.mnch_preg_birth_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='mnch_preg_birth_districts_csv'),
    url(r'scorecards/mnch/pnc_child_subcounties\.php', views.mnch_pnc_child_scorecard, {'org_unit_level': 2}, name='mnch_pnc_child_subcounties'),
    url(r'scorecards/mnch/pnc_child_subcounties\.xls', views.mnch_pnc_child_scorecard, {'org_unit_level': 2, 'output_format': 'EXCEL'}, name='mnch_pnc_child_subcounties_excel'),
    url(r'scorecards/mnch/pnc_child_subcounties\.csv', views.mnch_pnc_child_scorecard, {'org_unit_level': 2, 'output_format': 'CSV'}, name='mnch_pnc_child_subcounties_csv'),
    url(r'scorecards/mnch/pnc_child_districts\.php', views.mnch_pnc_child_scorecard, {'org_unit_level': 1}, name='mnch_pnc_child_districts'),
    url(r'scorecards/mnch/pnc_child_districts\.xls', views.mnch_pnc_child_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='mnch_pnc_child_districts_excel'),
    url(r'scorecards/mnch/pnc_child_districts\.csv', views.mnch_pnc_child_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='mnch_pnc_child_districts_csv'),
    url(r'dashboards/lqas/$', views.index, name='thematic_lqas'),
    url(r'scorecards/lqas/sites\.php', views.lqas_scorecard, {'org_unit_level': 3}, name='lqas_sites'),
    url(r'scorecards/lqas/sites\.xls', views.lqas_scorecard, {'org_unit_level': 3, 'output_format': 'EXCEL'}, name='lqas_sites_excel'),
    url(r'scorecards/lqas/sites\.csv', views.lqas_scorecard, {'org_unit_level': 3, 'output_format': 'CSV'}, name='lqas_sites_csv'),
    url(r'scorecards/lqas/districts\.php', views.lqas_scorecard, {'org_unit_level': 1}, name='lqas_districts'),
    url(r'scorecards/lqas/districts\.xls', views.lqas_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='lqas_districts_excel'),
    url(r'scorecards/lqas/districts\.csv', views.lqas_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='lqas_districts_csv'),

    url(r'scorecards/lqas/districts_child\.php', views.lqas_scorecard_child, {'org_unit_level': 1}, name='lqas_districts_child'),
    url(r'scorecards/lqas/districts_child\.xls', views.lqas_scorecard_child, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='lqas_districts_child_excel'),
    url(r'scorecards/lqas/districts_child\.csv', views.lqas_scorecard_child, {'org_unit_level': 1, 'output_format': 'CSV'}, name='lqas_districts_child_csv'),
   
   
   

    url(r'dashboards/kp/$', views.index, name='thematic_kp'),
    url(r'scorecards/kp/subcounties\.php', views.kp_scorecard, {'org_unit_level': 2}, name='kp_subcounties'),
    url(r'scorecards/kp/subcounties\.xls', views.kp_scorecard, {'org_unit_level': 2, 'output_format': 'EXCEL'}, name='kp_subcounties_excel'),
    url(r'scorecards/kp/subcounties\.csv', views.kp_scorecard, {'org_unit_level': 2, 'output_format': 'CSV'}, name='kp_subcounties_csv'),
    url(r'scorecards/kp/districts\.php', views.kp_scorecard, {'org_unit_level': 1}, name='kp_districts'),
    url(r'scorecards/kp/districts\.xls', views.kp_scorecard, {'org_unit_level': 1, 'output_format': 'EXCEL'}, name='kp_districts_excel'),
    url(r'scorecards/kp/districts\.csv', views.kp_scorecard, {'org_unit_level': 1, 'output_format': 'CSV'}, name='kp_districts_csv'),

    #reports
    url(r'dashboards/reports/$', views.indexreport, name='performance_reports'),
    url(r'scorecards/reports/reports_sites_2016_to_2017\.php', views.reports_sites_2016_to_2017, name='reports_sites_2016_to_2017'),
    url(r'scorecards/reports/reports_sites_2017_to_2018\.php', views.reports_sites_2017_to_2018, name='reports_sites_2017_to_2018'),

    #suplementary tools
    #TB PREV
    url(r'dashboards/prev/$', views.index, name='thematic_prev'),
    url(r'scorecards/prev/tb_prev\.php', views.tb_prev, name='prev'),
    url(r'scorecards/prev/tb_prev_summary\.php', views.tb_prev_summary, name='prev_summary'),
    
    #MNCH and Malaria
    url(r'scorecards/mnch/mnchandmalarial_additional_summary\.php', views.mnchandmalarial_additional_summary,name='mnchandmalarial_additional_summary'),
    url(r'scorecards/mnch/mnchandmalarial_additional_scorecard\.php', views.mnchandmalarial_additional_scorecard,name='mnchandmalarial_additional_scorecard'),
    url(r'scorecards/mnch/mnchandmalarial_additional_scorecard_facility\.php', views.mnchandmalarial_additional_scorecard_facility,name='read_data_mms_scorecard_data_facility'),
    url(r'scorecards/mnch/mnchandmalarial_additional_scorecard_doos_facility\.php', views.mnchandmalarial_additional_scorecard_doos_facility,name='mnchandmalarial_additional_scorecard_doos_facility'),


    #pmtct
    url(r'scorecards/pmtct/pmtct_districts_new\.php', views.pmtct_scorecard_new,name='pmtct_districts_new'),
    url(r'scorecards/pmtct/pmtct_scorecard_new_facility\.php', views.pmtct_scorecard_new_facility,name='pmtct_scorecard_new_facility'),



    url(r'dashboards/vl_lab/$', views.index, name='thematic_vl_lab'),
    url(r'scorecards/sp_vl_lab/vl_lab\.php', views.vl_lab, name='vl_lab'),
    #url(r'scorecards/prev/tb_prev_summary\.php', views.tb_prev_summary, name='prev_summary'),
]
