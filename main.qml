
import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2
import QtQuick.Dialogs 1.0


//import familytree.uimanager 1.0

ApplicationWindow {
    visible: true
    width: 1000
    height: 800
    title: qsTr("Family tree")


    FileDialog {
        id: loadDialog
        title: "Please choose a file"
        nameFilters: ["Text files (*.xml)", "All files (*)"]
        onAccepted: {
            console.log("You chose: " + saveDialog.fileUrls)
            uimanager.requestLoad(saveDialog.fileUrls)
        }
        onRejected: {
            console.log("Canceled")
        }

    }

    FileDialog {
        id: saveDialog
        title: "Please choose a file"
        selectExisting: false
        nameFilters: ["Text files (*.xml)", "All files (*)"]
        onAccepted: {
            console.log("You chose: " + saveDialog.fileUrl)
            uimanager.requestSave(saveDialog.fileUrl)
        }
        onRejected: {
            console.log("Canceled")
        }

    }

    RowLayout {
        id: saveLoadId

        Button {
            id: saveButton
            text: "Save"
            onClicked: {
                saveDialog.open()
            }

        }

        Button {
            id: loadButton
            text: "Load"
            anchors.left: saveButton.right
            anchors.leftMargin: 10
            onClicked: {
                loadDialog.open()
            }
        }
    }

    Rectangle {
        id: separatorId
        height: 2
        width: 1000
        color: "black"
        anchors.topMargin: 5
        anchors.top: saveLoadId.bottom
    }



    ColumnLayout {
        id: addIndividualLayoutId
        anchors.top: separatorId.bottom
        anchors.topMargin: 5

        Label {
            text: "New Individual"
        }

        RowLayout {
            Label {
                text: "ID"
            }

            TextField {
                id: idTextId
                width: 100
            }
        }
        RowLayout {
            Label {

                text: "First Name"
            }
            TextField {
                id: firstNameId
                width: 100
            }
        }

        RowLayout {
            Label {
                text: "Last Name"
            }
            TextField {
                id: lastNameId
                width: 100
            }
        }

        RowLayout {
            Label {
                text: "Sex"
            }
            CheckBox {
                id: sexId
            }
        }

        RowLayout {
            Label {
                text: "Birthday"
            }
            Calendar {
                id: birthdayId
            }
        }

        RowLayout {
            Label {
                id: deathdayId
                text: "Deathday"
            }

            Calendar {
            }
        }

        RowLayout {
            Label {
                text: "Children(ids separated by coma i.e. id1,id2, id3):"
            }
            TextField {
                id: childrenId
                width: 100
            }
        }
        Button {
            text: "Submit"
            onClicked: {
                uimanager.requestSubmit(idTextId.text, firstNameId.text, lastNameId.text, sexId.checked?"M":"F", childrenId.text)
            }
        }
    }

    ColumnLayout {
        anchors.left: addIndividualLayoutId.right
        anchors.top: separatorId.bottom
        anchors.topMargin: 5
        anchors.leftMargin: 100
        Label {
            text: "Search"
        }
        RowLayout {
            Label {
                text: "ID: "
            }

            TextField {
                width: 100
            }

            Button {
                text: "Search"
            }
        }

    }

}
