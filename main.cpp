#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QtQml>

#include "uimanager.h"
#include "familytree.h"

int main(int argc, char *argv[])
{
    FamilyTree familyTree;

    QGuiApplication app(argc, argv);

    //qmlRegisterType<UIManager>("familytree.uimanager", 1, 0, "UIManager");

    QQmlApplicationEngine engine;
    engine.rootContext()->setContextProperty("uimanager", familyTree.getUIManager());

    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    return app.exec();
}
