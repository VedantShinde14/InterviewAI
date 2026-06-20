from managers.interview_manager import conduct_interview

name = input("Enter your name: ")

domain = input("Which interview do you want? ")

print(f"\nStarting {domain} Interview...\n")

conduct_interview(domain)