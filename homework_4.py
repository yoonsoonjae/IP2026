import numpy as np
import cv2

def run_main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while(True):
        ret, frame = cap.read()
        roi = frame[0:500, 0:500]

        # HSV 변환
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        # 연두색 범위
        lower = np.array([40, 50, 50])
        upper = np.array([80, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)

        # 🔥 구멍 메우기 (조금 더 강하게)
        kernel = np.ones((5, 5), np.uint8)
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=3)

        # contour 찾기
        contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 🔥 가장 큰 덩어리만 사용
        if contours:
            cnt = max(contours, key=cv2.contourArea)

            area = cv2.contourArea(cnt)
            if area > 2000:
                # 🔥 convex hull 적용 (모양 깔끔하게)
                hull = cv2.convexHull(cnt)
                cv2.drawContours(roi, [hull], -1, (0,255,0), 2)

        cv2.imshow("Mask", mask)
        cv2.imshow("Closing", closing)
        cv2.imshow('Contours', roi)

        # 아무 키나 종료
        if cv2.waitKey(1) != -1:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_main()