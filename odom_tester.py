#!/usr/bin/env python
import requests
import json
import csv
from pathlib import Path
from datetime import datetime
import time
from threading import Thread
import os
import multiprocessing

import roslib
import sys
import rospy
from gazebo_msgs.srv import *

import numpy as np

link_navigate = "http://localhost:8080/gs-robot/cmd/position/navigate"
link_amcl_pose = 'http://localhost:8080/gs-robot/real_time_data/amcl_pose'
dest_array = ['end', 'start', 'mid']
dest_array_alt = ['end2', 'start2', 'mid2']

deviation_list = []

successed = True

index = 0


def tester(map_name, round):
    # print('start running')
    global index
    global successed
    thread_logger = Thread(target=test_logger)
    thread_logger.start()

    if round == 0:
        dest_array_now = dest_array
    if round == 1:
        dest_array_now = dest_array_alt

    while (1):
        
        navigation_params = {
            'map_name': map_name,
            'position_name': dest_array_now[index % len(dest_array_now)]
        }
        results = requests.get(link_navigate, navigation_params)
        print(index)
        index += 1
        if results.status_code == 200:
            (results.status_code)
            res_obj = json.loads(results.text)
            if not res_obj['successed']:
                successed = False
                break
            if index == 30:
                # successed = False
                break
        else:
            break


def test_logger():
    global index
    parent_path = Path(__file__).parent
    (parent_path / 'csvs').mkdir(parents=True, exist_ok=True)
    with open(parent_path.joinpath(
            'csvs/test_auto{}.csv'.format(datetime.now().strftime('%d%H%M%S'))),
            'w', encoding='UTF-8', newline='') as csv_log:
        writer = csv.writer(csv_log)

        row_index = index

        log_recrods = [row_index]

        while (1):
            if not successed:
                writer.writerow(log_recrods)
                # print('logging')
                csv_log.close()
                break
            if row_index != index:
                writer.writerow(log_recrods)
                if index == 30:
                    deviation_var = np.var(deviation_list)
                    print(deviation_var)
                    writer.writerow(deviation_list)
                    writer.writerow([deviation_var])
                    csv_log.close()
                    break
                print('logging')
                row_index = index
                log_recrods = [row_index]
            results = requests.get(link_amcl_pose)
            if results.status_code == 200:
                res_obj = json.loads(results.text)
                if res_obj['successed']:
                    pos = res_obj['data']['pose']['pose']['position']
                    gazebo = gms_client('robot_base', 'world')
                    log_recrods.append('({},{};{},{})'.format(
                        pos['x'], pos['y'], gazebo.pose.position.x, gazebo.pose.position.y))
                    deviation = np.square(
                        gazebo.pose.position.x - pos['x']) + np.square(gazebo.pose.position.y - pos['y'])
                    deviation_list.append(deviation)
                    # print(log_recrods)
            time.sleep(1)
    return


def gms_client(model_name, relative_entity_name):
    rospy.wait_for_service('/gazebo/get_model_state')
    try:
        gms = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        resp1 = gms(model_name, relative_entity_name)
        return resp1
    except rospy.ServiceException:
        print("Service call failed")


def restart_ros():
    global index
    global successed
    index = 0
    successed = True
    proc = multiprocessing.Process(target=restart_ros_fun)
    proc.start()
    time.sleep(60)
    proc.terminate()


def restart_ros_fun():
    os.system('sh {}'.format(Path(__file__).with_name('restart_ros.sh')))


if __name__ == '__main__':
    tester(sys.argv[1], sys.argv[2])
    # for i in range(5):
    #     tester()
    #     print('round {} finished'.format(i))
    #     restart_ros()
    #     print('ros restarted for the {}th time'.format(i))
