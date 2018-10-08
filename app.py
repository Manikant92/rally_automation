# from pyral import Rally
from flask import Flask, request, render_template
from rally_user_story_task_creation import create_user_story_from_xlsx, create_user_story_from_csv

app = Flask(__name__)
__RALLY_URL = "rally1.rallydev.com"


@app.route('/')
def home():
    return render_template('home.html')


@app.route("/", methods=['GET', 'POST'])
def create():
    try:
        if request.method == 'POST':
            request_data = request.form
            __apikey = request_data['api_key']
            # print(__apikey)
            __username = request_data['username']
            # print(__username)
            __workspace = request_data['workspace']
            # print(__workspace)
            __project = request_data['project']
            # print(__project)
            description = request_data['description']
            # print(description)
            # print(type(description))
            create_task = request_data['create_task']
            # task_names_input = request_data['task_input']
            __uploaded_file = request.files['file']

            if '.xlsx' in __uploaded_file.filename and description == "No" and create_task == "No":
                user_story = create_user_story_from_xlsx(server=__RALLY_URL, apikey=__apikey, workspace=__workspace,
                                                         project=__project, username=__username, file=__uploaded_file,
                                                         description="No", create_task=False)
                if user_story == "Success":
                    return render_template('success.html')
                else:
                    return render_template('failure.html', error=user_story)
            elif ".xlsx" in __uploaded_file.filename and description == "Yes" and create_task == "No":
                user_story = create_user_story_from_xlsx(server=__RALLY_URL, apikey=__apikey, workspace=__workspace,
                                                         project=__project, username=__username, file=__uploaded_file,
                                                         description="Yes", create_task=False)
                if user_story == "Success":
                    return render_template('success.html')
                else:
                    return render_template('failure.html', error=user_story)
            elif ".xlsx" in __uploaded_file.filename and description == "No" and create_task == "Yes":
                task_names_input = request_data['task_input']
                task_names_input = task_names_input.split(',')
                task_names_input = [string.strip() for string in task_names_input]
                user_story = create_user_story_from_xlsx(server=__RALLY_URL, apikey=__apikey, workspace=__workspace,
                                                         project=__project, username=__username, file=__uploaded_file,
                                                         task_data=task_names_input, description="No", create_task=True)
                if user_story == "Success":
                    return render_template('success.html')
                else:
                    return render_template('failure.html', error=user_story)
            elif ".xlsx" in __uploaded_file.filename and description == "Yes" and create_task == "Yes":
                task_names_input = request_data['task_input']
                task_names_input = task_names_input.split(',')
                task_names_input = [string.strip() for string in task_names_input]
                # print(task_names_input)
                user_story = create_user_story_from_xlsx(server=__RALLY_URL, apikey=__apikey, workspace=__workspace,
                                                         project=__project, username=__username, file=__uploaded_file,
                                                         task_data=task_names_input, description="Yes", create_task=True)
                if user_story == "Success":
                    return render_template('success.html')
                else:
                    return render_template('failure.html', error=user_story)
            elif '.csv' in __uploaded_file.filename and description == "No" and create_task == "No":
                user_story = create_user_story_from_csv(server=__RALLY_URL, apikey=__apikey, workspace=__workspace,
                                                        project=__project, username = __username, file=__uploaded_file,
                                                        description ="No", create_task = False)
                if user_story == "Success":
                    return render_template('success.html')
                else:
                    return render_template('failure.html', error=user_story)
            elif ".csv" in __uploaded_file.filename and description == "Yes" and create_task == "No":
                user_story = create_user_story_from_csv(server=__RALLY_URL, apikey=__apikey, workspace=__workspace,
                                                        project=__project, username=__username, file=__uploaded_file,
                                                        description="Yes", create_task=False)
                if user_story == "Success":
                    return render_template('success.html')
                else:
                    return render_template('failure.html', error=user_story)
            elif ".csv" in __uploaded_file.filename and description == "No" and create_task == "Yes":
                task_names_input = request_data['task_input']
                task_names_input = task_names_input.split(',')
                task_names_input = [string.strip() for string in task_names_input]
                user_story = create_user_story_from_csv(server=__RALLY_URL, apikey=__apikey, workspace=__workspace,
                                                        project=__project, username=__username, file=__uploaded_file,
                                                        task_data=task_names_input, description="No", create_task=True)
                if user_story == "Success":
                    return render_template('success.html')
                else:
                    return render_template('failure.html', error=user_story)
            elif ".csv" in __uploaded_file.filename and description == "Yes" and create_task == "Yes":
                task_names_input = request_data['task_input']
                task_names_input = task_names_input.split(',')
                task_names_input = [string.strip() for string in task_names_input]
                user_story = create_user_story_from_csv(server=__RALLY_URL, apikey=__apikey, workspace=__workspace,
                                                        project=__project, username=__username, file=__uploaded_file,
                                                        task_data=task_names_input, description="Yes", create_task=True)
                if user_story == "Success":
                    return render_template('success.html')
                else:
                    return render_template('failure.html', error=user_story)
            else:
                message = "There is wrong in code or your file format. " \
                          "Please reach out to manikant.kella@accenture.com to get fixed!!"
                return render_template('failure.html', error=message)
    except Exception as e:
        render_template('failure.html', error=e)


if __name__ == '__main__':
    app.run()
