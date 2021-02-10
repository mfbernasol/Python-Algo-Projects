from functions import binary_search, analyze_func, generate_emails


# add domain to list below for additional email extensions
list_of_domains = ['test.com','example.com','sample.com']

#generate emails
emails = generate_emails(10,list_of_domains,1000000)

# Test email to add to list of emails, followed by append to list 
email = 'usertest@example.com'
emails.append(email)
#sort list of generated emails
sorted_emails = sorted(emails)

#Run binary search to find test email in list
print(binary_search(email, sorted_emails))

# Run analysis
analyze_func(binary_search,email,sorted_emails)
analyze_func(generate_emails, 10, list_of_domains, 1000000)