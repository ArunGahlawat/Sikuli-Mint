from SikuliLibrary import sikuli
import os


class SikuliKeywordHelper:
    os.environ["DISABLE_SIKULI_LOG"] = 'True'
    lib = sikuli.SikuliLibrary()

    def Add_Image_Path(self, path):
        """
        Add image path
        """
        args = [path]
        return self.lib.run_keyword('addImagePath', args)

    def Capture_Region(self, *coordinates):
        """
        Capture region
        Capture region passed
        Examples:
        | ${screenshotname}= | Capture region | [x, y, w, h] |
        """
        args = [coordinates]
        return self.lib.run_keyword('captureRegion', args)

    def Capture_Roi(self):
        """
        Capture Roi
        """
        args = []
        return self.lib.run_keyword('captureRoi', args)

    def Capture_Screen(self):
        """
        Capture whole screen, file name is returned
        """
        args = []
        return self.lib.run_keyword('captureScreen', args)

    def Change_Screen_Id(self, screenId):
        """
        Change screen id
         For multi display, user could use this keyword to switch to the correct screen

         Examples:
         | Change screen id | 1 |
        """
        args = [screenId]
        return self.lib.run_keyword('changeScreenId', args)

    def Clear_All_Highlights(self):
        """
        Clear all highlights from screen
        """
        args = []
        return self.lib.run_keyword('clearAllHighlights', args)

    def Clear_Highlight(self, image):
        """
        Clear highlight from screen
        """
        args = [image]
        return self.lib.run_keyword('clearHighlight', args)

    def Click_Using_Image(self, image, xOffset=0, yOffset=0):
        """
        Click

        Click on an image with similarity and offset.
        Examples:
        | Set Capture Matched Image | false |
        """
        args = [image, xOffset, yOffset]
        return self.lib.run_keyword('click', args)

    def Click_In(self, areaImage, targetImage):
        """
        Click in.
        Click target image in area image.
        """
        args = [areaImage, targetImage]
        return self.lib.run_keyword('clickIn', args)

    def Click_Nth(self, image, index, similarity, sortByColumn=True):
        """
        Click nth

         Click on specific image.
         Optionally pass similarity and sort by column or row.

         Examples:
         | Click on nth image in region | image.png | 1 | 0.9 |
         | Click on nth image in region | image.png | 1 | 0.9 | ${FALSE} |
        """
        args = [image, index, similarity, sortByColumn]
        return self.lib.run_keyword('clickNth', args)

    def Click_Region(self, coordinates, waitChange=0, timeout=0):
        """
        Click region

         Click on defined region coordinates.
         Optionally Wait for specified time to ensure region has changed.
         Also, optionally set highlight

         Examples:
         | Click on region | [x,y,w,h] | image.png |
         | Click on region | [x,y,w,h] | image.png | 0 |
         | Click on region | [x,y,w,h] | image.png | 0 | 2 |
        """
        args = [coordinates, waitChange, timeout]
        return self.lib.run_keyword('clickRegion', args)

    def Click_Text_Using_Image(self, text):
        """
        Click Text
            Click on text.
            Examples:
            | Click Text | Hello |
        """
        args = [text]
        return self.lib.run_keyword('clickText', args)

    def Close_Application(self, name):
        """
        Close application
        """
        args = [name]
        return self.lib.run_keyword('closeApplication', args)

    def Double_Click_Using_Image(self, image, xOffset=0, yOffset=0):
        """
        Double click
        """
        args = [image, xOffset, yOffset]
        return self.lib.run_keyword('doubleClick', args)

    def Double_Click_In(self, areaImage, targetImage):
        """
        Double click in.
        Double click target image in area image.
        """
        args = [areaImage, targetImage]
        return self.lib.run_keyword('doubleClickIn', args)

    def Drag_And_Drop_Using_Image(self, srcImage, targetImage):
        """
        Drag the source image to target image.
        If source image is empty, drag the last match and drop at given target
        """
        args = [srcImage, targetImage]
        return self.lib.run_keyword('dragAndDrop', args)

    def Drag_And_Drop_By_Offset(self, srcImage, xOffset, yOffset):
        """
        Drag the source image to target by offset.
        If source image is empty, drag the last match and drop at given target
        """
        args = [srcImage, xOffset, yOffset]
        return self.lib.run_keyword('dragAndDropByOffset', args)

    def Image_Exists(self, image, timeout=10):
        """
        Exists

         Check whether image exists in screen
         @image: expected image in screen
         @timeout: wait seconds

         Examples:
         | ${is_exist}=  | Exists | image.png | 0 |
        """
        args = [image, timeout]
        return self.lib.run_keyword('exists', args)

    def All_Image_Exists(self,images,timeout=10):
        for image in images:
            is_present = self.Image_Exists(image,timeout)
            if not is_present:
                return False
        return True


    def Get_Current_Screen_Id(self):
        """
        Get current screen id
        """
        args = []
        return self.lib.run_keyword('getCurrentScreenId', args)

    def Get_Extended_Region_From(self, image, direction, number_of_times_to_repeat):
        """
        Get extended region from
         Extended the given image creating a region above or below with the same width
         The height can change using the multiplier @number_of_times_to_repeat,
         if 2 is given the new region will have twice the height of the original
        """

        args = [image, direction, number_of_times_to_repeat]
        return self.lib.run_keyword('getExtendedRegionFrom', args)

    def Get_Image_Coordinates(self, image, *coordinates):
        """
        Get Image Coordinates

         Return image coordinates, within region
         Examples:
         | ${imageCoordinates}= | Get Image Coordinates | image.png=0.75 |
         | ${imageCoordinates}= | Get Image Coordinates | image.png=0.75 | [x, y, w, z] |
        """
        args = [image, coordinates]
        return self.lib.run_keyword('getImageCoordinates', args)

    def Get_Match_Score(self, image):
        """
        Get match score
        Tries to find the image on the screen, returns accuracy score (0-1)

         Examples:
         | ${score} = | Get Match Score |  somethingThatMayExist.png |
         | Run Keyword if | ${score} > 0.95 | keyword1 | ELSE | keyword2 |
        """
        args = [image]
        return self.lib.run_keyword('getMatchScore', args)

    def Get_Number_Of_Screens(self):
        """
        Get number of screens
        """
        args = []
        return self.lib.run_keyword('getNumberOfScreens', args)

    def Get_Screen_Coordinates(self):
        """
        Get screen coordinates

        Return screen coordinates for active screen

        Examples:
        | @{coordinates}=  | Get Screen Coordinates | 0 |
        """
        args = []
        return self.lib.run_keyword('getScreenCoordinates', args)

    def Get_Text_Using_Image(self, image=''):
        """
        Get text

         If image is not given, keyword will get text from whole Screen
         If image is given, keyword will get text from matched region
         Call keyword setOcrTextRead to set OcrTextRead as true, before using text recognition keywords

         Examples:
         | Set Ocr Text Read  | true       |
         | Get Text           |
         | Get Text           | test.png   |
        """

        args = []
        if image.strip() != '':
            args.append(image)
        return self.lib.run_keyword('getText', args)

    def Highlight(self, image, secs=0):
        """
        Highlight matched image.
         If secs is set, highlight will vanish automatically after set seconds
        """
        args = [image, secs]
        return self.lib.run_keyword('highlight', args)

    def Highlight_Region(self, *coordinates, timeout):
        """
        Highlight region
        """

        args = [coordinates, timeout]
        return self.lib.run_keyword('highlightRegion', args)

    def Highlight_Roi(self, timeout):
        """
        Highlight ROI
        """
        args = [timeout]
        return self.lib.run_keyword('highlightRoi', args)

    def Image_Count(self, steps, image=''):
        """
        Image Count
         Count how many times the same picture is detected in screen.\

         Examples:
         | ${image_cnt}=  |  Image Count  | test.png  |
        """
        args = [steps, image]
        return self.lib.run_keyword('imageCount', args)

    def Input_Text_Using_Image(self, image, text):
        """
        Input text
         Image could be empty

         Examples:
         | Input text | Sikuli |
        """
        args = [image, text]
        return self.lib.run_keyword('inputText', args)

    def Mouse_Down_Using_Image(self, *mouseButtons):
        """
        Mouse down
         Press and hold the specified buttons

         @mouseButtons: Could be LEFT, MIDDLE, RIGHT

         Examples:
         | Mouse Move   | test.png |
         | Mouse Down   | LEFT     | RIGHT |
         | Mouse Up     |
        """

        args = [mouseButtons]
        return self.lib.run_keyword('mouseDown', args)

    def Mouse_Move_Using_Image(self, image=''):
        """
        Mouse moveMove the mouse pointer to the target

         @image: if image is empty, will move mouse to the last matched.

         Examples:
         | Mouse Move              | test.png |
         | Screen Should Contain   | test.png |
         | Mouse Move |
        """
        args = [image]
        return self.lib.run_keyword('mouseMove', args)

    def Mouse_Up_Using_Image(self, *mouseButtons):
        """
        Mouse up
         Release the specified mouse buttons

         @mouseButtons: Could be LEFT, MIDDLE, RIGHT. If empty, all currently held buttons are released

         Examples:
         | Mouse Move   | test.png |
         | Mouse Down   | LEFT     | RIGHT |
         | Mouse Up     | LEFT     | RIGHT |
        """
        args = [mouseButtons]
        return self.lib.run_keyword('mouseUp', args)

    def Open_Application(self, path):
        """
        Open application
         To open app with parameters, refer:
         https://sikulix-2014.readthedocs.io/en/latest/appclass.html#App.App
        """
        args = [path]
        return self.lib.run_keyword('openApplication', args)

    def Paste_Text_Using_Image(self, image, text):
        """
        Paste text. Image could be empty
        """
        args = [image, text]
        return self.lib.run_keyword('pasteText', args)

    def Press_Special_Key(self, keyConstant):
        """
        Press special key
         Presses a special keyboard key.

         For a list of possible Keys view docs for org.sikuli.script.Key .

         Examples:
         | Double Click | textFieldWithDefaultText.png |
         | Press Special Key | DELETE |
        """
        args = [keyConstant]
        return self.lib.run_keyword('pressSpecialKey', args)

    def Read_Text_From_Region(self, reg):
        """
        Read text from region
        """
        args = [reg]
        return self.lib.run_keyword('readTextFromRegion', args)

    def Remove_Image_Path(self, path):
        """
        Remove image path
        """
        args = [path]
        return self.lib.run_keyword('removeImagePath', args)

    def Reset_Roi(self):
        """
        Reset ROI
         Set Region of interest to full screen

         Examples:
         | Reset roi |
        """
        args = []
        return self.lib.run_keyword('resetRoi', args)

    def Right_Click(self, image):
        """
        Right click
        """
        args = [image]
        return self.lib.run_keyword('rightClick', args)

    def Right_Click_In(self, areaImage, targetImage):
        """
        Right click in.
        Right click target image in area image.
        """
        args = [areaImage, targetImage]
        return self.lib.run_keyword('rightClickIn', args)

    def Screen_Should_Contain(self, image):
        """
        Screen should contain
        """
        args = [image]
        return self.lib.run_keyword('screenShouldContain', args)

    def Screen_Should_Not_Contain(self, image):
        """
        Screen should not contain
         Screen should not contain image

         Examples:
         | Screen should not contain | image.png |
        """
        args = [image]
        return self.lib.run_keyword('screenShouldNotContain', args)

    def Select_Region(self, message):
        """
        Select Region

         Allow user to select a region and capture it.
         Return array of [capturedImagePath, x, y, w, h]

         Examples:
         | @{SelectedRegion}= | Select region |
        """

        args = [message]
        return self.lib.run_keyword('selectRegion', args)

    def Set_Capture_Folder(self, path):
        """
        Set captured folder

        Set folder for captured images
        Examples:
        | Set captured folder | PATH |
        """
        args = [path]
        return self.lib.run_keyword('setCaptureFolder', args)

    def Set_Capture_Matched_Image(self, value):
        """
        Set capture matched image

        Set capture matched images, the default value is true
        Examples:
        | Set Capture Matched Image | false |
        """
        args = [value]
        return self.lib.run_keyword('setCaptureMatchedImage', args)

    def Set_Min_Similarity(self, minSimilarity):
        """
        Set min similarity
        """
        args = [minSimilarity]
        return self.lib.run_keyword('setMinSimilarity', args)

    def Set_Move_Mouse_Delay(self, delay):
        """
        Set move mouse delay
        """
        args = [delay]
        return self.lib.run_keyword('setMoveMouseDelay', args)

    def Set_Ocr_Text_Read(self, ocrTextRead):
        """
        OCR text read
        """
        args = [ocrTextRead]
        return self.lib.run_keyword('setOcrTextRead', args)

    def Set_Roi(self, coordinates, timeout=0):
        """
        Set ROI

         Set region of interest on screen
         Optionally pass highlight timeout.

         Examples:
         | Set ROI | [x, y, w, h] |
         | Set ROI | [x, y, w, h] | 2 |
        """
        args = [coordinates, timeout]
        return self.lib.run_keyword('setRoi', args)

    def Set_Show_Actions(self, showActions):
        """
        Set show actions
        """
        args = [showActions]
        return self.lib.run_keyword('setShowActions', args)

    def Set_Slow_Motion_Delay(self, delay):
        """
        Set slow motion delay
         Control the duration of the visual effect (seconds).
        """
        args = [delay]
        return self.lib.run_keyword('setSlowMotionDelay', args)

    def Set_Timeout_Using_Image(self, timeout):
        """
        Set timeout

        Set Sikuli timeout(seconds)
        Examples:
        | Set timeout | 10 |
        """
        args = [timeout]
        return self.lib.run_keyword('setTimeout', args)

    def Set_Wait_Scan_Rate(self, delay):
        """
        Set wait scan rate
         Specify the number of times actual search operations are performed per second while waiting
         for a pattern to appear or vanish.
        """
        args = [delay]
        return self.lib.run_keyword('setWaitScanRate', args)

    def Start_Sikuli_Process(self, port=None):
        """

                This keyword is used to start sikuli java process.
                If library is inited with mode OLD, sikuli java process is started automatically.
                If library is inited with mode NEW, this keyword should be used.

                :param port: port of sikuli java process, if value is None or 0, a random free port will be used
                :return: None

        """
        args = [port]
        return self.lib.run_keyword('start_sikuli_process', args)

    def Stop_Remote_Server(self):
        """
        Stops the remote server.

        The server may be configured so that users cannot stop it.
        """
        args = []
        return self.lib.run_keyword('stop_remote_server', args)

    def Type_With_Modifiers(self, text, *modifiers):
        """
        Type with modifiers

         Examples:
         |Type With Modifiers| A | CTRL |
        """
        args = [text, modifiers]
        return self.lib.run_keyword('typeWithModifiers', args)

    def Wait_For_Image(self, wantedImage, notWantedImage='', timeout=10):
        """
        Wait For Image

         Check wantedImage exist. If notWantedImage appear or timeout happened, throw exception

         @wantedImage: expected image in screen

         @notWantedImage: unexpected image in screen

         @timeout: wait seconds

         Examples:
         | Wait For Image  | wanted.png | notWanted.png | 5 |
        """
        args = [wantedImage, notWantedImage, timeout]
        return self.lib.run_keyword('waitForImage', args)

    def Wait_For_Multiple_Images(self, timeout, pollingInterval, expectedImages, notExpectedImages):
        """
        Wait For Multiple Images

         Check if images exists in expectedImages or notExpectedImages list.
         If image appears that is listed in notExpectedImages list or timeout happened,
         throw exception If image appears that is listed in expectedImageslist return successfully.

         @timeout: wait seconds

         @pollingInterval: time in seconds between screen checks

         @expectedImages: list of expected images in screen

         @notExpectedImages: list of not expected images in screen

         Examples:
         | @{wanted_images} =  | Create List | wanted_image1.png | wanted_image2.png |
         | @{not_wanted_images}= | Create List | not_wanted_image1.png | not_wanted_image2.png | not_wanted_image3.png |
         | Wait For Multiple Images | 900 | 10 | ${wanted_images} | ${not_wanted_images} |
        """
        args = [timeout, pollingInterval, expectedImages, notExpectedImages]
        return self.lib.run_keyword('waitForMultipleImages', args)

    def Wait_Until_Screen_Contain_Using_Image(self, image, timeout=10):
        """
        Wait until screen contain
         Wait until image shown in screen
        """
        args = [image, timeout]
        return self.lib.run_keyword('waitUntilScreenContain', args)

    def Wait_Until_Screen_Not_Contain_Using_Image(self, image, timeout=10):
        """
        Wait until screen not contain
         Wait until image not in screen
        """
        args = [image, timeout]
        return self.lib.run_keyword('waitUntilScreenNotContain', args)

    def Wheel_Down(self, steps, image=''):
        """
        Wheel down
         Move mouse to the target, and wheel down with give steps

         Examples:
         | Wheel Down     | 5   |
         | Wheel Down     | 5   |  test.png   |
        """
        args = [steps, image]
        return self.lib.run_keyword('wheelDown', args)

    def Wheel_Up(self, steps, image=''):
        """
        Wheel up
         Move mouse to the target, and wheel up with give steps

         Examples:
         | Wheel Up     | 5   |
         | Wheel Up     | 5   |  test.png   |
        """
        args = [steps, image]
        return self.lib.run_keyword('wheelUp', args)
