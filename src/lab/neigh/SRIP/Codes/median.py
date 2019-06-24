from cv2 import * #Import functions from OpenCV
import cv2

if __name__ == '__main__':
    source = cv2.imread("Medianfilterp.png", CV_LOAD_IMAGE_GRAYSCALE)
    final = source[:]
    for y in range(len(source)):
        for x in range(y):
            final[y,x]=source[y,x]

    members=[source[0,0]]*9
    for y in range(1,len(source)-1):
        for x in range(1,y-1):
            members[0] = source[y-1,x-1]
            members[1] = source[y,x-1]
            members[2] = source[y+1,x-1]
            members[3] = source[y-1,x]
            members[4] = source[y,x]
            members[5] = source[y+1,x]
            members[6] = source[y-1,x+1]
            members[7] = source[y,x+1]
            members[8] = source[y+1,x+1]

            members.sort()
            final[y,x]=members[4]

    cv.NamedWindow('Source_Picture', cv.CV_WINDOW_AUTOSIZE)
    cv.NamedWindow('Final_Picture', cv.CV_WINDOW_AUTOSIZE)
    cv2.imshow('Source_Picture', source) #Show the image
    cv2.imshow('Final_Picture', final) #Show the image
    cv2.waitKey()