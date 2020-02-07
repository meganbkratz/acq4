from moduleTemplate import Ui_Form
import zStackTemplate
from PyQt4 import QtGui, QtCore
from acq4.modules.Camera import CameraModuleInterface
from acq4.util.imaging.imaging_ctrl import ImagingCtrl
import acq4.pyqtgraph as pg
from acq4.util import Qt
from acq4.Manager import getManager


class PVImagerCamModInterface(CameraModuleInterface):
    """For plugging PrairieView images into the camera module"""

    def __init__(self, dev, cameraModule):
        CameraModuleInterface.__init__(self, dev, cameraModule)
        # self.widget = PVImagerModuleGui()

        self.view = cameraModule.window().view

        self.imagingCtrl = ImagingCtrl()
        self.frameDisplay = self.imagingCtrl.frameDisplay
        self.frameDisplay.contrastCtrl.ui.spinAutoGainSpeed.setValue(0)
        self.imageItem = self.frameDisplay.imageItem()

        self.view.addItem(self.imageItem)

        self.dev().setup() ##set save directory

        self.imagingCtrl.ui.stackWidget.hide()
        self.imagingCtrl.ui.frameRateWidget.hide()
        self.imagingCtrl.ui.acquireVideoBtn.setEnabled(False)

        self.zStackCtrl = ZStackCtrl(interface=self)
        cameraModule.window().sigSequenceFinished.connect(self.newZStack)
        self.zStackCtrl.ui.acquireZStackBtn.setEnabled(False)

        # ## set up item groups
        # self.cameraItemGroup = pg.ItemGroup()  ## translated with scope, scaled with camera objective
        # self.imageItemGroup = pg.ItemGroup()   ## translated and scaled as each frame arrives
        # self.view.addItem(self.imageItemGroup)
        # self.view.addItem(self.cameraItemGroup)
        # self.cameraItemGroup.setZValue(0)
        # self.imageItemGroup.setZValue(-2)

        # ## video image item
        # self.imageItem = self.frameDisplay.imageItem()
        # self.view.addItem(self.imageItem)
        # self.imageItem.setParentItem(self.imageItemGroup)
        # self.imageItem.setZValue(-10)
        self.lastFrame = None

        self.imagingCtrl.sigAcquireFrameClicked.connect(self.acquireFrameClicked)
        self.frameDisplay.imageUpdated.connect(self.imageUpdated)
        # self.zStackCtrl.ui.acquireZStackBtn.clicked.connect(self.acquireZStackClicked)


    # def graphicsItems(self):
    #     """Return a list of all graphics items displayed by this interface.
    #     """
    #     pass

    def controlWidget(self):
        """Return a widget to be docked in the camera module window.

        May return None.
        """
        return None

    def boundingRect(self):
        """Return the bounding rectangle of all graphics items.
        """
        return None

    def getImageItem(self):
        """Return the ImageItem used to display imaging data from this device.

        May return None.
        """
        #return None
        return self.frameDisplay.imageItem()

    def takeImage(self, closeShutter=None):
        """Request the imaging device to acquire a single frame.

        The optional closeShutter argument is used to tell laser scanning devices whether
        to close their shutter after imaging. Cameras can simply ignore this option.
        """
        # Note: this is a bit kludgy. 
        # Would be nice to have a more natural way of handling this..
        #raise NotImplementedError(str(self))
        frame = self.getDevice().acquireFrames(1, stack=False)
        self.imagingCtrl.newFrame(frame)
        #raise Exception('stop')
        return frame

    def setAcquireBtn(self, b):
        btn = self.imagingCtrl.ui.acquireFrameBtn
        # zBtn = self.zStackCtrl.ui.acquireZStackBtn
        if b:
            btn.setText('Acquire Frame')
            btn.setEnabled(True)
            # zBtn.setText('Acquire Z-Stack')
            # zBtn.setEnabled(True)
        else:
            btn.setText('Acquiring...')
            btn.setEnabled(False)
            # zBtn.setText('Acquiring...')
            # zBtn.setEnabled(False)

    def acquireFrameClicked(self):
        self.setAcquireBtn(False)
        frame = self.getDevice().acquireFrames(1, stack=False)
        self.setAcquireBtn(True)
        self.imagingCtrl.newFrame(frame)

    # def acquireZStackClicked(self):
    #     self.setAcquireBtn(False)
    #     zstack = self.getDevice().acquireZStack()
    #     self.setAcquireBtn(True)
    #     self.zStackCtrl.newFrame(zstack)

    def imageUpdated(self, frame):
        ## New image is displayed; update image transform
        self.lastFrame = frame
        self.imageItem.setTransform(frame.globalTransform().as2D())
        self.sigNewFrame.emit(self, frame)

    def newZStack(self, dh):
        #arr = fh[fh.ls()[0]].read()
        #raise Exception('stop')
        self.zStackCtrl.newFrame(dh)



