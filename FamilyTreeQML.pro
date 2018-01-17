TEMPLATE = app

QT += qml quick
CONFIG += c++11

SOURCES += \
    main.cpp \
    individual.cpp \
    children.cpp \
    parents.cpp \
    familytree.cpp \
    treemanager.cpp \
    uimanager.cpp

HEADERS += \
    individual.h \
    children.h \
    parents.h \
    familytree.h \
    treemanager.h \
    uimanager.h \
    uilistener.h

RESOURCES += qml.qrc

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
