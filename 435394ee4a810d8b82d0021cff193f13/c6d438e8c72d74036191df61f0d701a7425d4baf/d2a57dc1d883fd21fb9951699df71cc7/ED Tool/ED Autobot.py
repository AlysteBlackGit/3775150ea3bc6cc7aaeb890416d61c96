from inspect import _void

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.color import Color

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import StaleElementReferenceException

from selenium.common.exceptions import NoSuchElementException

from selenium.common.exceptions import UnexpectedAlertPresentException

from selenium.common.exceptions import TimeoutException

from termcolor import colored

import datetime

import time

import os

# Login

UserAccount = "hB21DCCN399"

UserPassword = "12345"

Path = "C:\\Program Files (x86)\\Chrome Driver\\chromedriver.exe"


NewOptions = Options()

NewOptions.add_argument("use-fake-ui-for-media-stream")

driver = webdriver.Chrome(Path, options=NewOptions)

driver.maximize_window()

driver.get("https://ed.engdis.com/ptit#/")

WebDriverWait(driver, 7200).until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div/div/section/form/div/div[1]/div[1]/div[2]/input")))

driver.find_element(
    By.XPATH, "/html/body/div/div/section/form/div/div[1]/div[1]/div[2]/input").send_keys(UserAccount)

driver.find_element(By.NAME, "password").send_keys(UserPassword, Keys.ENTER)


# Preparing modules


class Explore:

    def WatchVideo() -> _void:

        driver.find_element(
            By.CSS_SELECTOR, ".layout__mediaPlayPause.layout__mediaPlayPause--play").click()

        time.sleep(0.5)

        driver.find_element(
            By.CSS_SELECTOR, ".layout__mediaPlayPause.layout__mediaPlayPause--pause").click()

    def ListenToParagraph() -> _void:

        driver.find_element(
            By.CSS_SELECTOR, ".CTrackerPlayBtnE.layout__mediaPlayPause.layout__mediaPlayPause--play").click()

        time.sleep(0.5)

        driver.find_element(
            By.CSS_SELECTOR, ".CTrackerStopBtnE.layout__mediaPlayPause.layout__mediaPlayPause--pause").click()


