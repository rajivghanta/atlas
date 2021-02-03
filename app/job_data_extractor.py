from bs4 import BeautifulSoup

def job_data_extractor(job_url, job_dom_data):
	extracted_data = {}

	### LINKEDIN JOB SEARCH VIEW
	if 'https://www.linkedin.com/jobs/search/' in job_url:
		soup = BeautifulSoup(job_dom_data, 'html.parser')
		job_title = soup.find('h2', {'class': 'jobs-details-top-card__job-title'})
		if job_title != None:
			job_title = job_title.text.strip()
		company_name = soup.find('a', {'class': 'jobs-details-top-card__company-url'})
		if company_name != None:
			company_name = company_name.text.strip()
		job_location = soup.find('span', {'class': 'jobs-details-top-card__bullet'})
		if job_location != None:
			job_location = job_location.text.strip()
		job_url = soup.find('a', {'class': 'jobs-details-top-card__job-title-link'})
		if job_url != None:
			job_url = job_url['href']
			job_url = 'https://www.linkedin.com' + job_url
			job_url = job_url.split('?')[0]

		extracted_data = {'job_title': job_title,
							  'company_name': company_name,
							  'job_location': job_location,
							  'job_url': job_url}
		print(job_title)
		print(company_name)
		print(job_location)
		print(job_url)
		return extracted_data

	### LINKEDIN DETAIL JOB VIEW
	if 'https://www.linkedin.com/jobs/view/' in job_url:
		soup = BeautifulSoup(job_dom_data, 'html.parser')
		job_title = soup.find('div', {'class': 'jobs-unified-top-card'}).find('h1')
		if job_title != None:
			job_title = job_title.text.strip()
		company_name = soup.find('span', {'class': 'jobs-unified-top-card__subtitle-primary-grouping'}).span
		if company_name != None:
			company_name = company_name.text.strip()
		job_location = soup.find('span', {'class': 'jobs-unified-top-card__bullet'})
		if job_location != None:
			job_location = job_location.text.strip()
		job_url = job_url.split('?')[0]

		extracted_data = {'job_title': job_title,
							  'company_name': company_name,
							  'job_location': job_location,
							  'job_url': job_url}
		print(job_title)
		print(company_name)
		print(job_location)
		print(job_url)
		return extracted_data

	### GLASSDOOR JOB SEARCH VIEW
	if 'https://www.glassdoor.com/Job/jobs.htm' in job_url:
		soup = BeautifulSoup(job_dom_data, 'html.parser')
		job_title = soup.find('div', {'id': 'HeroHeaderModuleTop'}).next_sibling.next_sibling.div.div.next_sibling
		if job_title != None:
			job_title = job_title.find(text=True).strip()
		company_name = soup.find('div', {'id': 'HeroHeaderModuleTop'}).next_sibling.next_sibling.div.div
		if company_name != None:
			company_name = company_name.find(text=True).strip()
		job_location = soup.find('div', {'id': 'HeroHeaderModuleTop'}).next_sibling.next_sibling.div.div.next_sibling.next_sibling
		if job_location != None:
			job_location = job_location.find(text=True).strip()
		job_url = soup.find('div', {'id': 'HeroHeaderModuleTop'}).next_sibling.next_sibling.div.next_sibling.find('a')
		if job_url == None:
			job_url = soup.find('div', {'id': 'HeroHeaderModuleTop'}).next_sibling.next_sibling.div.next_sibling.find('span')
			job_url = job_url['data-indeed-apply-joburl']
		else:
			job_url = job_url['href']
			job_url = 'https://www.glassdoor.com' + job_url

		extracted_data = {'job_title': job_title,
					  'company_name': company_name,
					  'job_location': job_location,
					  'job_url': job_url}
		print(job_title)
		print(company_name)
		print(job_location)
		print(job_url)
		return extracted_data

	### INDEED JOB SEARCH VIEW
	if 'https://www.indeed.com/jobs' in job_url:
		soup = BeautifulSoup(job_dom_data, 'html.parser')
		job_title = soup.find('div', {'class': 'vjs-highlight'}).find('h2').a
		if job_title != None:
			job_title = job_title.text.strip()
		company_name = soup.find('div', {'class': 'vjs-highlight'}).find('span', {'class': 'company'})
		if company_name != None:
			company_name = company_name.text.strip()
		job_location = soup.find('div', {'class': 'vjs-highlight'}).find('div', {'class': 'location'})
		if job_location != None:
			job_location = job_location.text.strip()
		job_url = soup.find('div', {'class': 'vjs-highlight'}).find('a')
		if job_url != None:
			job_url = job_url['href']
		extracted_data = {'job_title': job_title,
					  'company_name': company_name,
					  'job_location': job_location,
					  'job_url': job_url}
		print(job_title)
		print(company_name)
		print(job_location)
		print(job_url)
		return extracted_data

	### INDEED DETAIL JOB VIEW
	if 'https://www.indeed.com/viewjob' in job_url:
		soup = BeautifulSoup(job_dom_data, 'html.parser')
		job_title = soup.find('h1', {'class': 'jobsearch-JobInfoHeader-title'})
		if job_title != None:
			job_title = job_title.text.strip()
		company_name = soup.find('div', {'class': 'jobsearch-InlineCompanyRating'}).div
		if company_name != None:
			company_name = company_name.text.strip()
		job_location = soup.find('div', {'class': 'jobsearch-InlineCompanyRating'}).next_sibling
		if job_location != None:
			job_location = job_location.text.strip()
		job_url = job_url.split('&')[0]

		extracted_data = {'job_title': job_title,
							  'company_name': company_name,
							  'job_location': job_location,
							  'job_url': job_url}
		print(job_title)
		print(company_name)
		print(job_location)
		print(job_url)
		return extracted_data

	return extracted_data
