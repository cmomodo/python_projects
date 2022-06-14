from gettext import install


# A dictionary that is storing the key and value for general response.
general_response = {"Good morning":"Good to speak to you, are you having a good morning","Yes":"How can i help?",
                "covid":"You need to have a test or be fully vaccinated",
                "Thank you!":"Any other questions let me know"}
# instruction1 = input("Enter your word: ")
# for k,v in chat_server.items():
#     if instruction1 == k:
#         print(v)

# Storing the key and value for the covid rules.
covid_rules = {"spain": {"vaccinated": "No restrictions, You can travel safely",
               "Not vaccinated":"You can't travel , you need to take the vaccine or else you can't travel"},
               "italy":{"vaccinated": "You can go the rules are the same",
                        "not vaccinated": "You need to show the proof of vaccination"},
               "gambia":{"vaccinated":"You dont to show proof of vaccination",
                         "not vaccinated":"You can't enter"},
               "portugal":{"vaccinated":"You can go",
                         "not vaccinated":"You can go but need to self-isolate for 7 days"},
               "brazil":{"vaccinated": "You need to still self-isolate",
                         "not vaccinated":"You need to do a pcr test before coming"},
               "america":{"vaccinated": "You can travel but must do a pcr test and self isolate",
                         "not vaccinated":"You need to do a pcr test before coming and self isolate for 14 days"}
               
               }