class ZStackCtrl(Qt.QWidget):

    def __init__(self, parent=None, interface=None):
        Qt.QWidget.__init__(self, parent) 
        self.interface = interface

        self.ui = zStackTemplate.Ui_Form()
        self.ui.setupUi(self)

        self.ui.focusSlider.valueChanged.connect(self.focusSliderChanged)
        self.ui.zStackTree.currentItemChanged.connect(self.selectedZStackChanged)

        self.zStacks = {}

        self.setUpFocusShortCuts()
        
    def newFrame(self, dh):
        fh = dh['image_000.ma']
        arr = fh.read()

        treeItem = QtGui.QTreeWidgetItem([dh.shortName()])
        self.ui.zStackTree.addTopLevelItem(treeItem)

        im = pg.ImageItem(arr[0])
        self.interface.view.addItem(im)
        im.setTransform(fh.info()['transform'].as2D())

        self.zStacks[treeItem] ={'data':arr, 'imageItem':im}

        self.ui.zStackTree.setCurrentItem(treeItem)

        #self.saveZStack(stack)


    def focusSliderChanged(self):
        i = self.ui.focusSlider.value()

        treeItem = self.ui.zStackTree.currentItem()
        data = self.zStacks[treeItem]['data'][i]
        self.zStacks[treeItem]['imageItem'].setImage(data)

        z = data.infoCopy()[-1]['values']
        self.interface.dev().scopeDevice().setFocusDepth(z)

    def selectedZStackChanged(self):
        treeItem = self.ui.zStackTree.currentItem()

        stack = self.zStacks[treeItem]['data']
        nFrames = stack.shape[0]
        self.ui.focusSlider.setRange(0, nFrames-1)

        top = stack[0].infoCopy()[-1]['values']
        bottom = stack[-1].infoCopy()[-1]['values']
        self.ui.topLabel.setText(pg.siFormat(top, suffix='m'))
        self.ui.bottomLabel.setText(pg.siFormat(bottom, suffix='m'))

    def saveZStack(self, stack):
        dh = getManager().getCurrentDir()

        data = stack.data()
        info = stack.info()

        dh.writeFile(data, info['name'], info=info, autoIncrement=False, fileType='MetaArray')

    def setUpFocusShortCuts(self):
        config = self.interface.dev().config
        leftKey = config.get('upShortcutKey')
        rightKey = config.get('downShortcutKey')

        if leftKey is not None and rightKey is not None:
            left_shortcut = Qt.QShortcut(Qt.QKeySequence(leftKey), self, context=Qt.Qt.ApplicationShortcut)
            right_shortcut = Qt.QShortcut(Qt.QKeySequence(rightKey), self, context=Qt.Qt.ApplicationShortcut)
            left_shortcut.activated.connect(self.leftShortcutPressed)
            right_shortcut.activated.connect(self.rightShortcutPressed)

    def leftShortcutPressed(self):
        self.ui.focusSlider.setValue(self.ui.focusSlider.value()-1)

    def rightShortcutPressed(self):
        self.ui.focusSlider.setValue(self.ui.focusSlider.value()+1)











