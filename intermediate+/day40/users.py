import pandas as pd

class UserManagement:
    #This class is responsible for talking to the local file and managing users.
    
    def __init__(self):
        self.df = pd.read_csv("./users.csv")

    def signup_user(self):
        """
        User Signup
        Check's if they exist. If not, add to database.
        """
        first = input("What is your name?: ")
        last = input("What is your surname?: ")
        email = input("What is your email address?: ")

        mask = self.df['Email'] == email

        if not mask.any():
            new_index = len(self.df)
            self.df.loc[new_index] = {
                'First': first,
                'Last': last,
                'Email': email
            }
            self.df.to_csv("./users.csv", index=False)
            return "User added successfully"
        else:
            return "User already exists"

    def return_emails(self):
        emails = self.df['Email'].tolist()
        return emails
