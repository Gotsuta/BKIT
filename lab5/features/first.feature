Feature: show behave
    Scenario: Test
        Given a list of people
        When I get the names
        Then I should get a list of names

        Given a list of str data
        When I call Unique with key ignore_case=True
        Then I get list of unique str data without big letters

        Given a list of str data2
        When I call Unique with key ignore_case=False
        Then I get list of unique str data without all letters

        

    
