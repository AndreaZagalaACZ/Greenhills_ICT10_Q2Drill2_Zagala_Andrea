# Candidate Verification System / Student Club Member Checker
from pyscript import display , document


def student_club(e):
    # Calls out the variables
    document.getElementById('output').innerHTML = ' '
    student_first = document.getElementById('first_name').value
    student_last = document.getElementById('last_name').value

    first_accepted = ['Mari', 'Suhan', 'Kuma', 'Yang', 'Cassiel', 'Yll']
    last_accepted = ['Kamimori', 'Holic', 'Teruhashi', 'De Fontaine', 'Doctor', 'Mao']

    member_checker1 = student_first in first_accepted
    member_checker2 = student_last in last_accepted
    member_checker3 = member_checker1 + member_checker2 + member_checker1

    # Displayed Message (Output)
    display_message = (f'Sorry, you are not part of the list.', f'Congratulations, you are qualified for the philosophy and psychology club!')

    display(display_message[member_checker3], target='output')
