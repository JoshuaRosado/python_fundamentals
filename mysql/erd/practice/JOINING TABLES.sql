--         >>>>>>JOINING TABLES<<<<<<<<
--         JOIN
--         Find all the clients(first and last name)billing amounts and charged dates
SELECT clients.first_name, clients.last_name, billing.amount, billing.charged_datetime 
FROM clients
JOIN billing ON clients.id = billing.clients_id; -- client.id (clients table id) = billing.clients_id(billing table foreign key)

--         List all the domain names and leads (first and last names) for each site
SELECT sites.domain_name, leads.first_name, leads.last_name 
FROM sites
JOIN leads ON sites.id = leads.sites_id;
--         >>>>>>JOIN ON MULTIPLES TABLES<<<<<<
--   	   Get the names of the clients, their domain names and first names of all leads generated from those sites
SELECT clients.first_name AS client_first, clients.last_name, sites.domain_name, leads.first_name AS leads_first
FROM clients
JOIN sites ON clients.id = sites.clients_id
JOIN leads ON sites.id = leads.sites_id;
-- 		   >>>>>>>>LEFT AND RIGHT JOIN<<<<<<<<<<
-- 			List all the clients and the sites each client has, even if the client hasn't landed a site yet
SELECT clients.first_name, clients.last_name, sites.domain_name
FROM clients
LEFT JOIN sites ON clients.id = sites.clients_id;

--        >>>>>>>> GROUPING ROWS<<<<<<<<<<
-- 		   GROUPING BY
-- 			SUM, MIN , MAX, AVG
-- 			Find all the clients(first and last name) and their total billing amounts
SELECT clients.first_name, clients.last_name, SUM(billing.amount)
FROM clients
JOIN billing ON clients.id = billing.clients_id
GROUP BY clients.id;

--   		>>>>>>>>GROUP CONCAT<<<<<<<<<<
--          List all the domain names associated with each client
SELECT GROUP_CONCAT('  ',sites.domain_name) AS domains, clients.first_name, clients.last_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
GROUP BY clients.id;

--  		 >>>>>>>COUNT<<<<<<<<<
--  	     Find the total number of leads for each site.
SELECT COUNT(leads.id), sites.domain_name
FROM sites
JOIN leads ON sites.id = leads.sites_id
GROUP BY sites.id;




