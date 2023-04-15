USER LOGIN

    tyler.gilroy.21@gmail.com
    admin0123

Options:

    View own info

    Edit own info (last name, first name, phone, email, password)
        - Names automatically title-case upon push to db
        - Phone input checked for XXX-XXX-XXXX formatting
        - Email format automatically verified via . following an @ before push to db
        - Password must be 8 or more characters long, checked and hashed before push to db
        - Display info updated and pushed to db after each update entry

    View own User Competency Summary
        - Average proficiency score for every competency calculated using most recent result from each assessment ID



MANAGER LOGIN

    tyler.gilroy.23@gmail.com
    admin0123

Options:

    Choice of user menu (same as above) or manager menu (as follows)

    Reports
        - Competency Levels Summary (average proficiency score for every user for chosen competency calculated using most recent result from each assessment ID)
        - User Competency Summary (chosen user's average proficiency score for every competency calculated using most recent result from each assessment ID)
        - User Assessment Summary (tally of chosen user's completed assessments)
        - Competency Result Summary (every user's most recent assessment, score, and date taken for chosen competency, then shows company average from displayed scores)

    View
        - Can view all results any each table, ordered by ID ASC (passwords not queried)
        - Can search users by either last or first name, able to search by partial entry

    Add
        - Add one record at a time to any table, inputs checked appropriately

    Update
        - Update any relevant field from a chosen record from any table, inputs checked appropriately

    Deactivate/Delete
        - Delete rather than deactivate any result from Assessment_Results table to reduce db size
        - Deactivate any record from any of the other three tables to avoid critical data loss (barring own user ID)

    Import/Export
        - Export all of any table to 'outfile.csv', over-writes with each export (will include header for ease-of-use)
        - Import user_id, assessment_id, score and date_taken fields from 'infile.csv' into Assessment_Results table line by line checking for good input in each field with each execute
            (Can partially execute and will return failure line, when replacing 'infile.csv' ensure field order is identical and header is included)