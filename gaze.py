import sys
import cv2
import numpy as np
import dlib
import array
import time

cap = cv2.VideoCapture(0)

# takes the values from the file
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# array which are needed for all the filters
arr_left = array.array('i', [])
arr_right = array.array('i', [])
decision_left = array.array('i', [])
decision_right = array.array('i', [])
fixation_time = []
print("OKAY HOLO KI")
cnt = 0
flag = 1
k_cnt = 0
cnt_fin = 0
a = 0
b = 0
a1 = 0
b1 = 0
a2 = 0
b2 = 0
a3 = 0
b3 = 0
a4 = 0
b4 = 0
a5 = 0
b5 = 0

# Famous font for printing on the screen
font = cv2.FONT_HERSHEY_SIMPLEX

start_time = time.time()

while True:
    # converting from RGB to GRAY
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)

        # Human face can be divided into many points or landmarks. left eye 36-41 and right eye 42-47
        # polyline is the red hyperbola which is appearing after detecting the eye

        left_eye_region = np.array([(landmarks.part(34).x, landmarks.part(34).y),
                                    (landmarks.part(36).x, landmarks.part(36).y),
                                    (landmarks.part(37).x, landmarks.part(37).y),
                                    (landmarks.part(38).x, landmarks.part(38).y),
                                    (landmarks.part(39).x, landmarks.part(39).y),
                                    (landmarks.part(40).x, landmarks.part(40).y),
                                    (landmarks.part(41).x, landmarks.part(41).y)], np.int32)
        right_eye_region = np.array([(landmarks.part(42).x, landmarks.part(42).y),
                                     (landmarks.part(43).x, landmarks.part(43).y),
                                     (landmarks.part(44).x, landmarks.part(44).y),
                                     (landmarks.part(45).x, landmarks.part(45).y),
                                     (landmarks.part(46).x, landmarks.part(46).y),
                                     (landmarks.part(47).x, landmarks.part(47).y)], np.int32)
        # cv2.putText(frame, "X"+" "+str(landmarks.part(36).x)+" "+str(landmarks.part(36).y),
        # (25,400), cv2.FONT_HERSHEY_SIMPLEX, 1,
        # (0, 255, 255))
        cv2  # .putText(frame, ".",
        #           (landmarks.part(34).x, landmarks.part(34).y), cv2.FONT_HERSHEY_SIMPLEX, 1,
        # cv2.putText(frame, "O",
        #  (landmarks.part(37).x*(-2)+100, landmarks.part(37).y*(2)-100), cv2.FONT_HERSHEY_SIMPLEX, 1,
        # (0, 255, 255))
        cv2.putText(frame, ".",
                    (landmarks.part(37).x, landmarks.part(37).y), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 255, 255))
        cv2.putText(frame, "Y",
                    (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 255, 255))
        cv2.putText(frame, "X",
                    (190, 200), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 255, 255))
        #  cv2.putText(frame, ".",
        #             (landmarks.part(37).x, landmarks.part(37).y), cv2.FONT_HERSHEY_SIMPLEX, 1,
        #            (0, 255, 255))
        print(landmarks.part(36).y, landmarks.part(37).y, landmarks.part(38).y, landmarks.part(39).y,
              landmarks.part(40).y, landmarks.part(41).y)
        print(landmarks.part(37).x, landmarks.part(37).y, landmarks.part(46).x, landmarks.part(46).y)
        if (landmarks.part(36).y < a and landmarks.part(37).y < a1 and landmarks.part(38).y < a2 and landmarks.part(
                39).y < a3 and landmarks.part(40).y < a4 and landmarks.part(41).y < a5 and landmarks.part(
                42).y < b and landmarks.part(43).y < b1 and landmarks.part(44).y < b2 and landmarks.part(
                45).y < b3 and landmarks.part(46).y < b4 and landmarks.part(47).y < b5):
            cv2.putText(frame,
                        "WELCOME!!!!!!!!!!!!!!!!!!!!" + str(landmarks.part(37).x) + "x  y" + str(landmarks.part(37).y),
                        (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 0, 120))
            print("Okay bro a b")
            print(a)
            print(b)
        a = landmarks.part(36).y
        b = landmarks.part(42).y
        a1 = landmarks.part(37).y
        b1 = landmarks.part(43).y
        a2 = landmarks.part(38).y
        b2 = landmarks.part(44).y
        a3 = landmarks.part(39).y
        b3 = landmarks.part(45).y
        a4 = landmarks.part(40).y
        b4 = landmarks.part(46).y
        a5 = landmarks.part(41).y
        b5 = landmarks.part(47).y
        # cv2.putText(frame, "Hello World!!!"+str(landmarks.part(37).x), (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,
        # 255, 255))
        if 220 <= landmarks.part(37).x <= 250 and landmarks.part(
                37).y >= 130 and landmarks.part(37).y <= 150 and landmarks.part(46).x >= 375 and landmarks.part(
            46).x <= 405 and 145 <= landmarks.part(46).y <= 165:
            print("Hellooooo")
            cv2.polylines(frame, [left_eye_region], True, (0, 0, 255), 2)
            cv2.polylines(frame, [right_eye_region], True, (0, 0, 255), 2)

            # minimum ar maximum value is the initial position of the eye
            left_min_x = np.min(left_eye_region[:, 0])
            left_max_x = np.max(left_eye_region[:, 0])
            left_min_y = np.min(left_eye_region[:, 1])
            left_max_y = np.max(left_eye_region[:, 1])

            right_min_x = np.min(right_eye_region[:, 0])
            right_max_x = np.max(right_eye_region[:, 0])
            right_min_y = np.min(right_eye_region[:, 1])
            right_max_y = np.max(right_eye_region[:, 1])

            left_eye = frame[left_min_y: left_max_y, left_min_x: left_max_x]
            right_eye = frame[right_min_y: right_max_y, right_min_x: right_max_x]

            # To locate the exact pupil, giving the threshold after converting into grey
            gray_left_eye = cv2.cvtColor(left_eye, cv2.COLOR_BGR2GRAY)
            gray_right_eye = cv2.cvtColor(right_eye, cv2.COLOR_BGR2GRAY)

            _, threshold_eye_left = cv2.threshold(gray_left_eye, 70, 255, cv2.THRESH_BINARY_INV)
            _, threshold_eye_right = cv2.threshold(gray_right_eye, 70, 255, cv2.THRESH_BINARY_INV)

            height, width = threshold_eye_left.shape

            threshold_left_side = threshold_eye_left[0: height, 0: int(width / 2)]
            threshold_left_side_white = cv2.countNonZero(threshold_left_side)

            height, width = threshold_eye_left.shape
            threshold_right_side = threshold_eye_right[0: height, int(width / 2): width]
            threshold_right_side_white = cv2.countNonZero(threshold_right_side)

            cv2.putText(frame, str(threshold_left_side_white), (50, 100), font, 2, (0, 0, 255), 3)
            cv2.putText(frame, str(threshold_right_side_white), (50, 150), font, 2, (0, 0, 255), 3)

            # Resizing the frame
            left_eye = cv2.resize(left_eye, None, fx=5, fy=5)
            right_eye = cv2.resize(right_eye, None, fx=5, fy=5)

            # array to save, sort the fluctuate random values generated by it
            arr_left.append(threshold_left_side_white)
            arr_right.append(threshold_right_side_white)

            arr_left = sorted(arr_left)
            arr_right = sorted(arr_right)

            left_len = len(arr_left)
            right_len = len(arr_right)

            end_time = time.time()

            # print(arr_left[2], arr_left[left_len-1],left_len,end_time-start_time)
            if flag == 1:
                decision_left.append(arr_left[int((left_len - 1) / 2)])
                decision_right.append(arr_right[int((right_len - 1) / 2)])

                decision_left_len = len(decision_left)
                decision_right_len = len(decision_right)

                keeper_left = arr_left[int((left_len - 1) / 2)]
                keeper_right = arr_right[int((right_len - 1) / 2)]

                flag = 0
                cnt_fin = cnt_fin + 1
            else:
                if (keeper_left - arr_left[int((left_len - 1) / 2)]) > 10 or (
                        keeper_left - arr_left[int((left_len - 1) / 2)]) < -10 or (
                        keeper_right - arr_right[int((right_len - 1) / 2)]) > 10 or (
                        keeper_right - arr_right[int((right_len - 1) / 2)]) < -10:
                    k_cnt = k_cnt + 1
                    if k_cnt == 3:
                        end_time = time.time()
                        if int(end_time - start_time) > 0:
                            fixation_time.append([average_left, average_right, int(end_time - start_time)])
                        del decision_left[:]
                        del decision_right[:]
                        decision_left = array.array('i', [arr_left[int((left_len - 1) / 2)]])
                        decision_right = array.array('i', [arr_right[int((right_len - 1) / 2)]])

                        decision_left_len = len(decision_left)
                        decision_right_len = len(decision_right)
                        print(threshold_left_side_white, threshold_right_side_white, '|',
                              arr_left[int((left_len - 1) / 2)], arr_right[int((right_len - 1) / 2)], '|',
                              decision_left[int((decision_left_len - 1) / 2)],
                              decision_right[int((decision_right_len - 1) / 2)], '|', average_left, average_right, '|',
                              fixation_time[(len(fixation_time) - 1)])

                        keeper_left = arr_left[int((left_len - 1) / 2)]
                        keeper_right = arr_right[int((right_len - 1) / 2)]
                        p = k_cnt
                        k_cnt = 0
                        cnt_fin = 1
                        end_time = 0
                        start_time = 0
                        start_time = time.time()
                else:
                    decision_left.append(arr_left[int((left_len - 1) / 2)])
                    decision_right.append(arr_right[int((right_len - 1) / 2)])

                    keeper_left = arr_left[int((left_len - 1) / 2)]
                    keeper_right = arr_right[int((right_len - 1) / 2)]

                    decision_left_len = len(decision_left)
                    decision_right_len = len(decision_right)
                    cnt_fin = cnt_fin + 1
            average_left = int(sum(decision_left) / len(decision_left))
            average_right = int(sum(decision_right) / len(decision_right))

            print(threshold_left_side_white, threshold_right_side_white, '|', arr_left[int((left_len - 1) / 2)],
                  arr_right[int((right_len - 1) / 2)], '|', decision_left[int((decision_left_len - 1) / 2)],
                  decision_right[int((decision_right_len - 1) / 2)], '|', average_left, average_right)
            cnt = cnt + 1
            if cnt == 10:
                a = arr_left[int((left_len - 1) / 2)]
                b = arr_right[int((right_len - 1) / 2)]
                del arr_left[:]
                del arr_right[:]
                arr_left = array.array('i', [a])
                arr_right = array.array('i', [b])
                cnt = 1
            if cnt_fin == 16:
                a = decision_left[int((decision_left_len - 1) / 2)]
                b = decision_right[int((decision_right_len - 1) / 2)]

                del decision_left[:]
                del decision_right[:]

                decision_left = array.array('i', [a, a])
                decision_right = array.array('i', [b, b])

                decision_left_len = len(decision_left)
                decision_right_len = len(decision_right)

                keeper_left = a
                keeper_right = b
                cnt_fin = 1
                k_cnt = 0

    # The rectangle is the place where the eye will be fixed
    cv2.rectangle(frame, (200, 120), (440, 180), (0, 255, 0), 3)
    cv2.imshow("Frame", frame)

    # Termination
    key = cv2.waitKey(30)
    if key == 27:
        break

# data release and camera rest
cap.release()
cv2.destroyAllWindows()
print("thik hai")
