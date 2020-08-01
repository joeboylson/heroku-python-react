# HEROKU PYTHON REACT

A boilerplate repo to get you up and running with React, Python, and Heroku.

<br/>

# SETUP

<br/>

### DEVELOPMENT

1. Clone this repo
2. To install Node depenedencies, run `npm install` (or `yarn install` if you prefer)
3. To install Python dependencies, run `pip install -r requirements.txt`
4. Start the Flask server with `python app.py`
5. Start the Webpack dev server with `npm run dev` (or `yarn dev`)

<br/>

### PRODUCTION (on Heroku)

>  ( Assuming you have a Heroku account and have pushed your latest code to github )

1. Create a new Heroku project (you can do this online or through Heroku CLI)
2. **Make sure this project has _BOTH_ Node.js and Python buildpacks**
3. Connect to Heroku project you your github repo with [Heroku's github integration](https://devcenter.heroku.com/articles/github-integration)
4. Fire off the deployment

**What the deployment actually does:** <br/> Heroku will first install all the Node and Python dependencies. Then, it will see that the `package.json` has a `heroku-postbuild` command and it will run it - this command tells webpack to build the React project into a `dist` folder. After this completes, Heroku will run the specified command in the `Procfile` (npm run production), which will serve the React app which webpack just bundled. Your app is up and running with React and Python!

<br/>

### OPTIONAL

- Turn on Automatic Deployments: when you push to master (or any other specified branch), Heroku will rebuild your project and release the new version. This usually takes about 2 minutes.

- Add a Heroku Postgres Add-On: now it's full-stack!

---

<br/><br/><br/>

Free to use for any personal or professional project. <br/>
Reach out if you have any questions!<br/>

Created by Joe Boylson <br/>
e: joeboylson@gmail.com <br/>

