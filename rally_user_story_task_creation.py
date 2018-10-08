from pyral import Rally
import pandas as pd
# import traceback


def create_user_story_from_xlsx(server, apikey, workspace, project, username, file, task_data=None, description="No",
                                create_task=False):
    try:
        file = file
        task_names = task_data
        access_rally = Rally(server=server, apikey=apikey, workspace=workspace, project=project)
        project_ref = access_rally.getProject()
        user_ref = access_rally.getUserInfo(username=username).pop(0)
        df = pd.read_excel(file)
        df.fillna('N/A', inplace=True)
        story_card_name = df['iTrack_Number/Jira_Number/Req_Number'] + ' ' + df['Name']
        story_card_name = story_card_name.tolist()
        if not create_task:
            if description == "No":
                for name in story_card_name:
                    user_story_data = {"Project": project_ref.ref,
                                       "Name": name,
                                       "Owner": user_ref.ref,
                                       "ScheduleState": "Backlogged"}
                    create_user_story = access_rally.put('UserStory', user_story_data)
                return 'Success'
            elif description == 'Yes':
                description_data = df['Description'].tolist()
                us_description_combination = list(zip(story_card_name, description_data))
                for value in us_description_combination:
                    user_story_data = {"Project": project_ref.ref,
                                       "Name": value[0],
                                       "Description": value[1],
                                       "Owner": user_ref.ref,
                                       "ScheduleState": "Backlogged"}
                    create_user_story = access_rally.put('UserStory', user_story_data)
                return 'Success'
        elif create_task:
            if description == "No":
                for name in story_card_name:
                    user_story_data = {"Project": project_ref.ref,
                                       "Name": name,
                                       "Owner": user_ref.ref,
                                       "ScheduleState": "Backlogged"}
                    create_user_story = access_rally.put('UserStory', user_story_data)
                    # task_names = task_data
                    user_story_id = create_user_story.FormattedID
                    target_story_card = access_rally.get('UserStory', query="FormattedID = " + user_story_id,
                                                         instance=True)
                    # target_story_card_ref = target_story_card.ref
                    for i in range(len(task_names)):
                        create_task_data = {"Project": project_ref.ref,
                                            "WorkProduct": target_story_card.ref,
                                            "Name": task_names[i],
                                            "Owner": user_ref.ref,
                                            "State": "Defined",
                                            "TaskIndex": i}
                        task = access_rally.put('Task', create_task_data)
                return 'Success'
            elif description == 'Yes':
                description_data = df['Description'].tolist()
                us_description_combination = list(zip(story_card_name, description_data))
                for value in us_description_combination:
                    user_story_data = {"Project": project_ref.ref,
                                       "Name": value[0],
                                       "Description": value[1],
                                       "Owner": user_ref.ref,
                                       "ScheduleState": "Backlogged"}
                    create_user_story = access_rally.put('UserStory', user_story_data)
                    user_story_id = create_user_story.FormattedID
                    target_story_card = access_rally.get('UserStory', query="FormattedID = " + user_story_id,
                                                         instance=True)
                    # target_story_card_ref = target_story_card.ref
                    for i in range(len(task_names)):
                        create_task_data = {"Project": project_ref.ref,
                                            "WorkProduct": target_story_card.ref,
                                            "Name": task_names[i],
                                            "Owner": user_ref.ref,
                                            "State": "Defined",
                                            "TaskIndex": i}
                        task = access_rally.put('Task', create_task_data)
                return 'Success'
    except Exception as e:
        # print(Exception)
        # print(traceback)
        #tb = traceback.format_exc()
        return "Failed Creation For Reasons: " + str(e) + ". Please re-try!"



def create_user_story_from_csv(server, apikey, workspace, project, username, file, task_data=None, description="No",
                               create_task=False):
    try:
        file = file
        task_names = task_data
        access_rally = Rally(server=server, apikey=apikey, workspace=workspace, project=project)
        project_ref = access_rally.getProject()
        user_ref = access_rally.getUserInfo(username=username).pop(0)
        df = pd.read_csv(file)
        df.fillna('N/A', inplace=True)
        story_card_name = df['iTrack_Number/Jira_Number/Req_Number'] + ' ' + df['Name']
        story_card_name = story_card_name.tolist()
        if not create_task:
            if description == "No":
                for name in story_card_name:
                    user_story_data = {"Project": project_ref.ref,
                                       "Name": name,
                                       "Owner": user_ref.ref,
                                       "ScheduleState": "Backlogged"}
                    create_user_story = access_rally.put('UserStory', user_story_data)
                return 'Success'
            elif description == 'Yes':
                description_data = df['Description'].tolist()
                us_description_combination = list(zip(story_card_name, description_data))
                for value in us_description_combination:
                    user_story_data = {"Project": project_ref.ref,
                                       "Name": value[0],
                                       "Description": value[1],
                                       "Owner": user_ref.ref,
                                       "ScheduleState": "Backlogged"}
                    create_user_story = access_rally.put('UserStory', user_story_data)
                return 'Success'
        elif create_task:
            if description == "No":
                for name in story_card_name:
                    user_story_data = {"Project": project_ref.ref,
                                       "Name": name,
                                       "Owner": user_ref.ref,
                                       "ScheduleState": "Backlogged"}
                    create_user_story = access_rally.put('UserStory', user_story_data)
                    # task_names = task_data
                    user_story_id = create_user_story.FormattedID
                    target_story_card = access_rally.get('UserStory', query="FormattedID = %s" % user_story_id,
                                                         instance=True)
                    # target_story_card_ref = target_story_card.ref
                    for i in range(len(task_names)):
                        create_task_data = {"Project": project_ref.ref,
                                            "WorkProduct": target_story_card.ref,
                                            "Name": task_names[i],
                                            "Owner": user_ref.ref,
                                            "State": "Defined",
                                            "TaskIndex": i}
                        task = access_rally.put('Task', create_task_data)
                return 'Success'
            elif description == 'Yes':
                description_data = df['Description'].tolist()
                us_description_combination = list(zip(story_card_name, description_data))
                for value in us_description_combination:
                    user_story_data = {"Project": project_ref.ref,
                                       "Name": value[0],
                                       "Description": value[1],
                                       "Owner": user_ref.ref,
                                       "ScheduleState": "Backlogged"}
                    create_user_story = access_rally.put('UserStory', user_story_data)
                    user_story_id = create_user_story.FormattedID
                    target_story_card = access_rally.get('UserStory', query="FormattedID = %s" % user_story_id,
                                                         instance=True)
                    # target_story_card_ref = target_story_card.ref
                    for i in range(len(task_names)):
                        create_task_data = {"Project": project_ref.ref,
                                            "WorkProduct": target_story_card.ref,
                                            "Name": task_names[i],
                                            "Owner": user_ref.ref,
                                            "State": "Defined",
                                            "TaskIndex": i}
                        task = access_rally.put('Task', create_task_data)
                return 'Success'
    except Exception as e:
        return "Failed Creation For Reasons: " + str(e) + ". Please re-try!"
