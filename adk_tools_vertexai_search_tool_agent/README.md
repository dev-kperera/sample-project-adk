# Pre setup
In your browser tab still showing the Cloud Console, navigate to "Cloud Storage" by searching for it at the top of the console.

Then create bucket and upload the PDF Persephone Analysis Report.pdf into it. 

.. and then

In your browser tab still showing the Cloud Console, navigate to AI Applications by searching for it at the top of the console.

Select the terms and conditions checkbox and click Continue and Activate the API.

From the left-hand navigation menu, select Data Stores.

Select Create Data Store.

Find the Cloud Storage card and click Select on it.

Select Unstructured documents (PDF, HTML, TXT and more)

For a GCS path, enter the bucket you created in the previous step.
Click Continue.

Keep the location set to global.

For a data store name, enter Planet Search.

Click Create.

# How to test

Run `adk web`

Select the agent.

Toggle on the Token Streaming option in the upper right.

Ask `is the new planet Persephone suitable for habitation?`