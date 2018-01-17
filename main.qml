import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

//import familytree.uimanager 1.0

ApplicationWindow {
    visible: true
    width: 1000
    height: 800
    title: qsTr("Hello World")

    RowLayout {
        id: saveLoadId

        Button {
            id: saveButton
            text: "Save"
        }

        Button {
            id: loadButton
            text: "Load"
            anchors.left: saveButton.right
            anchors.leftMargin: 10
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
        Button {
            text: "Submit"
            onClicked: {
                uimanager.requestSubmit()
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