class Practice:

    class ChooseCorrectAns:

        def RadioQuestion() -> _void:

            TotalAnswers = driver.find_elements(By.CLASS_NAME, "layout__radio")

            NumberOfAnsPerQuest = 4

            for i in range(0, len(TotalAnswers), NumberOfAnsPerQuest):

                TotalAnswers[i].click()

                if i:
                    TotalAnswers[i].send_keys(Keys.PAGE_DOWN)

                    time.sleep(0.8)


        def CheckBoxQuestion() -> _void:

            TotalAnswers = driver.find_elements(
                By.CLASS_NAME, "layout__checkbox")

            NumberOfAnsPerQuest = 4

            for i in range(0, len(TotalAnswers), NumberOfAnsPerQuest):

                TotalAnswers[i].click()

                if i:
                    TotalAnswers[i].send_keys(Keys.PAGE_DOWN)

                    time.sleep(0.8)

    class DragIntoBlank:

        def dnditem_DragIntoBlank() -> _void:

            FirstItem = driver.find_element(
                By.CSS_SELECTOR, ".dnditem.draggable")

            FirstBlank = driver.find_element(By.CLASS_NAME, "dndZone")

            ActionChains(driver).drag_and_drop(FirstItem, FirstBlank).perform()

            time.sleep(0.3)

        def wordBankTile_DragIntoBlank() -> _void:

            FirstItem = driver.find_element(
                By.CSS_SELECTOR, ".draggable.wordBankTile")

            FirstBlank = driver.find_element(
                By.CSS_SELECTOR, ".TTpanswerDiv.droptarget")

            ActionChains(driver).drag_and_drop(FirstItem, FirstBlank).perform()

            time.sleep(0.3)

    def FillBlankQuestion() -> _void:

        FirstBlank = driver.find_element(By.CLASS_NAME, "DDLOptions__selected")

        FirstBlank.click()

        time.sleep(0.5)

        FirstItem = driver.find_element(By.CLASS_NAME, "DDLOptions__listItem")

        FirstItem.click()

    def SelectQuestion() -> _void:

        FirstSelection = driver.find_element(
            By.CLASS_NAME, "lessonMultipleCheck")

        FirstSelection.click()

    class TypeTextQuestion:

        def TypeAudioTextQuestion() -> _void:

            FirstAudioQuestion = driver.find_element(
                By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[2]/ng-component/div/div/div[1]/div/div[1]/div/div/div[2]/textarea")

            FirstAudioQuestion.send_keys("Random words")

            time.sleep(0.5)

        def RewriteSentence() -> _void:

            FirstSentence = driver.find_element(
                By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[2]/ng-component/div/div/div[1]/div/div/div/div/div[1]/div/input")

            time.sleep(0.5)

            FirstSentence.send_keys("Hello, Worlds!")

            time.sleep(1)

        def TypeParagraph() -> _void:

            time.sleep(4)

            PopupWindow = True

            try:

                driver.find_element(By.CLASS_NAME, "utils__BSCancelBtnW")

            except NoSuchElementException:

                PopupWindow = False

            if PopupWindow:

                driver.find_element(
                    By.CSS_SELECTOR, ".utils__cancelLInk.utils__BSCancelBtn").click()

        def IntegratedWriting() -> _void:

            FirstBlank = driver.find_element(
                By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[1]/div[2]/div/div/div[3]/div/div[2]/p[1]/input[1]")

            FirstBlank.send_keys("Hello, Worlds!")

            time.sleep(0.5)

    def RerangeType() -> _void:

        AllItems = driver.find_elements(By.CSS_SELECTOR, ".dnditem.draggable")

        ActionChains(driver).drag_and_drop(AllItems[0], AllItems[1]).perform()

    class AudioQuestion:

        def AudioQuestionNormal() -> _void:

            time.sleep(5)

            driver.find_element(
                By.CSS_SELECTOR, ".button.continue").click()

        def AudioQuestionCharacter() -> _void:

            time.sleep(4)

            driver.find_element(By.CLASS_NAME, "chooseCaracterArrow").click()

            time.sleep(0.5)

            driver.find_element(By.CSS_SELECTOR, ".button.continue").click()

    def RerangePictures() -> _void:

        time.sleep(2.5)

        AllItems = driver.find_elements(By.CLASS_NAME, "dnditemImage")

        ActionChains(driver).drag_and_drop(AllItems[0], AllItems[1]).perform()

    def SelectSentence() -> _void:

        try:

            driver.find_element(
                By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/p[4]/span[2]/span").click()

        except NoSuchElementException:

            try:

                driver.find_element(
                    By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[1]/div/div/div/div/div/div/div[2]/div[1]/span[1]/span/span").click()

            except NoSuchElementException:

                pass

        time.sleep(0.5)

    def Speaking() -> _void:

        time.sleep(5)

        driver.find_element(
            By.CSS_SELECTOR, ".openSpeech__btn.openSpeech__btnStart").click()

        time.sleep(1)

        driver.find_element(
            By.CSS_SELECTOR, ".openSpeech__btn.openSpeech__btnSkip").click()

        time.sleep(0.5)

        driver.find_element(
            By.CSS_SELECTOR, ".openSpeech__btn.openSpeech__btnStop").click()

        driver.find_element(
            By.CSS_SELECTOR, ".openSpeech__btn.openSpeech__SentTTBtn").click()

        WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".okButton.utils__BSOKBtn")))

        driver.find_element(
            By.CSS_SELECTOR, ".okButton.utils__BSOKBtn").click()

        time.sleep(1)


class Test:

    def PassAway() -> _void:

        driver.find_element(
            By.CLASS_NAME, "learning__taskNavPagerCounterIW").click()

        time.sleep(1)

        driver.find_element(
            By.XPATH, "/html/body/app/div/div/ed-la-tasksmenu/div/div[2]/span").click()

        time.sleep(2)

        try:

            Window = driver.find_element(By.XPATH, "/html/body/div[10]/iframe")

            driver.switch_to.frame(Window)

        except NoSuchElementException:

            try:

                Window = driver.find_element(By.XPATH, "/html/body/div[12]/iframe")

                driver.switch_to.frame(Window)

            except NoSuchElementException:

                WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[8]/iframe")))

                driver.switch_to.frame(driver.find_element(
                    By.XPATH, "/html/body/div[8]/iframe"))

        print("SWITCHED SUCCESS")

        WebDriverWait(driver, 7200).until(
            EC.presence_of_element_located((By.NAME, "btnOk")))

        driver.find_element(By.NAME, "btnOk").click()

        WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".learning__pnItemLink.learning__testReviewLink")))

        driver.find_element(
            By.CSS_SELECTOR, ".learning__pnItemLink.learning__testReviewLink").click()

        time.sleep(1)

    class GetAnswer:

        class ChooseCorrectAnsQuestions:

            def ChooseCorrectAns() -> list:

                ExtractAns = driver.find_elements(
                    By.CSS_SELECTOR, ".multiRadio.correct")

                FinalExtractAns = []

                for item in ExtractAns:

                    FinalExtractAns.append(item.text)

                return FinalExtractAns

            def CheckBoxAns() -> list:

                driver.find_element(
                    By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-testresulttools/div/ul/li[2]").click()

                ExtractAns = driver.find_elements(
                    By.CSS_SELECTOR, ".multiRadio.correct")

                FinalExtractAns = []

                for item in ExtractAns:

                    FinalExtractAns.append(item.text)

                return FinalExtractAns

        class DragCorrectAns:

            def dnditem_DragCorrectAns() -> list:

                BlankSpaces = driver.find_elements(By.CLASS_NAME, "dndZone")

                if len(BlankSpaces) > 0:

                    BlankSpaces.pop()

                driver.find_element(
                    By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-testresulttools/div/ul/li[2]/a").click()

                ExtractAns = driver.find_elements(By.CLASS_NAME, "dnditem")

                ExtractAns = ExtractAns[:len(BlankSpaces)]

                FinalExtractAns = []

                for item in ExtractAns:

                    FinalExtractAns.append(item.text)

                return FinalExtractAns

            def wordBankTile_DragCorrectAns() -> list:

                driver.find_element(
                    By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[1]/div[1]/ul/li[2]/a").click()

                ExtractAns = driver.find_elements(
                    By.CSS_SELECTOR, ".TTpanswerDiv.droptarget.noLine")

                FinalExtractAns = []

                for item in ExtractAns:

                    FinalExtractAns.append(item.get_attribute("ans"))

                return FinalExtractAns

            def dnditem_DragToManyColumns() -> list:

                driver.find_element(
                    By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-testresulttools/div/ul/li[2]").click()

                ExtractAns = driver.find_elements(By.CLASS_NAME, "dnditem")

                FinalExtractAns = []

                for item in ExtractAns:

                    FinalExtractAns.append(item.get_attribute("ans_id"))

                return FinalExtractAns

        def FillBlank() -> list:

            driver.find_element(
                By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-testresulttools/div/ul/li[2]/a").click()

            time.sleep(0.3)

            ExtractAns = driver.find_elements(
                By.CLASS_NAME, "DDLOptions__selected")

            FinalExtractAns = []

            for item in ExtractAns:

                FinalExtractAns.append(item.text)

            return FinalExtractAns


        def RerangeQuestion() -> list:

            driver.find_element(
                By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-testresulttools/div/ul/li[2]/a").click()

    
            time.sleep(0.3)

            ExtractAns = driver.find_elements(By.CLASS_NAME, "dnditem")

            FinalExtractAns = []

            for item in ExtractAns:

                FinalExtractAns.append(item.text)

            return FinalExtractAns

    
    class DragCorrectAns:

        def dnditem_DragCorrectAns(Ans: list) -> _void:

            BlankSpaces = driver.find_elements(By.CLASS_NAME, "dndZone")

            BlankSpaces.pop()

            for i in range(len(BlankSpaces)):

                ItemsList = driver.find_elements(
                    By.CSS_SELECTOR, ".dnditem.draggable")

                time.sleep(0.3)

                for item in ItemsList:

                    if item.text == Ans[i]:

                        ActionChains(driver).drag_and_drop(
                            item, BlankSpaces[i]).perform()

                time.sleep(0.5)

        def wordBankTile_DragCorrectAns(Ans: list) -> _void:

            BlankSpaces = driver.find_elements(
                By.CSS_SELECTOR, ".TTpanswerDiv.droptarget")

            for i in range(len(BlankSpaces)):

                ItemsList = driver.find_elements(
                    By.CSS_SELECTOR, ".draggable.wordBankTile")

                for item in ItemsList:

                    if item.get_attribute("data-id") == Ans[i]:

                        ActionChains(driver).drag_and_drop(
                            item, BlankSpaces[i]).perform()

                        time.sleep(1)

                        break

        def dnditem_DragToManyColumns(Ans: list) -> _void:

            Column = driver.find_elements(By.CLASS_NAME, "dndZone")

            Column.pop()

            ItemsPerCol = int(len(driver.find_elements(
                By.CSS_SELECTOR, ".dnditem.draggable")) / len(Column))

            for i in range(len(Ans)):

                ItemsList = driver.find_elements(
                    By.CSS_SELECTOR, ".dnditem.draggable")

                for item in ItemsList:

                    if item.get_attribute("ans_id") == Ans[i]:

                        ActionChains(driver).drag_and_drop(
                            item, Column[int(i/ItemsPerCol)]).perform()


    def ChooseCorrectAns(Ans: list) -> _void:

        ItemsList = driver.find_elements(By.CLASS_NAME, "multiRadio")

        for i in range(len(Ans)):

            for item in ItemsList:

                if item.text == Ans[i]:

                    item.click()

                    time.sleep(0.5)

    def FillBlank(Ans: list) -> _void:

        Blanks = driver.find_elements(By.CLASS_NAME, "DDLOptions__selected")

        for i in range(len(Blanks)):

            Blanks[i].click()

            time.sleep(1)

            SubAns = driver.find_elements(
                By.CLASS_NAME, "DDLOptions__listItem")

            for ans in SubAns:

                if ans.text == Ans[i]:

                    ans.click()

                    break

            time.sleep(0.5)

    
    def RerangeQuestion(Ans: list) -> _void:

         Blanks = driver.find_elements(By.CLASS_NAME, "sequenceZone")

         for i in range(len(Blanks)):

            ItemsList = driver.find_elements(By.CSS_SELECTOR, ".dnditem.draggable")

            for item in ItemsList:

                if item.get_attribute("ans_id") == Ans[i]:

                     ActionChains(driver).drag_and_drop(item, Blanks[i]).perform()

                     time.sleep(0.5)

                     break

class Other:

    def CrossAway() -> _void:

        while True:

            time.sleep(1.5)

            isRadioQuestion = True

            isCheckBoxQuestion = True

            iswordBankTile_DragIntoBlank = True

            isdnditem_DragIntoBlank = True

            isFillBlankQuestion = True

            isSelectQuestion = True

            isTypeAudioTextQuestion = True

            isRewriteSentence = True

            isRerangeType = True

            isRerangePictures = True

            isAudioQuestionNormal = True

            isAudioQuestionCharacter = True

            isSelectSentenceQuestion = True

            isTypeParagraph = True

            isIntegratedWriting = True

            isSpeaking = True

            try:

                driver.find_element(By.CLASS_NAME, "layout__radio")

            except NoSuchElementException:

                isRadioQuestion = False

            try:

                driver.find_element(By.CLASS_NAME, "layout__checkbox")

            except NoSuchElementException:

                isCheckBoxQuestion = False

            try:

                driver.find_element(By.CSS_SELECTOR, ".draggable.wordBankTile")

            except NoSuchElementException:

                iswordBankTile_DragIntoBlank = False

            try:

                driver.find_element(By.CSS_SELECTOR, ".dnditem.draggable")

            except NoSuchElementException:

                isdnditem_DragIntoBlank = False

            try:

                driver.find_element(By.CLASS_NAME, "DDLOptions__selected")

            except NoSuchElementException:

                isFillBlankQuestion = False

            try:

                driver.find_element(By.NAME, "r1")

            except NoSuchElementException:

                isSelectQuestion = False

            try:

                driver.find_element(
                    By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[2]/ng-component/div/div/div[1]/div/div[1]/div/div/div[2]/textarea")

            except NoSuchElementException:

                isTypeAudioTextQuestion = False

            try:

                driver.find_element(By.CSS_SELECTOR, ".button.continue")

            except NoSuchElementException:

                isAudioQuestionNormal = False


            try:

                driver.find_element(By.CLASS_NAME, "chooseCaracterArrow")

                isAudioQuestionNormal = False

            except NoSuchElementException:

                isAudioQuestionCharacter = False

            try:

                driver.find_element(By.CSS_SELECTOR, ".mceIcon.mce_undo_")

            except NoSuchElementException:

                isTypeParagraph = False

            try:

                driver.find_element(By.CLASS_NAME, "dnditemImage")

                isdnditem_DragIntoBlank = False

            except NoSuchElementException:

                isRerangePictures = False

            try:

                driver.find_element(
                    By.CSS_SELECTOR, ".containerHeader.containerHeader--txt.header--x")

                isdnditem_DragIntoBlank = False

            except NoSuchElementException:

                isRerangeType = False

            try:

                driver.find_element(
                    By.CLASS_NAME, "prOpenEnded__qaItem_inputW")

            except NoSuchElementException:

                isRewriteSentence = False

            try:

                driver.find_element(By.CLASS_NAME, "unSegment")

            except NoSuchElementException:

                isSelectSentenceQuestion = False

            try:

                driver.find_element(
                    By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[1]/div[2]/div/div/div[3]/div/div[2]/p[1]/input[1]")

            except NoSuchElementException:

                isIntegratedWriting = False

            try:

                driver.find_element(
                    By.CSS_SELECTOR, ".openSpeech__btn.openSpeech__btnStart")

            except NoSuchElementException:

                isSpeaking = False

            if isRadioQuestion:
                Practice.ChooseCorrectAns.RadioQuestion()

            elif isCheckBoxQuestion:
                Practice.ChooseCorrectAns.CheckBoxQuestion()

            elif isRerangePictures:
                Practice.RerangePictures()

            elif isRerangeType:
                Practice.RerangeType()

            elif iswordBankTile_DragIntoBlank:
                Practice.DragIntoBlank.wordBankTile_DragIntoBlank()

            elif isdnditem_DragIntoBlank:
                Practice.DragIntoBlank.dnditem_DragIntoBlank()

            elif isFillBlankQuestion:
                Practice.FillBlankQuestion()

            elif isSelectQuestion:
                Practice.SelectQuestion()

            elif isTypeAudioTextQuestion:
                Practice.TypeTextQuestion.TypeAudioTextQuestion()

            elif isTypeParagraph:
                Practice.TypeTextQuestion.TypeParagraph()

            elif isAudioQuestionNormal:
                Practice.AudioQuestion.AudioQuestionNormal()

            elif isAudioQuestionCharacter:
                Practice.AudioQuestion.AudioQuestionCharacter()

            elif isRewriteSentence:
                Practice.TypeTextQuestion.RewriteSentence()

            elif isSelectSentenceQuestion:
                Practice.SelectSentence()

            elif isIntegratedWriting:
                Practice.TypeTextQuestion.IntegratedWriting()

            elif isSpeaking:
                Practice.Speaking()

            CurrentTask = driver.find_element(
                By.XPATH, "/html/body/app/div/div/div[4]/div[3]/div[4]/ed-la-tasksnav/div/div/span[1]").text

            TotalTasks = driver.find_element(
                By.XPATH, "/html/body/app/div/div/div[4]/div[3]/div[4]/ed-la-tasksnav/div/div/span[2]").text

            if CurrentTask == TotalTasks:

                driver.find_element(
                    By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                time.sleep(1)

                break

            else:

                driver.find_element(
                    By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

    def Test(UnitNumber: int, Lesson: int) -> _void:

        WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".layout__roundBtn.layout__action.btnStartTest")))

        driver.find_element(
            By.CSS_SELECTOR, ".layout__roundBtn.layout__action.btnStartTest").click()

        time.sleep(1.3)

        Test.PassAway()

        Key = []

        while True:

            isradioquestion_ChooseCorrectAns = True

            ischeckboxquestion_ChooseCorrectAns = True

            iswordBankTile_DragCorrectAns = True

            isdnditem_DragCorrectAns = True

            isRerange = True

            isFillBlank = True

            isdnditem_DragToManyColumns = True

            try:

                driver.find_element(By.CLASS_NAME, "layout__radio")

            except NoSuchElementException:

                isradioquestion_ChooseCorrectAns = False

            try:

                driver.find_element(By.CLASS_NAME, "layout__checkbox")

            except NoSuchElementException:

                ischeckboxquestion_ChooseCorrectAns = False

            try:

                driver.find_element(By.CLASS_NAME, "dnditem")

            except NoSuchElementException:

                isdnditem_DragCorrectAns = False

            try:

                driver.find_element(
                    By.CSS_SELECTOR, ".draggable.wordBankTile")

            except NoSuchElementException:

                iswordBankTile_DragCorrectAns = False

            try:

                driver.find_element(
                    By.CLASS_NAME, "DDLOptions__selected")

            except NoSuchElementException:

                isFillBlank = False

            try:

                driver.find_element(By.CLASS_NAME, "containerHeader")

                try:

                    driver.find_element(By.CLASS_NAME, "prMT_T2T__answersText")

                    isdnditem_DragToManyColumns = False

                except NoSuchElementException:

                    isdnditem_DragCorrectAns = False

                    iswordBankTile_DragCorrectAns = False

            except NoSuchElementException:

                isdnditem_DragToManyColumns = False

            try: 

                driver.find_element(By.CSS_SELECTOR, ".containerHeader.containerHeader--txt.header--x")

                isdnditem_DragCorrectAns = False

                isdnditem_DragToManyColumns = False

                iswordBankTile_DragCorrectAns = False

            except NoSuchElementException:

                isRerange = False


            if isradioquestion_ChooseCorrectAns:
                Key.append(
                    Test.GetAnswer.ChooseCorrectAnsQuestions.ChooseCorrectAns())

            elif ischeckboxquestion_ChooseCorrectAns:
                Key.append(
                    Test.GetAnswer.ChooseCorrectAnsQuestions.CheckBoxAns())

            elif iswordBankTile_DragCorrectAns:
                Key.append(
                    Test.GetAnswer.DragCorrectAns.wordBankTile_DragCorrectAns())

            elif isdnditem_DragCorrectAns:
                Key.append(
                    Test.GetAnswer.DragCorrectAns.dnditem_DragCorrectAns())

            elif isFillBlank:
                Key.append(Test.GetAnswer.FillBlank())

            elif isdnditem_DragToManyColumns:
                Key.append(
                    Test.GetAnswer.DragCorrectAns.dnditem_DragToManyColumns())

            elif isRerange:
                Key.append(Test.GetAnswer.RerangeQuestion())


            CurrentTask = driver.find_element(
                By.CLASS_NAME, "learning__taskNavPCCurrentTask").text

            TotalTasks = driver.find_element(
                By.CLASS_NAME, "learning__taskNavPCTotalTasks").text

            if CurrentTask == TotalTasks:

                print(
                    "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

                driver.find_element(
                    By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                time.sleep(0.7)

                PopupNotification = True

                try:

                    driver.find_element(By.CSS_SELECTOR, ".okButton.utils__BSOKBtn")

                except NoSuchElementException:

                    PopupNotification = False

                if PopupNotification:

                    driver.find_element(By.CSS_SELECTOR, ".okButton.utils__BSOKBtn").click()

                    time.sleep(0.3)

                    driver.find_element(By.CLASS_NAME, "learning__tasksPager").click()

                    time.sleep(0.3)

                    driver.find_element(By.CSS_SELECTOR, ".learning__tasksNav_task.learning__tasksNav_task--done").click()

                    time.sleep(0.7)

                    driver.find_element(By.CSS_SELECTOR, ".tasksBtprev.learning__pnItemLink.learning__prevItemLink").click()

                    WebDriverWait(driver, 7200).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink")))

                    driver.find_element(By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()
    
             
                else:

                    while True:

                        time.sleep(0.7)

                        driver.find_element(
                            By.CSS_SELECTOR, ".tasksBtprev.learning__pnItemLink.learning__prevItemLink").click()

                        try:

                            driver.find_element(
                                By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[1]/a")

                            break

                        except NoSuchElementException:

                            pass

                print("DONEEEEEEEEEEEEEEEEEEE")

                break

            else:

                driver.find_element(
                    By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                time.sleep(1)

        WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[1]/a")))

        driver.find_element(
            By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[1]/a").click()   

        time.sleep(0.5)

        for sub_ans in Key:

            try:

                print("CONTINUEEEEEEEE")

            except UnexpectedAlertPresentException:

                print("ALERTTTTTTTTTTTTTTT")

            pass

            print(sub_ans)

            isradioquestion_ChooseCorrectAns = True

            ischeckboxquestion_ChooseCorrectAns = True

            iswordBankTile_DragCorrectAns = True

            isdnditem_DragCorrectAns = True

            isFillBlank = True

            isRerange = True

            isdnditem_DragToManyColumns = True

            try:

                driver.find_element(By.CLASS_NAME, "layout__radio")

            except NoSuchElementException:

                isradioquestion_ChooseCorrectAns = False

            try:

                driver.find_element(By.CLASS_NAME, "layout__checkbox")

            except NoSuchElementException:

                ischeckboxquestion_ChooseCorrectAns = False

            try:

                driver.find_element(
                    By.CSS_SELECTOR, ".dnditem.draggable")

            except NoSuchElementException:

                isdnditem_DragCorrectAns = False

            try:

                driver.find_element(
                    By.CSS_SELECTOR, ".draggable.wordBankTile")

            except NoSuchElementException:

                iswordBankTile_DragCorrectAns = False

            try:

                driver.find_element(
                    By.CLASS_NAME, "DDLOptions__selected")

            except NoSuchElementException:

                isFillBlank = False

            try:

                driver.find_element(By.CLASS_NAME, "containerHeader")

                try:

                    driver.find_element(
                        By.CLASS_NAME, "prMT_T2T__answersText")

                    isdnditem_DragToManyColumns = False

                except NoSuchElementException:

                    isdnditem_DragCorrectAns = False

                    iswordBankTile_DragCorrectAns = False

            except NoSuchElementException:

                isdnditem_DragToManyColumns = False

            try:

                driver.find_element(By.CSS_SELECTOR, ".containerHeader.containerHeader--txt.header--x")

                isdnditem_DragCorrectAns = False

                isdnditem_DragToManyColumns = False

                iswordBankTile_DragCorrectAns = False

            except NoSuchElementException:

                isRerange = False


            if isradioquestion_ChooseCorrectAns:
                Test.ChooseCorrectAns(sub_ans)

            elif ischeckboxquestion_ChooseCorrectAns:
                Test.ChooseCorrectAns(sub_ans)

            elif iswordBankTile_DragCorrectAns:
                Test.DragCorrectAns.wordBankTile_DragCorrectAns(sub_ans)

            elif isdnditem_DragCorrectAns:
                Test.DragCorrectAns.dnditem_DragCorrectAns(sub_ans)

            elif isFillBlank:
                Test.FillBlank(sub_ans)

            elif isdnditem_DragToManyColumns:
                Test.DragCorrectAns.dnditem_DragToManyColumns(sub_ans)

            elif isRerange:
                Test.RerangeQuestion(sub_ans)


            CurrentTask = driver.find_element(
                By.CLASS_NAME, "learning__taskNavPCCurrentTask").text

            TotalTasks = driver.find_element(
                By.CLASS_NAME, "learning__taskNavPCTotalTasks").text

            if CurrentTask == TotalTasks:

                driver.find_element(
                    By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__submitTestLink").click()

                WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[1]/div[2]/div/div/div[1]/div[2]/div/div[2]")))

                if UnitNumber == 9 and Lesson == 6:

                    print("ENDDDDDDDDDDDDDDDDD")

                    driver.get("https://ed.engdis.com/ptit#/home")

                    WebDriverWait(driver, 7200).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "home__details")))

                    driver.find_element(By.CSS_SELECTOR, ".glyphicon.glyphicon-chevron-right").click()

                    time.sleep(0.5)

                    driver.find_element(By.CLASS_NAME, "home__details").click()

                    driver.find_element(By.CLASS_NAME, "home__courseListItemLink").click()

                    WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink")))

                else:

                    driver.find_element(
                        By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                    time.sleep(0.5)

                break

            else:

                driver.find_element(
                    By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                time.sleep(1)

                # Interact


WebDriverWait(driver, 7200).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "home__details")))


# driver.find_element(By.CSS_SELECTOR, ".glyphicon.glyphicon-chevron-right").click()

# time.sleep(1)


# driver.find_element(
#     By.CSS_SELECTOR, ".glyphicon.glyphicon-chevron-right").click()

# time.sleep(1)

Tasks = driver.find_elements(By.CLASS_NAME, "home__details")

UnitNumber = 0

DirectNumber = 2

Tasks[UnitNumber].click()

driver.find_element(By.CLASS_NAME, "home__courseListItemLink").click()

WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink")))

# driver.find_element(
#     By.XPATH, "/html/body/app/div/div/div[1]/ed-la-dropdownlist[2]/section[1]/div[2]").click()

# time.sleep(0.5)

# driver.find_element(
#     By.XPATH, "/html/body/app/div/div/div[1]/ed-la-dropdownlist[2]/section[2]/div/div/div[1]/div[1]   /div[1]/div").click()

# WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
#     (By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink")))


# Pick up lesson in unit

driver.find_element(
    By.XPATH, "/html/body/app/div/div/div[1]/ed-la-dropdownlist[1]/section[1]/div[2]").click()

time.sleep(1)

driver.find_element(
    By.XPATH, f"/html/body/app/div/div/div[1]/ed-la-dropdownlist[1]/section[2]/div[2]/div/div[1]/div[{DirectNumber}]/div[1]/div").click()

WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink")))

# Into that lesson, pick up path

driver.find_element(
    By.XPATH, "/html/body/app/div/div/div[1]/ed-la-dropdownlist[2]/section[1]/div[2]").click()

time.sleep(1)

driver.find_element(
    By.XPATH, "/html/body/app/div/div/div[1]/ed-la-dropdownlist[2]/section[2]/div/div/div[1]/div[1]/div[1]/div").click()


Explore_mode = True

Practice_mode = True

Test_mode = True

while True:

    print(colored(f"Current Unit: {UnitNumber + 1}", "green", "on_green"))

    print(colored(f"Lesson: {DirectNumber}", "red", "on_red"))

    time.sleep(1)

    if UnitNumber == 8 or UnitNumber == 9:

        DirectNumber = 0

        StepLesson = 1

        while StepLesson <= 6:

            time.sleep(1)

            StepIndex = 1   

            driver.find_element(
                By.XPATH, "/html/body/app/div/div/div[1]/ed-la-dropdownlist[2]/section[1]/div[2]").click()

            time.sleep(0.5)

            StepsCount = int(len(driver.find_elements(
                By.CLASS_NAME, "learning__dropDownList_itemNameText"))) - 6

            driver.find_element(
            By.XPATH, f"/html/body/app/div/div/div[1]/ed-la-dropdownlist[2]/section[2]/div/div/div[1]/div[{StepIndex}]/div[1]/div").click()

            time.sleep(1)

            while StepIndex <= StepsCount:

                time.sleep(1)

                if StepIndex != StepsCount:

                    driver.find_element(
                        By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                    Other.CrossAway()

                else:

                    Other.Test(UnitNumber, StepLesson)

                StepIndex += 1

            StepLesson += 1

        UnitNumber += 1

        if UnitNumber == 10: UnitNumber = 0

    else:

        while Explore_mode:

            time.sleep(2)

            isWatchVideo = True

            isListenToParagraph = True

            try:

                driver.find_element(
                    By.CSS_SELECTOR, ".layout__mediaPlayPause.layout__mediaPlayPause--play")

            except NoSuchElementException:

                isWatchVideo = False

            try:

                driver.find_element(
                    By.CSS_SELECTOR, ".layout__mediaPlayPause.layout__mediaPlayPause--play.CTrackerPlayBtnD")

            except NoSuchElementException:

                isListenToParagraph = False

            if isWatchVideo:
                Explore.WatchVideo()

            elif isListenToParagraph:
                Explore.ListenToParagraph()

            CurrentTask = driver.find_elements(
                By.XPATH, "/html/body/app/div/div/div[4]/div[3]/div[4]/ed-la-tasksnav/div/div/span[1]")

            if (len(CurrentTask)):

                TotalTasks = driver.find_element(
                    By.XPATH, "/html/body/app/div/div/div[4]/div[3]/div[4]/ed-la-tasksnav/div/div/span[2]").text

                if CurrentTask[0].text == TotalTasks:

                    driver.find_element(
                        By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                    WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink")))

                    time.sleep(1)

                    break

                else:

                    driver.find_element(
                        By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                    time.sleep(1)

            else:

                driver.find_element(
                    By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                time.sleep(0.3)

        while Practice_mode:

            driver.find_element(
                By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

            time.sleep(0.7)

            isRadioQuestion = True

            isCheckBoxQuestion = True

            iswordBankTile_DragIntoBlank = True

            isdnditem_DragIntoBlank = True

            isFillBlankQuestion = True

            isSelectQuestion = True

            isTypeAudioTextQuestion = True

            isRewriteSentence = True

            isRerangeType = True

            isRerangePictures = True

            isAudioQuestionNormal = True

            isAudioQuestionCharacter = True

            isSelectSentenceQuestion = True

            isTypeParagraph = True

            isIntegratedWriting = True

            isSpeaking = True

            try:

                driver.find_element(By.CLASS_NAME, "layout__radio")

            except NoSuchElementException:

                isRadioQuestion = False

            try:

                driver.find_element(By.CLASS_NAME, "layout__checkbox")

            except NoSuchElementException:

                isCheckBoxQuestion = False

            try:

                driver.find_element(By.CSS_SELECTOR, ".draggable.wordBankTile")

            except NoSuchElementException:

                iswordBankTile_DragIntoBlank = False

            try:

                driver.find_element(By.CSS_SELECTOR, ".dnditem.draggable")

            except NoSuchElementException:

                isdnditem_DragIntoBlank = False

            try:

                driver.find_element(By.CLASS_NAME, "DDLOptions__selected")

            except NoSuchElementException:

                isFillBlankQuestion = False

            try:

                driver.find_element(By.NAME, "r1")

            except NoSuchElementException:

                isSelectQuestion = False

            try:

                driver.find_element(
                    By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[2]/ng-component/div/div/div[1]/div/div[1]/div/div/div[2]/textarea")

            except NoSuchElementException:

                isTypeAudioTextQuestion = False

            try:

                driver.find_element(By.CSS_SELECTOR, ".button.continue")

            except NoSuchElementException:

                isAudioQuestionNormal = False

            try:

                driver.find_element(By.CLASS_NAME, "chooseCaracterArrow")

                isAudioQuestionNormal = False

            except NoSuchElementException:

                isAudioQuestionCharacter = False

            try:

                driver.find_element(By.CSS_SELECTOR, ".mceIcon.mce_undo_")

            except NoSuchElementException:

                isTypeParagraph = False

            try:

                driver.find_element(By.CLASS_NAME, "dnditemImage")

                isdnditem_DragIntoBlank = False

            except NoSuchElementException:

                isRerangePictures = False

            try:

                driver.find_element(
                    By.CSS_SELECTOR, ".containerHeader.containerHeader--txt.header--x")

                isdnditem_DragIntoBlank = False

            except NoSuchElementException:

                isRerangeType = False

            try:

                driver.find_element(
                    By.CLASS_NAME, "prOpenEnded__qaItem_inputW")

            except NoSuchElementException:

                isRewriteSentence = False

            try:

                driver.find_element(By.CLASS_NAME, "unSegment")

            except NoSuchElementException:

                isSelectSentenceQuestion = False

            try:

                driver.find_element(
                    By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[1]/div[2]/div/div/div[3]/div/div[2]/p[1]/input[1]")

            except NoSuchElementException:

                isIntegratedWriting = False

            try:

                driver.find_element(
                    By.CSS_SELECTOR, ".openSpeech__btn.openSpeech__btnStart")

            except NoSuchElementException:

                isSpeaking = False

            if isRadioQuestion:
                Practice.ChooseCorrectAns.RadioQuestion()

            elif isCheckBoxQuestion:
                Practice.ChooseCorrectAns.CheckBoxQuestion()

            elif isRerangePictures:
                Practice.RerangePictures()

            elif isRerangeType:
                Practice.RerangeType()

            elif iswordBankTile_DragIntoBlank:
                Practice.DragIntoBlank.wordBankTile_DragIntoBlank()

            elif isdnditem_DragIntoBlank:
                Practice.DragIntoBlank.dnditem_DragIntoBlank()

            elif isFillBlankQuestion:
                Practice.FillBlankQuestion()

            elif isSelectQuestion:
                Practice.SelectQuestion()

            elif isTypeAudioTextQuestion:
                Practice.TypeTextQuestion.TypeAudioTextQuestion()

            elif isTypeParagraph:
                Practice.TypeTextQuestion.TypeParagraph()

            elif isAudioQuestionNormal:
                Practice.AudioQuestion.AudioQuestionNormal()

            elif isAudioQuestionCharacter:
                Practice.AudioQuestion.AudioQuestionCharacter()

            elif isRewriteSentence:
                Practice.TypeTextQuestion.RewriteSentence()

            elif isSelectSentenceQuestion:
                Practice.SelectSentence()

            elif isIntegratedWriting:
                Practice.TypeTextQuestion.IntegratedWriting()

            elif isSpeaking:
                Practice.Speaking()

            CurrentTask = driver.find_element(
                By.XPATH, "/html/body/app/div/div/div[4]/div[3]/div[4]/ed-la-tasksnav/div/div/span[1]").text

            TotalTasks = driver.find_element(
                By.XPATH, "/html/body/app/div/div/div[4]/div[3]/div[4]/ed-la-tasksnav/div/div/span[2]").text

            if CurrentTask == TotalTasks:

                driver.find_element(
                    By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                time.sleep(1)

                break

        while Test_mode:

            time.sleep(1)

            isTest = True

            isInteract_1 = True

            isInteract_2 = True

            try:

                driver.find_element(
                    By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[1]/a")

            except NoSuchElementException:

                isTest = False

            try:

                Message = driver.find_element(
                    By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[1]/div[1]/div").text

                Message = Message.strip()

                if Message != "Take part in the conversation. Select the speaker you would like to practice.":

                    isInteract_1 = False

            except NoSuchElementException:

                isInteract_1 = False

            try:

                Message = driver.find_element(
                    By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[1]/div[1]/div").text

                Message = Message.strip()

                if Message != "Take part in a branching conversation. Choose your response and see how the conversation develops.":

                    isInteract_2 = False

            except NoSuchElementException:

                isInteract_2 = False

            if isTest:

                driver.find_element(
                    By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[1]/a").click()

                time.sleep(1)

                Test.PassAway()

                Key = []

                while True:

                    isChooseCorrectAns = True

                    iswordBankTile_DragCorrectAns = True

                    isdnditem_DragCorrectAns = True

                    isFillBlank = True

                    try:

                        driver.find_element(By.CLASS_NAME, "layout__radio")

                    except NoSuchElementException:

                        isChooseCorrectAns = False

                    try:

                        driver.find_element(By.CLASS_NAME, "dnditem")

                    except NoSuchElementException:

                        isdnditem_DragCorrectAns = False

                    try:

                        driver.find_element(
                            By.CSS_SELECTOR, ".draggable.wordBankTile")

                    except NoSuchElementException:

                        iswordBankTile_DragCorrectAns = False

                    try:

                        driver.find_element(
                            By.CLASS_NAME, "DDLOptions__selected")

                    except NoSuchElementException:

                        isFillBlank = False

                    if isChooseCorrectAns:
                        Key.append(
                            Test.GetAnswer.ChooseCorrectAnsQuestions.ChooseCorrectAns())

                    elif iswordBankTile_DragCorrectAns:
                        Key.append(
                            Test.GetAnswer.DragCorrectAns.wordBankTile_DragCorrectAns())

                    elif isdnditem_DragCorrectAns:
                        Key.append(
                            Test.GetAnswer.DragCorrectAns.dnditem_DragCorrectAns())

                    elif isFillBlank:
                        Key.append(Test.GetAnswer.FillBlank())

                    CurrentTask = driver.find_element(
                        By.CLASS_NAME, "learning__taskNavPCCurrentTask").text

                    TotalTasks = driver.find_element(
                        By.CLASS_NAME, "learning__taskNavPCTotalTasks").text

                    if CurrentTask == TotalTasks:

                        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

                        driver.find_element(
                            By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                        time.sleep(1)

                        PopupNotification = True

                        try:

                            driver.find_element(By.CSS_SELECTOR, ".modal-dialog.modal-lg")

                        except NoSuchElementException:

                            PopupNotification = False

                        if PopupNotification:

                            driver.find_element(
                                By.CLASS_NAME, "okButton utils__BSOKBtn").click()

                            time.sleep(0.3)

                            driver.find_element(
                                By.CLASS_NAME, "learning__tasksPager").click()

                            time.sleep(0.3)

                            driver.find_element(
                                By.CSS_SELECTOR, ".learning__tasksNav_task.learning__tasksNav_task--done").click()

                            time.sleep(0.7)

                            driver.find_element(
                                By.CSS_SELECTOR, ".tasksBtprev.learning__pnItemLink.learning__prevItemLink").click()

                            WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
                                (By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink")))

                            driver.find_element(
                                By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                        else:

                            while True:

                                time.sleep(0.7)

                                driver.find_element(
                                    By.CSS_SELECTOR, ".tasksBtprev.learning__pnItemLink.learning__prevItemLink").click()


                                try:

                                    driver.find_element(
                                        By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[1]/a")

                                    break

                                except NoSuchElementException:

                                    pass
                        
                        print("DONEEEEEEEEEEEEEEEEEEE")

                        break

                    else:

                        driver.find_element(By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                        time.sleep(0.7)



                WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[1]/a")))

                driver.find_element(
                    By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[1]/a").click()

                time.sleep(1)

                for sub_ans in Key:

                    print(sub_ans)

                    time.sleep(0.5)

                    isChooseCorrectAns = True

                    iswordBankTile_DragCorrectAns = True

                    isdnditem_DragCorrectAns = True

                    isFillBlank = True

                    try:

                        driver.find_element(By.CLASS_NAME, "layout__radio")

                    except NoSuchElementException:

                        isChooseCorrectAns = False

                    try:

                        driver.find_element(
                            By.CSS_SELECTOR, ".dnditem.draggable")

                    except NoSuchElementException:

                        isdnditem_DragCorrectAns = False

                    try:

                        driver.find_element(
                            By.CSS_SELECTOR, ".draggable.wordBankTile")

                    except NoSuchElementException:

                        iswordBankTile_DragCorrectAns = False

                    try:

                        driver.find_element(
                            By.CLASS_NAME, "DDLOptions__selected")

                    except NoSuchElementException:

                        isFillBlank = False

                    if isChooseCorrectAns:
                        Test.ChooseCorrectAns(sub_ans)

                    elif iswordBankTile_DragCorrectAns:
                        Test.DragCorrectAns.wordBankTile_DragCorrectAns(
                            sub_ans)

                    elif isdnditem_DragCorrectAns:
                        Test.DragCorrectAns.dnditem_DragCorrectAns(sub_ans)

                    elif isFillBlank:
                        Test.FillBlank(sub_ans)

                    CurrentTask = driver.find_element(
                        By.CLASS_NAME, "learning__taskNavPCCurrentTask").text

                    TotalTasks = driver.find_element(
                        By.CLASS_NAME, "learning__taskNavPCTotalTasks").text

                    if CurrentTask == TotalTasks:

                        driver.find_element(
                            By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__submitTestLink").click()

                        WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
                            (By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[1]/div[2]/div/div/div[1]/div[2]/div/div[2]")))


                    else:

                        driver.find_element(
                            By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                        time.sleep(0.5)

            elif isInteract_1:

                while True:

                    driver.find_element(
                        By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                    WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
                        (By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/a")))

                    time.sleep(5)

                    driver.find_element(
                        By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/a").click()

                    time.sleep(1)

                    driver.find_element(
                        By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[1]/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/a").click()

                    CurrentTask = driver.find_element(
                        By.CLASS_NAME, "learning__taskNavPCCurrentTask").text

                    TotalTasks = driver.find_element(
                        By.CLASS_NAME, "learning__taskNavPCTotalTasks").text

                    driver.find_element(
                        By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                    if CurrentTask == TotalTasks:

                        break

            elif isInteract_2:

                while True:

                    driver.find_element(
                        By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                    WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
                        (By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]")))

                    WebDriverWait(driver, 7200).until(EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/a")))

                    time.sleep(5)

                    driver.find_element(
                        By.XPATH, "/html/body/app/div/div/section/div/section[2]/div/div[1]/div[3]/ed-la-practicearea/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/a").click()

                    CurrentTask = driver.find_element(
                        By.CLASS_NAME, "learning__taskNavPCCurrentTask").text

                    TotalTasks = driver.find_element(
                        By.CLASS_NAME, "learning__taskNavPCTotalTasks").text

                    driver.find_element(
                        By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

                    if CurrentTask == TotalTasks:

                        break

            time.sleep(1)

            if isTest == False and isInteract_1 == False and isInteract_2 == False:

                break

        DirectNumber += 1

        # driver.find_element(
        #     By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

        # WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
        #     (By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink")))

        print(DirectNumber)

        driver.find_element(
            By.XPATH, "/html/body/app/div/div/div[1]/ed-la-dropdownlist[1]/section[1]/div[2]").click()

        time.sleep(0.5)

        NumberOfLessons = len(driver.find_elements(
            By.CLASS_NAME, "learning__dropDownList_itemNameText")) - 3

        if DirectNumber > NumberOfLessons:

            print("PASSED 1 UNIT")

            Url = f"/html/body/app/div/div/div[1]/ed-la-dropdownlist[1]/section[2]/div[2]/div/div[1]/div[{DirectNumber - 1}]/div[1]/div"

            driver.find_element(By.XPATH, Url).click()

            DirectNumber = 1

            UnitNumber += 1

            driver.find_element(
                By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

            time.sleep(1)

            driver.find_element(
                By.XPATH, "/html/body/app/div/div/div[1]/ed-la-dropdownlist[1]/section[1]/div[2]").click()

            time.sleep(0.5)

        time.sleep(0.5)

        Url = "/html/body/app/div/div/div[1]/ed-la-dropdownlist[1]/section[2]/div[2]/div/div[1]/div[" + str(
            DirectNumber) + "]/div[1]/div"

        driver.find_element(By.XPATH, Url).click()

        time.sleep(1)

    driver.find_element(
        By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink").click()

    WebDriverWait(driver, 7200).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".tasksBtnext.learning__pnItemLink.learning__nextItemLink")))

    #Logout

# ProfileButton = driver.find_element(By.XPATH, "/html/body/div/div[2]/header/section[2]/div[2]/div/div/ul/li[1]")

# ProfileButton.click()

# LogoutButton = driver.find_element(By.XPATH, "/html/body/div/div[2]/header/section[2]/div[2]/div/div/ul/li[1]/div/ul/li[5]/a")

# LogoutButton.click()

# WebDriverWait(driver, 7200).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[3]/iframe")))

# popupWrapper = driver.find_element(By.XPATH, "/html/body/div[3]/iframe")

# driver.switch_to.frame(popupWrapper)

# LogoutConfirm = driver.find_element(By.XPATH, "/html/body/div/div[2]/input")

# LogoutConfirm.click()

# driver.quit()
