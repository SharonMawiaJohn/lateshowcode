**Instructions**
**This code challenge is a chance for you to show off how much you've learned specifically about; models, relationships, and validations, routes and REST, and response structure. 
Setup
Create a new PRIVATE repository. Add your TM as a collaborator. Push your solution to this repo and submit for grading.
You have been provided a Postman collection Download Postman collection. This collection contains all the endpoints that you are required to create with this API. You can download and import it into your Postman application to test that your app works correctly. 
How to import postman collection.

Select `Upload Files`, navigate to this repo folder, and select `challenge-4-lateshow.postman_collection.json` as the file to import.
Before you submit! Save and run your code to verify that it works as you expect. 
You MUST have a well-written README in your repository. Ensure your markdown renders correctly before submission. You can use Visual Studio Code Markdown preview to see how it would appear on your GitHub repository.
Resources
How to write a good README.
 

Deliverables
Your job is to build out the Flask API to add the functionality described in the deliverables below.

Models
You will implement an API for the following data model:

domain.png

Now you can implement the relationships as shown in the ER Diagram:

- An `Episode` has many `Guest`s through `Appearance`
- A `Guest` has many `Episode`s through `Appearance`
- An `Appearance` belongs to a `Guest` and belongs to a `Episode`

Since a `Appearance` belongs to a `Episode` and a `Guest`, configure the model to cascade deletes.

Set serialization rules to limit the recursion depth.
Run the migrations and seed the database
Note that this seed file uses a CSV file Download CSV fileto populate the database. If you aren't able to get the provided seed file working, you are welcome to generate your own seed data to test the application.

Validations
Add validations to the `Appearance` model:

- must have a `rating` between 1 and 5 (inclusive - 1 and 5 are okay)