#!/usr/bin/python3 


def main():
	'''
	@breif: Our main function here will take in user input and perfrom string concationation.
	@return: We will return the finialized string.  
	'''
	Name = input("What is your name? ")
	return_string = "Hello, " + Name + ", Nice to meet you!"
	print(return_string)
	return return_string
if __name__ == "__main__":
	main()
