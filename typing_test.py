import speed_tests
from tkinter import *
import threading
import time
from tkinter import messagebox
import datetime


class typing_test:
    def __init__(self):
        self.tests = {
            'Easy': speed_tests.tests.test1(),  # Dictionary for choosing the desired difficulty of text to be typed
            'Medium': speed_tests.tests.test2(),
            'Hard': speed_tests.tests.test3()
            }

        self.tests_list = {
            'Easy': self.tests['Easy'].split(),  # Splitting the 3 tests into lists where each val is a
            'Medium': self.tests['Medium'].split(),  # whole word.
            'Hard': self.tests['Hard'].split()
            }

        #  Creating main window
        self.root = Tk()  # Creation of window here and altering of some of its properties below
        self.root.iconbitmap('printer.ico')
        self.root.geometry('900x900')
        self.root.title('Typing speed test')
        self.root['background'] = '#58F'

        #  Title Label
        lbl_title = Label(self.root, text='Typing Speed Test')  # Create and place (line 33) a title Label on screen
        lbl_title.config(font=('Verdana, 50'))  # Changing this title Label's font
        lbl_title.place(x=173, y=30)

        #  Choose difficulty OptionMenu
        self.test_chosen = StringVar()
        self.test_chosen.set('Choose difficulty')  # The below drop-down list is pre-set to this, to help the user use program
        choose_test = OptionMenu(self.root, self.test_chosen, *self.tests.keys())  # Creation of drop-down (OptionMenu) object
        choose_test.place(x=91, y=139)  # Placing drop-down for choosing difficulty on screen

        #  Run test Button
        self.btn_run_test = Button(self.root, text='Start test', command=self.run_test, borderwidth=5, width=10)  # Button that will
        self.btn_run_test.place(x=410, y=140)  # be used to run its command and is placed on screen

        #  Enter answer Text box
        self.text_enter_typing = Text(self.root)  # Where the user will type their answer
        self.text_enter_typing.config(state=DISABLED)  # Don't allow text entry
        self.text_enter_typing.place(x=50, y=510, width=800, height=320)  # below and made larger so there's enough space

        #  Time left Label
        self.length_of_time = 60  #  How long timer runs for (60)
        self.length_of_time_text = IntVar()  # Creating variable for our Label to use
        self.length_of_time_text.set(self.length_of_time)  # Setting it to line 52
        self.lab_show_time_left = Label(self.root, text=self.length_of_time_text.get())  # Object to display length of time left
        self.lab_show_time_left.config(font=('System', 18))  # Altering font
        self.lab_show_time_left.place(x=802, y=139)  # Placing above on screen

        #  All results Label
        self.results_text_update = 'Your results:'  # Text for displaying all user's results
        self.results_text = StringVar()  # Creating variable for our Label
        self.results_text.set(self.results_text_update)  # Setting above Label to the Text self.results_text_update
        self.lab_results = Label(self.root, text=self.results_text.get())  # Creating Label to show results_text
        self.lab_results.place(x=50, y=220)  # Placing the Label to show all results

        self.root.mainloop()  # So the user can see/ always see these objects


    def run_test(self):
        self.typed_correct = 0
        self.index_pos = 0
        self.test_named = self.test_chosen.get()
        self.delete_first_y = False

        if self.test_named != 'Choose difficulty':  # If a difficulty has been chosen and
            if self.delete_first_y:  # if run_test has run before
                self.lab_text_to_be_typed.place_forget()  # then delete the text to be typed
                self.text_enter_typing.delete('1.0', END)  # and delete answer entry box's contents
                self.score.destroy()  # and destroy the 2nd window in game over
            self.delete_first_y = True  # So that next run_test will delete prev test to be typed

            self.text_enter_typing.config(state=NORMAL)  # Let Text box be typed
            self.text_to_be_typed = StringVar()  # Create var for Message below
            self.text_to_be_typed.set(self.tests[self.test_named])  # Set var to the test diff chosen
            self.lab_text_to_be_typed = Message(self.root, text=self.text_to_be_typed.get(), bg='white')  # Create test display object
            self.lab_text_to_be_typed.place(x=262, y=180)  # and put it on screen

            self.new_thread = threading.Thread(target=self.timer)  # Here is creating a new
            self.new_thread.setDaemon(True)  # thread that calls the timer as otherwise
            self.new_thread.start()  # we can't run this in background and use our program

        else:  # This message will pop-up if the user hasn't chosen difficulty yet
            msg_not_chosen = messagebox.showwarning('Error', 'Please choose difficulty first')


    def timer(self):
        o_sec = datetime.datetime.now().second  # Collecting original time, once only and just the seconds

        while self.length_of_time > 0:  # Loops whilst length of time left is greater than 0
            time.sleep(1)  # Sleep program for one second
            self.length_of_time -= 1  # Decrement and reassign this by 1, so there is less seconds left
            self.length_of_time_text.set(self.length_of_time)  # Re-set time left text to the new value
            self.lab_show_time_left.config(text=self.length_of_time_text.get())  # Using << update time left on screen

        self.game_over()  # Run game over when there is no time left in the typing test


    def game_over(self):
        answer_entered = self.text_enter_typing.get('1.0', END)  # Collect the user's answer entered
        answer_entered_list = answer_entered.split()  # Split the user's answer into a list of each word entered
        test_chosen_list = self.tests_list[self.test_chosen.get()]  # Locate the chosen text to be typed

        words_in_test = 0
        for items in test_chosen_list:  # These lines will count how many words are in the text chosen
            words_in_test += 1

        #  Calculating how many words were typed correctly
        for word in answer_entered_list:  # For each word in typing test answer list
            if answer_entered_list[self.index_pos] == test_chosen_list[self.index_pos]:  # If answers match
                self.typed_correct += 1  # Increment how many typed correct by 1
            self.index_pos += 1  # Runs even if words don't match so we can check if next words match

        #  Window to present score
        self.score = Toplevel()  # Create window
        self.score.title('Your Score')  # Give it a title
        self.score.geometry('500x250')  # Change window size
        self.score.iconbitmap('printer.ico')  # Change window icon
        self.score['background'] = '#58F'  # Change window background fill

        #  Reassigning all test results variable...
        self.results_text_updated = 0
        if self.results_text_updated <= 13:  # Do this 13 times
            # [line 133] Add onto itself how many typed correctly and the name of the test chosen
            self.results_text_update = self.results_text_update +\
            '\n' + str(self.typed_correct) + ' WPM on ' + self.test_chosen.get()  # to itself
            self.results_text.set(self.results_text_update)  # Re-set all results text variable
            self.lab_results.config(text=self.results_text.get())  # Update this Label objects
            self.lab_results.place(x=50, y=220)  # Update the newly changed object on screen

            self.results_text_updated += 1  # Add 1 onto this var so the all results Label text doesn't get too long

        #  Score results Label
        typed_correct_text = 'You typed ' + str(self.typed_correct) + ' correctly'  # Var with how many typed correct
        lbl_typed_correct = Label(self.score, text=typed_correct_text, fg='green')  # Make Label to display above
        lbl_typed_correct.config(font=('MS Serif', 18))  # Amend above Label font
        lbl_typed_correct.place(x=150, y=100)  # Place above Label on screen
        #  Quit window button
        button_exit = Button(self.score, text='Exit', command=self.score.destroy, borderwidth=5, width=10 )  # Exit button
        button_exit.place(x=230, y=200)  # Place exit button on screen


typing_test()  # Call class
