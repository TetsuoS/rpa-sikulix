# rpa-sikulix

Local:
DOUGA-iMac:imovie4youtube TETSUO$ pwd
/Users/TETSUO/sikulix/imovie4youtube

【導入方法】
① 以下のサイトを参考にする。
https://stackoverflow.com/questions/50642586/how-to-get-sikuli-script-jar-for-mac

具体的にはダウンロードしたファイル　 sikulixsetup-1.1.3.jar
をダブルクリックしてインストール。
（ただし、MacではCTRLを押してクリックしてから導入すること。）

②導入後に、Sikulix用のPythonプログラムがあるフォルダを開き、sikulix.jar　をダブルクリックするとソフトが開く。

【エラーの注意点】
以下のようなエラーが発生する場合がある。

2019-04-25 11:00:17.608 java[1006:33310] pid(1006)/euid(501) is calling TIS/TSM in non-main thread environment, ERROR : This is NOT allowed. Please call TIS/TSM in main thread!!!
IDE terminated: returned: 0
DOUGA-iMac:automation-mac-garageband TETSUO$ java -jar sikulix.jar
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by org.sikuli.ide.CloseableModernTabbedPaneUI (file:/Users/TETSUO/tmp/automation-mac-garageband/sikulix.jar) to constructor javax.swing.plaf.basic.BasicTabbedPaneUI$Actions(java.lang.String)
WARNING: Please consider reporting this to the maintainers of org.sikuli.ide.CloseableModernTabbedPaneUI
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release

対処法ははっきり分から無いが、どうやら経験上、
「sikulix.jar」本体があるフォルダを開いた状態にすると治る？？
かもしれ無い。
