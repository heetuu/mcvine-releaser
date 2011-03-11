chmod -R a+rX EXPORT/docs/mcvine/sphinx/
rsync -r EXPORT/docs/mcvine/sphinx/ linjiao@login.cacr.caltech.edu:docs.danse.us-docroot/MCViNE/sphinx/
scp EXPORT/docs/mcvine/sphinx/examples.tgz linjiao@login.cacr.caltech.edu:projects/danse/packages/dev_danse_us/mcvine-examples.tgz
