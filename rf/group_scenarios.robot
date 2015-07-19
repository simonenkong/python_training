*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add new group
    ${old_list}=  Get Group List
    ${group}=  New Group  name1  header1  footer1
    Create Group  ${group}
    ${new_list}=  Get Group List
    Append To List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${old_list}  ${new_list}

Delete group
    ${old_list}=  Get Group List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${group}=  Get From List  ${old_list}  ${index}
    Delete Group  ${group}
    ${new_list}=  Get Group List
    Remove Values From List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${old_list}  ${new_list}

Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  firstname1  lastname1
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${old_list}  ${new_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${old_list}  ${new_list}

Change contact name
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Change Contact Name  ${contact}  new_name101
    ${new_list}=  Get Contact List
    Contact Lists Should Be Equal  ${old_list}  ${new_list}
