SELECT Company.company_code, Company.founder, 
    COUNT(DISTINCT Lead_Manager.lead_manager_code), COUNT(DISTINCT Senior_Manager.senior_manager_code), 
    COUNT(DISTINCT Manager.manager_code), COUNT(DISTINCT Employee.employee_code) 
FROM Company, Lead_Manager, Senior_Manager, Manager, Employee 
WHERE Company.company_code = Lead_Manager.company_code 
    AND Lead_Manager.lead_manager_code = Senior_Manager.lead_manager_code 
    AND Senior_Manager.senior_manager_code = Manager.senior_manager_code 
    AND Manager.manager_code = Employee.manager_code 
GROUP BY Company.company_code, Company.founder
ORDER BY Company.company_code;